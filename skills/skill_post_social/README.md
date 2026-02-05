# skill_post_social
Purpose: Publish content to a social platform via MCP tools.

## Inputs
- platform: string (twitter | instagram | threads)
- text_content: string
- media_urls: array of strings (optional)
- disclosure_level: string (automated | assisted | none)

## Outputs
- post_id: string
- permalink: string
- published_at: ISO-8601 string

## Constraints
- Uses MCP tool `social.post_content`
- Must set disclosure_level when required by platform policy
