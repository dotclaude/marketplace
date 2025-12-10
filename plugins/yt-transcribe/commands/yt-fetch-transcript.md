---
model: claude-sonnet-4-5
allowed-tools: Task, Bash, Read, Write, WebFetch
argument-hint: <video-url> [--method method] [--language lang] [--format format] [--quality quality]
description: Fetch transcript using YouTube API or speech-to-text
---

# YouTube Fetch Transcript Command

Retrieve the transcript from a YouTube video using the fastest available method. Supports YouTube's native transcript API, fallback providers, and speech-to-text.

## Arguments

**$1 (Required)**: `video-url`

The full YouTube URL to fetch transcript from. Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

**Optional flags**:

- `--method` - Retrieval method: `auto` (default), `api`, `speech-to-text`, `fallback`
- `--language` - Specific language code (e.g., `en`, `es`, `fr`). Default: auto-detect
- `--format` - Output format: `text` (default), `markdown`, `json`, `vtt`, `srt`
- `--quality` - Quality preference: `best` (default), `high`, `standard`, `draft`
- `--timestamps` - Include timestamps in transcript
- `--preserve-formatting` - Keep original formatting and paragraph breaks
- `--validate` - Check transcript completeness and quality

## Examples

```bash
/yt-fetch-transcript "https://www.youtube.com/watch?v=VIDEO_ID"
/yt-fetch-transcript "https://www.youtube.com/watch?v=VIDEO_ID" --method api --language en
/yt-fetch-transcript "https://www.youtube.com/watch?v=VIDEO_ID" --method speech-to-text --quality best
/yt-fetch-transcript "https://www.youtube.com/watch?v=VIDEO_ID" --format json --timestamps --validate
```

## Retrieval Methods

### `auto` (Default)
Intelligent fallback chain:
1. Check YouTube's native transcripts (fastest)
2. Look for manually added captions
3. Fall back to auto-generated captions
4. If no captions, use speech-to-text on downloaded video

### `api`
Direct YouTube Transcript API call - fastest if captions exist
- Works for videos with any type of captions
- Returns immediately
- High accuracy (uses existing captions)

### `speech-to-text`
Local transcription using Whisper or similar
- Works for any video with audio
- Slower but doesn't depend on captions
- Good for videos without captions

### `fallback`
Try multiple transcript providers
- YouTube API first
- Third-party providers second
- Speech-to-text as last resort

## Output Formats

- **text** - Plain text with timestamps
- **markdown** - Structured markdown with headers and formatting
- **json** - Structured JSON with timing metadata
- **vtt** - WebVTT subtitle format (for subtitles)
- **srt** - SubRip format (for subtitles)

## Quality Levels

- **best** - Use highest quality available (manual captions preferred)
- **high** - Use auto-generated captions from YouTube
- **standard** - Accept any available captions
- **draft** - Quick retrieval, may be incomplete

## Output

Returns:
- Full transcript text with optional timestamps
- Metadata: language, source (auto-generated vs. human), quality indicator
- Coverage: percentage of video covered by transcript
- Recommendations for quality or alternative methods

## Tips

- `--method auto` provides best balance of speed and quality
- For videos without captions, expect `--method speech-to-text` to take longer
- Use `--format json` for downstream processing and analysis
- Use `--format vtt` or `--format srt` to create subtitle files
- Add `--validate` to check transcript completeness before proceeding
- Use `--quality best` for important content that needs high accuracy

---

Invoke the transcript-fetcher agent to retrieve transcripts via multiple methods and ensure data quality.
