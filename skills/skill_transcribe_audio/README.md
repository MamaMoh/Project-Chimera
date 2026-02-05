# skill_transcribe_audio
Purpose: Transcribe audio into text segments for content generation.

## Inputs
- audio_path: string
- language: string

## Outputs
- transcript: string
- segments: array of { start_ms, end_ms, text }

## Constraints
- Uses MCP tool `audio.transcribe`
- No storage of raw audio in long-term memory
