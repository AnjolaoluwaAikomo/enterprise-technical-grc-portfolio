#!/usr/bin/env python3
"""Validate frozen synthetic baseline; standard library only."""
from pathlib import Path
import csv, hashlib, json, sys
root=Path(__file__).resolve().parent
manifest=root/"governance"/"sha256_manifest.txt"
entries=[]
for line in manifest.read_text().splitlines():
    if not line.strip(): continue
    digest,rel=line.split("  ",1)
    path=root/rel
    assert path.is_file(),f"Missing: {rel}"
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,f"Hash mismatch: {rel}"
    entries.append(rel)
index=json.loads((root/"governance"/"evidence_index.json").read_text())
assert len(index)==12
expected={"hr_roster":85,"hr_terminations":4,"identity_accounts":85,"privileged_role_assignments":5,"access_reviews":4,"change_requests":24,"deployments":24,"cloud_configurations":6,"backup_jobs":30,"restore_tests":2,"vendor_assurance_documents":3,"incident_summaries":2}
for rec in index:
    assert rec["synthetic_data"] is True and rec["snapshot_id"]=="BASE-20260930"
    p=root/rec["file_path"]
    assert hashlib.sha256(p.read_bytes()).hexdigest()==rec["sha256"]
    assert rec["label"]=="SIMULATED — FICTIONAL DATA — NOT FROM A LIVE SYSTEM"
    rows=list(csv.DictReader(p.open(encoding="utf-8",newline="")))
    assert len(rows)==expected[p.stem],(p.stem,len(rows))
hr={r["employee_id"] for r in csv.DictReader((root/"evidence/baseline/hr_roster.csv").open())}
for name in ["identity_accounts","hr_terminations","privileged_role_assignments"]:
    for row in csv.DictReader((root/"evidence/baseline"/(name+".csv")).open()):
        assert row["employee_id"] in hr
changes={r["change_id"] for r in csv.DictReader((root/"evidence/baseline/change_requests.csv").open())}
for row in csv.DictReader((root/"evidence/baseline/deployments.csv").open()):
    assert row["change_id"] in changes
assert all(x in entries for x in ["evidence/baseline/hr_roster.csv","evidence/metadata/EV-001.meta.json"])
print(f"PASS: {len(entries)} frozen files verified; {len(index)} evidence records; {sum(expected.values())} source rows; joins and snapshot labels valid.")
