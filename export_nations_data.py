#!/usr/bin/env python3
"""
SRD Alliance — Nation Data Exporter
=====================================
Exports the nation parameter database from generate_srd_models.py into a
standalone nations_data.json file. This lets analysts inspect, critique,
and update parameters without touching Python code.

Usage:
    python export_nations_data.py                      # writes nations_data.json
    python export_nations_data.py --output custom.json # custom output path
    python export_nations_data.py --region Pacific     # filter by region
    python export_nations_data.py --summary            # print summary table only

Once exported, you can edit nations_data.json and regenerate all models:
    python generate_srd_models.py --from-json nations_data.json

nations_data.json schema:
    {
      "metadata": { version, generated_at, total_nations, sources },
      "nations": [
        {
          "name":           string   — display name
          "code":           string   — filename-safe identifier
          "region":         string   — "Pacific" | "CARICOM" | "Guarantor"
          "status":         string   — "Full Member" | "Associate" | "Territory" | "Guarantor"
          "pop":            integer  — population (2024 estimate)
          "gdp_usd":        number   — nominal GDP USD (World Bank 2023)
          "project_cost":   number   — SRD programme cost estimate USD
          "bond_value":     number   — debt-financed portion USD
          "gross_savings":  number   — annual diesel savings USD
          "savings_real":   number   — savings realisation rate (0–1)
          "coupon":         number   — bond coupon rate (0–1)
          "diesel_pct":     number   — % electricity from diesel (0–1)
          "diesel_usd_kwh": number   — local diesel electricity cost $/kWh
          "ghi":            number   — solar GHI kWh/m²/day
          "wind_cf":        number   — wind capacity factor at 100m
          "excess_mw":      number   — estimated excess RE post domestic demand (MW)
          "dist_au":        integer  — sea distance to Australia (km)
          "trade_mult":     number   — strategic/trade multiplier (0–1)
          "capital_gap":    number   — self-healing example gap USD
          "e1":             number   — self-healing year 1 excess USD
          "notes":          string   — key modelling notes
          "derived": {
            "h2_tpy":         number   — modelled H₂ production (t/yr)
            "delivered_cost_au": number — delivered $/kg to Australia
            "au_viable":      boolean — AU-competitive at $5/kg threshold
            "annual_fee":     number   — AU guarantee fee income ($/yr)
            "total_fees_20yr":number   — total fee income over 20 years
            "direct_net":     number   — direct net benefit to AU
            "guarantee_exposure": number — AU max contingent liability
          }
        }
      ]
    }
"""

import json
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path

# ── Import nation database from generate_srd_models ─────────────────────────
try:
    sys.path.insert(0, str(Path(__file__).parent))
    from generate_srd_models import NATIONS
except ImportError as e:
    print(f"ERROR: Could not import NATIONS from generate_srd_models.py: {e}")
    print("Ensure generate_srd_models.py is in the same directory.")
    sys.exit(1)

# ── Derived calculations ─────────────────────────────────────────────────────

H2_GATE_PRICE   = 3.50   # $/kg (2025 CSIRO/ARENA target)
H2_SHIP_FIXED   = 0.40   # $/kg terminal cost
H2_SHIP_VAR     = 0.0002 # $/kg/km
AU_THRESHOLD    = 5.00   # $/kg delivered (AU Hydrogen Strategy 2030 target)
H2_EFF          = 55     # kWh/kg (IRENA 2024)
CAPACITY_FACTOR = 0.35   # blended solar+wind
GUARANTEE_PCT   = 0.05   # 5% of project cost
FEE_RATE        = 0.025  # 2.5% p.a. on bond value
BOND_TERM       = 20     # years
DEFAULT_PROB    = 0.02   # 2.0% — 50× MIGA actual
LGD             = 0.50   # loss given default


def derive(n: dict) -> dict:
    h2_tpy = n["excess_mw"] * 1000 * 8760 * CAPACITY_FACTOR / H2_EFF / 1000
    delivered = H2_GATE_PRICE + H2_SHIP_FIXED + n["dist_au"] * H2_SHIP_VAR
    au_viable = delivered <= AU_THRESHOLD and n["dist_au"] > 0

    exposure    = n["project_cost"] * GUARANTEE_PCT
    annual_fee  = n["bond_value"] * FEE_RATE
    total_fees  = annual_fee * BOND_TERM
    exp_loss    = exposure * DEFAULT_PROB * LGD
    direct_net  = total_fees - exp_loss
    strategic   = n["project_cost"] * n["trade_mult"]

    return {
        "h2_tpy":               round(h2_tpy, 1),
        "delivered_cost_au":    round(delivered, 3),
        "au_viable":            au_viable,
        "annual_fee":           round(annual_fee, 0),
        "total_fees_20yr":      round(total_fees, 0),
        "expected_loss":        round(exp_loss, 0),
        "direct_net":           round(direct_net, 0),
        "strategic_value":      round(strategic, 0),
        "total_net":            round(direct_net + strategic, 0),
        "guarantee_exposure":   round(exposure, 0),
    }


def build_export(nations: list, region_filter: str = None) -> dict:
    filtered = nations
    if region_filter:
        filtered = [n for n in nations if n["region"].lower() == region_filter.lower()]

    sids = [n for n in filtered if n["region"] in ("Pacific", "CARICOM")]

    enriched = []
    for n in filtered:
        entry = dict(n)
        entry["derived"] = derive(n)
        enriched.append(entry)

    # Alliance totals (SIDS only)
    total_proj      = sum(n["project_cost"] for n in sids)
    total_exposure  = sum(n["project_cost"] * GUARANTEE_PCT for n in sids)
    total_fees      = sum(n["bond_value"] * FEE_RATE * BOND_TERM for n in sids)
    total_loss      = sum(n["project_cost"] * GUARANTEE_PCT * DEFAULT_PROB * LGD for n in sids)
    total_net       = total_fees - total_loss
    total_strategic = sum(n["project_cost"] * n["trade_mult"] for n in sids)
    total_h2_au     = sum(
        n["excess_mw"] * 1000 * 8760 * CAPACITY_FACTOR / H2_EFF / 1000
        for n in sids if n["dist_au"] < 6000
    )

    return {
        "metadata": {
            "version":       "3.0",
            "generated_at":  datetime.now(timezone.utc).isoformat(),
            "total_nations": len(filtered),
            "sids_count":    len(sids),
            "region_filter": region_filter or "all",
            "model_seed":    7801909,
            "assumptions": {
                "h2_gate_price_usd_kg":   H2_GATE_PRICE,
                "h2_efficiency_kwh_kg":   H2_EFF,
                "h2_capacity_factor":     CAPACITY_FACTOR,
                "h2_ship_fixed_usd_kg":   H2_SHIP_FIXED,
                "h2_ship_variable_usd_km": H2_SHIP_VAR,
                "au_viable_threshold_usd_kg": AU_THRESHOLD,
                "guarantee_pct":          GUARANTEE_PCT,
                "fee_rate_pa":            FEE_RATE,
                "bond_term_years":        BOND_TERM,
                "default_probability":    DEFAULT_PROB,
                "loss_given_default":     LGD,
            },
            "sources": {
                "population":       "UN estimates (2024)",
                "gdp":              "World Bank (2023)",
                "project_cost":     "IRENA country profiles; World Bank energy data; population-scaled",
                "energy_savings":   "Diesel generation % × demand × $/kWh; Ministry of Energy data where available",
                "h2_production":    "World Bank ESMAP; Global Wind Atlas; modelled estimates",
                "h2_gate_price":    "CSIRO/ARENA 2025–2030 target",
                "h2_efficiency":    "IRENA Green Hydrogen Cost Reduction (2020)",
                "green_iron":       "Minerals Institute WA; Accenture; Deloitte/WWF-Australia",
                "miga_claim_rate":  "MIGA Annual Report (World Bank Group, 2024)",
                "swf_return":       "Norway GPFG 30yr average (Norges Bank IM, 2025)",
            },
            "caveats": [
                "All project_cost, gross_savings, and h2 figures are MODELLED ESTIMATES — not project-specific.",
                "trade_mult is a calibrated assumption (0.38 baseline) — not directly evidenced for any CARICOM nation.",
                "h2_tpy derived from excess_mw which is a modelled estimate of capacity after domestic demand.",
                "Replace all figures with official country renewable energy roadmaps before formal policy submission.",
                "Pending: Pacific H2 Strategy Report C (DCCEEW/UNSW, est late 2026).",
                "Pending: CCREEE Integrated Resource Plans for all CARICOM nations.",
            ],
        },
        "alliance_totals": {
            "total_programme_usd":      round(total_proj, 0),
            "au_guarantee_exposure_usd": round(total_exposure, 0),
            "au_total_fees_20yr_usd":   round(total_fees, 0),
            "au_expected_losses_usd":   round(total_loss, 0),
            "au_direct_net_benefit_usd": round(total_net, 0),
            "au_strategic_value_usd":   round(total_strategic, 0),
            "au_total_net_benefit_usd": round(total_net + total_strategic, 0),
            "pacific_h2_au_viable_tpy": round(total_h2_au, 0),
            "green_iron_plant_coverage": round(total_h2_au / 264000, 3),
        },
        "nations": enriched,
    }


def print_summary(export: dict):
    """Print a readable summary table to stdout."""
    meta = export["metadata"]
    totals = export["alliance_totals"]

    print(f"\nSRD Alliance Nation Database — {meta['generated_at'][:10]}")
    print(f"Nations: {meta['total_nations']}  |  SIDS: {meta['sids_count']}  |  Region: {meta['region_filter']}\n")

    # Header
    print(f"  {'Nation':<38} {'Region':<9} {'Proj Cost':>11} {'H₂ (t/yr)':>10} {'AU Viable':>10} {'Direct Net':>12}")
    print("  " + "─" * 96)

    for n in export["nations"]:
        if n["region"] == "Guarantor":
            continue
        d = n["derived"]
        viable = "✓ Yes" if d["au_viable"] else "✗ No"
        print(
            f"  {n['name']:<38} {n['region']:<9} "
            f"${n['project_cost']/1e6:>9.0f}M "
            f"{d['h2_tpy']:>10.0f} "
            f"{viable:>10} "
            f"${d['direct_net']/1e9:>10.2f}B"
        )

    print("  " + "─" * 96)
    print(f"\n  Alliance totals (SIDS only):")
    print(f"    Total programme:          ${totals['total_programme_usd']/1e9:.1f}B")
    print(f"    AU guarantee exposure:    ${totals['au_guarantee_exposure_usd']/1e9:.2f}B")
    print(f"    AU direct net benefit:    ${totals['au_direct_net_benefit_usd']/1e9:.2f}B")
    print(f"    AU total net benefit:     ${totals['au_total_net_benefit_usd']/1e9:.1f}B")
    print(f"    Pacific H₂ (AU-viable):   {totals['pacific_h2_au_viable_tpy']:,.0f} t/yr")
    print(f"    Green iron plant coverage: {totals['green_iron_plant_coverage']:.2f}× of one 4.8 Mtpa plant\n")


def main():
    parser = argparse.ArgumentParser(
        description="Export SRD nation parameter database to JSON."
    )
    parser.add_argument(
        "--output", type=Path, default=Path("nations_data.json"),
        help="Output JSON file path (default: nations_data.json)"
    )
    parser.add_argument(
        "--region", type=str, default=None,
        choices=["Pacific", "CARICOM", "Guarantor"],
        help="Filter to a specific region"
    )
    parser.add_argument(
        "--summary", action="store_true",
        help="Print summary table to stdout without writing file"
    )
    args = parser.parse_args()

    export = build_export(NATIONS, region_filter=args.region)

    if args.summary:
        print_summary(export)
        return

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(export, f, indent=2, ensure_ascii=False)

    print(f"✓ Exported {export['metadata']['total_nations']} nations → {args.output}")
    print(f"  SIDS: {export['metadata']['sids_count']} | "
          f"Alliance programme: ${export['alliance_totals']['total_programme_usd']/1e9:.1f}B | "
          f"AU direct net: ${export['alliance_totals']['au_direct_net_benefit_usd']/1e9:.2f}B")
    print(f"\nTo regenerate all models from this JSON:")
    print(f"  python generate_srd_models.py --from-json {args.output}")


if __name__ == "__main__":
    main()
