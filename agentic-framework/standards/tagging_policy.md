# Tagging Policy (2025)

## Purpose
Define a universal tagging standard for all resources (cloud, on-prem, data, ML/LLM/vector DB) to support cost management, security, compliance, and operational efficiency.

---

## Tagging Scope
- Applies to all cloud and on-prem resources (compute, storage, networking, AI/ML, vector DB, data pipelines, etc.)
- Applies to all environments (dev, test, staging, prod)
- Applies to all ML/LLM models, datasets, and experiment artifacts

---

## Required Tags
| Tag Key         | Description                                 | Example Value                |
|-----------------|---------------------------------------------|------------------------------|
| `Project`       | Project or system name                      | call-centre-agent            |
| `Environment`   | dev, test, staging, prod                    | prod                         |
| `Owner`         | Responsible team or person                  | ai-team@company.com          |
| `CostCenter`    | Billing or cost allocation code              | CC1234                       |
| `DataResidency` | Data residency/compliance zone              | ZA, EU, US                   |
| `Confidential`  | Data classification (yes/no)                | yes                          |
| `MLModel`       | ML/LLM model name/version (if applicable)   | mistral-7b-v1                |
| `VectorDB`      | Vector DB type/version (if applicable)      | qdrant-1.8.0                 |
| `IaC`           | IaC tool/version used for deployment        | terraform-1.7.0              |
| `DeployedBy`    | Automation or user who deployed             | github-actions                |

---

## Tagging Best Practices
- Tags must be applied at resource creation via IaC or automation
- Tags must be immutable for compliance and audit purposes
- Tag values must be standardized (use enums or controlled vocabularies where possible)
- Tags must be validated in CI/CD pipelines and IaC modules
- Tagging policy must be reviewed annually or when new resource types are introduced

---

## Tagging for ML/LLM & Data Assets
- All models, datasets, and experiment artifacts must be tagged with `Project`, `Owner`, `Environment`, `MLModel`, and `DataResidency`
- Use `Confidential` for any asset containing PII or sensitive data
- Tag experiment runs and artifacts in MLflow, DVC, or similar tools

---

## Compliance & Auditing
- Tagging compliance must be monitored via cloud policies and automated audits
- All exceptions must be documented and approved by the compliance team
