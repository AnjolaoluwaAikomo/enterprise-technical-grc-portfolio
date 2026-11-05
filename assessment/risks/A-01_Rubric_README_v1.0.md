# A-01 — Risk scoring rubric v1.0

**SIMULATED — FICTIONAL DATA — NOT FROM A LIVE SYSTEM.**

Authority: A-01_MapleBridge_Risk_Assessment_Methodology_v1.0.docx (and PDF). Version: 1.0, 2026-11-05.

## Rules
- Inherent and residual likelihood/impact each use integer levels 1–5. `score = likelihood * impact`.
- Low 1–4; Moderate 5–9; High 10–16; Critical 17–25. No rounding.
- Score impact independently for customer harm, service outage, CAD financial loss, compliance/contractual exposure, and reputation. Use the **maximum credible** impact. Full descriptions and calibration examples are in the methodology document; CSV labels are compact machine-readable references.
- Horizon: next 12 months. No statistical probability claim.
- Residual risk cannot be reduced without verified operating evidence; otherwise `Unknown` / provisional.
- Escalate credible impact=5 scenarios and material regulatory concerns regardless of band.
- Response timeframes are proposed planning defaults, not approved risk appetite.
- Preserve baseline scores; changes require dated versioned records and evidence.
- No assessed risk findings, management approvals, certification or independent assurance are asserted.

## Git placement and versioning
Place DOCX/PDF/CSV/README in `governance/authoritative/` or the project-approved methodology directory; risk records in `assessment/risks/`. Commit the rubric and document together. To change a rule, create v1.1 or v2.0 with a decision record; do not rewrite v1.0 historical scoring.
