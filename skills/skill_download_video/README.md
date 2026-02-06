# Skill: Download Video

## Overview

Downloads videos from various social media platforms for content processing and analysis.

## Skill Information

| Field | Value |
|-------|-------|
| **Name** | skill_download_video |
| **Version** | 1.0.0 |
| **Type** | Runtime Skill |
| **Category** | Content Acquisition |

## Purpose

This skill enables the Chimera Agent to download video content from platforms like YouTube, TikTok, and Twitter/X for:

- Content analysis and transcription
- Trend validation
- Content repurposing
- Quality assessment

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
      "description": "URL of the video to download"
    },
    "platform": {
      "type": "string",
      "enum": ["youtube", "tiktok", "twitter"],
      "description": "Source platform"
    },
    "options": {
      "type": "object",
      "properties": {
        "format": {
          "type": "string",
          "enum": ["mp4", "audio_only"],
          "default": "mp4"
        },
        "quality": {
          "type": "string",
          "enum": ["low", "medium", "high", "best"],
          "default": "high"
        },
        "timeout_seconds": {
          "type": "integer",
          "minimum": 30,
          "maximum": 600,
          "default": 300
        },
        "output_path": {
          "type": "string",
          "description": "Custom output path (optional)"
        }
      }
    }
  },
  "required": ["url", "platform"]
}
```

### Example Input

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "platform": "youtube",
  "options": {
    "format": "mp4",
    "quality": "high",
    "timeout_seconds": 300
  }
}
```

## Output Contract

### Output Schema (JSON)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "request_id": {
      "type": "string",
      "format": "uuid"
    },
    "download": {
      "type": "object",
      "properties": {
        "file_path": {
          "type": "string",
          "description": "Path to downloaded file"
        },
        "file_size_bytes": {
          "type": "integer"
        },
        "duration_seconds": {
          "type": "number"
        },
        "format": {
          "type": "string"
        },
        "resolution": {
          "type": "string"
        },
        "file_extension": {
          "type": "string"
        }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "uploader": {
          "type": "string"
        },
        "upload_date": {
          "type": "string",
          "format": "date"
        },
        "view_count": {
          "type": "integer"
        },
        "like_count": {
          "type": "integer"
        },
        "thumbnail_url": {
          "type": "string",
          "format": "uri"
        }
      }
    },
    "error": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string"
        },
        "message": {
          "type": "string"
        }
      }
    }
  }
}
```

### Example Output (Success)

```json
{
  "success": true,
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "download": {
    "file_path": "/data/downloads/youtube_video_123.mp4",
    "file_size_bytes": 52428800,
    "duration_seconds": 245.5,
    "format": "mp4",
    "resolution": "1920x1080",
    "file_extension": ".mp4"
  },
  "metadata": {
    "title": "Amazing Tech Demo 2025",
    "description": "A look at the latest AI developments",
    "uploader": "TechChannel",
    "upload_date": "2025-01-15",
    "view_count": 150000,
    "like_count": 8500,
    "thumbnail_url": "https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
  }
}
```

### Example Output (Error)

```json
{
  "success": false,
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "download": null,
  "metadata": null,
  "error": {
    "code": "VIDEO_UNAVAILABLE",
    "message": "Video is not available. It may be private or deleted."
  }
}
```

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| VIDEO_UNAVAILABLE | 404 | Video is private, deleted, or region-locked |
| PLATFORM_ERROR | 502 | Platform API returned error |
| DOWNLOAD_TIMEOUT | 408 | Download exceeded timeout |
| INVALID_URL | 400 | URL format invalid for platform |
| RATE_LIMITED | 429 | Too many requests to platform |
| STORAGE_ERROR | 507 | Insufficient storage space |
| UNKNOWN_ERROR | 500 | Unexpected error occurred |

## Dependencies

- **yt-dlp** >= 2023.9.0 — Video downloading backend
- **aiohttp** >= 3.9.0 — Async HTTP client
- **python-dotenv** >= 1.0.0 — Configuration management

## Usage Example

```python
from chimera.skills.skill_download_video import download_video

async def process_trend_video():
    result = await download_video(
        url="https://www.youtube.com/watch?v=abc123",
        platform="youtube",
        options={
            "format": "mp4",
            "quality": "high"
        }
    )

    if result["success"]:
        print(f"Downloaded: {result['metadata']['title']}")
        print(f"Size: {result['download']['file_size_bytes']} bytes")
        return result["download"]["file_path"]
    else:
        print(f"Error: {result['error']['message']}")
        return None
```

## Integration Points

- **Called By:** Content Generator Agent
- **Calls:** Platform-specific APIs (YouTube, TikTok, Twitter)
- **Outputs To:** skill_transcribe_audio for transcription
- **Stores In:** /data/downloads/ (configurable)

## Performance Requirements

| Metric | Target |
|--------|--------|
| Download Speed | 5 MB/s minimum |
| Success Rate | 95% average |
| Timeout | 300 seconds max |
| Concurrent Downloads | 3 max |

## Security Considerations

- **API Keys:** Stored in environment variables
- **File Validation:** Verify file type before processing
- **Storage Limits:** Maximum file size enforced (2GB)
- **Cleanup:** Temporary files deleted after processing

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Feb 4, 2025 | Initial specification |

---

This skill is part of the Chimera Autonomous Influencer System. See specs/functional.md for usage context.
