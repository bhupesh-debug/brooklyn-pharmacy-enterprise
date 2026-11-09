"""Tests for src/monte_carlo.py — Brooklyn pharmacy Monte Carlo.

Run from the repo root with the project venv:
    ~/workspace/quant-ipo-engine/.venv/bin/python -m pytest tests/test_monte_carlo.py -v
Or without pytest (plain asserts, runnable as a script):
    ~/workspace/quant-ipo-engine/.venv/bin/python tests/test_monte_carlo.py

All expected values trace to the master report
(Pharmacy_Startup_Advisory_Brooklyn_Master_Report_2026-11-09.md):
capital A $435,230 / B $791,010 / C $1,309,273 (s.5.2); steady opex
$30,641 / $51,050 / $80,083 (s.5.3); break-even 68 / 111 / 171 Rx/day
(s.5.5); first EBITDA-positive month 10 / 8 / 9 (s.5.4); Year-1 EBITDA
-$76,031 / -$56,315 / -$160,701 and 5-yr ROI ~105% / ~172% / ~135%
(s.5.6). See MONTE_CARLO.md for the one known $334 discrepancy:
the report's own spreadsheet puts Scenario A month 9 at +$334 EBITDA,
so the engine's month 9 vs the report text's month 10 is a report-side
rounding-level discrepancy, not an engine error.
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "src"))

from monte_carlo import (  # noqa: E402
    SCENARIOS, SEED, VARIANT_PARAMS, break_even_rx_per_day,
    deterministic_monthly_ebitda, gross_profit_per_rx,
    metrics_from_monthly_ebitda, simulate_scenario, summarise,
)

ATOL_BE = 1.0        # break-even Rx/day tolerance (report rounds to whole Rx)
ATOL_Y1 = 2_000      # Year-1 EBITDA tolerance ($; report rounds monthly tables)
ATOL_ROI = 0.10      # 5-yr ROI tolerance (10pp; report rounds to ~105/172/135%)


def test_reproducibility_same_seed_identical_results():
    """Same seed -> identical trial-level results (fixed-seed requirement)."""
    rng1 = np.random.default_rng(SEED)
    rng2 = np.random.default_rng(SEED)
    t1 = simulate_scenario(SCENARIOS["B_standard"], "base", 200, rng1)
    t2 = simulate_scenario(SCENARIOS["B_standard"], "base", 200, rng2)
    assert len(t1) == len(t2) == 200
    for a, b in zip(t1, t2):
        assert a == b, f"trial differs under same seed: {a} vs {b}"


def test_reproducibility_different_seed_differs():
    rng1 = np.random.default_rng(SEED)
    rng2 = np.random.default_rng(SEED + 1)
    t1 = simulate_scenario(SCENARIOS["B_standard"], "base", 200, rng1)
    t2 = simulate_scenario(SCENARIOS["B_standard"], "base", 200, rng2)
    assert any(a["roi_5yr"] != b["roi_5yr"] for a, b in zip(t1, t2))


def test_break_even_matches_report():
    """Report s.5.5 exact formula reproduces 68 / 111 / 171 Rx/day."""
    for key, expected in (("A_lean", 68), ("B_standard", 111),
                          ("C_larger", 171)):
        scn = SCENARIOS[key]
        got = break_even_rx_per_day(scn.opex_monthly, 79.20, 0.209,
                                    scn.front_end_pct)
        assert abs(got - expected) <= ATOL_BE, (key, got, expected)
        assert abs(got - scn.breakeven_rx_per_day) <= ATOL_BE


def test_deterministic_reproduces_report_year1_and_roi():
    """Deterministic engine reproduces the report's Year-1 EBITDA and ROI."""
    for key, scn in SCENARIOS.items():
        if key == "D_acquisition":
            continue
        monthly = np.asarray(deterministic_monthly_ebitda(scn, "base", 0))
        m = metrics_from_monthly_ebitda(monthly, scn.capital)
        assert abs(m["year1_ebitda"] - scn.year1_ebitda_base) <= ATOL_Y1, \
            (key, m["year1_ebitda"], scn.year1_ebitda_base)
        assert abs(m["roi_5yr"] - scn.roi_5yr_base) <= ATOL_ROI, \
            (key, m["roi_5yr"], scn.roi_5yr_base)
        assert abs(m["simple_payback_years"] - scn.simple_payback_base) <= 0.3, \
            (key, m["simple_payback_years"])


def test_deterministic_first_positive_month_within_one():
    """First EBITDA-positive month: B 8 and C 9 exact; A 9 vs report 10.

    The A gap is the report's own $334 month-9 discrepancy (see module
    docstring / MONTE_CARLO.md): the spreadsheet's own formulas give
    month-9 EBITDA of +$334 for A, so the engine follows the formulas.
    Tolerance of 1 month is therefore the honest bound, not a fudge.
    """
    for key, scn in SCENARIOS.items():
        if key == "D_acquisition":
            continue
        monthly = np.asarray(deterministic_monthly_ebitda(scn, "base", 0))
        m = metrics_from_monthly_ebitda(monthly, scn.capital)
        assert abs(m["time_to_breakeven_months"]
                   - scn.first_ebitda_positive_month) <= 1, (key, m)


def test_no_nan_or_inf_in_simulation_outputs():
    """Every trial ROI / Year-1 EBITDA is finite; event times are finite or NaN
    (NaN = event not achieved within 60 months, which is a valid outcome,
    never a numerical failure). No inf anywhere."""
    rng = np.random.default_rng(SEED)
    for key, scn in SCENARIOS.items():
        trials = simulate_scenario(scn, "base", 500, rng)
        for t in trials:
            assert math.isfinite(t["roi_5yr"]), (key, t)
            assert math.isfinite(t["year1_ebitda"]), (key, t)
            assert math.isfinite(t["cum_ebitda_5yr"]), (key, t)
            for field in ("time_to_breakeven_months",
                          "cumulative_payback_years", "simple_payback_years"):
                v = t[field]
                assert v is None or math.isnan(v) or math.isfinite(v), (key, t)
                assert not (isinstance(v, float) and math.isinf(v)), (key, t)


def test_roi_payback_sanity_bounds():
    """ROI within [-300%, +600%]; payback, when achieved, within (0, 5] years;
    time-to-break-even, when achieved, within 1..60 months. The -300%
    floor is a sanity bound, not a theoretical one: in the full 120,000-
    trial run the worst observed ROI is -250% (Lean bear — 60 months of
    losses on the smallest capital base), so -300% admits the observed
    tail with headroom while still catching a sign or scale error."""
    rng = np.random.default_rng(SEED)
    for key, scn in SCENARIOS.items():
        for variant in ("bear", "base", "bull"):
            trials = simulate_scenario(scn, variant, 500, rng)
            for t in trials:
                assert -3.0 <= t["roi_5yr"] <= 6.0, (key, variant, t)
                if not math.isnan(t["cumulative_payback_years"]):
                    assert 0 < t["cumulative_payback_years"] <= 5.0, (key, variant, t)
                if not math.isnan(t["time_to_breakeven_months"]):
                    assert 1 <= t["time_to_breakeven_months"] <= 60, (key, variant, t)


def test_moratorium_delay_monotone():
    """A longer moratorium delay cannot improve the deterministic outcome:
    12-month delay Year-1 EBITDA <= 6-month <= 0-month, for every scenario."""
    for key, scn in SCENARIOS.items():
        prev = math.inf
        for delay in (0, 6, 12):
            monthly = np.asarray(deterministic_monthly_ebitda(
                scn, "base", delay))
            y1 = float(monthly[:12].sum())
            assert y1 <= prev + 1e-9, (key, delay, y1, prev)
            prev = y1


def test_bear_worse_than_bull_ordering():
    """Variant ordering: median 5-yr ROI bear < base < bull (sanity: the
    variant centres actually move the outcome in the intended direction)."""
    rng = np.random.default_rng(SEED)
    for key, scn in SCENARIOS.items():
        medians = {}
        for variant in ("bear", "base", "bull"):
            trials = simulate_scenario(scn, variant, 1_000, rng)
            medians[variant] = summarise(trials)["roi_5yr"]["median"]
        assert medians["bear"] < medians["base"] < medians["bull"], \
            (key, medians)


def test_gross_profit_per_rx_benchmark():
    """Base-case dispensing GP/Rx is $79.20 x 20.9% = $16.55, and the NCPA
    $14.57 national average sits BELOW the base centre (it corresponds to
    the ~18.4% conservative-margin tail), as documented in the module.
    Front-end GP is additional."""
    disp = 79.20 * 0.209
    assert abs(disp - 16.55) < 0.01
    assert disp > 14.57
    assert abs(gross_profit_per_rx(79.20, 0.209, 0.03) - (disp + 79.20 * 0.03 * 0.45)) < 1e-9
    # Conservative margin reproduces the national-average level:
    assert abs(79.20 * 0.182 - 14.41) < 0.01


def test_acquisition_starts_at_steady_state():
    """Acquisition has no ramp: deterministic month-1 EBITDA is positive
    and equals the B steady-state run-rate (GP at 150 Rx/day - opex)."""
    scn = SCENARIOS["D_acquisition"]
    monthly = deterministic_monthly_ebitda(scn, "base", 0)
    assert monthly[0] > 0
    assert abs(monthly[0] - 17_676) <= 1  # 150 Rx/day GP $68,726 - $51,050
    assert scn.capital == 880_000  # $600k price + $180k inventory + $100k


def test_sba_not_available_note():
    """Guardrail: the module docstring must state SBA is closed to this
    owner and never claim SBA eligibility. (A text-level tripwire so a
    future edit cannot silently reintroduce the old wrong claim.)"""
    path = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "src", "monte_carlo.py")
    text = open(path, encoding="utf-8").read()
    assert "SBA is CLOSED to this owner" in text
    assert "5000-876441" in text
    assert "SBA eligibility is NEVER claimed" in text


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"{len(tests)} tests passed")
