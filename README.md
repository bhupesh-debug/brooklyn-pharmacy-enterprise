# Brooklyn Pharmacy Enterprise

**A complete enterprise package for opening — by acquiring — an independent retail community pharmacy in Brooklyn, New York, as a U.S. Green Card holder.**

## Verdict up front

**CONDITIONAL GO — ACQUIRE, DO NOT BUILD.**

Commit no capital until five gates clear:

1. **Medicaid moratorium resolved in writing** — New York's Medicaid enrollment moratorium on pharmacies (CMS-approved 27 July 2026, through 27 January 2027, extendable in 6-month periods) covers new enrollments **and** changes of ownership. It gates both the startup and the acquisition route.
2. **Suitable target at a disciplined price** — inside the U.S. valuation band of 2.5–3.5× adjusted EBITDA + inventory at cost (BizBuySell 2021–2025 average 2.79×, 2025 median sale $600,000).
3. **Supervising pharmacist secured in writing** — a full-time (30+ hrs/week, one pharmacy only) NY-licensed pharmacist-in-charge. The owner does not hold a pharmacist licence and never dispenses.
4. **Financing confirmed without SBA** — SBA 7(a)/504/Microloan is **closed** to this owner (Policy Notice 5000-876441, eff. 1 March 2026, now SOP 50 10 8.1): a green card holder may not own any share of an SBA borrower, even 1%. Financing = personal capital, conventional bank loans, non-SBA CDFI loans, seller financing.
5. **Healthcare attorney + pharmacy CPA engaged pre-LOI** — before any letter of intent, deposit, or lease signature.

If any gate fails for a target, **wait** — do not default to opening from scratch. If no pharmacist-in-charge can be secured at all, do neither.

## The opportunity in one paragraph

A green card holder can legally own 100% of a retail pharmacy in New York without personally holding a pharmacist licence (Ed. Law §6808). Brooklyn is the largest borough by population (2.74 million in 2020), holds one-third of New York City's Medicaid enrollees, and has just lost its entire Rite Aid footprint — real, block-specific gaps exist. But the economics are hostile to a dispensing-only business: at the national average in 2024, an independent pharmacy earned $14.57 of gross profit per prescription against a $15.00 cost to dispense it — a loss on the core act of dispensing. The profit has to come from the acquired book of business, front-end sales, and clinical services, and the purchase price has to leave room for it. That is why the verdict is acquire, not build.

## Key numbers (all traced to the master report — see Sources)

| Figure | Value |
|---|---|
| Startup capital — Lean / Standard / Larger | $435,230 / $791,010 / $1,309,273 |
| Break-even volume — Lean / Standard / Larger | 68 / 111 / 171 Rx/day |
| Acquisition case modelled (median price + inventory + closing/WC) | $880,000 |
| Gross profit per Rx vs cost to dispense (national average, NCPA 2026 Digest) | $14.57 vs $15.00 (−$0.43/Rx) |
| Gross margin (national average) | 20.9% |
| Monthly EBITDA turns positive | Months 8–10 of Year 1 |
| Cumulative payback (deterministic, base) | ~3.8 / 2.5 / 3.1 years (A / B / C) |
| 5-year ROI, deterministic base | ~105% / ~172% / ~135% (A / B / C) |
| Monte Carlo, base variant, median 5-yr ROI | 82.8% / 149.7% / 114.5% / 129.6% (A / B / C / Acquisition) |
| Monte Carlo, base variant, median time to break-even | 10 / 8 / 10 / 1 months (A / B / C / Acquisition) |
| Top neighbourhoods (0–100) | East New York–Starrett City 78.5, East Flatbush 75.0, Brownsville–Ocean Hill 74.5 |
| NYSED establishment registration (PH200/PH210/PH208) | $345, file 10–14 weeks ahead |
| DEA registration | $888 / 3 years |
| Medicare enrollment (2026) / Medicaid fee | $750 / waived if Medicare paid ($750 total) |

## How to use this package

**Read in this order:**

1. **[VIEWPOINT.md](VIEWPOINT.md)** — the investor viewpoint: the thesis in one page, and what would change the verdict.
2. **[RECOMMENDATION.md](RECOMMENDATION.md)** — the verdict, the evidence, the first five actions, and what to avoid (16 items).
3. **[SWOT.md](SWOT.md)** and **[HYPOTHESIS.md](HYPOTHESIS.md)** — the strategic picture and the six testable hypotheses with confirm/falsify conditions.
4. **[SCENARIOS.md](SCENARIOS.md)** and **[MONTE_CARLO.md](MONTE_CARLO.md)** — all scenarios and the simulation behind them.
5. **[PRD.md](PRD.md)** and **[PRD2PRO.md](PRD2PRO.md)** — what the enterprise is, and how it is built phase by phase.
6. **[IMPLEMENTATION.md](IMPLEMENTATION.md)** — the 180-day roadmap as 30 ordered steps, with the Day-60 moratorium hard pause.
7. **[JOB_MASTERY.md](JOB_MASTERY.md)** and **[OPERATING_PLAN.md](OPERATING_PLAN.md)** — what the owner-operator must be able to do, and the daily/weekly/monthly operating rhythm.
8. **[sop/](sop/)** — the 11 standard operating procedures for the running pharmacy.

**Run the numbers yourself:**

```bash
python src/monte_carlo.py        # 120,000 trials, fixed seed 20261109; writes results/
pytest tests/test_monte_carlo.py # 12 tests
```

## File index

| File | What it is |
|---|---|
| `README.md` | This file — verdict, gates, key numbers, reading order. |
| `VIEWPOINT.md` | Investor viewpoint: thesis, what would change the verdict. |
| `PRD.md` | Product requirements for the pharmacy enterprise (operating system + acquisition-and-launch product). 19 sections, requirements with acceptance criteria. |
| `PRD2PRO.md` | Professional implementation of the PRD: build/buy/hire decisions, 8 phases, acceptance criteria, go/no-go gates. |
| `SWOT.md` | Strengths, weaknesses, opportunities, threats — each with evidence. |
| `HYPOTHESIS.md` | 6 testable hypotheses with confirm/falsify conditions. |
| `SCENARIOS.md` | All scenarios: 3 startup + acquisition, base/bull/bear, 5 surprise overlays, walk-away triggers. |
| `MONTE_CARLO.md` | The simulation: distributions, parameters, headline results, limitations. |
| `RECOMMENDATION.md` | Verdict, evidence, first five actions, 16 things to avoid. |
| `JOB_MASTERY.md` | Owner-operator mastery plan: capability map, readiness rubric, learning path, 7 projects. |
| `OPERATING_PLAN.md` | Daily/weekly/monthly/quarterly/annual schedules and the operating cycle. |
| `IMPLEMENTATION.md` | 180-day roadmap as 30 ordered steps with owner, cost, dependency, milestone. |
| `sop/SOP-01-opening-closing.md` … `sop/SOP-11-staff-roles-escalation.md` | 11 SOPs: opening/closing, dispensing, inventory, PBM adjudication, cash, delivery, counselling & immunisations, compliance, fraud & security, controlled substances, staff roles & escalation. |
| `src/monte_carlo.py` | The Monte Carlo simulation (seed 20261109, 10,000 trials × 4 scenarios × 3 variants). |
| `tests/test_monte_carlo.py` | 12 tests (reproducibility, break-even logic, output sanity). |
| `results/monte_carlo_trials.csv` | 120,000 trial rows from the run. |
| `results/monte_carlo_summary.json` | Summary statistics from the run. |
| `_config.yml`, `index.md` | GitHub Pages site (Jekyll Cayman theme). |

## Source of truth

This package is built from the master advisory package delivered 9 November 2026:

- `Pharmacy_Startup_Advisory_Brooklyn_Master_Report_2026-11-09.md` (105 pages) and its PDF twin — all 10 phases of the original master prompt.
- `Pharmacy_Startup_Financial_Model_Brooklyn_2026-11-09.xlsx` (9 sheets, live formulas).
- `open-a-pharmacy-in-brooklyn-step-by-step.pdf` (5-page step-wise guide, corrected 9 November 2026).

Every number in this repository traces to that report/model or a cited primary source (NYSED, NYSDOH, DEA, CMS, SBA, NCPA). **Nothing in this package is invented**: no owner name, capital amount, credit score, or preferred neighbourhood was supplied, and none is assumed. Every assumption is labelled as an assumption with its basis.

## What is still missing (carried forward, not resolved)

- **Unverified items:** the master report's Appendix A.9 is headed "23 items" but names **21 items** in its list — the two-item count discrepancy is flagged in `OPERATING_PLAN.md` §9.1 and carried here. The 21 named items (NCPDP fees, processing times, permit fees, record-retention period, DSCSA exemption date, and others) are listed in full in `JOB_MASTERY.md` §9.
- **10 attorney questions** — listed in `JOB_MASTERY.md` §9, `PRD.md` Appendix C, and `PRD2PRO.md` §10, including whether an entity purchase escapes the moratorium and the BNE licence question.
- **12 owner inputs still missing** — available capital, credit profile, target neighbourhood, pharmacist status, naturalisation timeline, and others (`JOB_MASTERY.md` §8). The model runs on labelled assumptions until the owner supplies them.
- **12 market data gaps (G1–G12)** — neighbourhood-level competition and clinical-proximity counts that do not exist in public sources; no neighbourhood scores above 80 for that reason.
- **Two report discrepancies found during this build and documented, not smoothed over:** (1) the spreadsheet's check-line still prints Scenario C 5-year ROI as ~150%; the report corrected it to ~135% (134.6% at +5%/yr Years 4–5 growth) — this package uses ~135%; (2) the report's own spreadsheet puts Scenario A first-positive EBITDA in month 9, while the report text says month 10 — the simulation reproduces month 9 and documents the difference in `MONTE_CARLO.md` §2.2.

## What this package is not

Research and education, not legal, tax, immigration, or financial advice. Nothing in it authorises opening, filing, or spending. The owner must obtain advice from a licensed NY healthcare/pharmacy attorney, a pharmacy CPA, and — for immigration questions — an immigration attorney before acting. No agency was contacted, no one was interviewed, no money was spent in building it.

## Suggested repository

Suggested name: **`brooklyn-pharmacy-enterprise`**. Create the empty repository manually (integrations cannot create repositories), then push this directory to `main`. Enable GitHub Pages (Settings → Pages → Deploy from a branch, `main`, `/(root)`) to publish the site from `index.md`.
