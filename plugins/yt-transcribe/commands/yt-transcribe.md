---
model: claude-sonnet-4-5
allowed-tools: Task, Bash, Read, Write, WebFetch
argument-hint: <video-url> [--output-format format] [--summary] [--language lang]
description: Transcribe a YouTube video and extract key insights
---

# YouTube Transcribe Command

Transcribe a YouTube video, fetch the transcript, and extract key insights and summaries.

## Arguments

**$1 (Required)**: `video-url`

The full YouTube URL to transcribe. Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

**Optional flags**:

- `--output-format` - Output format: `text` (default), `markdown`, `json`, `vtt`
- `--summary` - Generate a concise summary alongside full transcript
- `--language` - Specific language code (e.g., `en`, `es`, `fr`). Default: auto-detect
- `--timestamps` - Include timestamps in output
- `--speakers` - Identify and separate speaker segments

## Examples

```bash
/yt-transcribe "https://www.youtube.com/watch?v=VIDEO_ID"
/yt-transcribe "https://www.youtube.com/watch?v=VIDEO_ID" --summary --format markdown
/yt-transcribe "https://www.youtube.com/watch?v=VIDEO_ID" --language es --timestamps
/yt-transcribe "https://www.youtube.com/watch?v=VIDEO_ID" --summary --speakers
```

## How It Works

1. **Video Analysis** - Uses the video-analyzer agent to inspect the video
2. **Transcript Fetching** - Uses the transcript-fetcher agent to get the best available transcript
3. **Processing** - Uses the transcript-processor agent to format and optionally summarize
4. **Output** - Delivers transcript in your specified format

## Output

The command returns:
- Complete transcript with timestamps (if requested)
- Speaker identification and segmentation (if requested)
- Summary and key points (if requested)
- Metadata including duration, language, source quality

## Tips

- For videos without captions, the system will attempt speech-to-text transcription
- Add `--summary` to get a concise overview alongside the full transcript
- Use `--speakers` to identify who's speaking and when
- Markdown format is best for reading; JSON is best for downstream processing

---

Invoke the transcript-fetcher agent to retrieve the transcript, then use the transcript-processor agent to format and analyze it.
