# YT-Transcribe Quick Reference

## The 4 Agents

| Agent | Purpose | Key Operation |
|-------|---------|---|
| **Video Analyzer** | Inspect videos | `metadata, formats, captions, quality` |
| **Media Downloader** | Download videos | `yt-dlp + post-processing + metadata` |
| **Transcript Fetcher** | Get transcripts | `YouTube API → Whisper fallback` |
| **Transcript Processor** | Analyze transcripts | `summarize, extract, format, analyze` |

## The 4 Commands

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| **yt-analyze** | Inspect video metadata | Before downloading, check quality/captions |
| **yt-download** | Download video file | Need the actual video file locally |
| **yt-transcribe** | Transcribe + analyze | Want text of spoken content + summary |
| **yt-fetch-transcript** | Get transcript only | Just need the transcript, not video |

## Common Workflows

### 1. Quick Summary (Fastest)
```bash
/yt-transcribe "URL" --summary
```
Takes seconds. Uses YouTube captions if available.

### 2. Full Archive (Download + Transcript)
```bash
/yt-analyze "URL" --detailed
/yt-download "URL" --quality 720p
/yt-transcribe "URL" --summary
```
Downloads video and gets transcript with summary.

### 3. Podcast Extraction (Audio Only)
```bash
/yt-download "URL" --audio-only --convert-to mp3
/yt-transcribe "URL" --summary
```
Extracts audio as MP3, gets transcript.

### 4. Research (Structured Data)
```bash
/yt-fetch-transcript "URL" --format json --timestamps
/yt-analyze "URL" --quality-report
```
Gets structured transcript data and quality assessment.

## Command Options at a Glance

### yt-transcribe
```
--summary              # Add concise summary
--format markdown      # Change output format
--language es          # Specify language
--timestamps           # Include timestamps
--speakers             # Identify speakers
```

### yt-download
```
--format best          # Format selection
--quality 720p         # Resolution
--audio-only           # Just audio
--convert-to mp3       # Post-convert format
--output-dir /path     # Custom location
```

### yt-analyze
```
--detailed             # Full technical specs
--check-captions       # Detailed subtitle info
--quality-report       # Transcription feasibility
--format-options       # All available formats
--estimate-sizes       # File size predictions
```

### yt-fetch-transcript
```
--method api           # YouTube API (fastest)
--language en          # Specific language
--format json          # Output format
--quality best         # Quality level
--timestamps           # Include timing
--validate             # Check completeness
```

## Format Options

### Video Formats
- `best` - Auto-select best (usually 1080p60)
- `best-video` - Video only, highest quality
- `best-audio` - Audio only, highest quality
- `mp4`, `webm`, `mkv` - Specific container

### Transcript Formats
- `text` - Plain text
- `markdown` - Formatted markdown
- `json` - Structured JSON (best for processing)
- `vtt` - WebVTT subtitles
- `srt` - SubRip subtitles

## Transcript Retrieval Methods

| Method | Speed | Works When | Best For |
|--------|-------|-----------|----------|
| `api` | ⚡ Seconds | Captions exist | Most common videos |
| `speech-to-text` | 🐢 Minutes | Any audio | Videos without captions |
| `fallback` | 🟡 Varies | Unknown | Automatic selection |
| `auto` | 🟡 Smart | Any case | Recommended default |

## Resolution Options

```
1080p / 1080p60  → Best quality, largest file
720p / 720p60    → Good quality, balanced size
480p             → Smaller file, adequate quality
360p             → Very small file, lower quality
auto             → Smart selection (usually 720p)
```

## File Locations

| What | Where | Notes |
|------|-------|-------|
| Downloaded videos | `./downloads/` | Change with `--output-dir` |
| Plugin files | `plugins/yt-transcribe/` | Installation location |
| Transcripts (cached) | `.cache/` (implicit) | Not created yet |
| Documentation | `README.md`, `SETUP_GUIDE.md`, `ARCHITECTURE.md` | In plugin root |

## Troubleshooting Checklist

**Video won't download**
- [ ] Is the URL correct?
- [ ] Is the video public?
- [ ] Try `--analyze` first to check accessibility

**No captions available**
- [ ] Check with `--analyze --check-captions`
- [ ] Use `--method speech-to-text` (requires Whisper)
- [ ] Manually add captions on YouTube

**Transcript missing content**
- [ ] Try `--method speech-to-text` for full content
- [ ] Use `--validate` to check completeness
- [ ] Check if video has overlapping audio

**Download is too slow**
- [ ] Try lower quality: `--quality 480p`
- [ ] Use audio-only: `--audio-only`
- [ ] Add `--no-js` for speed (if not needed)

**File size is huge**
- [ ] Reduce quality: `--quality 480p`
- [ ] Use audio-only: `--audio-only`
- [ ] Try WebM format: `--format webm`

## Learning Path

1. **Beginner**: Start with `/yt-analyze` to explore
2. **Basic**: Try `/yt-transcribe` for quick summaries
3. **Intermediate**: Use `/yt-download` for archival
4. **Advanced**: Read ARCHITECTURE.md for deep dives

## Performance Tips

| Goal | Approach |
|------|----------|
| Fastest | `/yt-transcribe URL --summary` (no download) |
| Smallest files | `/yt-download URL --audio-only` |
| Best quality | `/yt-download URL --quality 1080p` |
| Most compatible | `/yt-download URL --format mp4` |
| Research-ready | `/yt-fetch-transcript URL --format json` |

## Installing Prerequisites

```bash
# Essential
pip install yt-dlp

# Highly recommended
pip install youtube-transcript-api

# For speech-to-text
pip install openai-whisper

# For audio/video conversion
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Ubuntu/Debian
choco install ffmpeg  # Windows
```

## Example Real-World Commands

### Extract a podcast as MP3
```bash
/yt-download "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only --convert-to mp3
```

### Get English subtitle file (SRT format)
```bash
/yt-fetch-transcript "URL" --language en --format srt
```

### Download best quality for archival
```bash
/yt-download "URL" --format best --quality 1080p
```

### Quick summary in Markdown
```bash
/yt-transcribe "URL" --summary --format markdown
```

### Check before downloading (slow/expensive videos)
```bash
/yt-analyze "URL" --detailed --estimate-sizes
```

### Get JSON data for processing
```bash
/yt-fetch-transcript "URL" --format json --timestamps
```

## Keyboard Shortcuts

In Claude Code IDE:
- `⌘+K` / `Ctrl+K` → Open command palette
- Type `/yt-` → See all available commands
- `⌘+Enter` → Execute command

## Further Help

- **Setup issues**: See SETUP_GUIDE.md
- **How it works**: See ARCHITECTURE.md
- **Full reference**: See individual command/agent .md files
- **External tools**: See links in README.md

---

**Tip**: Combine commands for powerful workflows!

Example research workflow:
```bash
# 1. Analyze first (no download)
/yt-analyze "URL" --quality-report

# 2. Make decision based on info

# 3a. If yes, download + transcribe
/yt-download "URL" --quality 720p
/yt-transcribe "URL" --summary --format markdown

# 3b. Or just get transcript (faster)
/yt-fetch-transcript "URL" --method api --format json
```
