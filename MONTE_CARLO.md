# Monte Carlo Simulation — Brooklyn Independent Pharmacy Enterprise

**Owner:** a U.S. Green Card holder (Lawful Permanent Resident). **Not Bhupesh.**
Bhupesh asked for this package on the owner's behalf. Nothing here applies
Bhupesh's background, resume, or STEM OPT situation to the owner, and no
owner name, capital figure, credit score, or preferred neighbourhood is
invented anywhere in this package — where the owner has not supplied an
input, the simulation uses the report's scenario figure and says so.

**Source of truth:** `Pharmacy_Startup_Advisory_Brooklyn_Master_Report_2026-11-09.md`
(105 pp) and its companion model `Pharmacy_Startup_Financial_Model_Brooklyn_2026-11-09.xlsx`.
Every report-sourced number below cites the report section. Anything marked
**ASSUMPTION** is this simulation's assumption, with its basis stated.

**Code:** `src/monte_carlo.py` · **Tests:** `tests/test_monte_carlo.py` (12 passed)
· **Outputs:** `results/monte_carlo_trials.csv` (120,000 trials),
`results/monte_carlo_summary.json` · **Seed:** `20261109` ·
**Trials:** 10,000 per scenario × variant (4 scenarios × 3 variants) ·
**Horizon:** 60 months · **Run:** `python src/monte_carlo.py` from the repo root.

---

## 0. Verdict — followed, not relitigated

**CONDITIONAL GO — ACQUIRE, DO NOT BUILD.** Commit no capital until five
gates clear: (1) Medicaid moratorium resolved in writing; (2) suitable
target at a disciplined price; (3) supervising pharmacist secured in
writing; (4) financing confirmed **without SBA**; (5) healthcare attorney
+ pharmacy CPA engaged pre-LOI. If any gate fails, wait — do not default
to startup. This simulation quantifies the economics *if* the gates clear;
it does not clear any gate.

Two hard facts the simulation carries correctly, because the earlier draft
of this package got one of them wrong:

- **SBA is CLOSED to this owner.** SBA Policy Notice 5000-876441 (eff.
  1 Mar 2026, now SOP 50 10 8.1) bars a lawful permanent resident from
  owning *any* share of a 7(a)/504/Microloan borrower, even 1%.
  Financing in this model is personal capital, conventional bank loans,
  non-SBA CDFI loans, and seller financing only. **No SBA eligibility is
  claimed anywhere in this package.** (A text-level test,
  `test_sba_not_available_note`, trips if a future edit reintroduces the
  old wrong claim.)
- **NY Medicaid moratorium** (CMS-approved 27 Jul 2026, through 27 Jan
  2027, extendable in 6-month periods) covers new enrollments **and**
  changes of ownership. No Medicaid revenue is counted until enrollment is
  active. It is modelled as a delay of 0 / 6 / 12 months before Medicaid
  gross profit starts (see §2).

A green card holder **can** own 100% of a NY retail pharmacy without a
pharmacist licence (Ed. Law §6808); the binding constraint is a full-time
(30+ hrs/wk, one pharmacy only) NY-licensed supervising pharmacist.

---

## 1. Headline results — base variant (10,000 trials each)

All figures are **EBITDA** (excl. debt service, tax, depreciation, owner
draw), exactly as in the report. **Cumulative payback** = first month
cumulative EBITDA reaches the initial capital. The report's headline
payback (~3.8 / ~2.5 / ~3.1 yrs) is a *different* definition — capital ÷
mean Year 2–3 EBITDA — and is reported alongside as "simple payback"
(see §5). The two must not be compared as if they were the same number.

**Read the medians with the probabilities beside them.** Time-to-break-even
and payback medians are *conditional* on the event happening within 60
months. In the base variant most trials break even, so the medians are
representative; in the bear variant they describe a small surviving subset
(e.g. Lean bear payback median 4.67 yrs is computed from **5 of 10,000**
trials — the other 9,995 never pay back).

| Scenario (base) | Capital | TTB median (P5–P95) | Cum. payback median* (P5–P95) | 5-yr ROI median (P5–P95) | P(never break even) | P(payback > 5 yrs) | P(5-yr ROI < 0) |
|---|---|---|---|---|---|---|---|
| A — Lean startup | $435,230 | 10 mo (7–13) | 4.25 yrs (3.17–4.92) | 82.8% (−9.9% to 176.1%) | 1.0% | 61.6% | 7.1% |
| B — Standard startup | $791,010 | 8 mo (6–13) | 3.67 yrs (2.75–4.83) | 149.7% (54.4% to 246.3%) | 0.04% | 19.9% | 0.4% |
| C — Larger + delivery | $1,309,273 | 10 mo (7–13) | 4.00 yrs (3.00–4.92) | 114.5% (29.1% to 202.0%) | 0.1% | 39.5% | 1.2% |
| D — Acquisition (B-sized steady store) | $880,000 | 1 mo (1–13) | 3.50 yrs (2.33–4.83) | 129.6% (24.3% to 240.9%) | 0.8% | 33.2% | 2.1% |

\* Conditional median — see the warning above. Payback achieved in
3,840 / 8,012 / 6,051 / 6,681 of 10,000 trials respectively.

**What the base case actually says:** even in the base variant, a startup
usually does **not** pay back its capital within five years on a cumulative
EBITDA basis (A 61.6%, C 39.5% fail to do so; B 19.9%). The report's
deterministic base case *does* pay back (cumulative payback 4.92 / 3.67 /
4.25 yrs) because it assumes the base margin holds, the ramp completes on
schedule, and no moratorium delay. The Monte Carlo adds exactly the
uncertainty the report warns about — margin reversion, ramp slippage,
moratorium delay, PBM drift — and that uncertainty is mostly downside:
the base-variant ROI medians (82.8% / 149.7% / 114.5%) sit **below** the
report's deterministic ROIs (105% / 172% / 135%), and the acquisition
(129.6% vs 184.7% deterministic) likewise. The acquisition's advantage is
not a higher median ROI than the best startup — it is **time**: it is
EBITDA-positive in month 1 in the median trial, with no 18–24-month ramp
to survive, and it never faces the startup cash trough of months 1–6.

### Bear variant (conservative: $75.00/Rx, 18.2% margin, +5% growth)

| Scenario (bear) | TTB median (P5–P95) | Cum. payback median* | 5-yr ROI median (P5–P95) | P(never break even) | P(payback > 5 yrs) | P(5-yr ROI < 0) |
|---|---|---|---|---|---|---|
| A — Lean | 13 mo (11–25) | 4.67 yrs (n = 5 trials) | −82.4% (−160.5% to +2.5%) | 73.0% | 99.95% | 94.5% |
| B — Standard | 13 mo (10–13) | 4.58 yrs (n = 120) | −21.3% (−100.5% to +65.5%) | 29.5% | 98.8% | 66.2% |
| C — Larger | 13 mo (12–13) | 4.75 yrs (n = 30) | −38.2% (−109.8% to +41.7%) | 42.7% | 99.7% | 79.2% |
| D — Acquisition | 7 mo (1–13) | 4.42 yrs (n = 281) | −12.8% (−100.3% to +83.9%) | 45.6% | 97.2% | 59.0% |

\* Bear payback medians are computed from the tiny number of trials shown;
they are reported for completeness and must not be quoted without the
P(payback > 5 yrs) beside them. The bear case is the report's own warning
in numbers: at the verified 2024 margin (18.2%), Lean **never breaks even**
in 73% of trials, and even the acquisition fails to break even in 45.6%
— because the bear variant combines a low margin with +5% opex, a 12-month
moratorium delay in half of trials, and post-sale volume retention risk.
A bear-case acquisition is not a safe harbour; it is a diligence test.

### Bull variant (optimistic: $85.00/Rx, 23.0% margin, +15% growth)

| Scenario (bull) | TTB median (P5–P95) | Cum. payback median (P5–P95) | 5-yr ROI median (P5–P95) | P(never break even) | P(payback > 5 yrs) |
|---|---|---|---|---|---|
| A — Lean | 7 mo (5–9) | 2.75 yrs (2.17–3.83) | 249.1% (152.1% to 345.4%) | 0% | 0.6% |
| B — Standard | 6 mo (4–7) | 2.33 yrs (1.83–3.00) | 319.8% (220.7% to 418.5%) | 0% | 0.03% |
| C — Larger | 7 mo (5–9) | 2.67 yrs (2.08–3.50) | 267.3% (178.6% to 357.1%) | 0% | 0.1% |
| D — Acquisition | 1 mo (1–1) | 2.33 yrs (1.58–3.58) | 276.8% (156.2% to 400.8%) | 0% | 0.7% |

The bull case is shown because the report defines an optimistic variant;
it is not a forecast. Note the bull ROIs are far above the report's
deterministic base ROIs — that is what a 23.0% margin (just below the
2021 peak of 23.3%) plus 15% growth does. Do not underwrite to it.

---

## 2. Model — deterministic core and distributions

### 2.1 Deterministic core (report ss.5.3–5.6, reproduced exactly)

26 working days/month. Monthly gross profit =
`Rx/day × 26 × revenue/Rx × (margin + front-end% × 45%)`.
Monthly EBITDA = gross profit − opex (85% of steady opex in months 1–3
for startups, full thereafter; opex inflates 3%/yr). Owner draw, debt
service, tax, depreciation excluded, as in the report.

Year-1 ramp (Rx/day, from the model sheets Monthly_A/B/C):

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A — Lean | 15 | 22 | 29 | 37 | 44 | 52 | 58 | 64 | 69 | 73 | 77 | 79 |
| B — Standard | 25 | 38 | 55 | 70 | 85 | 98 | 110 | 120 | 130 | 138 | 145 | 150 |
| C — Larger | 35 | 60 | 85 | 105 | 125 | 140 | 152 | 163 | 173 | 182 | 195 | 220 |

Years 2–3 volume = steady × (1+g), (1+g)²; Years 4–5 +5%/yr (report
s.5.6; growth rates are report **ASSUMPTIONS**). Post-ramp volume is
capped at 135% of steady state (simulation **ASSUMPTION** — the base
path peaks at 1.10² × 1.05² = 1.334, so the cap binds only in the bull tail).

### 2.2 Verification — the engine reproduces the report

| Check | A — Lean | B — Standard | C — Larger |
|---|---|---|---|
| Break-even Rx/day (model / report s.5.5) | 68.3 / 68 | 111.4 / 111 | 171.3 / 171 |
| First EBITDA-positive month (model / report s.5.4) | **9 / 10** † | 8 / 8 | 9 / 9 |
| Year-1 EBITDA (model / report) | −$76,031 / −$76,031 | −$56,315 / −$56,315 | −$160,697 / −$160,701 |
| 5-yr ROI (model / report s.5.6) | 105.1% / ~105% | 171.5% / ~172% | 134.7% / ~135% |
| Simple payback (model / report s.1.4) | 3.84 / ~3.8 yrs | 2.53 / ~2.5 yrs | 3.11 / ~3.1 yrs |
| Cumulative payback, deterministic | 4.92 yrs | 3.67 yrs | 4.25 yrs |

† **A known $334 discrepancy in the report, found by reproducing its
formulas exactly.** The report's own spreadsheet (Monthly_A, base case)
gives month 9: 69 Rx/day × 26 × $79.20 × (20.9% + 2% × 45%) = $30,975
gross profit − $30,641 opex = **+$334** EBITDA, so month 9 — not month 10 —
is the first EBITDA-positive month under the report's own formulas, while
the report text (§§1.4, 5.4) says month 10. Year-1 EBITDA still matches to
the dollar, so this is a one-month labelling discrepancy worth $334, in
the same spirit as the report's own Appendix A corrections (A.5–A.7). The
engine follows the formulas; the test allows ±1 month and documents why.
It does not change any conclusion.

### 2.3 Distributions (all spreads are simulation ASSUMPTIONS — the report gives no spreads)

| Variable | Centre by variant (bear / base / bull) | Spread (SD, truncated) | Basis |
|---|---|---|---|
| Gross margin | 18.2% / 20.9% / 23.0% | 1.5pp, clipped [14%, 26%] | Centres: report s.5.1 (18.2% verified 2024 10-yr low; 20.9% verified 2025; 23.0% assumption just below 2021 peak 23.3%). SD: the 10-yr Digest margin series spans 18.2–23.3%, so 1.5pp keeps ~95% of draws inside the observed decade range. |
| Revenue per Rx | $75.00 / $79.20 / $85.00 | $3.00, clipped [$60, $100] | Centres: report s.5.1 ($79.20 verified NCPA 2026 Digest; $75/$85 assumptions, mix-dependent). |
| Ramp speed (startups) | 0.85 / 1.00 / 1.10 | 0.12, clipped [0.55, 1.45] | Multiplies the Year-1 monthly ramp. Centres are the variant growth paths; SD is an assumption (report: "a 3-month slip extends the cash trough past the working-capital reserve", s.5.5). |
| Steady-state volume | 80 / 150 / 220 Rx/day | 7% of steady, clipped [60%, 140%] | Report s.5.1 steady targets. |
| Monthly opex | $30,641 / $51,050 / $80,083 | 4%, clipped [80%, 125%] of variant multiple | Report s.5.3, verified against the model (opex lines sum exactly). Variant multiples: bear 1.05 / base 1.00 / bull 0.95. |
| Post-Year-1 growth | 5% / 10% / 15% (Yrs 2–3); 5% (Yrs 4–5) | 3pp, clipped [−5%, 30%] | Report s.5.1/s.5.6 assumptions. |
| PBM reimbursement drift | −0.50 / −0.20 / 0.00 pp per year | — (deterministic per variant) | **ASSUMPTION.** Retroactive DIR ended 1 Jan 2024 but PBMs lowered baseline rates (report s.8.3); margin erosion is the #1 sensitivity (s.5.5). The deterministic reproduction carries **no** drift (the report's model has none); drift lives only in the Monte Carlo draws, which is why MC medians sit below the deterministic base ROIs. Stress-tested by the −2.0pp PBM overlay (§6). |
| Moratorium delay | P(0, 6, 12 mo) = bear (10%, 40%, 50%) / base (25%, 50%, 25%) / bull (50%, 40%, 10%) | Discrete | **ASSUMPTION.** Moratorium runs through 27 Jan 2027, extendable in 6-month periods (report s.1.3), so 6 months is the modal base outcome, 12 the extension case, 0 the already-lifted case. During the delay, Medicaid gross profit is zero. |
| Medicaid share of GP | 18% | — | NCPA via report: Medicaid 18% of independent prescriptions (Medicare Part D 34% + Medicaid 18% = over half). During the delay, monthly GP × (1 − 0.18). **Understates** the hit in the top-ranked neighbourhoods, where Medicaid share reaches 46.9% (Brownsville–Ocean Hill, report s.4) — the simulation is conservative on neighbourhood and optimistic on substitution (it assumes no Medicaid script is replaced 1-for-1 by another payer). |
| Acquisition retention | Mean 95% | SD 8%, clipped [60%, 105%] | **ASSUMPTION** (acquisition only). Post-sale volume retention; the "declining volume is the most common value trap" (report s.9). Deterministic overlay tests a 20% drop (§6). |

### 2.4 The $14.57 question — why the simulation does not centre GP/Rx on $14.57

The task brief said to centre gross profit per Rx on the $14.57 national
average. The simulation deliberately does **not** do that, and says why:
$14.57 is the **national-average dispensing GP per Rx** (NCPA 2026 Digest),
corresponding to roughly an 18.4% effective margin at $79.20 — i.e. it sits
at the **conservative** end of the report's model (18.2% margin gives
$14.41 dispensing GP/Rx), not at the base case. Centring on $14.57 would
silently re-base the whole model to the conservative case and break
reconciliation with the report's break-evens (68/111/171) and ROIs
(105/172/135%). Instead the simulation centres on the report's margin
(20.9% base) and lets $14.57 appear where it belongs — in the lower tail:

| Dispensing GP/Rx, base variant (excl. front-end) | Value |
|---|---|
| Median | $16.54 |
| P5 | $14.38 |
| P25 | $15.65 |
| P95 | $18.78 |
| NCPA national-average benchmark | **$14.57** (between P5 and P25) |

Total GP/Rx including front-end at the base case is $17.26 (A) / $17.62 (B)
/ $17.98 (C). The $14.57 vs $15.00 cost-to-dispense loss (−$0.43/Rx) is
carried as a headline fact: **dispensing alone loses money at the national
average**; the business only works on front-end + clinical-service gross
profit and on beating the national-average margin. Any trial whose drawn
margin falls near 18% is living at the national average — and, as the bear
table shows, that is where Lean stops breaking even.

### 2.5 Acquisition scenario — what it is and is not

D buys a **B-sized steady store** (150 Rx/day, B opex $51,050/mo) at the
BizBuySell 2025 median price: total cash needed **$880,000** = $600,000
price + $180,000 inventory at cost (midpoint of the report's $150k–$210k
illustration range) + $100,000 closing costs + working-capital reserve
(report s.6.11 / Financing sheet; all three lines illustrative except the
$600,000 median price itself). No ramp: volume starts at steady state in
month 1. Deterministic base: Year-1 EBITDA $212,110, cumulative payback
3.17 yrs, 5-yr ROI 184.7%, simple payback 2.82 yrs.

Two reconciliations, stated plainly because the medians invite misuse:

- At the 2.79× average multiple, the B-sized store's ~$212k run-rate
  EBITDA implies ~$593k of goodwill — i.e. the $600,000 median price is
  internally consistent **for a B-sized store**.
- The BizBuySell median owner earnings of **$150,000** describe a
  **smaller** national-median store (median revenue $1,334,270 ≈ 54 Rx/day
  at $79.20), **not** this B-sized target. The two medians must not be
  divided into each other (that would give a spurious 4.0× multiple).
  Valuation discipline stays 2.5–3.5× adjusted EBITDA + inventory at cost
  (report s.9.3). The **4–6× EBITDA figure is Canadian and is not used.**

---

## 3. Moratorium — deterministic effect (base variant)

Delay in months before Medicaid gross profit starts. Same delay applies to
startups and to acquisition (change of ownership is caught too).

| Scenario | Delay 0 mo: Y1 EBITDA / 5-yr ROI / cum. payback | Delay 6 mo | Delay 12 mo |
|---|---|---|---|
| A — Lean | −$76,031 / 105.1% / 4.92 yrs | −$92,111 / 101.4% / 5.00 yrs | −$126,048 / 93.6% / **never in 60 mo** |
| B — Standard | −$56,315 / 171.5% / 3.67 yrs | −$86,912 / 167.7% / 3.75 yrs | −$152,311 / 159.4% / 3.92 yrs |
| C — Larger | −$160,697 / 134.7% / 4.25 yrs | −$206,973 / 131.1% / 4.33 yrs | −$298,264 / 124.1% / 4.50 yrs |
| D — Acquisition | +$212,110 / 184.7% / 3.17 yrs | +$137,886 / 176.3% / 3.33 yrs | +$63,662 / 167.8% / 3.58 yrs |

Two readings: (1) a 12-month delay costs roughly $50k (A) to $148k (D) of
Year-1 EBITDA and ~10–17pp of 5-yr ROI — material, but it does not by
itself kill the base case for B, C, or D; (2) for **Lean it is the
difference between paying back and not paying back at all** — Lean's
cumulative payback slips past the 5-year horizon on a 12-month delay
alone. And note the acquisition stays EBITDA-positive in month 1 even
with a 12-month delay (Medicaid-free GP $56,355/mo still exceeds $51,050
opex) — the moratorium wounds an acquisition's first year; it does not
stop it trading. The Monte Carlo folds the delay distribution into every
base-variant number in §1; the deterministic table isolates it.

---

## 4. What the simulation proves — and does not prove

**It proves (within its assumptions):**

- The report's deterministic model is internally consistent and
  reproducible: break-evens, Year-1 EBITDA, and 5-yr ROIs all reproduce
  from the report's own formulas (except the $334 / one-month Lean
  discrepancy above, which the report's own spreadsheet confirms).
- The ranking the report asserts is robust to uncertainty: B (Standard)
  has the best risk-adjusted profile of the startups in every variant
  (lowest P(never break even), lowest P(payback > 5 yrs), highest median
  ROI among startups); Lean is fragile in every variant; Larger needs the
  most volume and the most capital for a worse median ROI than Standard.
- The acquisition's edge is **time and the absence of a ramp**, not a
  higher median ROI: base median ROI 129.6% vs B's 149.7%, but month-1
  EBITDA-positive vs month 8, and no months 1–6 cash trough.
- The bear case is a real possibility, not a tail artefact: at the
  verified 2024 margin, Lean fails in ~3 of 4 trials and even the
  acquisition fails to break even in ~46% of trials. Margin, not footfall,
  is the binding variable (report s.5.5).

**It does not prove:**

- That any specific store, site, or neighbourhood will perform this way.
  No target has been diligenced; no PBM contract rate, wholesaler term,
  lease, or PIC offer exists yet. All volume, margin, and opex inputs are
  scenario assumptions or national averages, not quotes for a real store.
- That the owner can finance the deal. Financing affects this model only
  through the capital figure and the (excluded) debt-service line. The
  illustrative stacks (report s.6.11) are assumptions to be replaced by
  term sheets; **SBA is not available** and no lender has been approached.
- Anything about cash to the owner. These are EBITDA returns, pre-tax,
  pre-debt, before any owner draw. The report's illustrative Year-2 net
  profit for B (~$164,000 after debt service and tax, s.5.6) is an
  illustration, not a forecast, and is not reproduced here.
- That the moratorium will lift on any date. The 0/6/12-month delay
  weights are assumptions; 27 Jan 2027 is not a confirmed reopening date.
- That a 2.5–3.5× multiple will be achievable for a specific Brooklyn
  target. The acquisition scenario prices a B-sized store at the national
  median; a real Brooklyn target with proven volume will typically cost
  more in absolute dollars (report s.9.4).

---

## 5. Two payback definitions — do not mix them

| Definition | Formula | Report base values (A / B / C) | MC base medians (A / B / C / D) |
|---|---|---|---|
| **Simple payback** (report's headline) | Capital ÷ mean(Year 2, Year 3 EBITDA) | 3.8 / 2.5 / 3.1 yrs | 4.08 / 2.65 / 3.29 / 3.61 yrs |
| **Cumulative payback** (this simulation's headline) | First month cumulative EBITDA ≥ capital | 4.92 / 3.67 / 4.25 yrs (deterministic) | 4.25 / 3.67 / 4.00 / 3.50 yrs (conditional medians) |

Cumulative payback is the stricter measure — it charges the Year-1 losses
against the capital before counting any payback. Simple payback ignores
Year 1. Both are reported because the report headlines the simple one;
the MC headline uses the cumulative one because it is the honest answer
to "when do I get my money back?".

Simple-payback medians in the **bear** variant (A 18.81, B 10.46, C 13.83,
D 12.62 yrs) are unstable: when mean Year 2–3 EBITDA is near zero, the
ratio explodes (P95 up to ~280 yrs). They are reported in the JSON for
completeness and should not be quoted.

---

## 6. Surprise overlays (deterministic, base variant — one change at a time)

Full table in `results/monte_carlo_summary.json`
(`overlays_deterministic_base`); definitions and walk-away triggers are in
`SCENARIOS.md`. Headline effects on 5-yr ROI (deterministic base in
brackets):

| Overlay | A — Lean [105.1%] | B — Standard [171.5%] | C — Larger [134.7%] | D — Acquisition [184.7%] |
|---|---|---|---|---|
| Moratorium extended 12 mo | 93.6% (payback: never) | 159.4% | 124.1% | 167.8% |
| PBM rate cut −2.0pp | 54.6% (payback: never) | 119.4% | 88.7% (payback: never) | 134.9% |
| PIC departs (3 mo × +$5,000 locum/premium — ASSUMPTION, no verified locum rate in the report) | 101.7% | 169.7% | 133.5% | 183.0% |
| Rent spike +$10/sq ft/yr | 91.3% (payback: never) | 160.2% | 125.1% | 174.5% |
| Volume −20% post-sale / ramp shortfall | — (B startup: 55.6%, payback: never) | 55.6% | — | 73.8% (payback: never) |

The overlay that kills every route is a **20% volume shortfall** and a
**−2pp PBM cut** — both strike gross profit directly, and neither is
absorbed by opex. The PIC-departure overlay is small in EBITDA terms
($15,000 total) only because it is modelled as a cost adder; its real risk
is operational (a store cannot trade without a PIC — see SCENARIOS.md),
which no EBITDA overlay can capture.

---

## 7. Limitations (honest list)

1. **No target exists yet.** Every acquisition number is built from
   national medians and a B-sized model store, not a real target's
   dispensing-system data. A real target's 3-year script trend, payer mix,
   and inventory count will move every number.
2. **Spreads are assumed, not estimated.** The report gives variant
   centres but no distributions; the SDs in §2.3 are judgement calls with
   stated bases. Different spreads would give different P5–P95 bands.
   The medians are more robust than the tails.
3. **Variables are drawn independently.** In reality margin, volume, and
   opex correlate (a weak store loses volume *and* margin *and* pays more
   for a locum). Independent draws understate joint-downside risk.
4. **Moratorium modelled as a GP haircut only.** It does not model an
   opening delay, a closing delay, PBM recredentialing gaps, or the
   possibility that an entity (stock/membership) purchase escapes the
   moratorium — a structure-specific legal conclusion for counsel only.
5. **Medicaid share fixed at the 18% national figure.** In the top-ranked
   neighbourhoods (Medicaid up to 46.9%) the moratorium hit is up to ~2.6×
   larger than modelled. Site selection changes this number more than any
   other single choice after margin.
6. **No debt service, tax, depreciation, or owner draw.** A leveraged
   buyer with a 60% loan at 9.5%/10 yr pays $3,379 (A) / $6,141 (B) /
   $10,165 (C) per month in debt service (report s.5.4) — that comes out
   of the EBITDA shown here before the owner is paid.
7. **No seasonality, no front-store detail, no clinical-service revenue
   beyond the front-end %** (2%/3%/4% of Rx revenue at 45% margin,
   report s.5.1). Vaccines/MTM upside is not modelled; neither is a
   specialty/compounding downside.
8. **The 23 unverified items, 10 attorney questions, and 12 missing owner
   inputs from the master report are carried forward, not resolved**
   (Appendix A). Any one of them can change a specific target's numbers.

---

## Appendix A. Carried forward — unresolved from the master report

### A.1 The 23 unverified items (report Appendix A.9, verbatim in substance)

NCPDP first-ID fee/time; Medicare/Medicaid and PBM processing times;
NYSED re-inspection and PIC-change fees; NYC DOB/FDNY permit
fees/timelines; NY prescription-record retention period;
employer-registration fees/timing; workers' comp/disability premiums;
whether MATE 8-hour training attestation applies to a pharmacy-entity DEA
registration; exact ownership-change reporting deadline; attorney/CPA/
valuation/stocktaking/recruiting fee schedules (no verified NYC
pharmacy-specific schedule found — "quote required" in report §10);
per-neighbourhood independent-vs-chain pharmacy counts;
per-neighbourhood physician-office counts; PUMA Medicaid/Medicare splits
for 7 of 12 neighbourhoods; neighbourhood-level rent series; current
block-level foot traffic; current NYRx dispensing-fee/ingredient schedule
(obtain the eMedNY schedule before forecasting); 2026 Part B immunisation
admin fee ($34.62 in one secondary source — not verified from CMS); DSCSA
small-dispenser exemption date (27 Nov 2026 vs 27 Nov 2027); pending NY
immunisation-expansion bills (not enacted); February 2026 federal
PBM-reform implementation timeline (not verified); cost-plus PBM offer
terms/availability (not verified). None changes the verdict; any can change
a specific target's numbers.

### A.2 The 12 missing owner inputs (report §5.8 / model Inputs rows 75–86)

1. Available capital (total cash investable). 2. Credit profile (FICO
   band, U.S. credit-history length, bankruptcies/liens/judgments,
   existing debts). 3. Target neighbourhood(s), rent ceiling, lease vs.
   buy premises. 4. Are they a NY-licensed pharmacist — and if yes, will
   they act as pharmacist-in-charge? 5. Pharmacy experience (years,
   PBM/wholesaler relationships, prior ownership). 6. Business structure
   (LLC/corporation/partnership; partners and their citizenship /
   ownership %). 7. Immigration timeline — is naturalisation
   planned/underway, and when? (SBA eligibility could return on
   naturalisation.) 8. Income needs during ramp (monthly draw needed; how
   many months can the owner live without one?). 9. Risk tolerance /
   scenario choice (Lean, Standard, Larger) — and is acquisition on the
   table? 10. Tax position (entity preference, CPA engaged or not,
   personal tax returns available, 2–3 yrs). 11. Delivery / clinical-service
   ambition (delivery radius, vehicle, vaccines/MTM/compounding plans).
   12. Timeline (target opening date — drives the NYSED 10–14-week filing
   critical path). **None of these is assumed in this simulation** — the
   model uses the report's scenario figures where an input is missing, and
   the results must be re-run once the owner supplies them. Input 4
   matters most: if the owner is a licensed NY pharmacist acting as PIC,
   opex falls ~$14k–$16k/mo and break-even falls ~30 Rx/day (report s.5.5).

### A.3 The 10 attorney questions

The master report carries 10 attorney questions (see report §10 and
Appendix A.9); the attorney/CPA questions named in report §8.5 include:
the current text of 8 NYCRR §63.14 / §29.7 and Educ. Law §6841; the notice
period for a change of PIC; immunisation scope and non-patient-specific-order
requirements; any NYC requirement beyond state rules; Anti-Kickback
analysis of every marketing, delivery, discount-card, coupon, and
prescriber-outreach proposal; the 340B question; PBM/PSAO agreement review;
the 3-scenario forecast, inventory-valuation method, U&C price, delivery
and packaging fees, working-capital reserve, payroll budget, and tax /
sales-tax position (CPA); and the moratorium position and entity choice
(LLC vs. business corporation — a professional corporation is not
available to a non-pharmacist owner), which are the attorney's first two
written answers (report §1.5). No attorney has been engaged; nothing here
is legal advice.

---

## Appendix B. Reproducing this run

```bash
cd ~/workspace/brooklyn-pharmacy-enterprise
~/workspace/quant-ipo-engine/.venv/bin/python src/monte_carlo.py
~/workspace/quant-ipo-engine/.venv/bin/python -m pytest tests/test_monte_carlo.py -v
```

Seed `20261109`, numpy `Generator` only, no time-based or global RNG
state. Re-running reproduces `results/monte_carlo_trials.csv` (120,000
rows) and `results/monte_carlo_summary.json` exactly. The JSON uses
`null` where an event was not achieved within 60 months; the CSV writes
`nan` in the same cells (documented in the file header note below).
National context for scale: the average independent filled 67,601 Rx in
2024 (~217/day, NCPA 2025 Digest) — a mature-store benchmark, not a
startup target; the report's steady targets (80/150/220 Rx/day) sit below
it deliberately.

*Research and education, not legal, tax, immigration, or financial advice.
The owner must obtain advice from a licensed NY healthcare/pharmacy
attorney, a pharmacy CPA, and — for immigration questions — an immigration
attorney before acting on it. Nothing was submitted to any agency, no one
was contacted, no money was spent.*
