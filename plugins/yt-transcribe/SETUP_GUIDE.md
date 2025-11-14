# YT-Transcribe Plugin Setup & Usage Guide

Welcome to the **YouTube Transcribe & Download** plugin! This guide walks you through setup, configuration, and usage.

## Prerequisites

### Required

- **Python 3.7+** - Core runtime
- **yt-dlp** - For downloading YouTube videos
  ```bash
  pip install yt-dlp
  ```

### Optional

- **ffmpeg** - For format conversion and audio extraction
  ```bash
  # macOS
  brew install ffmpeg

  # Ubuntu/Debian
  sudo apt-get install ffmpeg

  # Windows
  choco install ffmpeg
  ```

- **OpenAI Whisper** - For local speech-to-text transcription
  ```bash
  pip install openai-whisper
  ```

- **YouTube Transcript API** - For fetching transcripts
  ```bash
  pip install youtube-transcript-api
  ```

## Installation

1. **Via DotClaude Marketplace** (Recommended)
   ```bash
   /plugin marketplace add dotclaude/marketplace
   # yt-transcribe installs automatically with all plugins
   ```

2. **Manual Installation**
   ```bash
   # Clone or copy the plugin to your .claude/plugins directory
   cp -r yt-transcribe ~/.claude/plugins/
   ```

## Plugin Structure

```
yt-transcribe/
├── agents/
│   ├── transcript-processor.md      # Analyzes & summarizes transcripts
│   ├── media-downloader.md          # Handles yt-dlp operations
│   ├── transcript-fetcher.md        # Retrieves transcripts from multiple sources
│   └── video-analyzer.md            # Inspects video metadata
├── commands/
│   ├── yt-transcribe.md             # Main transcription command
│   ├── yt-download.md               # Download command
│   ├── yt-analyze.md                # Analysis command
│   └── yt-fetch-transcript.md       # Transcript fetching command
├── .claude-plugin/
│   └── plugin.json                  # Plugin metadata
├── README.md                         # Plugin overview
└── SETUP_GUIDE.md                   # This file
```

## Quick Start

### 1. Analyze a Video (No Download)

```bash
/yt-analyze "https://www.youtube.com/watch?v=VIDEO_ID"
```

This shows:
- Video metadata (title, duration, view count)
- Available caption tracks and languages
- Technical specifications (codecs, bitrates, resolutions)
- Quality assessment for transcription

### 2. Transcribe a Video

```bash
/yt-transcribe "https://www.youtube.com/watch?v=VIDEO_ID"
```

This:
- Fetches the transcript (via YouTube API if available)
- Formats it nicely
- Optionally generates a summary

### 3. Download a Video

```bash
/yt-download "https://www.youtube.com/watch?v=VIDEO_ID"
```

This:
- Downloads the best available quality
- Embeds metadata
- Saves to `./downloads/`

### 4. Fetch Transcript with Options

```bash
/yt-fetch-transcript "https://www.youtube.com/watch?v=VIDEO_ID" --format json --timestamps
```

## Agents Overview

### 🎬 Video Analyzer

Inspects videos without downloading them.

**When to use**: Before deciding on download strategy
- Check available captions and languages
- Assess video technical properties
- Determine transcription feasibility
- Estimate file sizes

**Example workflow**:
```bash
/yt-analyze "URL" --detailed --check-captions
```

### ⬇️ Media Downloader

Handles all download operations with intelligent format selection.

**When to use**: When you need the actual video file
- Download for local streaming
- Extract audio for podcasts
- Archive important content
- Convert to specific format

**Key features**:
- JavaScript support for protected content
- Format/codec optimization
- Post-processing (conversion, metadata)
- Batch operations (playlists, channels)

### 📝 Transcript Fetcher

Retrieves transcripts using multiple methods.

**When to use**: When you need the spoken content as text
- Extract dialogue and captions
- Get transcripts for videos without captions (via Whisper)
- Retrieve in multiple languages
- Choose between speed (API) and accuracy (speech-to-text)

**Methods**:
- YouTube API (fastest, if captions exist)
- YouTube fallback provider
- Local speech-to-text (Whisper)

### 📊 Transcript Processor

Analyzes and transforms transcripts.

**When to use**: After getting a transcript
- Generate summaries and key points
- Extract topics and themes
- Identify speakers and segments
- Format for different outputs (markdown, JSON, VTT)

## Command Reference

### `/yt-transcribe`

**Purpose**: One-command transcription with analysis

```bash
/yt-transcribe "URL" [options]

Options:
  --summary              Generate summary alongside transcript
  --format markdown      Output format (text, markdown, json, vtt)
  --language es          Specific language code
  --timestamps           Include timestamps
  --speakers             Separate by speaker segments
```

**Output**:
- Full transcript with optional timestamps
- Speaker segments (if requested)
- Summary and key points (if requested)
- Metadata (language, source, quality)

### `/yt-download`

**Purpose**: Download video with smart format selection

```bash
/yt-download "URL" [options]

Options:
  --format best          Format selection (best, best-video, best-audio, mp4, webm)
  --quality 720p         Quality preference (1080p, 720p, 480p, auto)
  --audio-only           Extract audio only
  --convert-to mp3       Post-process conversion (mp3, wav, etc.)
  --output-dir /path     Custom output directory
```

**Output**:
- Downloaded video in specified format
- Embedded metadata (title, description, thumbnail)
- File saved as: `{Video Title}.{extension}`

### `/yt-analyze`

**Purpose**: Inspect video without downloading

```bash
/yt-analyze "URL" [options]

Options:
  --detailed             Show comprehensive technical specs
  --check-captions       Detailed subtitle track inspection
  --quality-report       Generate transcription feasibility report
  --format-options       List all available formats
  --estimate-sizes       Estimate file sizes per quality
```

**Output**:
- Metadata overview
- Technical specifications
- Caption/subtitle availability
- Quality assessment
- Format recommendations

### `/yt-fetch-transcript`

**Purpose**: Retrieve transcript using preferred method

```bash
/yt-fetch-transcript "URL" [options]

Options:
  --method auto          Retrieval method (auto, api, speech-to-text, fallback)
  --language en          Specific language code
  --format json          Output format (text, markdown, json, vtt, srt)
  --quality best         Quality preference (best, high, standard, draft)
  --timestamps           Include timestamps
  --validate             Check transcript completeness
```

**Output**:
- Full transcript in chosen format
- Metadata (language, source, quality)
- Timestamps (if requested)
- Quality indicators

## Workflow Examples

### Example 1: Quick Transcription

```bash
# 1. Check if video has captions
/yt-analyze "URL"

# 2. Transcribe
/yt-transcribe "URL" --summary --format markdown

# 3. Read the summary and transcript
```

### Example 2: Full Video Archive

```bash
# 1. Analyze video
/yt-analyze "URL" --detailed --quality-report

# 2. Download video
/yt-download "URL" --format best --quality 1080p

# 3. Fetch transcript
/yt-fetch-transcript "URL" --format json --timestamps

# 4. Get processed summary
/yt-transcribe "URL" --summary
```

### Example 3: Podcast Extraction

```bash
# 1. Download audio only
/yt-download "URL" --audio-only --convert-to mp3

# 2. Get transcript
/yt-fetch-transcript "URL" --timestamps

# 3. Get summary
/yt-transcribe "URL" --summary --format markdown
```

### Example 4: Multi-Language Content

```bash
# 1. Check available languages
/yt-analyze "URL" --check-captions

# 2. Transcribe in specific language
/yt-fetch-transcript "URL" --language es --format srt

# 3. Get summary
/yt-transcribe "URL" --summary --language es
```

## Configuration

### yt-dlp Settings

The plugin uses sensible defaults but you can customize:

```python
# JavaScript support (enabled by default)
yt-dlp --enable-javascript-renderer

# Format selection
yt-dlp -f "bestvideo[height<=720]+bestaudio"

# Metadata embedding
yt-dlp --embed-metadata --embed-thumbnail
```

### Whisper Settings

For speech-to-text transcription:

```bash
# Use smaller model for speed
whisper video.mp4 --model tiny

# Use larger model for accuracy
whisper video.mp4 --model large
```

### Output Directory

By default, downloads go to `./downloads/`. Customize with:

```bash
/yt-download "URL" --output-dir ~/Videos/YouTube
```

## Troubleshooting

### "Video not found" or 404 errors

- Verify URL is correct and video still exists
- Check if video is age-restricted
- Try with `--analyze` first to check accessibility

### No captions available

- Use `--method speech-to-text` to transcribe from audio
- This requires Whisper to be installed
- Takes longer but works for any video

### Download fails with format error

- Use `--analyze --format-options` to see available formats
- Try `--format best` (auto-selects optimal)
- Check if video is protected or region-locked

### Whisper transcription is slow

- Use smaller model: `--quality draft` (uses tiny model)
- Increase `--quality` only if accuracy is critical
- Ensure ffmpeg is installed for efficiency

### File size is too large

- Use `--quality 480p` or lower
- Use `--audio-only` if you don't need video
- Try MP4 format which tends to be more compressed

## API Reference

When calling agents via Task tool:

### Video Analyzer Agent

```
Task: Use video-analyzer agent
- Inspect video metadata
- Check available formats and captions
- Assess transcription feasibility
```

### Media Downloader Agent

```
Task: Use media-downloader agent
- Download video with specified format
- Perform post-processing (conversion, metadata)
- Handle JavaScript-protected content
```

### Transcript Fetcher Agent

```
Task: Use transcript-fetcher agent
- Retrieve transcript via API if available
- Fall back to speech-to-text if needed
- Validate transcript quality
```

### Transcript Processor Agent

```
Task: Use transcript-processor agent
- Summarize and analyze transcript
- Extract key points and topics
- Format for different outputs
- Identify speakers and segments
```

## Performance Tips

1. **For speed**: Use YouTube API method (`--method api`)
2. **For quality**: Use speech-to-text with large Whisper model
3. **For storage**: Use audio-only downloads (`--audio-only`)
4. **For compatibility**: Use MP4 format (`--format mp4`)

## Privacy & Safety

- Videos are downloaded to local `./downloads` directory
- Transcripts are processed locally
- No data is sent to external services (except YouTube API)
- Respect copyright and Terms of Service

## Common Use Cases

| Use Case | Command | Notes |
|----------|---------|-------|
| Quick summary | `/yt-transcribe URL --summary` | Uses YouTube captions if available |
| Full video archive | `/yt-download URL --format best` | Downloads best quality |
| Podcast extraction | `/yt-download URL --audio-only` | Extract audio as MP3 |
| Accessibility | `/yt-transcribe URL` | Creates transcript for SDH |
| Research | `/yt-fetch-transcript URL --format json` | Structured data export |
| Multi-language | `/yt-fetch-transcript URL --language es` | Get specific language |

---

**Questions or issues?** Check the README.md or consult the agent descriptions for detailed capabilities.
