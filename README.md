# SRD Alliance — Full Nation Model Set

**Sovereign Resilience Debt** | Pacific + CARICOM + Guarantors | 42 Nation Models

This repository contains the complete SRD financial model for every nation in the Pacific Islands Forum and CARICOM — one workbook per country, two regional rollups, two guarantor benefit analyses, and a full alliance summary. All 42 files are generated from a single parameterised source (`generate_srd_models.py`) and share the same model architecture as the Barbados pilot ([srd-barbados](../srd-barbados)).

---

## Repository Structure

```
srd-alliance/
│
├── individual/
│   ├── pacific/          17 nation models (15 SIDS + 2 territories)
│   └── caricom/          20 nation models (15 full + 5 associate members)
│
├── regional/
│   ├── SRD_Pacific_Regional.xlsx     Pacific comparison + H₂ by nation
│   └── SRD_CARICOM_Regional.xlsx     CARICOM comparison + H₂ routing
│
├── guarantors/
│   ├── SRD_Australia_Guarantor_model.xlsx   AU benefit from full programme
│   └── SRD_New_Zealand_Guarantor_model.xlsx NZ benefit from Pacific programme
│
├── alliance/
│   └── SRD_Full_Alliance.xlsx        All 37 SIDS + regional comparison
│
├── generate_srd_models.py            Regenerates all 42 files from the nation database
└── README.md                         This file
```

---

## Nations Covered

### Pacific Islands Forum (17 models)

| Nation | Status | Project Cost | Key Notes |
|--------|--------|-------------|-----------|
| Papua New Guinea | Full Member | $4.5B | Hydro + LNG; AU strategic partner |
| Timor-Leste | Full Member | $1.5B | Existing Petroleum Fund; Darwin proximity |
| Fiji | Full Member | $1.2B | Regional hub; hydro base |
| Solomon Islands | Full Member | $900M | Critical AU security partner |
| Vanuatu | Full Member | $400M | Geothermal potential |
| Samoa | Full Member | $250M | Regional aviation hub |
| Tonga | Full Member | $130M | High remittance economy |
| Kiribati | Full Member | $150M | Revenue Equalisation Reserve Fund; equatorial solar |
| Federated States of Micronesia | Full Member | $140M | 607 islands; US Compact |
| Marshall Islands | Full Member | $100M | Marshall Islands Climate Fund |
| Palau | Full Member | $50M | Marine sanctuary; AU defence cooperation |
| Cook Islands | Full Member | $50M | Free Association with NZ |
| Nauru | Full Member | $30M | 100% diesel; exceptional wind |
| Tuvalu | Full Member | $30M | Tuvalu National Trust Fund; AU Pacific access agreement |
| Niue | Full Member | $15M | World's smallest self-governing nation; 100% RE target set |
| French Polynesia | Territory | $350M | Requires EU/France coordination |
| New Caledonia | Territory | $340M | Nickel economy; close AU trade |

### CARICOM Full Members (15 models)

| Nation | Status | Project Cost | Key Notes |
|--------|--------|-------------|-----------|
| Haiti | Full Member | $5.0B | Highest population; 5.5% coupon (governance risk premium) |
| Jamaica | Full Member | $2.8B | Largest CARICOM economy |
| Barbados ★ | Full Member | $1.84B | SRD pilot — all parameters fully evidenced |
| Trinidad and Tobago | Full Member | $1.5B | CertHiLAC H₂ certification body; oil transition |
| Guyana | Full Member | $600M | World's fastest-growing economy (oil boom) |
| Suriname | Full Member | $500M | Hydro + new offshore oil |
| Bahamas | Full Member | $500M | 700 islands; 98% diesel |
| Belize | Full Member | $400M | English-speaking Commonwealth; hydro ~40% |
| Saint Lucia | Full Member | $250M | OECS Eastern Caribbean sub-group |
| Antigua and Barbuda | Full Member | $200M | 99% diesel; hurricane vulnerability |
| Grenada | Full Member | $150M | 3-island federation |
| Saint Vincent and the Grenadines | Full Member | $140M | Post-volcanic recovery |
| Dominica | Full Member | $100M | Geothermal potential — "Nature Isle" |
| Saint Kitts and Nevis | Full Member | $100M | Citizenship by Investment economy |
| Montserrat | Full Member | $20M | UK territory; CARICOM full member; half-island uninhabitable |

### CARICOM Associate Members (5 models)

Anguilla · Bermuda · British Virgin Islands · Cayman Islands · Turks and Caicos Islands

All are UK Overseas Territories. Guarantee structure would require UK coordination. Included for completeness of the CARICOM universe.

### Guarantors (2 models)

**Australia** — primary guarantor across all 37 SIDS. Model shows cumulative fee income, guarantee exposure, and net benefit across the full Pacific + CARICOM programme.

**New Zealand** — co-guarantor focused on Pacific SIDS, with natural interest in Cook Islands and Niue (Free Association states). Model uses 35% co-guarantee share.

---

## What Each File Contains

Every individual nation file is a complete, self-contained SRD model with 10 sheets and 532 live formulas — the same architecture as the Barbados pilot, fully parameterised for each nation:

| Sheet | Contents |
|-------|----------|
| Assumptions | All inputs (blue cells) with source notes per nation |
| Bond Cashflows | 20-year amortisation schedule |
| SWF Projection | 25-year Sovereign Wealth Fund growth |
| Self-Healing | Capital gap closure formula |
| Australia Benefit | Guarantee fee income and net benefit |
| Sensitivity | One-at-a-time ±20% parameter sweeps |
| Unit Tests | 6 automated checks (green = pass) |
| Hydrogen Alliance | Nation H₂ export potential |
| H2 Economics (AU) | Price scenarios and green iron supply sizing |
| Data Gaps Tracker | Open data gaps with priority flags |

**Regional files** add a nation comparison table sorted by project cost, aggregate programme metrics, and a H₂-by-nation sheet with AU viability and market routing.

**The Full Alliance file** covers all 37 SIDS on one sheet with a Regional Comparison tab showing Pacific vs CARICOM side-by-side across every metric.

**Guarantor files** show cumulative benefit across the programme scope: total fees, exposure, expected losses, direct and total net benefit, risk ratios, and H₂ opportunity sizing.

---

## Alliance-Level Numbers

Programme-wide aggregates across all 37 SIDS nations. All figures are **modelled estimates** — see Caveats below.

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

This repo builds directly on the Barbados pilot. Key differences:

| | [srd-barbados](../srd-barbados) | srd-alliance |
|---|---|---|
| Scope | 1 nation (Barbados) | 37 SIDS + 2 guarantors |
| Parameters | Fully evidenced with primary sources | Modelled estimates (population-scaled) |
| Python tester | Full Monte Carlo + unit tests | Generator script only |
| React dashboard | ✓ Interactive | Not included |
| Intended use | Academic review, model auditing | Policy briefings, nation-level negotiations |

For the Python tester, React dashboard, Monte Carlo engine, and full audit trail — use srd-barbados. This repo is the deliverable set for ministers, officials, and briefing rooms.

---

## Regenerating All Files

```bash
pip install openpyxl
python generate_srd_models.py
```

Completes in under 60 seconds. Output: 42 files, 0 errors. To update any nation's parameters, edit the `NATIONS` list in `generate_srd_models.py` and re-run. To add a nation, add an entry — folder creation is automatic.

---

## Parameter Methodology

**Project cost** — population-scaled from IRENA country profiles and World Bank energy data. Barbados baseline ($6,571/capita) applied conservatively, adjusted for diesel dependency, existing generation mix, and GDP. PNG and Jamaica anchored to IDB/IRENA preliminary estimates.

**Gross annual savings** — diesel generation percentage × estimated annual electricity demand × local diesel tariff ($/kWh). Ministry of Energy or national utility data cited where available; modelled elsewhere.

**Coupon rate** — AU 20-year bond + 50bps = 4.5% baseline for all nations. Haiti receives 5.5% (additional 100bps governance risk premium).

**Trade/strategic multiplier** — 0.38 baseline across all nations (calibrated assumption, not directly evidenced — see CAVEATS.md in srd-barbados). Pacific nations with active AU security relationships use 0.40–0.45. Associate territory members use 0.28. All flagged as calibrated assumptions in each file's source notes.

**H₂ production** — `excessMW × 8,760h × 35% CF ÷ 55 kWh/kg ÷ 1,000`. Excess RE is a modelled estimate of capacity after domestic demand. To be replaced with Pacific Hydrogen Strategy Report C (DCCEEW/UNSW, est. late 2026) and CCREEE Integrated Resource Plans when published.

**All figures are modelled estimates. Replace with official country renewable energy roadmaps before any formal policy submission.**

---

## H₂ Market Routing

Geographic proximity to Australia is the decisive factor — not gate price.

| Region | Distance to AU | Delivered cost | AU-viable? | Primary market |
|--------|---------------|----------------|------------|----------------|
| Pacific SIDS | 1,400–5,200 km | $4.18–$4.94/kg | ✓ Yes | Australia |
| CARICOM | 15,800–17,800 km | $6.56–$7.96/kg | ✗ No | US Gulf Coast / EU |

All 15 Pacific SIDS are AU-competitive at current (2025) prices. No CARICOM nation is AU-competitive at any modelled price scenario. CARICOM H₂ is viable — it simply routes to US or EU markets. The SRD framework applies equally to both regions; the H₂ export market is a separate downstream opportunity that differs by region.

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

If using nation model outputs in policy or academic work, cite the SRD working paper and the underlying IRENA/World Bank source for that nation's parameters. Do not cite modelled estimates as if they were official national figures.

[Add SSRN citation when published]

License: MIT
