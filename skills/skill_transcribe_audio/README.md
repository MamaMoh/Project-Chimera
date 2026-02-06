# Skill: Transcribe Audio

## Overview

Transcribes audio into text and time-coded segments for content generation. Uses the MCP tool `audio.transcribe`. Raw audio is not stored in long-term memory.

## Skill Information

| Field | Value |
|-------|-------|
| **Name** | skill_transcribe_audio |
| **Version** | 1.0.0 |
| **Type** | Runtime Skill |
| **Category** | Content Processing |

## Purpose

This skill enables the Chimera Agent to:

- Convert audio (e.g. from downloaded video) into transcript text
- Produce segments with start/end times for subtitles or editing
- Support content repurposing and search without retaining raw audio

## Input Contract

### Input Schema (JSON)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "audio_path": {
      "type": "string",
      "description": "Path to audio file (local or accessible URI)"
    },
    "language": {
      "type": "string",
      "description": "Language code for transcription (e.g. en, es)"
    }
  },
  "required": ["audio_path", "language"]
}
```

### Example Input

```json
{
  "audio_path": "/data/downloads/youtube_abc123.mp4",
  "language": "en"
}
```

## Output Contract

### Output Schema (JSON)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "success": { "type": "boolean" },
    "transcript": { "type": "string", "description": "Full transcript text" },
    "segments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "start_ms": { "type": "integer" },
          "end_ms": { "type": "integer" },
          "text": { "type": "string" }
        }
      }
    },
    "error": {
      "type": "object",
      "properties": {
        "code": { "type": "string" },
        "message": { "type": "string" }
      }
    }
  }
}
```

### Example Output (Success)

```json
{
  "success": true,
  "transcript": "Welcome to the channel. Today we're covering AI trends.",
  "segments": [
    { "start_ms": 0, "end_ms": 1200, "text": "Welcome to the channel." },
    { "start_ms": 1200, "end_ms": 3500, "text": "Today we're covering AI trends." }
  ]
}
```

### Example Output (Error)

```json
{
  "success": false,
  "transcript": null,
  "segments": null,
  "error": {
    "code": "FILE_NOT_FOUND",
    "message": "Audio file not found or not accessible."
  }
}
```

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| FILE_NOT_FOUND | 404 | Audio file not found or not accessible |
| UNSUPPORTED_FORMAT | 400 | Audio format not supported |
| TRANSCRIPTION_FAILED | 502 | MCP tool or provider returned error |
| LANGUAGE_NOT_SUPPORTED | 400 | Language code not supported |
| QUOTA_EXCEEDED | 429 | Transcription quota exceeded |
| UNKNOWN_ERROR | 500 | Unexpected error occurred |

## Dependencies

- **MCP tool:** `audio.transcribe`
- **python-dotenv** >= 1.0.0 — Configuration (if used)

## Usage Example

```python
from chimera.skills.skill_transcribe_audio import transcribe_audio

async def get_transcript():
    result = await transcribe_audio(
        audio_path="/data/downloads/video.mp4",
        language="en"
    )

    if result["success"]:
        return result["transcript"], result["segments"]
    else:
        print(f"Error: {result['error']['message']}")
        return None, []
```

## Integration Points

- **Called By:** Content Generator Agent, trend analysis pipeline
- **Calls:** MCP tool `audio.transcribe`
- **Inputs From:** skill_download_youtube or skill_download_video (local file path)
- **Outputs To:** Content generation, subtitles, search indexing
- **Storage:** No long-term storage of raw audio

## Performance Requirements

| Metric | Target |
|--------|--------|
| Success Rate | 95% for supported formats and languages |
| Latency | Within MCP/transcription provider limits |
| Segments | start_ms, end_ms, text per segment |

## Security Considerations

- **Privacy:** No storage of raw audio in long-term memory
- **Paths:** Validate audio_path is within allowed directories
- **Credentials:** API keys for transcription in environment variables

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Feb 6, 2025 | Initial specification (refactored to full format) |

---

This skill is part of the Chimera Autonomous Influencer System. See specs/functional.md for usage context.
