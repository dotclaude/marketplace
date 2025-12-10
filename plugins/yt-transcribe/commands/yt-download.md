---
model: claude-sonnet-4-5
allowed-tools: Task, Bash, Read, Write
argument-hint: <video-url> [--format format] [--audio-only] [--quality quality]
description: Download a YouTube video with intelligent format selection
---

# YouTube Download Command

Download a YouTube video using yt-dlp with support for JavaScript-protected content, flexible format selection, and optional post-processing.

## Arguments

**$1 (Required)**: `video-url`

The full YouTube URL to download. Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

**Optional flags**:

- `--format` - Format selection: `best` (default), `best-video`, `best-audio`, `mp4`, `webm`, `mkv`
- `--audio-only` - Extract audio only (creates m4a/mp3 file)
- `--quality` - Quality preference: `1080p`, `720p`, `480p`, `360p`, `auto` (default)
- `--no-js` - Disable JavaScript rendering (faster for standard videos)
- `--output-dir` - Custom output directory (default: `./downloads`)
- `--convert-to` - Convert to target format using ffmpeg (e.g., `mp3`, `wav`)

## Examples

```bash
/yt-download "https://www.youtube.com/watch?v=VIDEO_ID"
/yt-download "https://www.youtube.com/watch?v=VIDEO_ID" --format best --quality 720p
/yt-download "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only --convert-to mp3
/yt-download "https://www.youtube.com/watch?v=VIDEO_ID" --format webm --quality 1080p
```

## How It Works

1. **Video Analysis** - Inspects video source and available formats
2. **Format Selection** - Recommends optimal codec/container for your use case
3. **Download** - Executes yt-dlp with JavaScript support for protected content
4. **Post-Processing** - Optionally converts format or extracts audio
5. **Validation** - Confirms successful download and file integrity

## Configuration

The downloader automatically:
- Enables JavaScript rendering for protected content
- Sets appropriate user agents and headers
- Handles throttling and rate limiting
- Embeds metadata (title, description, thumbnail)
- Creates output directory if needed

## Output

- Downloaded video file with metadata embedded
- File naming: `{Video Title}.{extension}`
- Metadata includes thumbnail, description, and upload date
- Console output shows progress, speed, and estimated time remaining

## Tips

- Use `--audio-only` for podcasts, music, or when video content isn't needed
- `--format best` auto-selects best available quality (usually 1080p60 if available)
- JavaScript rendering is enabled by default but can be disabled for speed with `--no-js`
- Conversions use ffmpeg, so ensure it's installed for audio extraction
- Downloads are stored in `./downloads` by default; change with `--output-dir`

---

Invoke the media-downloader agent to handle download operations and format optimization.
