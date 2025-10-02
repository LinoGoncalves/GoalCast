# User Story Template (2025)

## 1. User Story (Gherkin Format)
```
As a <role>,
I want <feature/goal>,
So that <business value/benefit>.
```

---

## 2. Acceptance Criteria (Gherkin)
```
Given <context>
When <action>
Then <expected outcome>
```

*Repeat for each scenario. Use clear, testable language.*

---

## 3. Additional Details
- **Priority:** (Must, Should, Could)
- **Dependencies:** (other stories, technical, data)
- **Non-Functional Requirements:** (performance, security, accessibility, compliance)
- **Data Residency/Compliance:** (POPIA, GDPR, etc.)

---

## 4. Traceability
- **Epic/Feature Link:**
- **Related Test Cases:**
- **Stakeholders:**

---

## 5. Example
```
As a call centre agent,
I want to see similar legacy tickets for a new customer query,
So that I can resolve issues faster and ensure compliance.

Acceptance Criteria:
Given a new customer query,
When the system retrieves similar tickets using the LLM and vector DB,
Then the agent sees the top 5 most relevant tickets with compliance tags.
```
