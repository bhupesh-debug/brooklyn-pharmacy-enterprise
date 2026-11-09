# Scenarios — Brooklyn Independent Pharmacy Enterprise

**Owner:** a U.S. Green Card holder (Lawful Permanent Resident). **Not Bhupesh.**
No owner name, capital, credit score, or preferred neighbourhood is invented
here. **Verdict (master report): CONDITIONAL GO — ACQUIRE, DO NOT BUILD.**
Commit no capital until the five gates clear (moratorium resolved in writing;
suitable target at a disciplined price; supervising pharmacist secured in
writing; financing confirmed **without SBA** — Policy Notice 5000-876441,
eff. 1 Mar 2026, now SOP 50 10 8.1, bars any LPR ownership in an SBA
borrower; healthcare attorney + pharmacy CPA engaged pre-LOI). If any gate
fails, wait.

All numbers trace to the master report
(`Pharmacy_Startup_Advisory_Brooklyn_Master_Report_2026-11-09.md`) or are
labelled **ASSUMPTION**. Monte Carlo results are from `MONTE_CARLO.md`
(seed 20261109, 10,000 trials per scenario × variant); deterministic
figures are the report's own model reproduced by `src/monte_carlo.py`.
All returns are **EBITDA** (excl. debt service, tax, depreciation, owner
draw). "Payback" below means **cumulative** payback (first month cumulative
EBITDA ≥ capital) unless labelled "simple" (capital ÷ mean Year 2–3
EBITDA, the report's headline definition).

Neighbourhood context (report §4, for site selection — not a
site-selection decision): East New York–Starrett City 78.5,
East Flatbush 75.0, Brownsville–Ocean Hill 74.5, Bedford-Stuyvesant 72.5,
Flatbush/Midwood 70.5. Top-ranked neighbourhoods carry the highest
Medicaid shares (Brownsville–Ocean Hill 46.9% Medicaid) — which is why the
moratorium bites hardest exactly where the ranking points.

---

## 1. The four scenarios at a glance (deterministic base case)

| | A — Lean startup | B — Standard startup | C — Larger + delivery | D — Acquisition |
|---|---|---|---|---|
| Footprint / steady volume | ~1,200 sq ft / 80 Rx/day | ~1,800 sq ft / 150 Rx/day | ~2,500 sq ft / 220 Rx/day | B-sized steady store / 150 Rx/day from month 1 |
| Initial capital / cash to close | $435,230 | $791,010 | $1,309,273 | **$880,000** ($600k median price + $180k inventory at cost + $100k closing/WC) |
| Steady monthly opex | $30,641 | $51,050 | $80,083 | $51,050 |
| Break-even (base $79.20/Rx, 20.9%) | 68 Rx/day | 111 Rx/day | 171 Rx/day | 111 Rx/day |
| First EBITDA-positive month | 10 (report text; model formulas give 9 — see MONTE_CARLO.md §2.2) | 8 | 9 | 1 |
| Year-1 EBITDA (base) | −$76,031 | −$56,315 | −$160,701 | +$212,110 |
| 3-yr cumulative EBITDA (base) | +$150,655 | +$567,879 | +$680,571 | n/a (see §4) |
| 5-yr ROI, deterministic base | ~105% | ~172% | ~135% | ~185% |
| 5-yr ROI, Monte Carlo median (base) | 82.8% | 149.7% | 114.5% | 129.6% |
| Cumulative payback, deterministic | 4.92 yrs | 3.67 yrs | 4.25 yrs | 3.17 yrs |
| Cumulative payback, MC median (base) | 4.25 yrs* | 3.67 yrs* | 4.00 yrs* | 3.50 yrs* |
| P(payback > 5 yrs), MC base | 61.6% | 19.9% | 39.5% | 33.2% |
| P(never break even), MC base | 1.0% | 0.04% | 0.1% | 0.8% |

\* Conditional median — only among trials that pay back within 60 months.

---

## 2. Scenario A — Lean startup ($435,230)

**Shape:** ~1,200 sq ft, secondary street, $55/sq ft/yr rent, PIC + 1.25
tech FTE, dispensing + vaccines only, 80 Rx/day steady target. Front-end
2% of Rx revenue. Working capital 4 months of opex ($122,564).

**Base:** first EBITDA-positive month 10 (model: 9, +$334 in month 9 —
the report's $334 discrepancy, MONTE_CARLO.md §2.2); Year-1 EBITDA
−$76,031; 5-yr ROI 105.1% deterministic, **82.8% MC median**
(P5 −9.9%, P95 176.1%); cumulative payback 4.92 yrs deterministic,
4.25 yrs MC conditional median — but **61.6% of base trials never pay
back within 5 years**. P(never break even) 1.0%.

**Bull** ($85.00, 23.0%, +15%): TTB 7 mo; payback 2.75 yrs; ROI 249.1%
(152.1–345.4%); P(payback > 5 yrs) 0.6%.

**Bear** ($75.00, 18.2%, +5%): TTB 13 mo; ROI **−82.4%**
(−160.5% to +2.5%); P(never break even) **73.0%**; P(payback > 5 yrs)
**99.95%** (only 5 of 10,000 trials pay back). This is the report's own
warning in numbers: at the conservative margin its break-even is 73–82
Rx/day — **above its 80 Rx/day steady target**. In the conservative
variant Lean never breaks even, full stop.

**What would move the venture:** Lean only works if margin holds ≥ ~20%
*and* the ramp completes *and* the moratorium delay is short (a 12-month
delay alone pushes deterministic cumulative payback past 5 years: ROI
93.6%, Year-1 EBITDA −$126,048). A −2pp PBM cut alone does the same
(ROI 54.6%, payback never). **Walk away if:** margin prints at or below
18.2% for two consecutive quarters with no PSAO/contract remedy; the
ramp is still below 58 Rx/day at month 7 (the deterministic path); the
moratorium extends a second 6-month period with no written structure
opinion; or the owner needs a living draw during the ramp (draw is
excluded from opex — adding even $5,000/mo lifts break-even by ~11
Rx/day and the model has no headroom for it).

---

## 3. Scenario B — Standard startup ($791,010)

**Shape:** ~1,800 sq ft, neighbourhood corridor, $65/sq ft/yr rent,
PIC + 2.5 tech FTE + 1 clerk, + MTM, blister packaging, contracted local
delivery, 150 Rx/day steady target. Front-end 3%. Working capital 5 months
($255,250). **The reference case — and the only scenario cumulatively
EBITDA-positive after three years in all three report variants**
(conservative +$50,289; base +$567,879; optimistic +$1,150,846).

**Base:** first EBITDA-positive month 8; Year-1 EBITDA −$56,315; 5-yr ROI
171.5% deterministic, **149.7% MC median** (54.4–246.3%); cumulative
payback 3.67 yrs (deterministic and MC median agree); P(payback > 5 yrs)
19.9%; P(never break even) 0.04%. Widest safety margin: base break-even
111 vs target 150 (26% headroom); even at 18.2% margin it breaks even at
127 Rx/day.

**Bull:** TTB 6 mo; payback 2.33 yrs; ROI 319.8% (220.7–418.5%);
P(payback > 5 yrs) 0.03%.

**Bear:** TTB 13 mo; ROI −21.3% (−100.5% to +65.5%); P(never break even)
29.5%; P(payback > 5 yrs) 98.8% (only 120 of 10,000 trials pay back).
Even the best startup fails in the bear case — the difference from A and
C is that B's bear failure is a *payback* failure (it breaks even, then
earns too slowly), not a *never-break-even* failure.

**What would move the venture:** B is the fallback if no acquisition
target exists at a disciplined price — **only** with a specific
underserved location or captive patient flow plus capital for an 18–24
month ramp (report §1.2). A 12-month moratorium delay costs it ~$96k of
Year-1 EBITDA but leaves the base case intact (ROI 159.4%, payback
3.92 yrs). **Walk away if:** the site is a prime corridor (rents
$150–$450/sq ft/yr break every scenario — report s.5.1); the ramp is
below 98 Rx/day at month 6; margin falls to 18.2% with no recovery path
(a −2pp PBM cut drops ROI to 119.4% and payback to 4.58 yrs); or the
working-capital reserve is raided for build-out overruns (the reserve is
what funds months 4–6; without it the pharmacy runs out of cash even
though the model later turns profitable).

---

## 4. Scenario C — Larger + delivery startup ($1,309,273)

**Shape:** ~2,500 sq ft, high-footfall corridor, $70/sq ft/yr rent,
PIC + relief pharmacist + 4 tech FTE + 2 clerks, in-house delivery
driver/vehicle (operating cost, not a purchase — add $25k–$45k if buying
a van, ASSUMPTION), expanded clinical services, larger front end,
220 Rx/day steady target. Front-end 4%. Working capital 6 months
($480,498) — the largest soft line in the package.

**Base:** first EBITDA-positive month 9; Year-1 EBITDA −$160,701 (the
deepest trough); 5-yr ROI 134.7% deterministic, **114.5% MC median**
(29.1–202.0%); cumulative payback 4.25 yrs deterministic, 4.00 yrs MC
conditional median; P(payback > 5 yrs) 39.5%; P(never break even) 0.1%.
Most headroom vs target (171 vs 220) **provided the delivery/facility
volume actually materialises — that volume is the least certain
assumption in the file** (report s.5.5).

**Bull:** TTB 7 mo; payback 2.67 yrs; ROI 267.3% (178.6–357.1%).

**Bear:** TTB 13 mo; ROI −38.2% (−109.8% to +41.7%); P(never break even)
42.7%; P(payback > 5 yrs) 99.7% (30 of 10,000 trials pay back).
Conservative 3-yr cumulative EBITDA is −$80,453 — C does not pay back in
three years if margin reverts to 18.2% and volume grows only 5%.

**What would move the venture:** C only makes sense with a signed
delivery/facility channel (care-home / facility accounts — an assumption
needing owner confirmation) or a demonstrably underserved high-footfall
site. It needs the most capital for a worse median ROI than B, so it must
earn its place on volume certainty, not on ambition. **Walk away if:**
the delivery/facility volume is uncontracted at signing; the ramp is below
140 Rx/day at month 6; a prime-corridor rent is proposed; or capital is
under $1.31M with no committed reserve — C's working capital alone is
$480,498, and cutting it is the single most common way a pharmacy fails
in months 3–9.

---

## 5. Scenario D — Acquisition (B-sized steady store, $880,000 cash to close)

**Shape:** buy an existing, diligenced independent pharmacy in Brooklyn
by asset purchase at a U.S.-multiple price (2.5–3.5× adjusted EBITDA, or
2.5–4.5× seller's discretionary earnings for a small owner-operated store),
**plus inventory at cost**. Modelled as a B-sized steady store (150
Rx/day, $51,050/mo opex) at the BizBuySell 2025 median price: $600,000
price + $180,000 inventory at cost (midpoint of the report's $150k–$210k
illustration range) + $100,000 closing costs + working-capital reserve =
**$880,000** total cash needed. Illustrative financing (report s.6.11,
**ASSUMPTION** — to be replaced by term sheets): personal capital 27.5%,
conventional bank acquisition loan 60%, seller note 12.5%. **No SBA.**
No ramp: volume starts at steady state in month 1; deterministic Year-1
EBITDA +$212,110.

**Base:** EBITDA-positive month 1 (median; P95 month 13 — the tail is
trials where a 12-month moratorium delay plus low retention coincide);
5-yr ROI 184.7% deterministic, **129.6% MC median** (24.3–240.9%);
cumulative payback 3.17 yrs deterministic, 3.50 yrs MC conditional median;
P(payback > 5 yrs) 33.2%; P(never break even) 0.8%; P(5-yr ROI < 0) 2.1%.

**Bull:** TTB 1 mo; payback 2.33 yrs; ROI 276.8% (156.2–400.8%).

**Bear:** TTB 7 mo (1–13); ROI −12.8% (−100.3% to +83.9%); P(never break
even) **45.6%**; P(payback > 5 yrs) 97.2%. The bear acquisition fails
because the bear variant combines an 18.2% margin (break-even 127
Rx/day), +5% opex, a 12-month moratorium delay in half of trials, and
retention risk — at 150 Rx/day with those headwinds there is only ~$3.6k/mo
of headroom, and retention below ~93% erases it. **A bear-case acquisition
is not a safe harbour; it is a diligence test.**

**Why acquire rather than build (the verdict's logic, quantified):**
the acquisition buys proven volume and skips the 18–24-month ramp and the
months 1–6 cash trough (Year-1 EBITDA +$212k vs −$56k for the same-sized
startup). Its median ROI is *lower* than B's (129.6% vs 149.7%) because it
costs $880k against B's $791k for the same run-rate — the premium is the
price of certainty, and it is only worth paying if diligence confirms the
volume. **Valuation discipline:** 2.5–3.5× adjusted EBITDA + inventory at
cost; a price above the U.S. range needs documented justification. **Do
not use the 4–6× EBITDA figure — it is Canadian** (report s.9.3). The
national median owner earnings of $150,000 describe a smaller store
(~54 Rx/day) and are not this target's earnings (see MONTE_CARLO.md §2.5).

**What would move the venture:** D is the recommended route *if* a target
passes diligence (3 years of monthly script counts from the dispensing
system, not a broker summary; trend and the month any decline started;
PBM recredentialing position; Medicaid change-of-ownership position in
writing). A target at the low end of the multiple range, or with a seller
note / earn-out, moves D decisively ahead of B; a target at the top of the
range with declining volume moves it behind B. **Walk away if:** volume
is declining and the decline is unexplained (the most common value trap);
PBM contracts will not recredential or the address carries a negative
history; the Medicaid change-of-ownership position is not confirmed in
writing; the price exceeds 3.5× adjusted EBITDA without documented
justification; inventory cannot be counted from invoices; or the PIC
will not stay / no replacement PIC is secured in writing (a store cannot
trade without one — see overlay 3).

---

## 6. Surprise overlays — one change at a time (deterministic, base variant)

Each overlay changes **one** thing from the base deterministic path, so the
effect is attributable. All figures are in `results/monte_carlo_summary.json`
(`overlays_deterministic_base`). "Payback: never" means cumulative EBITDA
does not reach the capital within 60 months.

### Overlay 1 — Moratorium extended 12 months (Medicaid GP starts month 13)

| | A | B | C | D |
|---|---|---|---|---|
| Year-1 EBITDA | −$126,048 (from −$76,031) | −$152,311 (from −$56,315) | −$298,264 (from −$160,701) | +$63,662 (from +$212,110) |
| 5-yr ROI | 93.6% | 159.4% | 124.1% | 167.8% |
| Cumulative payback | **never** | 3.92 yrs | 4.50 yrs | 3.58 yrs |
| First EBITDA-positive month | 13 | 10 | 12 | 1 |

**Trigger / walk-away:** a second 6-month extension with no written
structure opinion (entity-purchase escape is counsel-only) ends the
startup routes for Lean outright and should pause B/C/D until the
position is confirmed in writing. Gate 1 is the verdict's first gate for
exactly this reason. Note D stays EBITDA-positive in month 1 even here —
the moratorium wounds an acquisition's first year; it does not stop it
trading.

### Overlay 2 — PBM rate cut, margin −2.0pp for the whole horizon

| | A | B | C | D |
|---|---|---|---|---|
| Year-1 EBITDA | −$101,524 | −$104,253 | −$228,033 | +$137,978 |
| 5-yr ROI | 54.6% | 119.4% | 88.7% | 134.9% |
| Cumulative payback | **never** | 4.58 yrs | **never** | 4.08 yrs |

**Trigger / walk-away:** margin is the #1 sensitivity (report s.5.5):
±2.7pp of margin = ±$100k+/yr of gross profit at B's volume; break-even
shifts 12–25 Rx/day. A −2pp cut is *smaller* than the verified 2024
reversion (20.9% → 18.2% = −2.7pp), so this overlay is not a stress test
beyond history — it is history, repeated. Walk away from Lean and Larger
if a cut of this size is in force with no PSAO renegotiation, generic-mix
remedy, or clinical-service revenue to offset it. For any target, the
diligence question is the target's *actual* remittance history, not the
national margin.

### Overlay 3 — Pharmacist-in-charge departs (3 months × +$5,000/mo locum/premium)

| | A | B | C | D |
|---|---|---|---|---|
| 5-yr ROI | 101.7% | 169.7% | 133.5% | 183.0% |
| Cumulative payback | 5.00 yrs | 3.67 yrs | 4.25 yrs | 3.17 yrs |

The +$5,000/mo figure is an **ASSUMPTION — no verified locum rate is in
the report**. The EBITDA effect is small ($15,000 total) and the overlay
understates the risk on purpose: the real PIC risk is **operational, not
financial**. A pharmacy cannot trade without a full-time NY-licensed PIC
(30+ hrs/wk, one pharmacy only); a departure without a replacement is a
closure event, not a $5,000/mo cost. **Trigger / walk-away:** no signed
PIC (or identified, interviewed replacement) = no closing, no lease, no
LOI. Gate 3. If the owner is a NY-licensed pharmacist and acts as PIC,
opex falls ~$14k–$16k/mo and break-even falls ~30 Rx/day (report s.5.5) —
owner input 4 (MONTE_CARLO.md Appendix A.2) is the single most valuable
missing fact in the package.

### Overlay 4 — Rent spike, +$10/sq ft/yr on the scenario footprint

| | A (+$1,000/mo) | B (+$1,500/mo) | C (+$2,083/mo) | D (+$1,500/mo) |
|---|---|---|---|---|
| Year-1 EBITDA | −$88,031 | −$74,315 | −$185,693 | +$194,110 |
| 5-yr ROI | 91.3% | 160.2% | 125.1% | 174.5% |
| Cumulative payback | **never** | 3.83 yrs | 4.42 yrs | 3.33 yrs |

**Trigger / walk-away:** $10/sq ft on 1,800 sq ft = $1,500/mo = ~$18k/yr
(report s.5.5); prime corridors ($150–$450/sq ft/yr) would add
$15k–$60k/mo and break every scenario. Site selection is a financial
decision, not a branding one. Walk away from any site whose rent pushes
B's rent above ~3.1% of steady revenue (the model's level) unless volume
is contracted to match. Re-price from a real listing before signing —
the scenario rents ($55/$65/$70) sit at the low-to-mid end of the verified
Brooklyn range and assume a non-prime neighbourhood corridor.

### Overlay 5 — Acquisition target's volume drops 20% post-sale (retention 0.80)

| | D — Acquisition | (B startup, same −20% volume, for comparison) |
|---|---|---|
| Year-1 EBITDA | +$47,168 (from +$212,110) | −$162,978 (from −$56,315) |
| 5-yr ROI | 73.8% (from 184.7%) | 55.6% (from 171.5%) |
| Cumulative payback | **never** | **never** |
| Simple payback | 7.24 yrs | 6.51 yrs |

**Trigger / walk-away:** this is the overlay that kills every route, and
it is the most common real-world failure (declining volume is the most
common value trap, report s.9). A 20% post-sale volume drop turns the
best acquisition into a non-payback and the best startup into one too.
Diligence must establish the 3-year script trend from the dispensing
system, the month any decline started, and *why* — and the purchase
agreement must price the answer (retention / earn-out / price chip).
**Walk away if:** volume is down >10% year-on-year with no credible,
verifiable cause; the seller will not warrant script counts; or the
transfer campaign (prescriber + patient) has no named owner and no
pre-closing start date.

---

## 7. Moving between scenarios — the decision map

| If… | Then… |
|---|---|
| A diligenced target appears at ≤3.0× adjusted EBITDA + inventory, volume flat or growing, PIC staying | **D (acquire)** — the verdict's route; re-run the MC with the target's actuals before LOI |
| No target after a genuine search, but a specific underserved location or captive flow exists, capital ≥ $791k, PIC secured | **B (Standard startup)** — the only startup cumulatively positive in all three report variants |
| Capital is <$500k and the owner needs a living draw during the ramp | **Wait.** Lean cannot fund a draw and cannot survive a 12-month moratorium delay; do not shrink the working-capital reserve to fit the capital available |
| Only a larger/delivery opportunity exists, with contracted facility volume | **C** — only with the volume contracted, not assumed |
| Margin reverts to 18.2% with no remedy, or volume is down >10% YoY | **Wait / walk away** from every route — the bear case is not a scenario to underwrite, it is the signal to stop |
| Moratorium extends, or the structure opinion is adverse | **Wait** — Gate 1; do not sign an LOI or pay a deposit |
| Owner is a NY-licensed pharmacist willing to act as PIC | **Re-run everything** — opex −$14k–$16k/mo, break-even −~30 Rx/day; Lean may become viable and B improves materially |

---

## 8. What is NOT in these scenarios

Specialty/compounding build-out (sterile compounding can add $100k+);
delivery vehicle purchase (add $25k–$45k if buying, ASSUMPTION); owner
living expenses during the ramp; loan fees/interest during construction;
340B revenue (not assessed — separate feasibility and legal review
required, report s.8.2); any grant (no grant funds a new Brooklyn
pharmacy — the NYC Future Fund and ESD Main Street Capital Loan Fund are
**loans**, and START-UP NY is closed to new applicants since 1 Jan 2026).
The 23 unverified items, 10 attorney questions, and 12 missing owner
inputs are carried forward in MONTE_CARLO.md Appendix A — none is resolved
here, and any of them can change a specific target's numbers.

*Research and education, not legal, tax, immigration, or financial advice.
Nothing was submitted to any agency, no one was contacted, no money was spent.*
