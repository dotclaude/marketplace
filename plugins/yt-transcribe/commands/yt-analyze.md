---
model: claude-sonnet-4-5
allowed-tools: Task, Bash, Read, Write, WebFetch
argument-hint: <video-url> [--detailed] [--check-captions] [--quality-report]
description: Analyze YouTube video metadata and technical properties
---

# YouTube Analyze Command

Inspect and analyze a YouTube video without downloading it. Get detailed metadata, assess transcribability, check available captions, and generate quality reports.

## Arguments

**$1 (Required)**: `video-url`

The full YouTube URL to analyze. Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

**Optional flags**:

- `--detailed` - Show comprehensive technical specifications (codecs, bitrates, etc.)
- `--check-captions` - Detailed inspection of available subtitle/caption tracks
- `--quality-report` - Generate quality assessment and transcription feasibility report
- `--format-options` - List all available format combinations
- `--estimate-sizes` - Estimate file sizes for each available quality

## Examples

```bash
/yt-analyze "https://www.youtube.com/watch?v=VIDEO_ID"
/yt-analyze "https://www.youtube.com/watch?v=VIDEO_ID" --detailed --check-captions
/yt-analyze "https://www.youtube.com/watch?v=VIDEO_ID" --quality-report --format-options
/yt-analyze "https://www.youtube.com/watch?v=VIDEO_ID" --detailed --estimate-sizes
```

## How It Works

The analyzer inspects the video and provides:

1. **Basic Metadata** - Title, channel, duration, view count, upload date
2. **Technical Specs** - Available codecs, resolutions, frame rates, bitrates
3. **Caption Analysis** - Available subtitles, auto-generated status, language options
4. **Access Information** - Age restrictions, geo-blocking, authentication requirements
5. **Quality Assessment** - Estimated transcription quality, audio clarity indicators
6. **Format Recommendations** - Best formats for different use cases (streaming, archival, etc.)

## Output Structure

```
Video: {Title}
Channel: {Channel Name}
Duration: {HH:MM:SS}
Published: {Date}

METADATA
- Views: {count}
- Likes: {count}
- Language: {language}

CAPTION TRACKS
- English (auto-generated)
- Spanish (user-provided)
- French (user-provided)

TECHNICAL SPECIFICATIONS
- Best video: {codec} @ {resolution}p {fps}
- Best audio: {codec} {bitrate}
- Available formats: {count}

QUALITY ASSESSMENT
- Transcription feasibility: {High/Medium/Low}
- Recommended approach: {API/Speech-to-text/Manual}
- Audio clarity: {Good/Fair/Poor}

RECOMMENDATIONS
- For download: {recommended format}
- For transcription: {recommended method}
- For streaming: {recommended quality}
```

## Tips

- Use without flags for quick overview
- Add `--quality-report` to assess transcription reliability before committing to download
- Check `--captions` to see all available subtitle options before downloading
- Use `--estimate-sizes` to plan bandwidth if internet is limited
- Detailed technical info is helpful for troubleshooting download issues

---

Invoke the video-analyzer agent to perform comprehensive video inspection and quality assessment.
