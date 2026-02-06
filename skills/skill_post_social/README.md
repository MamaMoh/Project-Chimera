# Skill: Post Social

## Overview

Publishes content to social platforms (Twitter, Instagram, Threads) via the MCP tool `social.post_content`. Supports text and optional media; enforces disclosure level when required by platform policy.

## Skill Information

| Field | Value |
|-------|-------|
| **Name** | skill_post_social |
| **Version** | 1.0.0 |
| **Type** | Runtime Skill |
| **Category** | Content Distribution |

## Purpose

This skill enables the Chimera Agent to:

- Publish text and optional media to Twitter, Instagram, or Threads
- Set disclosure level (automated | assisted | none) per platform policy
- Return post ID, permalink, and publish timestamp for tracking

## Input Contract

### Input Schema (JSON)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "platform": {
      "type": "string",
      "enum": ["twitter", "instagram", "threads"],
      "description": "Target platform"
    },
    "text_content": {
      "type": "string",
      "description": "Post body text"
    },
    "media_urls": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Optional list of media URLs to attach"
    },
    "disclosure_level": {
      "type": "string",
      "enum": ["automated", "assisted", "none"],
      "description": "Disclosure level when required by platform policy"
    }
  },
  "required": ["platform", "text_content"]
}
```

### Example Input

```json
{
  "platform": "twitter",
  "text_content": "Check out our latest AI insights.",
  "media_urls": ["https://cdn.example.com/image.png"],
  "disclosure_level": "automated"
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
    "post_id": { "type": "string" },
    "permalink": { "type": "string", "format": "uri" },
    "published_at": { "type": "string", "format": "date-time", "description": "ISO-8601" },
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
  "post_id": "1234567890_abcdef",
  "permalink": "https://twitter.com/user/status/1234567890",
  "published_at": "2025-02-06T14:30:00Z"
}
```

### Example Output (Error)

```json
{
  "success": false,
  "post_id": null,
  "permalink": null,
  "published_at": null,
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many posts; retry after cooldown."
  }
}
```

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| INVALID_PLATFORM | 400 | Platform not supported or misconfigured |
| CONTENT_REJECTED | 400 | Content or media rejected by platform |
| RATE_LIMITED | 429 | Too many requests; retry after cooldown |
| AUTH_FAILED | 401 | Credentials invalid or expired |
| PLATFORM_ERROR | 502 | Platform API returned error |
| DISCLOSURE_REQUIRED | 400 | disclosure_level required by policy but missing |
| UNKNOWN_ERROR | 500 | Unexpected error occurred |

## Dependencies

- **MCP tool:** `social.post_content`
- **python-dotenv** >= 1.0.0 — Configuration / credentials (if used)

## Usage Example

```python
from chimera.skills.skill_post_social import post_social

async def publish_update():
    result = await post_social(
        platform="twitter",
        text_content="New post from Chimera.",
        media_urls=[],
        disclosure_level="automated"
    )

    if result["success"]:
        print(f"Posted: {result['permalink']}")
        return result["post_id"]
    else:
        print(f"Error: {result['error']['message']}")
        return None
```

## Integration Points

- **Called By:** Content Generator Agent, scheduling pipeline
- **Calls:** MCP tool `social.post_content`
- **Inputs From:** Content generation and media preparation steps
- **Stores:** Post ID and permalink for analytics/tracking

## Performance Requirements

| Metric | Target |
|--------|--------|
| Success Rate | 98% for valid content and credentials |
| Latency | Within platform API limits |
| Disclosure | Must set disclosure_level when required by platform policy |

## Security Considerations

- **Credentials:** Stored in environment variables or secure config
- **Disclosure:** Must set disclosure_level when required by platform policy
- **Content:** No sensitive data in logs; validate media URLs

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Feb 6, 2025 | Initial specification (refactored to full format) |

---

This skill is part of the Chimera Autonomous Influencer System. See specs/functional.md for usage context.
