# SRD Alliance — Full Nation Model Set

**Sovereign Resilience Debt** | Pacific + CARICOM + Guarantors | 42 Nation Models

This repository contains the complete SRD financial model for every nation in the Pacific Islands Forum and CARICOM — one workbook per country, two regional rollups, two guarantor benefit analyses, and a full alliance summary. All files are generated from a single parameterised source (`generate_srd_models.py`) and share the same model architecture as the Barbados pilot at [stevenbrandon88/srd-barbados](https://github.com/stevenbrandon88/srd-barbados).

---

## Files in This Repository

### Alliance & Regional

| File | Contents |
|------|----------|
| `SRD_Full_Alliance.xlsx` | All 37 SIDS on one sheet + Pacific vs CARICOM comparison tab |
| `SRD_Pacific_Regional.xlsx` | Pacific nation comparison, programme totals, H₂ by nation |
| `SRD_CARICOM_Regional.xlsx` | CARICOM nation comparison, programme totals, H₂ routing |

### Guarantors

| File | Contents |
|------|----------|
| `SRD_Australia_Guarantor_model.xlsx` | AU cumulative benefit from full Pacific + CARICOM programme |
| `SRD_New_Zealand_Guarantor_model.xlsx` | NZ benefit from Pacific programme (35% co-guarantee share) |

### Pacific Nations (17 models)

| File | Nation | Status | Project Cost |
|------|--------|--------|-------------|
| `SRD_PNG_model.xlsx` | Papua New Guinea | Full Member | $4.5B |
| `SRD_Timor_Leste_model.xlsx` | Timor-Leste | Full Member | $1.5B |
| `SRD_Fiji_model.xlsx` | Fiji | Full Member | $1.2B |
| `SRD_Solomon_Islands_model.xlsx` | Solomon Islands | Full Member | $900M |
| `SRD_Vanuatu_model.xlsx` | Vanuatu | Full Member | $400M |
| `SRD_French_Polynesia_model.xlsx` | French Polynesia | Territory | $350M |
| `SRD_New_Caledonia_model.xlsx` | New Caledonia | Territory | $340M |
| `SRD_Samoa_model.xlsx` | Samoa | Full Member | $250M |
| `SRD_Kiribati_model.xlsx` | Kiribati | Full Member | $150M |
| `SRD_FSM_model.xlsx` | Federated States of Micronesia | Full Member | $140M |
| `SRD_Tonga_model.xlsx` | Tonga | Full Member | $130M |
| `SRD_Marshall_Islands_model.xlsx` | Marshall Islands | Full Member | $100M |
| `SRD_Cook_Islands_model.xlsx` | Cook Islands | Full Member | $50M |
| `SRD_Palau_model.xlsx` | Palau | Full Member | $50M |
| `SRD_Nauru_model.xlsx` | Nauru | Full Member | $30M |
| `SRD_Tuvalu_model.xlsx` | Tuvalu | Full Member | $30M |
| `SRD_Niue_model.xlsx` | Niue | Full Member | $15M |

### CARICOM Nations (20 models)

| File | Nation | Status | Project Cost |
|------|--------|--------|-------------|
| `SRD_Haiti_model.xlsx` | Haiti | Full Member | $5.0B |
| `SRD_Jamaica_model.xlsx` | Jamaica | Full Member | $2.8B |
| `SRD_Barbados_model.xlsx` | Barbados ★ | Full Member | $1.84B |
| `SRD_Trinidad_Tobago_model.xlsx` | Trinidad and Tobago | Full Member | $1.5B |
| `SRD_Guyana_model.xlsx` | Guyana | Full Member | $600M |
| `SRD_Suriname_model.xlsx` | Suriname | Full Member | $500M |
| `SRD_Bahamas_model.xlsx` | Bahamas | Full Member | $500M |
| `SRD_Belize_model.xlsx` | Belize | Full Member | $400M |
| `SRD_Saint_Lucia_model.xlsx` | Saint Lucia | Full Member | $250M |
| `SRD_Antigua_Barbuda_model.xlsx` | Antigua and Barbuda | Full Member | $200M |
| `SRD_Grenada_model.xlsx` | Grenada | Full Member | $150M |
| `SRD_Saint_Vincent_model.xlsx` | Saint Vincent and the Grenadines | Full Member | $140M |
| `SRD_Dominica_model.xlsx` | Dominica | Full Member | $100M |
| `SRD_Saint_Kitts_Nevis_model.xlsx` | Saint Kitts and Nevis | Full Member | $100M |
| `SRD_Montserrat_model.xlsx` | Montserrat | Full Member | $20M |
| `SRD_Anguilla_model.xlsx` | Anguilla | Associate | $40M |
| `SRD_Bermuda_model.xlsx` | Bermuda | Associate | $150M |
| `SRD_British_Virgin_Islands_model.xlsx` | British Virgin Islands | Associate | $60M |
| `SRD_Cayman_Islands_model.xlsx` | Cayman Islands | Associate | $150M |
| `SRD_Turks_Caicos_model.xlsx` | Turks and Caicos | Associate | $80M |

★ Barbados is the SRD pilot — all parameters are fully evidenced with primary sources. All other nation files use modelled estimates.

CARICOM Associate Members are UK Overseas Territories. Their guarantee structure would require UK coordination and are included for completeness of the CARICOM universe.

### Scripts

| File | Purpose |
|------|---------|
| `generate_srd_models.py` | Regenerates all 42 Excel files from the nation database |
| `validate_models.py` | Verifies every xlsx for formula errors — run after any changes |
| `export_nations_data.py` | Exports the nation parameter database to `nations_data.json` |

---

## What Each Nation File Contains

Every individual nation file is a complete, self-contained SRD model with 10 sheets and 532 live formulas — identical architecture to the Barbados pilot, parameterised for each nation:

| Sheet | Contents |
|-------|----------|
| Assumptions | All inputs (blue cells) with source notes per nation |
| Bond Cashflows | 20-year amortisation schedule |
| SWF Projection | 25-year Sovereign Wealth Fund growth |
| Self-Healing | Capital gap closure formula |
| Australia Benefit | Guarantee fee income and net benefit |
| Sensitivity | One-at-a-time ±20% parameter sweeps |
| Unit Tests | 6 automated checks — green = pass |
| Hydrogen Alliance | Nation H₂ export potential |
| H2 Economics (AU) | Price scenarios and green iron supply sizing |
| Data Gaps Tracker | Open data gaps with priority flags |

---

## Alliance-Level Numbers

Programme-wide aggregates across all 37 SIDS. All figures are **modelled estimates** — see Caveats below.

| Metric | Value |
|--------|-------|
| Total programme investment | ~$51B across 37 nations |
| Australia guarantee exposure (5%) | ~$2.6B *(contingent — only triggered on default)* |
| Total AU guarantee fees (20yr) | ~$18.9B |
| Total AU direct net benefit | ~$18.8B |
| Total AU strategic value (0.38×) | ~$19.4B ← calibrated assumption |
| Total AU net benefit | ~$38.2B |
| Alliance population covered | ~33M people |
| Pacific H₂ viable supply to AU | ~49,000 t/yr (~19% of one 4.8 Mtpa green iron plant) |
| MIGA 35yr actual claim rate | <0.04% (model uses 2.0% — 50× more conservative) |

---

## Relationship to srd-barbados

This repo is the deliverable set. The full model engine — Python tester, Monte Carlo, unit tests, React dashboard, and complete audit trail — lives in [srd-barbados](https://github.com/stevenbrandon88/srd-barbados).

| | [srd-barbados](https://github.com/stevenbrandon88/srd-barbados) | srd-alliance |
|---|---|---|
| Scope | 1 nation (Barbados) | 37 SIDS + 2 guarantors |
| Parameters | Fully evidenced with primary sources | Modelled estimates (population-scaled) |
| Python tester | Full Monte Carlo + unit tests | Generator + validation scripts |
| React dashboard | ✓ Interactive | Not included |
| Intended use | Academic review, model auditing | Policy briefings, nation-level negotiations |

---

## Regenerating All Files

```bash
pip install openpyxl
python generate_srd_models.py
```

Completes in under 60 seconds. Output: 42 files, 0 errors.

To verify integrity after any changes:

```bash
python validate_models.py
```

To inspect or update nation parameters without touching Python:

```bash
python export_nations_data.py
# edits nations_data.json
python generate_srd_models.py --from-json nations_data.json
```

To update a nation's parameters, edit the `NATIONS` list in `generate_srd_models.py` (or edit `nations_data.json` after exporting) and re-run the generator.

---

## Parameter Methodology

**Project cost** — population-scaled from IRENA country profiles and World Bank energy data. Barbados baseline ($6,571/capita) applied conservatively, adjusted for diesel dependency, existing generation mix, and GDP. PNG and Jamaica anchored to IDB/IRENA preliminary estimates.

**Gross annual savings** — diesel generation percentage × estimated annual electricity demand × local diesel tariff ($/kWh). Ministry of Energy or national utility data cited where available; modelled elsewhere.

**Coupon rate** — AU 20-year bond + 50bps = 4.5% baseline. Haiti receives 5.5% (additional 100bps governance risk premium).

**Trade/strategic multiplier** — 0.38 baseline (calibrated assumption — see [CAVEATS.md](https://github.com/stevenbrandon88/srd-barbados/blob/main/CAVEATS.md)). Pacific nations with active AU security relationships use 0.40–0.45. Associate territory members use 0.28. All flagged in each file's source notes.

**H₂ production** — `excessMW × 8,760h × 35% CF ÷ 55 kWh/kg ÷ 1,000`. Excess RE is a modelled estimate of capacity after domestic demand. To be replaced with Pacific Hydrogen Strategy Report C (DCCEEW/UNSW, est. late 2026) and CCREEE Integrated Resource Plans when published.

> **All figures are modelled estimates. Replace with official country renewable energy roadmaps before any formal policy submission.**

---

## H₂ Market Routing

Geographic proximity to Australia is the decisive factor — not gate price.

| Region | Distance to AU | Delivered cost | AU-viable? | Primary market |
|--------|---------------|----------------|------------|----------------|
| Pacific SIDS | 1,400–5,200 km | $4.18–$4.94/kg | ✓ Yes | Australia |
| CARICOM | 15,800–17,800 km | $6.56–$7.96/kg | ✗ No | US Gulf Coast / EU |

All 15 Pacific SIDS are AU-competitive at current (2025) prices. No CARICOM nation is AU-competitive at any modelled price scenario. CARICOM H₂ routes to US or EU markets — the SRD framework still applies fully; only the downstream H₂ export market differs by region.

---

## Key Data Gaps

| Gap | Affects | When |
|-----|---------|------|
| Pacific H₂ Strategy Report C (DCCEEW/UNSW) | All Pacific H₂ figures | Est. late 2026 |
| CCREEE Integrated Resource Plans | All CARICOM H₂ figures | Est. end 2024 |
| IRENA SIDS-specific country roadmaps | Project costs + savings | Ongoing |
| AU DRI plant confirmed H₂ demand trajectory | Green iron plant coverage | When projects confirmed |
| Bilateral trade data (AU–CARICOM, NZ–Pacific) | Trade multiplier accuracy | DFAT / CARICOM Secretariat |

---

## Citation

Cite the SRD working paper and the underlying IRENA/World Bank source for each nation's parameters when using these models in policy or academic work. Do not cite modelled estimates as official national figures.

[Add SSRN citation when published]

License: MIT
