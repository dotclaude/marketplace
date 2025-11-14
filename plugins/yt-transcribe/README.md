# YouTube Transcribe & Download

**Download videos, fetch transcripts, and analyze YouTube content**

Download videos with yt-dlp (with JavaScript support), fetch transcripts via API, and perform intelligent analysis with built-in speech-to-text capabilities.

## 🎯 Commands

- **`/yt-transcribe`** - Main command to transcribe a video
- **`/yt-download`** - Download a video with format selection
- **`/yt-analyze`** - Analyze video metadata and transcript quality
- **`/yt-fetch-transcript`** - Fetch transcript via API or speech-to-text

## 📦 Installation

```bash
# Add the dotclaude marketplace
/plugin marketplace add dotclaude/marketplace

# All plugins install automatically with the marketplace
```

## 🚀 Quick Start

```bash
/yt-transcribe "https://www.youtube.com/watch?v=VIDEO_ID"
/yt-download "https://www.youtube.com/watch?v=VIDEO_ID" --format best
/yt-analyze "https://www.youtube.com/watch?v=VIDEO_ID"
/yt-fetch-transcript "https://www.youtube.com/watch?v=VIDEO_ID" --method api
```

## 💡 Use Cases

- **Content Analysis** - Transcribe videos, extract key points, summarize content
- **Research & Documentation** - Download and analyze educational content, lectures
- **Accessibility** - Generate transcripts for videos without captions
- **Data Collection** - Extract transcript data for NLP analysis or archival
- **Quality Checking** - Validate transcript accuracy and completeness

## 🔧 Requirements

- **yt-dlp** - For downloading videos with JavaScript support
- **Python 3.7+** - Runtime for yt-dlp and transcript processing
- **ffmpeg** (optional) - For video format conversion
- **OpenAI Whisper** (optional) - For local speech-to-text transcription

## 📄 License

MIT License - see LICENSE file for details

## 🌟 Part of the DotClaude Ecosystem

Complete development pipeline with 14 specialized plugins:
- **Adaptive Learning** - Skill building and teaching
- **Dev Accelerator** - TDD and development workflows
- **Insight Engine** - Meta-cognitive analysis
- **Personalities** - Multi-persona problem solving
- **Data Intelligence & Analytics** - Data processing
- **YouTube Transcribe & Download** - This plugin
- [8 more plugins](https://github.com/dotclaude/marketplace)

---

**Ready to get started?** Install the marketplace and access all DotClaude plugins.
