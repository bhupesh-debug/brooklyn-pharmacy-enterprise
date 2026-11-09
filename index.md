# Brooklyn Pharmacy Enterprise

**A complete enterprise package for acquiring — not building — an independent retail community pharmacy in Brooklyn, New York, as a U.S. Green Card holder.**

## Verdict: CONDITIONAL GO — ACQUIRE, DO NOT BUILD

Commit no capital until five gates clear:

1. **Medicaid moratorium resolved in writing** (NY freeze on pharmacy enrollments and ownership changes, through at least 27 January 2027).
2. **Suitable target at a disciplined price** (2.5–3.5× adjusted EBITDA + inventory at cost).
3. **Supervising pharmacist secured in writing** (full-time, 30+ hrs/week, one pharmacy only).
4. **Financing confirmed without SBA** (SBA is closed to a green card holder owner since 1 March 2026).
5. **Healthcare attorney + pharmacy CPA engaged pre-LOI.**

If any gate fails, wait. If no pharmacist-in-charge can be secured at all, do neither.

## The numbers

| Figure | Value |
|---|---|
| Startup capital — Lean / Standard / Larger | $435,230 / $791,010 / $1,309,273 |
| Break-even volume | 68 / 111 / 171 Rx/day |
| Acquisition case modelled | $880,000 cash to close |
| Gross profit per Rx vs cost to dispense | $14.57 vs $15.00 — dispensing alone loses money |
| Monte Carlo, base — median 5-yr ROI | Lean 82.8% / Standard 149.7% / Larger 114.5% / Acquisition 129.6% |
| Monte Carlo, base — median time to break-even | 10 / 8 / 10 / 1 months |
| Top neighbourhoods | East New York–Starrett City 78.5, East Flatbush 75.0, Brownsville–Ocean Hill 74.5 |

## What's in this project

- **[README.md](README.md)** — verdict, gates, key numbers, reading order.
- **[VIEWPOINT.md](VIEWPOINT.md)** — the investor viewpoint: the thesis, and what would change the verdict.
- **[RECOMMENDATION.md](RECOMMENDATION.md)** — verdict, evidence, first five actions, 16 things to avoid.
- **[SWOT.md](SWOT.md)** — strengths, weaknesses, opportunities, threats, each with evidence.
- **[HYPOTHESIS.md](HYPOTHESIS.md)** — six testable hypotheses with confirm/falsify conditions.
- **[SCENARIOS.md](SCENARIOS.md)** — three startup scenarios plus acquisition, base/bull/bear, surprise overlays.
- **[MONTE_CARLO.md](MONTE_CARLO.md)** — the simulation: 120,000 trials, seed 20261109, reproducible.
- **[PRD.md](PRD.md)** — product requirements for the pharmacy enterprise.
- **[PRD2PRO.md](PRD2PRO.md)** — professional implementation: build/buy/hire, 8 phases, go/no-go gates.
- **[IMPLEMENTATION.md](IMPLEMENTATION.md)** — the 180-day roadmap as 30 ordered steps, Day-60 moratorium hard pause.
- **[JOB_MASTERY.md](JOB_MASTERY.md)** — owner-operator mastery plan: capability map, readiness rubric, 7 projects.
- **[OPERATING_PLAN.md](OPERATING_PLAN.md)** — daily, weekly, monthly, quarterly, annual operating rhythm.
- **[sop/](sop/)** — 11 standard operating procedures for the running pharmacy.
- **[src/monte_carlo.py](src/monte_carlo.py)** and **[tests/test_monte_carlo.py](tests/test_monte_carlo.py)** — the simulation and its 12 tests.
- **[results/](results/)** — 120,000 trial rows and the summary statistics.

## Run it yourself

```bash
python src/monte_carlo.py
pytest tests/test_monte_carlo.py
```

## Sources

Built from the master advisory package of 9 November 2026 (105-page report + financial model + corrected step-wise guide). Every number traces to that report or a cited primary source (NYSED, NYSDOH, DEA, CMS, SBA, NCPA). Nothing is invented: no owner name, capital, credit score, or neighbourhood was supplied, and none is assumed. Research and education only — not legal, tax, immigration, or financial advice.
