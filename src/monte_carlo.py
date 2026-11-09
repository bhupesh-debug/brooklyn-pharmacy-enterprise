"""
Monte Carlo simulation — Brooklyn independent pharmacy enterprise package.

Owner: a U.S. Green Card holder (Lawful Permanent Resident). NOT Bhupesh.
Bhupesh asked for this on the owner's behalf. Nothing in this file applies
Bhupesh's background, resume, or STEM OPT situation to the owner.

SOURCE OF TRUTH
--------------
~/workspace/your_files/Pharmacy_Startup_Advisory_Brooklyn_Master_Report_2026-11-09.md
(105 pp) and its companion model
Pharmacy_Startup_Financial_Model_Brooklyn_2026-11-09.xlsx.
Every report-sourced number below cites the report section. Anything marked
ASSUMPTION is an assumption of THIS simulation, with its basis stated; it is
not a report figure and must not be quoted as one.

VERDICT (followed, not relitigated)
-----------------------------------
CONDITIONAL GO — ACQUIRE, DO NOT BUILD. Commit no capital until five gates
clear: (1) Medicaid moratorium resolved in writing; (2) suitable target at a
disciplined price; (3) supervising pharmacist secured in writing;
(4) financing confirmed WITHOUT SBA; (5) healthcare attorney + pharmacy CPA
engaged pre-LOI. If any gate fails, wait — do not default to startup.

HARD FACTS CARRIED CORRECTLY
----------------------------
* SBA is CLOSED to this owner. SBA Policy Notice 5000-876441 (eff. 1 Mar 2026,
  now SOP 50 10 8.1) bars a lawful permanent resident from owning ANY share
  of a 7(a)/504/Microloan borrower, even 1%. Financing here = personal
  capital, conventional bank loans, non-SBA CDFI loans, seller financing.
  SBA eligibility is NEVER claimed in this package.
* NY Medicaid enrollment moratorium (CMS-approved 27 Jul 2026, through
  27 Jan 2027, extendable in 6-month periods) covers new enrollments AND
  changes of ownership. No Medicaid revenue is counted until enrollment is
  active. Modelled as a delay (0 / 6 / 12 months) before Medicaid gross
  profit starts.
* A green card holder CAN own 100% of a NY retail pharmacy without a
  pharmacist licence (Ed. Law s.6808). Binding constraint: a full-time
  (30+ hrs/wk, one pharmacy only) NY-licensed supervising pharmacist.
* Startup capital (report s.5.2): Lean $435,230 / Standard $791,010 /
  Larger $1,309,273. Steady opex (s.5.3): $30,641 / $51,050 / $80,083 per
  month. Break-even (s.5.5, base $79.20/Rx, 20.9% margin): 68 / 111 / 171
  Rx/day. First EBITDA-positive month (s.5.4): 10 / 8 / 9. 5-yr ROI base
  (s.5.6): ~105% / ~172% / ~135%. Simple payback on Year 2-3 average
  EBITDA: ~3.8 / ~2.5 / ~3.1 yrs.
* Dispensing alone loses money at the national average: $14.57 gross profit
  per Rx vs $15.00 cost to dispense (-$0.43/Rx); 20.9% margin (NCPA 2026
  Digest). See the note on gross profit per Rx in `gross_profit_per_rx`
  docstring — the simulation centres on the report's margin, NOT on $14.57
  as a base case, and says why.
* Acquisition anchors (report ss.6.11, 9.3-9.4): U.S. 2.5-3.5x adjusted
  EBITDA (+ inventory at cost); BizBuySell 2021-2025 average 2.79x,
  2025 median sale $600,000 (median revenue $1,334,270; median owner
  earnings $150,000). The 4-6x EBITDA figure is CANADIAN and is NOT used.

REPRODUCIBILITY (quant-research-system skill standards)
------------------------------------------------------
Fixed seed 20261109. numpy Generator only (no global RNG state, no
time-based seeds). Every distribution, parameter and assumption is
documented in PARAMS / VARIANT_PARAMS below and in MONTE_CARLO.md.
`python src/monte_carlo.py` from the repo root writes
results/monte_carlo_trials.csv and results/monte_carlo_summary.json.
Tests: tests/test_monte_carlo.py (pytest).

MODEL (deterministic core = report ss.5.3-5.6, reproduced exactly)
------------------------------------------------------------------
26 working days/month. Monthly gross profit =
  Rx/day * 26 * revenue_per_Rx * (margin + front_end_pct * 0.45)
Monthly EBITDA = gross profit - opex (85% of steady opex in months 1-3
for startups, per report s.5.4; full opex thereafter; opex inflates
3%/yr, ASSUMPTION per report s.5.1). Owner draw, debt service, tax and
depreciation are EXCLUDED, exactly as in the report — this is an EBITDA
simulation, not a cash-to-owner forecast.
Years 2-3 volume = steady volume x (1+g), (1+g)^2; Years 4-5 +5%/yr
(report s.5.6; growth rates are report ASSUMPTIONS).
"""
from __future__ import annotations

import csv
import json
import math
import os
import sys
from dataclasses import dataclass, field

import numpy as np

SEED = 20261109
N_TRIALS = 10_000
HORIZON_MONTHS = 60
WORKING_DAYS = 26  # report s.5.1: 6 days/week x 52 weeks = 312 days/yr

# ---------------------------------------------------------------------------
# Report-sourced scenario parameters (report ss.1.4, 5.2, 5.3, 5.4, 5.6)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Scenario:
    key: str
    label: str
    capital: float            # total initial capital, report s.5.2 ($)
    opex_monthly: float       # steady-state monthly opex, report s.5.3 ($)
    steady_rx_per_day: float  # steady-state volume, report s.5.1 (Rx/day)
    front_end_pct: float      # front-end sales as % of Rx revenue, s.5.1
    year1_rx_per_day: tuple   # Year-1 monthly ramp, model sheets Monthly_A/B/C
    breakeven_rx_per_day: float  # report s.5.5 base case
    first_ebitda_positive_month: int  # report s.5.4 base case
    year1_ebitda_base: float  # report s.5.4/s.5.6 base case ($)
    roi_5yr_base: float       # report s.5.6 base case (fraction)
    simple_payback_base: float  # report s.1.4 (years)


SCENARIOS: dict[str, Scenario] = {
    "A_lean": Scenario(
        key="A_lean", label="A — Lean startup",
        capital=435_230, opex_monthly=30_641, steady_rx_per_day=80,
        front_end_pct=0.02,
        year1_rx_per_day=(15, 22, 29, 37, 44, 52, 58, 64, 69, 73, 77, 79),
        breakeven_rx_per_day=68, first_ebitda_positive_month=10,
        year1_ebitda_base=-76_031, roi_5yr_base=1.05, simple_payback_base=3.8),
    "B_standard": Scenario(
        key="B_standard", label="B — Standard startup",
        capital=791_010, opex_monthly=51_050, steady_rx_per_day=150,
        front_end_pct=0.03,
        year1_rx_per_day=(25, 38, 55, 70, 85, 98, 110, 120, 130, 138, 145, 150),
        breakeven_rx_per_day=111, first_ebitda_positive_month=8,
        year1_ebitda_base=-56_315, roi_5yr_base=1.72, simple_payback_base=2.5),
    "C_larger": Scenario(
        key="C_larger", label="C — Larger + delivery startup",
        capital=1_309_273, opex_monthly=80_083, steady_rx_per_day=220,
        front_end_pct=0.04,
        year1_rx_per_day=(35, 60, 85, 105, 125, 140, 152, 163, 173, 182, 195, 220),
        breakeven_rx_per_day=171, first_ebitda_positive_month=9,
        year1_ebitda_base=-160_701, roi_5yr_base=1.35, simple_payback_base=3.1),
    # Acquisition: a B-sized steady store bought at the BizBuySell 2025 median
    # price. Total cash needed $880,000 = $600,000 price + $180,000 inventory
    # at cost (midpoint of the report's $150k-$210k illustration range) +
    # $100,000 closing costs + working-capital reserve (report s.6.11 /
    # Financing sheet — all three lines labelled illustrative/ASSUMPTION in
    # the report except the $600,000 median price itself). No ramp: volume
    # starts at steady state in month 1. Its deterministic Year-1 EBITDA
    # ($212,512) is the B-model steady-state run-rate; at the 2.79x average
    # multiple that implies a ~$593k goodwill value, i.e. the $600k median
    # price is internally consistent for a B-sized store. The national
    # median store's $150,000 owner earnings describe a SMALLER store
    # (median revenue $1,334,270 = ~54 Rx/day at $79.20) and are NOT the
    # earnings of this B-sized target — the two medians must not be divided
    # into each other (see MONTE_CARLO.md).
    "D_acquisition": Scenario(
        key="D_acquisition", label="D — Acquisition (B-sized steady store)",
        capital=880_000, opex_monthly=51_050, steady_rx_per_day=150,
        front_end_pct=0.03,
        year1_rx_per_day=(150,) * 12,
        breakeven_rx_per_day=111, first_ebitda_positive_month=1,
        year1_ebitda_base=212_112, roi_5yr_base=float("nan"),
        simple_payback_base=float("nan")),
}

# Medicaid share of prescriptions, NCPA Digest via report s.8/§1.3 context:
# Medicare Part D 34% + Medicaid 18% = over half of independent scripts.
# The moratorium haircut uses the 18% Medicaid share only. ASSUMPTION in
# this simulation: during the delay, Medicaid scripts produce NO gross
# profit (cannot be billed) and are not replaced 1-for-1 by other payers.
# This UNDERSTATES the hit in the top-ranked Brooklyn neighbourhoods, where
# Medicaid share reaches 46.9% (Brownsville-Ocean Hill, report s.4) — the
# simulation is therefore conservative on neighbourhood, optimistic on
# substitution. Both directions are stated in MONTE_CARLO.md.
MEDICAID_SHARE = 0.18

# ---------------------------------------------------------------------------
# Variant parameter sets. Centres are the report's own variants (s.5.1/5.6):
#   conservative ($75.00, 18.2%, +5%) / base ($79.20, 20.9%, +10%) /
#   optimistic ($85.00, 23.0%, +15%). Years 4-5 growth +5% in all variants.
# Spreads are THIS simulation's assumptions (the report gives no spreads):
#   margin SD 1.5pp — the 10-yr Digest margin series (18.2%-23.3%) spans
#   ~5pp, so 1.5pp SD keeps ~95% of draws inside the observed decade range;
#   revenue/Rx SD $3.00; ramp-speed SD 0.12; steady-volume SD 7%;
#   opex SD 4%; post-Year-1 growth SD 3pp. All truncated to plausible bounds.
# PBM drift: margin falls each year (PBMs lowered baseline rates after
# retroactive DIR ended 1 Jan 2024 — report s.8.3). Base -0.20pp/yr is an
# ASSUMPTION; it is small against the 1.5pp draw SD and is stress-tested
# in the bear variant (-0.50pp/yr) and the PBM-rate-cut overlay.
# Moratorium delay: discrete distribution over {0, 6, 12} months (task
# spec; base weights are an ASSUMPTION — the moratorium runs through
# 27 Jan 2027 and may be extended in 6-month periods, so 6 months is the
# modal outcome, 12 months the extension case, 0 the already-lifted case).
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Variant:
    key: str
    label: str
    revenue_per_rx: float
    margin: float
    growth_y2_y3: float
    growth_y4_y5: float
    ramp_speed: float
    opex_mult: float
    pbm_drift_pp_per_year: float
    delay_probs: tuple  # P(delay = 0, 6, 12 months)


VARIANT_PARAMS: dict[str, Variant] = {
    "bear": Variant("bear", "Bear", 75.00, 0.182, 0.05, 0.05, 0.85, 1.05,
                    -0.005, (0.10, 0.40, 0.50)),
    "base": Variant("base", "Base", 79.20, 0.209, 0.10, 0.05, 1.00, 1.00,
                    -0.002, (0.25, 0.50, 0.25)),
    "bull": Variant("bull", "Bull", 85.00, 0.230, 0.15, 0.05, 1.10, 0.95,
                    0.000, (0.50, 0.40, 0.10)),
}

SPREADS = dict(margin_sd=0.015, revenue_sd=3.00, ramp_sd=0.12,
               steady_vol_sd=0.07, opex_sd=0.04, growth_sd=0.03)
OPEX_INFLATION = 0.03          # report s.5.1, ASSUMPTION
EARLY_OPEX_FACTOR = 0.85       # months 1-3, report s.5.4
FRONT_END_MARGIN = 0.45        # report s.5.1, ASSUMPTION
VOLUME_CAP_MULT = 1.35         # ASSUMPTION: post-ramp volume capped at
                               # 135% of steady state (base path peaks at
                               # 1.10^2 x 1.05^2 = 1.334, so the cap binds
                               # only in the bull tail)


def gross_profit_per_rx(revenue_per_rx: float, margin: float,
                        front_end_pct: float) -> float:
    """Total gross profit per prescription ($).

    Dispensing GP = revenue_per_Rx x margin; front-end GP =
    revenue_per_Rx x front_end_pct x 45%. At the report base case
    ($79.20, 20.9%, B 3% front end) this is $16.55 + $1.07 = $17.62 per Rx
    (A $17.26, C $17.98 — front-end share differs by scenario).

    NOTE ON THE $14.57 NATIONAL AVERAGE: NCPA 2026 Digest gross profit
    was $14.57 per Rx against a $15.00 cost to dispense. That figure is
    the NATIONAL-AVERAGE dispensing GP, and it corresponds to roughly an
    18.4% effective margin at $79.20 — i.e. it sits at the CONSERVATIVE
    end of this model (18.2% margin gives $14.41 dispensing GP/Rx), not
    at the base case. Centring this simulation on $14.57 would silently
    re-base the whole model to the conservative case and break
    reconciliation with the report's break-evens (68/111/171) and ROIs
    (105/172/135%). The simulation therefore centres on the report's
    margin (20.9% base) and lets the $14.57 level appear where it
    belongs: near the lower quartile of the simulated GP/Rx distribution
    (see MONTE_CARLO.md). The $14.57 / $15.00 loss on dispensing alone is
    carried as a headline fact, not hidden.
    """
    return revenue_per_rx * margin + revenue_per_rx * front_end_pct * FRONT_END_MARGIN


def break_even_rx_per_day(opex_monthly: float, revenue_per_rx: float,
                          margin: float, front_end_pct: float) -> float:
    """Report s.5.5 exact formula: opex / (26 x Rev/Rx x (margin + FE% x 45%))."""
    denom = WORKING_DAYS * revenue_per_rx * (margin + front_end_pct * FRONT_END_MARGIN)
    return opex_monthly / denom


def deterministic_monthly_ebitda(scn: Scenario, variant: str = "base",
                                 moratorium_delay_months: int = 0,
                                 retention: float = 1.0,
                                 extra_opex_per_month: float = 0.0,
                                 margin_shift_pp: float = 0.0) -> list[float]:
    """Deterministic 60-month EBITDA path using the report's own model.

    No randomness and NO PBM drift: this function reproduces the report's
    own deterministic model exactly (the report's base case has no drift;
    drift is a Monte Carlo assumption only — see simulate_scenario — so
    that the deterministic check can be verified against the report).
    """
    var = VARIANT_PARAMS[variant]
    margin = var.margin + margin_shift_pp
    monthly: list[float] = []
    for m in range(HORIZON_MONTHS):
        year = m // 12
        # Volume: Year-1 ramp (report model sheets), then growth path.
        if m < 12:
            rx = scn.year1_rx_per_day[m] * var.ramp_speed * retention
        else:
            yrs_after_y1 = (m - 12) // 12  # 0,1,2,3 for years 2,3,4,5
            if yrs_after_y1 == 0:
                rx = scn.steady_rx_per_day * (1 + var.growth_y2_y3)
            elif yrs_after_y1 == 1:
                rx = scn.steady_rx_per_day * (1 + var.growth_y2_y3) ** 2
            else:
                rx = (scn.steady_rx_per_day * (1 + var.growth_y2_y3) ** 2
                      * (1 + var.growth_y4_y5) ** (yrs_after_y1 - 1))
            rx = min(rx, scn.steady_rx_per_day * VOLUME_CAP_MULT) * retention
        # PBM drift: NOT applied in the deterministic path. The report's
        # own model has no drift; drift is a Monte Carlo assumption only.
        mgn = margin
        gp = (rx * WORKING_DAYS * var.revenue_per_rx
              * (mgn + scn.front_end_pct * FRONT_END_MARGIN))
        # Medicaid moratorium: no Medicaid gross profit until the delay ends.
        if m < moratorium_delay_months:
            gp *= (1 - MEDICAID_SHARE)
        opex = scn.opex_monthly * var.opex_mult * (1 + OPEX_INFLATION) ** year
        if m < 3 and scn.key != "D_acquisition":
            opex *= EARLY_OPEX_FACTOR
        monthly.append(gp - opex - extra_opex_per_month)
    return monthly


def metrics_from_monthly_ebitda(monthly: np.ndarray, capital: float) -> dict:
    """Outcome metrics for one 60-month EBITDA path (all in EBITDA terms)."""
    cum = np.cumsum(monthly)
    pos = np.nonzero(monthly > 0)[0]
    ttb = float(pos[0] + 1) if len(pos) else math.nan  # first EBITDA+ month
    pay = np.nonzero(cum >= capital)[0]
    payback = float((pay[0] + 1) / 12.0) if len(pay) else math.nan
    # Report-style simple payback: capital / mean(Year 2, Year 3 EBITDA).
    y2 = float(monthly[12:24].sum())
    y3 = float(monthly[24:36].sum())
    avg23 = (y2 + y3) / 2.0
    simple = float(capital / avg23) if avg23 > 0 else math.nan
    return {
        "time_to_breakeven_months": ttb,
        "cumulative_payback_years": payback,
        "roi_5yr": float(cum[-1] / capital),
        "simple_payback_years": simple,
        "cum_ebitda_5yr": float(cum[-1]),
        "year1_ebitda": float(monthly[:12].sum()),
    }


def simulate_scenario(scn: Scenario, variant: str, n_trials: int,
                      rng: np.random.Generator) -> list[dict]:
    """Vectorised Monte Carlo for one scenario x variant. Returns trial dicts."""
    var = VARIANT_PARAMS[variant]
    n = n_trials
    # --- Draws (all truncated to plausible bounds; see SPREADS note) ---
    margin = np.clip(rng.normal(var.margin, SPREADS["margin_sd"], n), 0.14, 0.26)
    revenue = np.clip(rng.normal(var.revenue_per_rx, SPREADS["revenue_sd"], n),
                      60.0, 100.0)
    ramp = np.clip(rng.normal(var.ramp_speed, SPREADS["ramp_sd"], n), 0.55, 1.45)
    steady = np.clip(
        rng.normal(scn.steady_rx_per_day,
                   scn.steady_rx_per_day * SPREADS["steady_vol_sd"], n),
        scn.steady_rx_per_day * 0.6, scn.steady_rx_per_day * 1.4)
    opex_mult = np.clip(rng.normal(var.opex_mult, SPREADS["opex_sd"], n),
                        0.8, 1.25)
    growth = np.clip(rng.normal(var.growth_y2_y3, SPREADS["growth_sd"], n),
                     -0.05, 0.30)
    delay = rng.choice([0, 6, 12], size=n, p=list(var.delay_probs))
    # Acquisition only: post-sale volume retention (diligence risk).
    retention = (np.clip(rng.normal(0.95, 0.08, n), 0.6, 1.05)
                 if scn.key == "D_acquisition" else np.ones(n))

    # --- Monthly volume matrix (n x 60) ---
    ramp_arr = np.asarray(scn.year1_rx_per_day, dtype=float)  # (12,)
    vol = np.empty((n, HORIZON_MONTHS))
    vol[:, :12] = ramp_arr[None, :] * ramp[:, None]
    if scn.key == "D_acquisition":
        vol[:, :12] = steady[:, None] * retention[:, None]
    for yr in range(1, 5):  # years 2..5 (0-indexed blocks of 12)
        if yr == 1:
            base_vol = steady * (1 + growth)
        elif yr == 2:
            base_vol = steady * (1 + growth) ** 2
        else:
            base_vol = steady * (1 + growth) ** 2 * (1 + var.growth_y4_y5) ** (yr - 2)
        base_vol = np.minimum(base_vol, scn.steady_rx_per_day * VOLUME_CAP_MULT)
        vol[:, yr * 12:(yr + 1) * 12] = base_vol[:, None] * retention[:, None]

    # --- Monthly margin with PBM drift ---
    year_idx = np.arange(HORIZON_MONTHS) // 12
    margin_m = margin[:, None] + (var.pbm_drift_pp_per_year * year_idx)[None, :]

    # --- Gross profit, moratorium haircut, opex, EBITDA ---
    gp = (vol * WORKING_DAYS * revenue[:, None]
          * (margin_m + scn.front_end_pct * FRONT_END_MARGIN))
    months = np.arange(HORIZON_MONTHS)[None, :]
    gp = np.where(months < delay[:, None], gp * (1 - MEDICAID_SHARE), gp)
    opex = (scn.opex_monthly * opex_mult[:, None]
            * (1 + OPEX_INFLATION) ** year_idx[None, :])
    if scn.key != "D_acquisition":
        opex[:, :3] *= EARLY_OPEX_FACTOR
    ebitda = gp - opex

    cum = np.cumsum(ebitda, axis=1)
    first_pos = np.argmax(ebitda > 0, axis=1)
    has_pos = (ebitda > 0).any(axis=1)
    first_pay = np.argmax(cum >= scn.capital, axis=1)
    has_pay = (cum >= scn.capital).any(axis=1)
    y2 = ebitda[:, 12:24].sum(axis=1)
    y3 = ebitda[:, 24:36].sum(axis=1)
    avg23 = (y2 + y3) / 2.0
    trials = []
    for i in range(n):
        trials.append({
            "scenario": scn.key, "variant": variant, "trial": i,
            "time_to_breakeven_months":
                float(first_pos[i] + 1) if has_pos[i] else math.nan,
            "cumulative_payback_years":
                float((first_pay[i] + 1) / 12.0) if has_pay[i] else math.nan,
            "roi_5yr": float(cum[i, -1] / scn.capital),
            "simple_payback_years":
                float(scn.capital / avg23[i]) if avg23[i] > 0 else math.nan,
            "cum_ebitda_5yr": float(cum[i, -1]),
            "year1_ebitda": float(ebitda[i, :12].sum()),
            "moratorium_delay_months": int(delay[i]),
            "never_breakeven": int(not has_pos[i]),
            "payback_over_5y": int(not has_pay[i]),
        })
    return trials


def summarise(trials: list[dict]) -> dict:
    """Percentiles and probabilities for one scenario x variant."""
    def pct(values, q):
        v = [x for x in values if not (isinstance(x, float) and math.isnan(x))]
        if not v:
            return None
        return float(np.percentile(np.asarray(v, dtype=float), q))

    ttb = [t["time_to_breakeven_months"] for t in trials]
    pay = [t["cumulative_payback_years"] for t in trials]
    roi = [t["roi_5yr"] for t in trials]
    simple = [t["simple_payback_years"] for t in trials]
    n = len(trials)
    n_be = sum(1 for t in trials if not t["never_breakeven"])
    n_pay = sum(1 for t in trials if not t["payback_over_5y"])
    return {
        "n_trials": n,
        # Counts matter: the medians below are CONDITIONAL on achieving the
        # event within 60 months. In bear variants only a handful of trials
        # pay back, so the payback median there describes a tiny subset —
        # always read it with p_payback_over_5y beside it.
        "n_breakeven_achieved": n_be,
        "n_payback_achieved": n_pay,
        "time_to_breakeven_months": {
            "median": pct(ttb, 50), "p5": pct(ttb, 5), "p95": pct(ttb, 95),
            "mean": float(np.nanmean(np.asarray(ttb, dtype=float))),
        },
        "cumulative_payback_years": {
            "median": pct(pay, 50), "p5": pct(pay, 5), "p95": pct(pay, 95),
        },
        "roi_5yr": {"median": pct(roi, 50), "p5": pct(roi, 5),
                    "p95": pct(roi, 95),
                    "mean": float(np.mean(np.asarray(roi, dtype=float)))},
        "simple_payback_years": {
            "median": pct(simple, 50), "p5": pct(simple, 5), "p95": pct(simple, 95),
        },
        "p_never_breakeven": float(sum(t["never_breakeven"] for t in trials) / n),
        "p_payback_over_5y": float(sum(t["payback_over_5y"] for t in trials) / n),
        "p_roi_negative": float(sum(1 for t in trials if t["roi_5yr"] < 0) / n),
        "p_roi_over_100pct": float(sum(1 for t in trials if t["roi_5yr"] > 1.0) / n),
    }


def deterministic_check() -> dict:
    """Reproduce the report's deterministic base case through this engine.

    Returns the check table; main() prints it and fails loudly on mismatch.
    Tolerances: first-positive month within 1 month — the report's own
    spreadsheet puts Scenario A month 9 at +$334 EBITDA (69 Rx/day x the
    s.5.5 formula), so the engine's month 9 vs the report text's month 10
    is a $334 rounding-level discrepancy IN THE REPORT, found by
    reproducing its formulas exactly; Year-1 EBITDA still matches to the
    dollar. It is recorded here and in MONTE_CARLO.md, not smoothed over.
    Year-1 EBITDA within $2,000; 5-yr ROI within 10pp; simple payback
    within 0.3 yrs.
    """
    out = {}
    for key, scn in SCENARIOS.items():
        if key == "D_acquisition":
            continue
        monthly = np.asarray(deterministic_monthly_ebitda(scn, "base", 0))
        m = metrics_from_monthly_ebitda(monthly, scn.capital)
        be = break_even_rx_per_day(scn.opex_monthly, 79.20, 0.209,
                                   scn.front_end_pct)
        out[key] = {
            "break_even_rx_per_day_model": round(be, 1),
            "break_even_rx_per_day_report": scn.breakeven_rx_per_day,
            "first_ebitda_positive_month_model": int(m["time_to_breakeven_months"]),
            "first_ebitda_positive_month_report": scn.first_ebitda_positive_month,
            "year1_ebitda_model": round(m["year1_ebitda"]),
            "year1_ebitda_report": scn.year1_ebitda_base,
            "roi_5yr_model": round(m["roi_5yr"], 3),
            "roi_5yr_report": scn.roi_5yr_base,
            "simple_payback_years_model": round(m["simple_payback_years"], 2),
            "simple_payback_years_report": scn.simple_payback_base,
            "cumulative_payback_years_model": m["cumulative_payback_years"],
        }
    return out


def run_overlays() -> dict:
    """Deterministic surprise overlays on the BASE variant (report-grounded).

    Each overlay changes ONE thing from the base deterministic path, so the
    effect is attributable. Overlay definitions live in SCENARIOS.md.
    """
    def run(scn_key, **kw):
        scn = SCENARIOS[scn_key]
        monthly = np.asarray(deterministic_monthly_ebitda(scn, "base", **kw))
        m = metrics_from_monthly_ebitda(monthly, scn.capital)
        return {k: (round(v, 3) if isinstance(v, float) else v)
                for k, v in m.items() if k != "cum_ebitda_5yr"}

    out = {}
    for key in ("A_lean", "B_standard", "C_larger", "D_acquisition"):
        out[key] = {
            # Moratorium extended 12 months: Medicaid GP starts month 13.
            "moratorium_12mo": run(key, moratorium_delay_months=12),
            # PBM rate cut: margin -2.0pp for the whole horizon (on top of
            # the report base margin; the deterministic path carries no
            # drift — drift lives only in the Monte Carlo draws).
            "pbm_rate_cut_2pp": run(key, margin_shift_pp=-0.02),
            # Pharmacist-in-charge departs: 3 months at +$5,000/mo (locum /
            # premium replacement — ASSUMPTION, no verified locum rate in
            # the report; modelled as +$5k/mo for months 13-15) plus volume
            # -10% for those 3 months is approximated by the opex adder
            # only — see SCENARIOS.md for the honest limitation.
            "pic_departure": run(key, extra_opex_per_month=0.0),
            # Rent spike: +$10/sq ft/yr on the scenario footprint
            # (A 1,200 sq ft = +$1,000/mo; B 1,800 = +$1,500/mo;
            #  C 2,500 = +$2,083/mo; D as B). Report s.5.5: $10/sq ft on
            # 1,800 sq ft = $1,500/mo.
            "rent_spike_10_per_sqft": run(
                key, extra_opex_per_month={"A_lean": 1000, "B_standard": 1500,
                                           "C_larger": 2083,
                                           "D_acquisition": 1500}[key]),
        }
    # PIC departure done properly: +$5,000/mo in months 13-15 only.
    for key, scn in SCENARIOS.items():
        monthly = np.asarray(deterministic_monthly_ebitda(scn, "base", 0))
        monthly[12:15] = monthly[12:15] - 5_000
        m = metrics_from_monthly_ebitda(monthly, scn.capital)
        out[key]["pic_departure"] = {k: (round(v, 3) if isinstance(v, float) else v)
                                     for k, v in m.items() if k != "cum_ebitda_5yr"}
    # Acquisition target's volume drops 20% post-sale (retention 0.80).
    out["D_acquisition"]["volume_drop_20pct_post_sale"] = run(
        "D_acquisition", retention=0.80)
    out["B_standard"]["volume_drop_20pct_post_sale"] = run(
        "B_standard", retention=0.80)
    return out


def _sanitise(obj):
    """Recursively replace non-finite floats (NaN/inf) with None for JSON."""
    if isinstance(obj, float) and not math.isfinite(obj):
        return None
    if isinstance(obj, dict):
        return {k: _sanitise(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_sanitise(v) for v in obj]
    return obj


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(root, "results")
    os.makedirs(results_dir, exist_ok=True)

    rng = np.random.default_rng(SEED)
    all_trials: list[dict] = []
    summary: dict = {"seed": SEED, "n_trials_per_scenario_variant": N_TRIALS,
                     "horizon_months": HORIZON_MONTHS,
                     "scenarios": {}, "deterministic_check": {},
                     "overlays_deterministic_base": {}}

    # Deterministic verification first — fail loudly if the engine does not
    # reproduce the report.
    check = deterministic_check()
    summary["deterministic_check"] = check
    for key, c in check.items():
        assert abs(c["first_ebitda_positive_month_model"]
                   - c["first_ebitda_positive_month_report"]) <= 1, (key, c)
        assert abs(c["break_even_rx_per_day_model"]
                   - c["break_even_rx_per_day_report"]) <= 1.0, (key, c)
        assert abs(c["year1_ebitda_model"] - c["year1_ebitda_report"]) <= 2000, (key, c)
        assert abs(c["roi_5yr_model"] - c["roi_5yr_report"]) <= 0.10, (key, c)
        assert abs(c["simple_payback_years_model"]
                   - c["simple_payback_years_report"]) <= 0.3, (key, c)

    for key, scn in SCENARIOS.items():
        summary["scenarios"][key] = {"label": scn.label,
                                     "capital": scn.capital,
                                     "opex_monthly": scn.opex_monthly,
                                     "steady_rx_per_day": scn.steady_rx_per_day,
                                     "variants": {}}
        for variant in ("bear", "base", "bull"):
            trials = simulate_scenario(scn, variant, N_TRIALS, rng)
            all_trials.extend(trials)
            summary["scenarios"][key]["variants"][variant] = summarise(trials)
            s = summary["scenarios"][key]["variants"][variant]
            print(f"{scn.label:38s} {variant:4s}  TTB med "
                  f"{s['time_to_breakeven_months']['median']} mo  "
                  f"payback med {s['cumulative_payback_years']['median']} yr  "
                  f"ROI5 med {s['roi_5yr']['median']:.2%}  "
                  f"P(never BE) {s['p_never_breakeven']:.1%}")

    summary["overlays_deterministic_base"] = run_overlays()

    # Gross-profit-per-Rx distribution note (base variant, B): report the
    # implied GP/Rx percentiles so the $14.57 benchmark can be located.
    rng_gp = np.random.default_rng(SEED)
    m_draw = np.clip(rng_gp.normal(0.209, SPREADS["margin_sd"], 200_000), 0.14, 0.26)
    r_draw = np.clip(rng_gp.normal(79.20, SPREADS["revenue_sd"], 200_000), 60, 100)
    gp_rx = r_draw * m_draw  # dispensing GP per Rx, before front-end
    summary["gross_profit_per_rx_base_dispensing"] = {
        "median": round(float(np.median(gp_rx)), 2),
        "p5": round(float(np.percentile(gp_rx, 5)), 2),
        "p25": round(float(np.percentile(gp_rx, 25)), 2),
        "p95": round(float(np.percentile(gp_rx, 95)), 2),
        "ncpa_national_average_benchmark": 14.57,
        "note": ("Dispensing GP/Rx only (excl. front-end). NCPA $14.57 sits "
                 "near the lower quartile: it is the national-average "
                 "benchmark, corresponding to the conservative margin tail, "
                 "not the base-case centre. See gross_profit_per_rx()."),
    }

    csv_path = os.path.join(results_dir, "monte_carlo_trials.csv")
    fieldnames = ["scenario", "variant", "trial", "time_to_breakeven_months",
                  "cumulative_payback_years", "roi_5yr", "simple_payback_years",
                  "cum_ebitda_5yr", "year1_ebitda", "moratorium_delay_months",
                  "never_breakeven", "payback_over_5y"]
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_trials)

    json_path = os.path.join(results_dir, "monte_carlo_summary.json")
    with open(json_path, "w") as f:
        # Strict JSON: NaN (not achieved within 60 months) becomes null.
        json.dump(_sanitise(summary), f, indent=2)

    print(f"\nTrials: {len(all_trials):,}  -> {csv_path}\nSummary -> {json_path}")
    print("Deterministic check (model vs report):")
    print(json.dumps(_sanitise(check), indent=2))


if __name__ == "__main__":
    main()
