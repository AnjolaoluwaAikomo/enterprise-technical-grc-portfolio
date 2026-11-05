# Enterprise Technical GRC Portfolio

> **SIMULATED — FICTIONAL CASE STUDY — NOT INDEPENDENT ASSURANCE**

This repository showcases practical technical governance, risk, compliance, security assessment, IT general controls, vendor assurance, and automation work through a structured **fictional Canadian fintech** case study.

## MapleBridge Financial Technology Inc.

MapleBridge is a **fictional Ontario-based, non-bank B2B payment service provider** used solely for a portfolio simulation. Its assumed products are BridgeAPI (payment-instruction integration), MatchLedger (reconciliation), and OpsConsole (operational access and reporting). Its fictional processor is CedarPay Processing Ltd.

**This is not a live company, client engagement, independent audit, SOC 2 attestation, ISO certification, or claim of employment experience.** People, customers, vendors, system configurations, interviews and operational logs are simulated. No production systems were accessed.

### Foundation F-01–F-07
- **F-01:** Scenario charter; assumptions and limitations
- **F-02:** Governance, stakeholders, RACI, calendar and interview templates
- **F-03:** Architecture, asset and data-flow inventories
- **F-04:** Canonical identifiers and evidence governance
- **F-05:** Framework source and edition register
- **F-06:** Deterministic synthetic evidence baseline, source records, metadata and integrity hashes
- **F-07:** Repository structure, document templates, project tracker and quality gate

### Repository layout
| Folder | Purpose |
|---|---|
| `source-data/` | Synthetic baseline, future remediation and retest snapshots |
| `assessment/` | Risk, control, ITGC and vendor workpapers (future modules) |
| `automation/` | Future control-check scripts, tests and results |
| `evidence/` | Synthetic evidence metadata and provenance |
| `reports/` | Reusable reporting templates and issued reports |
| `references/` | Framework editions and source governance |
| `governance/` | Foundation deliverables, quality assurance and project tracking |

### Assessment and evidence rules
The simulated assessment covers **2026-09-01 through 2026-10-31**. The frozen synthetic baseline is **BASE-20260930**; later remediation/retest snapshots are reserved, not completed. Source-data exports are **not** control-test results. No risk scores, audit findings, remediation closure conclusions or certification claims exist at the Foundation stage.

Canonical identifiers include `SYS-001`, `AST-001`, `CTRL-001`, `RSK-001`, `EV-001`, `TEST-001`, `FND-001`, `ACT-001`, `VEN-001`. Earlier short IDs such as `SYS-01` remain aliases, not separate records.

NIST CSF 2.0 and NIST SP 800-30 inform governance/risk; AICPA Trust Services Criteria, ISO/IEC 27001:2022 and CSA CCM/CAIQ inform readiness mapping. OSFI B-10/B-13 are **benchmark references**, not asserted direct legal obligations for a non-FRFI. Copyrighted normative text is not reproduced.

### Publication status
This is an **initial repository setup on a review branch**. Foundation deliverables are not considered published until their actual files, synthetic evidence records, and hashes are uploaded and independently checked. The full original local F-07 package remains the authoritative release until then.

### Safety and integrity
Never commit credentials, tokens, private keys, real personal/customer information, or proprietary source documents. Label every synthetic evidence record `SIMULATED — FICTIONAL DATA — NOT FROM A LIVE SYSTEM`. Preserve the frozen baseline and record changes in a dated change log.

### Roadmap
After Foundation QA: Module A (risk), B (SOC 2/ISO readiness), C (automation), D (ITGC), E (vendor assurance), F (executive reporting). Each module is added in a separate reviewed change set.
