# skill_download_youtube
Purpose: Download a YouTube video asset for downstream processing.

## Inputs
- url: string (YouTube URL)
- max_duration_seconds: integer

## Outputs
- local_path: string
- duration_seconds: integer
- source_id: string

## Constraints
- Uses MCP tool `youtube.download_video`
- Fails if duration exceeds max_duration_seconds
