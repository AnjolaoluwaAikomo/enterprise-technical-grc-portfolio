from pathlib import Path
import json,hashlib,csv
root=Path(__file__).resolve().parent
index=json.loads((root/'governance/authoritative/F06_evidence_index.json').read_text())
assert len(index)==12
for rec in index:
    source=root/'source-data/baseline'/Path(rec['file_path']).name
    assert source.is_file(),source
    assert hashlib.sha256(source.read_bytes()).hexdigest()==rec['sha256'],source
    assert rec['snapshot_id']=='BASE-20260930' and rec['synthetic_data'] is True
    assert list(csv.DictReader(source.open(encoding='utf-8',newline='')))
print('PASS: 12 evidence records and source hashes; original baseline unchanged')
