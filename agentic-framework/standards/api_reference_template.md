# API Reference Template (2025)

## Overview
This template provides a standardized structure for documenting APIs in Python-based, LLM-enabled, and vector database-integrated systems. It is designed for REST, OpenAPI, and hybrid AI endpoints (FastAPI, LangChain, etc.).

---

## 1. API Metadata
- **Title:**
- **Version:**
- **Status:** (draft, stable, deprecated)
- **Owner:**
- **Last Updated:**

---

## 2. Description
Brief summary of the API's purpose, domain, and key features.

---

## 3. Authentication & Security
- **Auth Method:** (OAuth2, API Key, JWT, etc.)
- **Scopes:**
- **Rate Limits:**
- **Data Residency/Compliance:** (e.g., POPIA, GDPR)

---

## 4. Endpoints
### Example Table
| Method | Path | Summary | Auth | Request Model | Response Model | Status |
|--------|------|---------|------|--------------|---------------|--------|
| GET    | /tickets/{id} | Get ticket by ID | JWT | TicketRequest | TicketResponse | 200 |
| POST   | /llm/query    | LLM RAG query    | API Key | LLMQueryRequest | LLMQueryResponse | 200 |

---

## 5. Request/Response Models
### Example (Pydantic)
```python
class LLMQueryRequest(BaseModel):
	query: str
	top_k: int = 5

class LLMQueryResponse(BaseModel):
	answer: str
	sources: List[str]
```

---

## 6. Error Handling
| Code | Message | Description |
|------|---------|-------------|
| 400  | Bad Request | Invalid input |
| 401  | Unauthorized | Invalid or missing token |
| 500  | Internal Error | Unexpected server error |

---

## 7. Examples
### cURL
```bash
curl -X POST https://api.example.com/llm/query \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I reset my password?"}'
```

### Python (requests)
```python
import requests
resp = requests.post(
	"https://api.example.com/llm/query",
	headers={"Authorization": f"Bearer {token}"},
	json={"query": "How do I reset my password?"}
)
print(resp.json())
```

---

## 8. Changelog
- v1.0.0: Initial release

---

## 9. References
- [OpenAPI 3.1 Spec](https://spec.openapis.org/oas/v3.1.0)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [LangChain API Reference](https://python.langchain.com/docs/api_reference.html)
