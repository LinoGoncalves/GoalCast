
# API Design Patterns (2025)

## Overview

This document outlines best-practice API design patterns for Python-based systems, including FastAPI, LLM integration, and vector database (Qdrant, Milvus, Weaviate, Chroma) backends. All patterns are compatible with multi-agent, multi-tool, and compliance-driven environments.

---

## 1. General Principles

- **RESTful by Default**: Use REST for CRUD, but support GraphQL or gRPC for advanced use cases.
- **OpenAPI First**: Define all endpoints with OpenAPI 3.1+ specs. Auto-generate docs.
- **Versioning**: Use URI versioning (`/v1/`), never break existing clients.
- **Idempotency**: All POST/PUT/PATCH endpoints must be idempotent where possible.
- **Statelessness**: APIs must not rely on server-side session state.
- **Security**: Enforce OAuth2/JWT, input validation, and output sanitization (see secure_coding_checklist.md).
- **Compliance**: Support data residency, audit logging, and consent management (POPIA/GDPR).

---

## 2. Endpoint Design

- **Nouns, Not Verbs**: Use resource-based URIs (`/tickets/`, `/agents/`, `/llm/classify/`).
- **Pluralization**: Use plural nouns for collections (`/tickets/`).
- **Filtering & Pagination**: Use query params (`?status=open&page=2&limit=50`).
- **Error Handling**: Standardize error responses (see below).
- **Async Operations**: For long-running tasks, return 202 with a status endpoint.

---

## 3. Response Patterns

- **Consistent Envelope**:



```json
{
	"success": true,
	"data": {...},
	"error": null,
	"meta": {...}
}
```

- **Error Format**:



```json
{
	"success": false,
	"data": null,
	"error": {
		"code": "VALIDATION_ERROR",
		"message": "Field 'email' is required.",
		"details": {...}
	},
	"meta": {...}
}
```

- **HTTP Status Codes**: Use 2xx for success, 4xx for client errors, 5xx for server errors.

---

## 4. LLM & Vector DB Integration

- **LLM Endpoints**: Expose `/llm/classify/`, `/llm/generate/`, `/llm/embeddings/` with clear input/output schemas.
- **Vector Search**: Use `/search/vector/` with POST for complex queries (payload: query, filters, top_k).
- **Streaming**: For large LLM responses, support HTTP chunked transfer or WebSockets.
- **Metadata**: Always return inference metadata (model, version, latency, compliance tags).

---

## 5. FastAPI Patterns

- **Dependency Injection**: Use FastAPI's `Depends` for auth, DB, and config.
- **Pydantic Models**: All request/response bodies must use Pydantic for validation.
- **Background Tasks**: Use FastAPI's `BackgroundTasks` for async jobs.
- **CORS**: Restrict origins, support preflight requests.

---

## 6. API Documentation

- **Auto-Docs**: Serve Swagger UI and ReDoc at `/docs` and `/redoc`.
- **Examples**: Provide request/response examples for all endpoints.
- **Changelog**: Maintain API changelog in OpenAPI `info` section.

---

## 7. Testing & Quality Gates

- **Contract Tests**: Use Schemathesis or Dredd for OpenAPI contract testing.
- **Integration Tests**: Cover all endpoints, including LLM/vector DB flows.
- **Rate Limiting**: Test for abuse scenarios.

---

## 8. Multi-Agent & Tool Compatibility

- **Agent Metadata**: All endpoints must support agent context headers (e.g., `X-Agent-Id`, `X-Tool-Name`).
- **YAML/JSON**: Accept and return both YAML and JSON where feasible.
- **Extensibility**: Design for new agent types and tools without breaking changes.

---

## 9. Compliance & Observability

- **Audit Logging**: Log all access and mutations with agent/user context.
- **PII Masking**: Mask sensitive fields in logs and responses.
- **Tracing**: Support OpenTelemetry for distributed tracing.

---

## 10. References

- See `coding_styleguide.md`, `secure_coding_checklist.md`, `testing_strategy.md`, and `architectural-principles.md` for further details.

---

---

Last updated: 2025-10-01
