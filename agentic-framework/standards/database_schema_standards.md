
# Database Schema Standards (2025)

## Overview

This document defines schema standards for relational, NoSQL, and vector databases in AI/ML, LLM, and agentic systems. It supports compliance, scalability, and interoperability.

---

## 1. General Principles
- Use clear, consistent naming conventions (snake_case for tables/fields)
- Document all schemas with ERDs and data dictionaries
- Enforce primary keys and unique constraints

## 2. Relational DB Standards
- Normalize to 3NF unless justified
- Use foreign keys for referential integrity
- Index frequently queried fields

## 3. NoSQL DB Standards
- Define clear partition/sharding keys
- Document schema evolution and versioning
- Apply access control at collection/bucket level

## 4. Vector DB Standards
- Store embeddings as arrays/vectors with metadata
- Use UUIDs for unique identification
- Document vector dimensions and model provenance

## 5. Compliance & Security
- Mask or encrypt PII/PHI fields
- Enforce data residency and retention policies
- Log all schema changes and access events

---

## References
- See `data_pipeline_patterns.md`, `network_security_policy.md`, and `secure_coding_checklist.md` for more details.

Last updated: 2025-10-01
