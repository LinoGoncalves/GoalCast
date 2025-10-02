# Infrastructure as Code (IaC) Standards (2025)

## Purpose
Define best practices for provisioning, managing, and securing cloud and on-prem resources using IaC tools (Terraform, Bicep, Pulumi, etc.) for AI/ML, LLM, and vector DB workloads.

---

## 1. Tooling
- **Primary:** Terraform (multi-cloud), Bicep (Azure), Pulumi (TypeScript/Python)
- **Version Pinning:** All modules and providers must be version-locked
- **IaC code must be stored in version control (git)**

---

## 2. Structure & Modularity
- Use modular, reusable components for all resources (compute, storage, networking, AI/ML, vector DB)
- Separate environments (dev, test, prod) by directory or workspace
- Use remote state with encryption (e.g., Azure Blob, AWS S3, GCP GCS)

---

## 3. Security & Compliance
- Enforce least privilege via managed identities/service principals
- All secrets/keys must be stored in secure vaults (Azure Key Vault, AWS Secrets Manager, etc.)
- Tag all resources per the tagging policy
- Enable logging, monitoring, and audit trails for all critical resources
- Validate data residency and compliance (POPIA, GDPR) in resource definitions

---

## 4. Automation & CI/CD
- All IaC changes must go through code review and automated testing (e.g., `terraform plan`, `bicep linter`)
- Use CI/CD pipelines for deployment (GitHub Actions, Azure DevOps, etc.)
- Block merges/deployments on policy violations or missing tags

---

## 5. Documentation
- Every module must include a README with usage, inputs/outputs, and examples
- All resources must be documented in the system architecture diagrams

---

## 6. Drift Detection & Remediation
- Run drift detection regularly (e.g., `terraform plan` in CI)
- Remediate drift via IaC, not manual changes

---

## 7. Review & Updates
- Review standards annually or when adopting new cloud services/tools
- All exceptions must be documented and approved by the cloud/security team
