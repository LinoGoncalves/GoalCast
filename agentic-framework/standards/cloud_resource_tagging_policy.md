# Cloud Resource Tagging Policy (2025)

## Purpose
Establish a consistent, automated tagging standard for all cloud resources (Azure, AWS, GCP, on-prem) to support cost management, security, compliance, and AI/ML/data residency requirements.

---

## Tagging Principles
- **Mandatory for all resources** (compute, storage, networking, AI/ML, vector DB, etc.)
- **Automated enforcement** via IaC (Terraform, Bicep, ARM, CloudFormation)
- **Immutable tags for compliance** (e.g., POPIA, GDPR, internal audits)
- **No resource may be deployed without required tags**

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

## Tagging Enforcement
- **IaC modules must validate tags at plan/apply time**
- **CI/CD pipelines must block deployments missing required tags**
- **Cloud policies (Azure Policy, AWS Config, GCP Org Policy) must audit and remediate tag drift**

---

## Tagging for AI/ML & Data Workloads
- Tag all AI/ML compute, storage, and vector DB resources with `MLModel`, `VectorDB`, and `DataResidency`.
- Use `Confidential` for any resource processing PII or sensitive data.
- Ensure tags are propagated to ephemeral/auto-scaled resources (e.g., spot VMs, serverless, batch jobs).

---

## Review & Updates
- Tagging policy must be reviewed annually or when new cloud services are adopted.
- All exceptions must be documented and approved by the security/compliance team.
