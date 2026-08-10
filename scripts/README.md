# Scripts — Deliverable Generators

PPTX generators for **plant autonomy / operating-model** client deliverables (anonymized).

## Setup

```bash
python3 -m venv .venv-pptx
source .venv-pptx/bin/activate
pip install python-pptx
```

## Run

Output is written to `outputs/` at the repo root (gitignored).

```bash
source .venv-pptx/bin/activate
python scripts/generate_plant_autonomy_draft_v6_1.py
```

## Files

| Script | Version | Notes |
|--------|---------|-------|
| `generate_plant_autonomy_draft_v3.py` | v3 | Full deck from scratch |
| `generate_plant_autonomy_draft_v5_2.py` | v5.2 | Requires `outputs/plant-autonomy_operating-model_draft_v5.1.pptx` as input |
| `generate_plant_autonomy_draft_v6.py` | v6 | Definition-first (9 slides) |
| `generate_plant_autonomy_draft_v6_1.py` | v6.2 | Fact→Issue→IBM hypothesis |

## Anonymization

- Client name → `クライアント様`
- Personal names → roles (PO, 作成者, etc.)
- Paths → repo-relative `outputs/`
- See `core/identity.md` Confidentiality Boundary

## Related

- `core/author-voice.md`
- `standards/deliverable-archetypes.md`
