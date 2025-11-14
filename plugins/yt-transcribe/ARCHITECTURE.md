# YT-Transcribe Plugin Architecture

This document describes the technical architecture and design patterns of the yt-transcribe plugin.

## Overview

The **yt-transcribe** plugin is a modular system for YouTube content interaction, built on four specialized agents and four slash commands that work in concert.

```
┌─────────────────────────────────────────────────────────┐
│                    Slash Commands                        │
│  ┌──────────────┬──────────────┬──────────────┬────────┐ │
│  │ yt-transcribe│ yt-download  │  yt-analyze  │yt-fetch│ │
│  └──────────────┴──────────────┴──────────────┴────────┘ │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┼────────────┬──────────────┐
        │            │            │              │
┌───────▼──────┐ ┌──▼──────────┐ ┌─▼──────────┐ ┌─▼──────────┐
│   Transcript │ │Media        │ │Transcript  │ │   Video    │
│   Processor  │ │Downloader   │ │  Fetcher   │ │ Analyzer   │
└──────────────┘ └─────────────┘ └────────────┘ └────────────┘
     Agent            Agent          Agent         Agent
```

## Component Breakdown

### Agents (Specialized Problem-Solvers)

Each agent is a specialized expert with focused responsibilities:

#### 1. Video Analyzer Agent
- **Purpose**: Inspect and assess videos without downloading
- **Key operations**:
  - Extract video metadata (title, duration, channel, stats)
  - List available formats and codecs
  - Check subtitle/caption availability
  - Detect access restrictions and geo-blocking
  - Assess transcription feasibility
- **Model**: Sonnet (optimized for analysis)
- **Tools**: Task, Bash, Read, Write
- **Characteristics**:
  - Quick assessment (no downloads)
  - Provides quality predictions
  - Recommends download/transcription approaches

#### 2. Media Downloader Agent
- **Purpose**: Download and process video files
- **Key operations**:
  - Configure yt-dlp with JavaScript support
  - Select optimal codec/container combinations
  - Handle post-processing (format conversion, metadata)
  - Manage error recovery and retries
  - Process playlists and batch downloads
- **Model**: Sonnet (handles complex logic)
- **Tools**: Task, Bash, Read, Write
- **Characteristics**:
  - JavaScript support for protected content
  - Quality/size optimization
  - Metadata embedding
  - Progress tracking

#### 3. Transcript Fetcher Agent
- **Purpose**: Acquire transcripts from multiple sources
- **Key operations**:
  - Call YouTube Transcript API
  - Fallback to alternative providers
  - Trigger Whisper speech-to-text
  - Validate transcript completeness
  - Cache retrieved transcripts
- **Model**: Sonnet (intelligent fallback logic)
- **Tools**: Task, Bash, Read, Write, WebFetch
- **Characteristics**:
  - Multi-source retrieval strategy
  - Language detection and selection
  - Quality metrics and validation
  - Smart fallback chain

#### 4. Transcript Processor Agent
- **Purpose**: Analyze and transform transcript data
- **Key operations**:
  - Generate executive summaries
  - Extract key points and themes
  - Identify speakers and segments
  - Map timestamps to content
  - Format for different outputs
- **Model**: Sonnet (content analysis)
- **Tools**: Task, Bash, Read, Write
- **Characteristics**:
  - Hierarchical summarization
  - Topic extraction and modeling
  - Speaker identification
  - Multiple output formats

### Commands (User Entry Points)

Each command orchestrates agents to accomplish a user goal:

#### 1. `/yt-transcribe`
**Purpose**: One-command video transcription with analysis

**Workflow**:
```
User input: URL + options
    ↓
Video Analyzer (inspect video)
    ↓
Transcript Fetcher (get transcript)
    ↓
Transcript Processor (summarize/format)
    ↓
Return: Full transcript + summary + metadata
```

**Options**:
- `--summary`: Generate concise overview
- `--format`: Output format (text, markdown, json, vtt)
- `--language`: Specific language
- `--timestamps`: Include timing info
- `--speakers`: Identify speakers

#### 2. `/yt-download`
**Purpose**: Download videos with intelligent format selection

**Workflow**:
```
User input: URL + options
    ↓
Video Analyzer (check formats and quality)
    ↓
Media Downloader (execute download)
    ↓
Return: Downloaded file + metadata
```

**Options**:
- `--format`: Format type (best, mp4, webm, mkv)
- `--quality`: Resolution (1080p, 720p, 480p)
- `--audio-only`: Extract audio only
- `--convert-to`: Post-process conversion

#### 3. `/yt-analyze`
**Purpose**: Inspect video without downloading

**Workflow**:
```
User input: URL + options
    ↓
Video Analyzer (comprehensive inspection)
    ↓
Return: Metadata + formats + captions + quality report
```

**Options**:
- `--detailed`: Comprehensive technical specs
- `--check-captions`: Subtitle track inspection
- `--quality-report`: Transcription feasibility
- `--format-options`: List all formats
- `--estimate-sizes`: File size estimates

#### 4. `/yt-fetch-transcript`
**Purpose**: Retrieve transcript using preferred method

**Workflow**:
```
User input: URL + options
    ↓
Transcript Fetcher (multi-method retrieval)
    ↓
Return: Transcript in chosen format + metadata
```

**Options**:
- `--method`: Retrieval strategy (api, speech-to-text, fallback)
- `--language`: Specific language
- `--format`: Output format (json, vtt, srt, text)
- `--quality`: Quality level (best, high, standard, draft)
- `--timestamps`: Include timing
- `--validate`: Check completeness

## Data Flow Patterns

### Pattern 1: Simple Transcription
```
User → yt-transcribe → Video Analyzer → Transcript Fetcher → Processor → Output
```
**Use case**: Quick transcript of a video

### Pattern 2: Full Archive
```
User → yt-analyze → (user reviews) → yt-download + yt-fetch-transcript → Output
```
**Use case**: Download + transcribe video for archival

### Pattern 3: Selective Download
```
User → yt-analyze → Video Analyzer → (user decides) → yt-download → Output
```
**Use case**: Check quality before downloading large file

### Pattern 4: Multi-Method Transcript
```
User → yt-fetch-transcript → Transcript Fetcher → (API/Speech-to-text) → Output
```
**Use case**: Get transcript by preferred method

## Technical Decisions

### Why Four Agents?
1. **Separation of Concerns**: Each agent has one expertise area
2. **Reusability**: Agents can be called independently via Task tool
3. **Specialization**: Allows deep expertise in each domain
4. **Testability**: Each can be validated independently

### Why YAML Frontmatter?
- Standardized across DotClaude ecosystem
- Enables tool allocation and model selection
- Compatible with plugin registration
- Clear versioning and metadata

### JavaScript Support in yt-dlp
- Required for videos with protection mechanisms
- Enabled by default in media-downloader
- Can be disabled with `--no-js` for speed
- Handled transparently to user

### Multi-Source Transcript Strategy
1. **API First**: Fastest if YouTube captions exist
2. **Fallback Provider**: 3PlayMedia, Rev (if integrated)
3. **Speech-to-Text**: Whisper for full coverage
4. **Validation**: Quality checks at each step

### Model Selection
- **Sonnet** for all agents (balanced for analysis + action)
- **Sonnet-4-5** for all commands (latest, most capable)
- Agents: 200K token budget for deep analysis
- Commands: Task tool with agent invocation

## File Organization

```
yt-transcribe/
├── agents/                          # Specialized experts
│   ├── video-analyzer.md           # Video inspection expert
│   ├── media-downloader.md         # Download & processing expert
│   ├── transcript-fetcher.md       # Transcript acquisition expert
│   └── transcript-processor.md     # Content analysis expert
├── commands/                        # User entry points
│   ├── yt-transcribe.md            # Main transcription command
│   ├── yt-download.md              # Download command
│   ├── yt-analyze.md               # Analysis command
│   └── yt-fetch-transcript.md      # Transcript fetch command
├── .claude-plugin/
│   └── plugin.json                 # Plugin metadata & registration
├── README.md                        # Plugin overview
├── SETUP_GUIDE.md                  # Installation & usage guide
├── ARCHITECTURE.md                 # This file
├── .gitignore                      # Git configuration
└── LICENSE                         # MIT License (implicit)
```

## Extension Points

### Adding New Commands
1. Create `commands/my-command.md` with YAML frontmatter
2. Reference appropriate agents in command body
3. Document options and examples
4. Follow naming convention: `yt-{operation}`

### Extending Agents
- Modify agent capabilities in their `.md` files
- Update characteristic questions
- Add new analytical approaches
- Document new interaction patterns

### Integrating New Transcript Sources
- Add to fallback chain in transcript-fetcher
- Document method in agent description
- Add quality metrics for new source
- Validate output format consistency

## Performance Considerations

### Speed Optimizations
- **Video Analyzer**: No downloads, metadata-only
- **Transcript Fetcher**: API method fastest (seconds)
- **Speech-to-Text**: Slowest (minutes for long videos)
- **Smaller Whisper Model**: "tiny" for speed, "large" for accuracy

### Resource Usage
- **Disk**: Downloads use `./downloads/` directory
- **Memory**: Streaming for large transcripts
- **Network**: Single requests where possible
- **CPU**: ffmpeg encoding if format conversion needed

### Caching Strategy
- Transcripts cached locally to avoid re-fetching
- Downloads stored in `./downloads/` (persistent)
- Metadata cached with transcript files
- Cache invalidation on user refresh request

## Error Handling

### Video Analyzer Errors
- 404: Video not found or removed
- 403: Age-restricted or region-blocked
- 429: Rate limited (retry with backoff)

### Media Downloader Errors
- Format unavailable: Fall back to best available
- Download interrupted: Retry mechanism
- JavaScript rendering fails: Fall back to standard mode

### Transcript Fetcher Errors
- No captions: Suggest speech-to-text
- Language unavailable: Show available options
- API rate limit: Use cached version or offer speech-to-text

### Transcript Processor Errors
- Malformed input: Graceful degradation
- Encoding issues: UTF-8 normalization
- Format conversion: Fallback to text

## Security Considerations

1. **Local Processing**: All transcripts processed locally
2. **No Data Sharing**: Only YouTube API calls to YouTube
3. **Respect ToS**: Follows YouTube Terms of Service
4. **Copyright**: Users responsible for compliance
5. **File Permissions**: Downloads in user-writable directory

## Testing Strategy

### Unit Tests (Per Agent)
- Video Analyzer: Mock video metadata
- Media Downloader: Mock yt-dlp calls
- Transcript Fetcher: Mock API responses
- Transcript Processor: Test text analysis

### Integration Tests
- End-to-end workflows
- Command + Agent combinations
- Error recovery paths
- Format conversions

### Manual Testing
- Real YouTube videos (various types)
- Age-restricted content
- JavaScript-protected videos
- Multiple languages

---

**For questions about architecture, see the README.md or SETUP_GUIDE.md**
