# Skill: Download YouTube

## Overview

Downloads a YouTube video asset for downstream processing (transcription, analysis, repurposing). Uses the MCP tool `youtube.download_video`.

## Skill Information

| Field | Value |
|-------|-------|
| **Name** | skill_download_youtube |
| **Version** | 1.0.0 |
| **Type** | Runtime Skill |
| **Category** | Content Acquisition |

## Purpose

This skill enables the Chimera Agent to:

- Download YouTube videos for content analysis and transcription
- Enforce maximum duration to avoid oversized downloads
- Provide a local path and source ID for downstream skills

## Input Contract

### Input Schema (JSON)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "format": "uri",
      "description": "YouTube video URL"
    },
    "max_duration_seconds": {
      "type": "integer",
      "minimum": 1,
      "description": "Maximum allowed video duration in seconds"
    }
  },
  "required": ["url", "max_duration_seconds"]
}
```

### Example Input

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "max_duration_seconds": 600
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
    "local_path": { "type": "string", "description": "Path to downloaded file" },
    "duration_seconds": { "type": "number" },
    "source_id": { "type": "string", "description": "YouTube video ID" },
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
  "local_path": "/data/downloads/youtube_abc123.mp4",
  "duration_seconds": 245.5,
  "source_id": "dQw4w9WgXcQ"
}
```

### Example Output (Error)

```json
{
  "success": false,
  "local_path": null,
  "duration_seconds": null,
  "source_id": null,
  "error": {
    "code": "DURATION_EXCEEDED",
    "message": "Video duration exceeds max_duration_seconds."
  }
}
```

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| DURATION_EXCEEDED | 400 | Video duration exceeds max_duration_seconds |
| VIDEO_UNAVAILABLE | 404 | Video is private, deleted, or region-locked |
| INVALID_URL | 400 | URL is not a valid YouTube URL |
| DOWNLOAD_FAILED | 502 | MCP tool or platform returned error |
| STORAGE_ERROR | 507 | Insufficient storage space |
| UNKNOWN_ERROR | 500 | Unexpected error occurred |

## Dependencies

- **MCP tool:** `youtube.download_video`
- **python-dotenv** >= 1.0.0 — Configuration management (if used)

## Usage Example

```python
from chimera.skills.skill_download_youtube import download_youtube

async def fetch_video():
    result = await download_youtube(
        url="https://www.youtube.com/watch?v=abc123",
        max_duration_seconds=600
    )

    if result["success"]:
        return result["local_path"]
    else:
        print(f"Error: {result['error']['message']}")
        return None
```

## Integration Points

- **Called By:** Content Generator Agent, trend processing pipelines
- **Calls:** MCP tool `youtube.download_video`
- **Outputs To:** skill_transcribe_audio for transcription
- **Stores In:** Configurable download directory

## Performance Requirements

| Metric | Target |
|--------|--------|
| Success Rate | 95% average for public videos |
| Max Duration | Enforced via max_duration_seconds |
| Timeout | Align with MCP tool configuration |

## Security Considerations

- **URL validation:** Only YouTube URLs accepted
- **Duration cap:** Prevents unbounded downloads
- **Storage:** Temporary files cleaned after processing when applicable

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Feb 6, 2025 | Initial specification (refactored to full format) |

---

This skill is part of the Chimera Autonomous Influencer System. See specs/functional.md for usage context.
