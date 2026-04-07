---
model: sonnet
allowed-tools: Task, Read, Write, Bash(*), Glob, Grep
argument-hint: <service-or-endpoint> [audience]
description: API Reference documentation shortcut — assembles an API-focused persona team to produce endpoint docs, schemas, auth flows, error codes, and code examples
---

# API Reference Documentation Command

Shortcut for producing API Reference Guides. Pre-selects the API document type and assembles an API-focused documentation team to produce complete endpoint documentation with schemas, authentication flows, error codes, and working code examples.

## How It Works

This command invokes the doc-coordinator agent in API Reference mode to:
1. Assemble an API-focused team (API Specialist lead + Domain Researcher + Accuracy Reviewer + Technical Writer)
2. Research endpoints, schemas, and authentication from available source material
3. Present an API Document Plan for your approval
4. Draft complete endpoint documentation with request/response examples
5. Review for technical accuracy and completeness
6. Iterate based on your feedback

## Arguments

**$1 (Required)**: Service name, endpoint path, or API area to document

**$2 (Optional)**: Target audience
- `developer`: Internal engineers integrating with the API (default)
- `external-consumer`: External third-party developers
- If not specified, defaults to `developer`

## Examples

### Full Service API Documentation
```bash
/api-doc "Payment Processing Service"
```
Documents all endpoints for the Payment Processing Service with auth, schemas, errors, and examples.

### Specific Endpoint Group
```bash
/api-doc "/api/v2/users/*"
```
Documents the user-related endpoint group with CRUD operations, filtering, pagination, and error handling.

### External Consumer Focus
```bash
/api-doc "Webhook Delivery API" external-consumer
```
Documents the webhook API with emphasis on setup, payload schemas, retry behavior, signature verification, and SDK examples — written for external consumers who need clear integration guidance.

### Authentication Flow
```bash
/api-doc "OAuth2 Authorization Flow"
```
Documents the OAuth2 flow with token endpoints, scopes, refresh patterns, and error scenarios.

## What Gets Documented

The API Specialist ensures comprehensive coverage of:

| Section | Contents |
|---------|----------|
| **Overview** | API purpose, base URL, versioning strategy |
| **Authentication** | Auth methods, token lifecycle, scopes/permissions |
| **Endpoints** | Method, path, description, parameters, request/response |
| **Request Examples** | Working curl/SDK examples for each endpoint |
| **Response Schemas** | JSON schemas with field descriptions and types |
| **Error Codes** | Status codes, error response format, troubleshooting |
| **Rate Limiting** | Limits, headers, retry strategies |
| **Pagination** | Pagination pattern, cursor/offset usage |
| **Webhooks** | Event types, payload schemas, delivery guarantees (if applicable) |
| **Changelog** | Version history and breaking changes (if applicable) |

## Team Composition

| Persona | Role in API Docs |
|---------|-----------------|
| **API Specialist** (Lead) | Writes endpoint docs, schemas, examples, auth flows |
| **Domain Researcher** | Reads code to extract endpoint behavior, edge cases, and undocumented details |
| **Accuracy Reviewer** | Verifies all endpoints, parameters, and examples against actual code |
| **Technical Writer** | Ensures clear prose, consistent formatting, and logical section flow |
| **Audience Advocate** | Added for external-consumer audience to ensure integration-friendly writing |
| **Information Architect** | Added for large API surfaces to organize endpoint groups and navigation |

## Output Format

```markdown
## API Reference: [Service/Endpoint Name]

### Overview
[API purpose, base URL, versioning]

### Authentication
[Auth methods, token examples, scopes]

### Endpoints

#### [METHOD] /path/to/endpoint
**Description**: [What this endpoint does]

**Parameters**:
| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| ... | ... | ... | ... | ... |

**Request Example**:
\`\`\`bash
curl -X POST https://api.example.com/v1/resource \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
\`\`\`

**Response** (200 OK):
\`\`\`json
{
  "id": "res_123",
  "status": "created"
}
\`\`\`

**Error Responses**:
| Status | Code | Description |
|--------|------|-------------|
| 400 | INVALID_REQUEST | Request body validation failed |
| 401 | UNAUTHORIZED | Missing or invalid authentication |
| 404 | NOT_FOUND | Resource does not exist |

[Continue for all endpoints]

### Rate Limiting
[Limits, headers, retry guidance]

### Error Reference
[Complete error code catalog]

### Changelog
[Version history]
```

## Tips for Best API Docs

1. **Point to Source Code**: Share the service repo, route definitions, or OpenAPI spec if available
2. **Mention Auth Type**: Note if it uses API keys, OAuth2, JWT, or other auth mechanisms
3. **Flag Special Behavior**: Mention idempotency, async operations, webhooks, or batch endpoints
4. **Specify Audience**: External consumers need more context than internal developers
5. **Include Versioning**: Note the API version and any deprecation policies

Invoke the doc-coordinator agent with API Reference mode: $ARGUMENTS
