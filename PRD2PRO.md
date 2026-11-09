# PRD2Pro — Professional Implementation Plan
## Brooklyn Independent Pharmacy Enterprise (Acquisition Route)

| Field | Value |
|---|---|
| Document ID | PRD2PRO-20261109-BPX1 |
| Version | 1.0 — DRAFT |
| Date | 9 November 2026 |
| Classification | CONFIDENTIAL — PROPRIETARY |
| Implements | PRD-20261109-BPX1 (`PRD.md`, v1.0, 9 Nov 2026) |
| Source of truth | `Pharmacy_Startup_Advisory_Brooklyn_Master_Report_2026-11-09.md` (105 pp, research date 9 Nov 2026) + companion financial model `Pharmacy_Startup_Financial_Model_Brooklyn_2026-11-09.xlsx` |
| Prepared for | The prospective owner — a U.S. Green Card holder (Lawful Permanent Resident). **The owner is not Bhupesh.** Bhupesh Chandra Dimri asked for this research on the owner's behalf. |
| Status | Planning only. Nothing has been submitted to any agency, no one has been contacted, no money has been spent. |

> **This document is general research, not legal, tax, immigration, or financial advice.** It does not replace a New York pharmacy attorney, a pharmacy-savvy CPA, or an immigration attorney. Where the PRD or master report says "attorney's opinion required," that is a hard instruction, not a formality.
>
> **Grounding rule:** every number in this document traces to the PRD, the master report, or a cited primary source. Figures marked **VERIFIED** trace to a cited source. Figures marked **ASSUMPTION** are judgements with their basis stated and must be replaced by a written quote or contract rate before any money is committed. Figures marked **UNVERIFIED** could not be confirmed from a primary source — confirm with the agency or vendor before budgeting. **No owner facts are invented:** the owner's name, available capital, credit score, and preferred neighbourhood were not supplied and are not assumed anywhere. Every place the plan needs one of those inputs is flagged as an **owner input** (Appendix B of the PRD; carried forward in §10 of this document).
>
> **Adaptation note on the controlling skill:** the prd2pro skill's Mode 2 (PRD → Prototype) is written for software products. This product is a regulated physical enterprise — a pharmacy acquisition — so the skill's prototype sections are adapted, not applied literally: there is no clickable software prototype to build. The "prototype" here is the *diligence-and-closing system itself* (target screen, demo-script PMS selection, SOPs, compliance calendar, management pack), specified screen-by-screen and control-by-control in §§3–5 below. The skill's quality bar is kept: every section is product-specific, every table is populated, every risk has a concrete mitigation and owner, every metric has a number or formula.

---

## 0. The verdict — the constraint this plan implements, not relitigates

**CONDITIONAL GO — ACQUIRE, DO NOT BUILD; commit no capital until five gates clear.**

| Gate | Requirement | Evidence required | Owner |
|---|---|---|---|
| **G1 — Medicaid moratorium resolved** | Moratorium confirmed lifted, or intended structure confirmed **in writing by a healthcare attorney** as outside it | Written attorney opinion letter (not verbal); re-confirmed at the Day-60 hard pause | Attorney |
| **G2 — Suitable target at a disciplined price** | Stable/growing script count over 3 years; gross profit per script by payer verified and positive on material contracts; no open or recently settled PBM audit with material recoupment; no single-prescriber or single-facility concentration; lease ≥5 years remaining or renewal options the buyer controls (ASSUMPTION — no published minimum found); PIC and key staff willing to stay; inventory verified by count; seller willing to stay for a transition period | Diligence report (PRD §9.4 checklist A–I); valuation memo at U.S. multiples | CPA + attorney |
| **G3 — Supervising pharmacist secured in writing** | NY-licensed, full-time (30+ hrs/week), supervising only this one pharmacy, named on the registration | Written confirmation from the pharmacist; NYSED licence verification | Owner + PIC |
| **G4 — Financing confirmed without SBA** | Conventional bank loan and/or CDFI stack + personal capital, with equity injection and a working-capital line sized to several weeks of post-closing reimbursement delay. **No SBA 7(a), 504, or Microloan is available to this owner** | Written lender commitment letter | CPA + owner |
| **G5 — Attorney + pharmacy CPA engaged pre-LOI** | Healthcare attorney and pharmacy-savvy CPA engaged before the letter of intent, not after | Engagement letters | Owner |

**If any gate fails, wait — do not default to a startup.** If no full-time supervising pharmacist can be secured at all, **do neither**. (PRD §4.2–4.3.)

### 0.1 Hard facts this plan carries correctly

- **SBA is CLOSED to this owner.** SBA Policy Notice 5000-876441 (eff. 1 Mar 2026, now SOP 50 10 8.1, eff. 1 Oct 2026) — a green card holder may not own any share of a 7(a)/504/Microloan borrower, even 1%. Financing = personal capital, conventional bank loans, non-SBA CDFI loans, seller financing, equipment/inventory financing. **This plan never presents the owner as SBA-eligible.** The SOP is re-checked at the point of application (PRD FR-C4); naturalisation is the only route back, and financing must not be planned around a future naturalisation date. A nominal U.S.-citizen co-owner to restore SBA eligibility is a serious compliance problem and is **not** attempted (PRD §20).
- **NY Medicaid enrollment moratorium gates both routes.** CMS-approved 27 Jul 2026, announced 4 Aug 2026, through 27 Jan 2027, extendable in 6-month periods; it covers new enrollments, reinstatements, **and changes of ownership** for pharmacies. Pending applications are discontinued and do not automatically resume. **Do not count Medicaid revenue until enrollment is active.** The plan preserves the PRD's **Day-60 hard pause** and restarts the 180-day clock from Stage 3 if the moratorium is still in force (PRD §14).
- **A green card holder CAN own 100% of a NY retail pharmacy without a pharmacist licence** (Ed. Law §6808). The binding constraint is a full-time (30+ hrs/week, one pharmacy only) NY-licensed supervising pharmacist (PIC). Owner + PIC are jointly responsible (Ed. Law §6808(2)(c), (e)).
- **Fees (VERIFIED, as of 9 Nov 2026 — re-confirm before filing/paying):** NYSED PH200/PH210/PH208, **$345**, file 10–14 weeks ahead (12–16 weeks if sterile compounding); NYSED triennial renewal **$260**, relocation endorsement $50; DEA Form 224 **$888 / 3 years**; Medicare CMS-855B **$750 (2026)**; Medicaid **$750 listed, WAIVED if already paid to Medicare — budget $750 total, not $1,500**; entity formation LLC **$200** / corporation **$125**, EIN free; RPhT initial licensure + first registration **$175** ($75 licence + $100 registration), triennial **$100**.
- **Startup-model reference economics (Scenario B is the reference case; an acquisition must be modelled from the target's actuals — never apply startup projections to a target):**

| | A — Lean | B — Standard | C — Larger + delivery |
|---|---|---|---|
| Footprint / steady volume | ~1,200 sq ft / 80 Rx/day | ~1,800 sq ft / 150 Rx/day | ~2,500 sq ft / 220 Rx/day |
| **Total initial capital** | **$435,230** | **$791,010** | **$1,309,273** |
| Monthly opex at steady state (excl. COGS, debt, owner draw) | $30,641 | $51,050 | $80,083 |
| Working capital (largest soft line — do not cut it) | $122,564 (4 mo opex) | $255,250 (5 mo) | $480,498 (6 mo) |
| Break-even volume, base ($79.20/Rx, 20.9% margin) | 68 Rx/day | 111 Rx/day | 171 Rx/day |
| First EBITDA-positive month, Year 1 | Month 10 | Month 8 | Month 9 |
| Year 1 EBITDA (base) | −$76,031 | −$56,315 | −$160,701 |
| 3-yr cumulative EBITDA (base / conservative) | +$150,655 / −$122,534 | +$567,879 / +$50,289 | +$680,571 / −$80,453 |
| 5-yr ROI, simple (base, EBITDA ÷ capital, pre-tax, pre-debt) | ~105% | ~172% | **~135%** |
| Simple payback (Year 2–3 avg EBITDA) | ~3.8 yrs | ~2.5 yrs | ~3.1 yrs |

  > **Correction carried forward:** the spreadsheet's check-line still prints Scenario C 5-yr ROI as ~150%; the report corrected this to **~135%** (the ~150% figure implied +10%/yr Years 4–5 growth, contradicting the inputs table's +5%/yr; the spreadsheet computes 134.6%). **Use ~135%.** These are EBITDA returns, not cash returns — debt service, owner draw, and tax are not in them. Only Standard (B) is cumulatively EBITDA-positive after 3 years in all three variants. Year 1 is EBITDA-negative in 8 of 9 model variants (only B-optimistic is positive).
- **Dispensing alone loses money at the national average:** **$14.57** gross profit per Rx vs. **$15.00** cost to dispense = **−$0.43/Rx** (NCPA 2025 Digest, 2024 data, VERIFIED); gross margin 20.9% base (2025, VERIFIED) / 18.2% conservative (2024, 10-year low, VERIFIED); average revenue per Rx $79.20 base (VERIFIED). Retroactive DIR ended 1 Jan 2024, but PBMs lowered baseline rates. The product must earn from services, front store, and disciplined inventory — not from volume on below-cost contracts.
- **Top neighbourhoods (none above 80; gaps G1–G12 apply):** East New York–Starrett City **78.5**, East Flatbush **75.0**, Brownsville–Ocean Hill **74.5**, Bedford-Stuyvesant **72.5**, Flatbush/Midwood **70.5**. Shortlist of three, not a single winner — gaps between ranks 1–3 are within the proxy-cap margin.
- **Acquisition valuation anchors (U.S. only):** 2.5–3.5× adjusted EBITDA (Cencora) or 2.5–4.5× Seller's Discretionary Earnings for small owner-operated stores (BridgePoint, 2026), **plus inventory at cost**; BizBuySell 2021–2025 average earnings multiple **2.79×**, 2025 median sale price **$600,000** (median revenue $1,334,270; median owner earnings $150,000). **Do NOT use the 4–6× EBITDA figure — it is Canadian** (PharmacyBroker.ca); using it would overpay by roughly 1–2 turns of EBITDA. Illustrative acquisition cash to close and trade for a median-sized store: roughly **$650,000–$1.1M** (ASSUMPTION range from the report, built from BizBuySell medians — the exact figure for any real target comes only from that target's normalised earnings, counted inventory, and receivables cycle).
- **North-star metric:** gross profit per prescription **by payer**, trailing 30 days (PRD §9.1). If positive on the material contracts and stable, the store can survive; if negative, volume growth makes losses worse.

### 0.2 Provisional figures — flagged, not report figures

- **Defensibility score 5/10** (PRD §3.7, §17.3) and the **RICE scores** in PRD §18.3 are the PRD agent's judgements — provisional, not master-report figures. This plan uses them only as prioritisation guides and re-tests them at each gate.
- **Dollar TAM/SAM/SOM and CAC/LTV are NOT verified** and are not invented here. The addressable market is defined operationally as one acquired store's verified script file in a top-3 shortlist neighbourhood, at 80–220 Rx/day. A dollar TAM/SAM/SOM and a CAC/LTV must be built by the CPA from the target's actuals (PRD §3.1, §12.2). No paid-advertising plan is specified — no verified CAC exists and no discount/inducement marketing may run without counsel's clearance.
- **Assumptions labelled ASSUMPTION in the PRD** (e.g. lease ≥5 years, short-dated flag at 90 days, dead stock = no dispense in 90 days, $10 daily-close threshold, legal-fees planning envelope $12,000–$25,000, CDFI rates commonly 8–18%, delivery-vehicle purchase $25K–$45K) are carried forward as assumptions with the same basis and must be replaced by a written quote, contract rate, or the PIC/CPA's written decision before money is committed.

---

## 1. Implementation summary — what "done" looks like

The deliverable of this plan is **one acquired Brooklyn independent pharmacy, closed cleanly and trading**: gates G1–G5 cleared in writing, diligence complete, licences transferred, PBMs answering in writing, PIC in post, cash controls live, and the first 30 days of trading measured against the diligence baseline. Everything else — immunisation clinics, adherence packaging, delivery expansion, LTC — is V1/V2 (PRD §19.4). **Cut nothing from diligence, escrow, or the working-capital reserve to make the deal look cheaper.**

| Implementation phase | Days | PRD milestone | Exit state |
|---|---|---|---|
| **P0 — Inputs & team** | 1–14 | M0–M1 | 12 inputs in writing; attorney + CPA engaged; written moratorium opinion; entity decision |
| **P1 — Finance pre-work, PIC search, screen** | 15–30 | M2 | Entity formed + EIN; lender round in progress; PIC candidate(s) identified; target screen signed off |
| **P2 — Search & HARD PAUSE** | 31–60 | M3 | Longlist 5–10 → shortlist 2–3; updated moratorium opinion; **no LOI unless G1 clears** |
| **P3 — LOI & exclusivity** | 61–75 | M4 | Non-binding LOI signed; exclusivity running; PIC confirmed in writing for this target |
| **P4 — Diligence, valuation, financing, filings** | 76–120 | M5 | Diligence A–I complete; valuation memo; lender commitment; PH200 filed in-window; PBM recredentialing started |
| **P5 — Purchase agreement & closing conditions** | 121–150 | M6 | Agreement signed; landlord consent in writing; escrow funded; all five gates re-verified |
| **P6 — Closing & first 30 days** | 151–180 | M7 | Bill of sale; joint inventory count; post-closing notices filed; week-1/week-4 trading reports vs. baseline |
| **P7 — First 90 days of ownership (post-roadmap stabilisation)** | 181–270 | PRD §6.5, §13.1, §19.7 H1 | File stabilised; immunisations + med sync live; monthly management pack discipline established |

**Day 1** is the day the owner decides to proceed and supplies the 12 inputs (PRD Appendix B). **Two sequencing facts fix the calendar:** (1) PH200 must be filed 10–14 weeks before the transfer — for a closing on ~Day 175, file by ~Day 80–105, during diligence; the bill of sale must be signed before the registration can issue. If diligence runs long, the closing date moves, never the filing rule. (2) PBM recredentialing takes weeks to months with no published guaranteed turnaround — it must start in Phase P4, not at closing.

**Sprint plan (first 4 sprints, 2 weeks each, Phases P0–P1):** Sprint 1 — inputs + attorney/CPA selection; Sprint 2 — moratorium opinion + entity decision + personal lender-ready file; Sprint 3 — entity formation + SBS/Funds Finder + CDFI/bank approaches; Sprint 4 — PIC recruitment + target screen + NCPA/CPANY/PSAO contact. (PRD §14.)

---

## 2. Build-vs-buy decisions (per PRD domain / epic)

Rule applied throughout (PRD §8.2): **buy the PMS, POS, and switch; build nothing a vendor already provides. Build only the SOPs, the compliance calendar, and the management-pack reporting — those are the product's own IP.** "Hire" means a professional service engaged under a written engagement letter; "Buy" means a licensed/off-the-shelf product under a written contract with data-ownership, export, and exit terms in writing.

### 2.1 Decision matrix

| # | Capability (PRD ref) | Decision | What is bought / hired / built | Why this way | Acceptance evidence |
|---|---|---|---|---|---|
| 1 | Pharmacy management system (FR-D7, §8.1) | **BUY** | Licensed PMS from shortlist: PioneerRx, PrimeRx, Liberty (+ WinRx if preferred). Written 3-year quotes from ≥3 vendors on the same demo script. **Do not buy QS/1 NRx — it sunsets 31 Dec 2027.** Price is "Quote required" for every system (no vendor publishes a list price — UNVERIFIED until quoted). | The PMS is the audit trail, inventory record, and revenue record; building one is a regulated-software project with no upside for a single store. | 3 written quotes covering the 11-item selection checklist (Surescripts; DSCSA solution; PMP/I-STOP; immunisation/CIR reporting; med sync; POS; Part B roster billing; reporting incl. GP/Rx and PBM reconciliation; data ownership/export/exit in writing; support; NYC references; total 3-year cost itemised). Demo script passed: a day's prescriptions incl. a controlled substance, a rejection/PA, a med-sync patient, an immunisation. |
| 2 | E-prescribing / Surescripts (FR-D1, §8.1) | **BUY (via PMS)** | Surescripts integration through the chosen PMS, live on day one. | Only the certified network route is accepted by prescribers; pharmacist/intern reviews and initials e-prescriptions before acceptance. | Surescripts live and tested before opening; eRx intake SOP signed by PIC. |
| 3 | PBM adjudication / switch (§8.1) | **BUY** | Adjudication via the standard switch; per-claim/transaction charges confirmed in the PMS quote. | Adjudication is not payment — remittance reconciliation is a separate function (built, see #14). | Switch charges itemised in the quote; first live adjudications reconciled in week 1. |
| 4 | Point of sale (§8.1, FR-D5) | **BUY** | POS integrated with the PMS or bought separately (confirm in the quote); card-processor arrangement confirmed. | Copay collection and the daily close depend on POS↔PMS reconciliation. | POS↔PMS reconciliation demonstrated in the demo script; daily close signed by two people from day one. |
| 5 | DSCSA compliance (FR-D8, §8.1) | **BUY (via PMS/wholesaler)** | Electronic TI/TS receipt, 6-year retention, suspect-product verification (VRS), saleable-return verification (typically via GS1 EPCIS) — supplied by the PMS vendor / wholesaler. | DSCSA-ready on opening day regardless of any small-dispenser exemption (exemption date UNVERIFIED: 27 Nov 2026 vs. 27 Nov 2027). | Solution live on opening day; PIC's check of the current FDA DSCSA exemptions page and the wholesaler/PMS vendor's readiness on file. |
| 6 | PMP / I-STOP reporting (§8.1, FR-D4) | **BUY (via PMS) + state system** | Health Commerce System (HCS) + 24-hour dispensing reporting; software configured and tested before opening. | Late transmissions (>24 hrs) are a compliance failure. | HCS configured and test transmission completed before opening. |
| 7 | Immunisation registry reporting (FR-E2, §8.1) | **BUY (via PMS)** | NYSIIS/CIR reporting support through the PMS (Brooklyn is in NYC → CIR; under-19s mandatory, 19+ on consent). | Registry reporting is a vendor function; the clinical act and documentation are the PIC's. | CIR reporting demonstrated in the demo script; first clinic's registry reports filed. |
| 8 | Patient communications — IVR/refill, app, SMS (§8.1, §10) | **BUY (via PMS, add-on if needed)** | IVR/refill and patient app/texting — confirm included vs. add-on in the quote; Rx 2 Go patient app is a WinRx feature. | Refill and med-sync workflows depend on it; building a patient app for one store is unjustifiable. | Included/add-on status confirmed in writing; refill-reminder and will-call follow-up automation live in P7. |
| 9 | Wholesaler supply (FR-D3, §13.3) | **BUY (contract)** | Primary wholesaler + secondary wholesaler kept active with small regular orders. Competing proposals from Cardinal Health, McKesson, Cencora/AmerisourceBergen. Buy only from authorised trading partners with full DSCSA transaction data; never grey-market/internet/"too cheap" sources. | Supply continuity and DSCSA legitimacy; the secondary wholesaler is the PMS-outage/wholesaler-failure control. | Written wholesaler agreements; DSCSA transaction information/statements retained (6-year retention); secondary wholesaler receiving regular small orders. |
| 10 | PBM network contracting + audit support (FR-B5, FR-E1, §13.3) | **HIRE (PSAO)** | PSAO membership for collective bargaining and audit support. | A single store has no leverage on rates alone; the PSAO is the only leverage on PBM terms. | PSAO engaged before PBM recredentialing; written confirmation from each material PBM/PSAO on continuation vs. recredentialing vs. new application, with expected timeline, before closing. |
| 11 | Healthcare/pharmacy attorney (G1, G5, PRD App. C) | **HIRE** | NY healthcare/pharmacy attorney, engaged before any LOI, lease, or lender step. First two written answers: moratorium position and entity choice (LLC vs. business corporation; P.C./PLLC not available to a non-pharmacist owner). | Every gate that can kill the deal is a legal question; a verbal assurance is not evidence. | Engagement letter; written moratorium opinion letter; entity-decision memo; answers to all 10 attorney questions (App. C) + acquisition-specific questions on file before closing. |
| 12 | Pharmacy-savvy CPA + valuation (G2, G4, FR-B3/B4, FR-C6) | **HIRE** | Pharmacy-savvy CPA, engaged pre-LOI. Owns normalisation, valuation memo, financing stack, monthly management pack, and the target's GP/script-by-payer model. | Earnings a new owner can actually keep can only be established by line-by-line normalisation of the target's system data. | Engagement letter; valuation memo at U.S. multiples; monthly management pack (inventory report, GP/script by payer, remittance reconciliation). |
| 13 | Lenders — conventional bank + CDFI (FR-C1/C2, G4) | **HIRE/BUY (debt)** | Parallel approaches: free SBS / NYC Funds Finder session (hotline 888-SBS-4NYC / 888-727-4692); Accompany Capital own-funds products (microloan $1,000–$50,000 at 8% fixed; small-business loan $50,000–$75,000); Pursuit SmartLoan to $100,000 at 11.9% fixed, 6-year; two conventional banks; ESD Main Street Capital Loan Fund via Pursuit (up to $100,000 at 9.90% fixed, up to 6 years, interest-only first year, startups <4 yrs). **No SBA programme in the stack.** | CDFI loans top out well below the capital need ($5K–$250K typical; rates commonly 8–18% — ASSUMPTION) — a CDFI tranche funds part of a stack, never the whole build. Illustrative stack (PRD §16.4): personal capital 25–30% + conventional bank acquisition loan 55–65% + seller note 10–15%. **Seller financing is the single most valuable acquisition tool for this owner** — a private contract with no SBA rule. | Each lender's response (term sheet or written declination) on file; written lender commitment letter before the purchase agreement. **Never describe any loan as a grant** (FR-C5): no standing grant funds a new Brooklyn pharmacy; NYC Future Fund is a revenue-based loan requiring ≥12 months in business; START-UP NY closed 1 Jan 2026. |
| 14 | Management-pack reporting + remittance reconciliation (FR-C6, FR-E8, §9.1) | **BUILD** | Monthly pack built by the CPA from PMS exports: inventory value/turns/days' supply/dead stock/shrinkage; GP/script by payer; PBM remittance reconciliation claim-by-claim (835 matched to the dispensing system). North-star metric: GP/script by payer, trailing 30 days. | This is the product's own IP and the survival dashboard; no vendor sells the owner's judgement about which contracts to keep. | Month-end pack produced on schedule; 100% of claims matched weekly; every short-pay investigated the same week. |
| 15 | Prescription-journey SOPs (FR-D1) | **BUILD** | 8-step SOP set written by the PIC with the owner: intake (pharmacist-only for oral orders; pharmacist/intern reviews and initials e-prescriptions) → data entry + DUR (pharmacist verifies all information before dispensing) → controlled substances (PMP/I-STOP check documented) → adjudication → filling (pharmacist-only final verification) → counselling (offer on every new prescription, documented) → will-call/pickup/delivery → post-dispensing records and error log. | The SOPs are the audit trail and the PIC-succession asset; they cannot be bought off the shelf for this store's workflow. | Every sampled prescription traces end-to-end with who did what and when; pharmacist verification recorded; counselling offer/refusal documented. |
| 16 | Compliance calendar (FR-A12, §11.2) | **BUILD** | Calendar built by the PIC + owner covering: NYSED triennial renewal ($260; relocation endorsement $50), pharmacist/RPhT triennial renewals, DEA renewal, NPI/NCPDP maintenance, NYRx/eMedNY maintenance, PBM re-credentialing, DSCSA checks, PMP enrolment, immunisation-certification renewal, insurance renewals. | No renewal or re-credentialing may lapse unnoticed; the calendar is the control that prevents it. | Calendar live by closing; any item within 60 days of expiry has a named owner and a renewal in progress. |
| 17 | Inventory, cash, and segregation-of-duties controls (FR-D2, D5, D6) | **BUILD (process, on bought PMS/POS)** | Perpetual inventory in the PMS; cycle-count high-value/high-theft weekly; full count monthly in early phases (PIC + bookkeeper together); FEFO rotation; short-dated flag (expiring within 90 days — ASSUMPTION, set with the PIC); dead stock = no dispense in 90 days (ASSUMPTION) reviewed by the PIC. Daily close by one person, **checked by a second**, both sign; over/short above a small threshold (e.g. $10 — ASSUMPTION, set with the CPA) investigated same day. Segregation of duties per FR-D6 role matrix. | Controls are process, not product; the PMS records them but cannot enforce the human separation. | Monthly inventory report signed by the PIC (value, turns, dead stock, shrinkage, top-10 variances); daily close signed by two people; role-matrix audit shows no single person holding both halves of any listed duty pair. |
| 18 | Controlled-substance controls (FR-D4) | **BUILD (process, on bought PMS)** | Ordered only by the PIC or a pharmacist holding the PIC's DEA power of attorney (CSOS); receipt reconciled same day; perpetual inventory reconciled daily; any variance investigated same week; confirmed loss reported as counsel advises (Form 106). | A DEA audit finds either zero unexplained variance or a licensing/criminal problem — there is no middle state. | Daily perpetual reconciles to receipts and dispenses with zero unexplained variance. |
| 19 | Audit-response procedure (FR-E8) | **BUILD** | Written procedure before the first audit letter: PIC + owner notified same day; attorney and PSAO notified same day; no records altered, back-dated, or created after the fact; records produced within the deadline with cover letter and index; every recoupment appealed in writing within the deadline; outcome logged and SOP changed. | Most PBM chargebacks are documentation failures, not fraud; the procedure converts a complete record into retained revenue. | Procedure written and rehearsed before opening; first audit (when it comes) answered on time from complete records. |
| 20 | Immunisation programme (FR-E2) | **BUILD (service, on bought PMS/registry)** | SED-certified immuniser(s) on duty for every session (certification + approved course within past 3 years + current CPR/BLS); private area; standing (non-patient-specific) order from a NY-licensed physician/NP; screening, consent, 15-minute observation, anaphylaxis readiness (epinephrine on hand); CIR reporting; bill the correct benefit per patient per vaccine (Part B roster billing for flu/pneumococcal/COVID-19/hepatitis B; Part D for shingles/RSV/Tdap). **Do not use the 2026 Part B administration fee of $34.62 in one secondary source for forecasting until verified from a CMS fee schedule (UNVERIFIED).** | Immunisations are the priority service revenue line — the one that can exceed cost *if* billed correctly. | Session audit shows order, consent, screening, administration, observation, registry report, and billing benefit all documented. |
| 21 | Medication synchronisation + adherence (FR-E3) | **BUILD (service)** | Align chronic prescriptions to a single monthly pickup/delivery date from month 1; no direct per-patient fee forecast unless contracted in writing. | Adherence improves star-ratings measures and retains patients; it is retention infrastructure, not a fee line. | Share of chronic patients synchronised and will-call backlog tracked monthly. |
| 22 | Delivery (FR-E6) | **BUILD (service; vehicle BUY if needed)** | Charge a fee or offer free delivery above a threshold (owner's decision, with the CPA); track delivery cost per delivery and prescriptions retained because of delivery; if delivery costs more than the margin on the prescriptions it retains, budget it as a marketing cost. Delivery-vehicle purchase $25K–$45K is an ASSUMPTION if a vehicle is bought. | Delivery is retention, not acquisition; its economics must be measured, not assumed. | Monthly delivery data reported: cost per delivery and retained prescriptions. |
| 23 | Staffing — PIC, relief pool, RPhTs, front-store, driver, bookkeeper (FR-F1–F6) | **HIRE** | Staff to the PIC's safe capacity, not to the budget; second pharmacist only when queue/phone/counselling load demonstrably exceeds one pharmacist's safe capacity. Relief-pharmacist pool from day one; PIC succession documented (SOPs written so a successor can step in); never open without a pharmacist. RPhTs: NY-licensed (PTCB CPhT or NHA ExCPT accepted); ≤2 RPhTs per pharmacist on duty, total ≤4 individuals at one time (confirm current 8 NYCRR §63.14 / §29.7 text in writing); RPhTs must NOT interpret a prescription, evaluate it, receive oral prescriptions, or counsel; final verification is a pharmacist function. Role prohibitions written into every job description (owner if not a pharmacist must not counsel, verify, receive oral prescriptions, or supervise practice; bookkeeper must not dispense or handle controlled-substance ordering/receipt alone; driver must not counsel or take new prescription orders by phone). Mandatory training on hire and annually, with signed attendance records (HIPAA, fraud/waste/abuse, controlled substances, DSCSA, immunisation, own SOPs). PIC salary benchmark: $140,910 (BLS May 2025 median, VERIFIED); pharmacy technician $45,750. | The PIC is the licence to trade; the relief pool is the difference between a rota problem and a closure. | Every shift roster passes the RPhT ratio check; every employee file holds signed training records for hire and the current year; relief pool covers every open hour when the PIC is unavailable. |
| 24 | Insurance (PRD §11.2) | **BUY (broker)** | Professional liability, general liability, property, business interruption, cyber/privacy, workers' compensation, commercial/non-owned auto if delivering — coverages and limits confirmed with a broker; **no premium is stated here (UNVERIFIED — broker quote required)**. Workers' comp, disability, and Paid Family Leave insurance before first hire. | Coverages and limits are broker-priced for this store; no premium figure exists to budget from. | Binders in hand before closing (P4); renewals on the compliance calendar. |
| 25 | Trade associations (PRD §13.3) | **BUY (membership)** | NCPA and CPANY (Community Pharmacy Association of New York State) membership for market intelligence, reform engagement, and contract support. | The only collective intelligence channel a single store has on PBM reform and contracting. | Memberships active by P1; PSAO/wholesaler conversations started before a target is found. |
| 26 | AI / automation (PRD §10) | **BUY (vendor feature) + BUILD (workflow)** | Copilot (PIC-facing): DUR summarisation, interaction flagging, PA-letter drafting — pharmacist verifies every output; never auto-fills or auto-counsels. Recommendation: generic-substitution and MAC-appeal batching. NLP: prescriber-call notes and audit-response drafting from the record — attorney reviews before any audit response is sent. Automation: refill reminders (SMS), will-call follow-up, expiry alerts, temperature-log alerts, remittance matching, inventory par-level alerts. **Human-in-the-loop checkpoints (mandatory):** final verification, counselling, oral prescriptions, controlled-substance decisions, immunisation screening, and any record created after an audit starts (prohibited). No LLM output touches a prescription, a claim, or a patient communication without a licensed pharmacist's review. | AI is an assistant to the pharmacist, never a substitute; patient safety is not an experiment and no A/B testing framework is specified for a single store (PRD §9.5). | AI outputs logged with pharmacist verification; no unreviewed AI output in any prescription, claim, or patient communication. |

### 2.2 Build/buy summary

| Decision | Count | Items |
|---|---|---|
| **BUY** (off-the-shelf product / contract) | 11 | PMS, e-prescribing, switch, POS, DSCSA solution, PMP/I-STOP, immunisation registry, patient communications, wholesaler supply, insurance, trade-association membership |
| **HIRE** (professional service) | 5 | Attorney, CPA/valuation, lenders (bank + CDFI debt), PSAO, staffing (PIC, relief pool, RPhTs, front-store, driver, bookkeeper) |
| **BUILD** (process / SOP / service — the product's own IP) | 10 | Management-pack reporting + remittance reconciliation, prescription-journey SOPs, compliance calendar, inventory/cash/segregation controls, controlled-substance controls, audit-response procedure, immunisation programme, med sync, delivery service, AI workflows (human-in-the-loop) |
| **Explicitly NOT built** | — | See §8 (PRD §20 out of scope) |

---

## 3. Phased delivery plan — phases, acceptance criteria, definition of done, go/no-go gates

Each phase states: **objective, work, owner, acceptance criteria (Given/When/Then, tied to the PRD's criteria), definition of done, and the go/no-go gate to the next phase.** A phase is not "done" when work is started; it is done when its acceptance criteria are evidenced in writing.

### Phase P0 — Inputs & team (Days 1–14) · PRD M0–M1 · Epics E1

**Objective:** make the enterprise costable and legally advised before any external commitment.

| Work | Owner |
|---|---|
| Owner supplies the 12 inputs in writing (PRD App. B) — capital, credit band, neighbourhood/rent ceiling, NY-licensed pharmacist? (Yes/No), pharmacy experience, structure/partners + citizenship of every owner, immigration/naturalisation timeline, income needs during ramp, risk tolerance/scenario choice, tax position, delivery/clinical ambition, timeline/target opening date | Owner |
| Engage NY healthcare/pharmacy attorney + pharmacy-savvy CPA (engagement letters signed) | Owner |
| Attorney's first written answers: moratorium position (G1) + entity choice (LLC vs. business corporation; P.C./PLLC excluded) | Attorney |
| SBA SOP re-checked at the point of application and noted in the financing file (FR-C4) | CPA |
| Entity-formation decision memo | Attorney + CPA |

**Acceptance criteria (Given/When/Then):**
- Given the 12 inputs, when the inputs sheet is reviewed, then all 12 are supplied in writing — nothing else in the roadmap can be costed without them (PRD M0).
- Given the attorney and CPA, when engagement is checked, then both are engaged **before** any LOI, lease, or lender step (G5).
- Given the moratorium, when the opinion is reviewed, then it is a **written letter**, not a verbal assurance (G1).
- Given the entity choice, when the memo is reviewed, then LLC vs. corporation is documented with liability, tax, NYC Unincorporated Business Tax, S-election, and PIC-governance reasoning.

**Definition of done:** inputs sheet signed by the owner; two engagement letters on file; written moratorium opinion letter on file; entity-decision memo on file; SBA SOP check noted.

**Go / No-go gate → P1:** GO only if all four DoD items exist. NO-GO (stop, do not proceed to lender or target work) if the attorney's opinion says the moratorium position cannot be confirmed, or if the owner cannot supply the 12 inputs — the plan cannot be costed without them. **Re-plan trigger:** moratorium opinion is adverse and no structure is available outside it → move to the waiting posture (§6.3) rather than to P1.

### Phase P1 — Finance pre-work, PIC search, target screen (Days 15–30) · PRD M2 · Epics E1–E2

**Objective:** stand up a fundable entity, a financeable structure, a named PIC candidate, and a signed target screen.

| Work | Owner |
|---|---|
| Entity formed (LLC $200 / corp $125 — VERIFIED; EIN free, immediate); bank account opened | Owner + attorney |
| Lender round opens in parallel: free SBS / NYC Funds Finder session (888-SBS-4NYC / 888-727-4692); Accompany Capital; Pursuit SmartLoan; two conventional banks; ESD Main Street Capital Loan Fund via Pursuit (FR-C2). **No SBA programme approached as an available option.** | CPA + owner |
| PIC recruitment: candidate list with NYSED licence verification; confirm whether the owner is a NY-licensed pharmacist (App. B input 4 — if yes and acting as PIC, opex falls ~$14K–$16K/month and break-even falls ~30 Rx/day, ASSUMPTION from the report) | Owner |
| One-page written target screen signed off (Gate G2 criteria); NCPA/CPANY + PSAO contacted | Owner + CPA |
| PMS vendor longlist started (for the demo script in P4 — no purchase yet) | PIC (candidate) + owner |

**Acceptance criteria:**
- Given the entity, when it is checked, then it exists with EIN and bank account.
- Given the PIC search, when it is reviewed, then at least one named, NY-licensed, full-time PIC candidate is identified (G3 in progress).
- Given the target screen, when it is reviewed, then it is signed off by the owner and applies the G2 criteria to every target.
- Given the lender round, when it is reviewed, then each lender approached has a named contact and a response date; no SBA 7(a)/504/Microloan appears in the stack (FR-C1).

**Definition of done:** entity + EIN + bank account evidenced; PIC candidate list with licence verifications; signed target screen; lender-round log opened; NCPA/CPANY + PSAO contact recorded.

**Go / No-go gate → P2:** GO if a PIC candidate exists and at least one lender confirms the *structure* is financeable in principle. NO-GO if no PIC candidate can be found — **do not proceed to target search on the hope a PIC appears** (R8). **Re-plan trigger:** every lender declines the acquisition structure → re-weigh on actual terms (PRD §19.5 flip condition) but do not let startup funding availability override ramp risk; if no financeable structure exists, wait.

### Phase P2 — Search & HARD PAUSE (Days 31–60) · PRD M3 · Epic E3

**Objective:** produce a disciplined shortlist — and then stop, by design, until the moratorium gate is re-confirmed.

| Work | Owner |
|---|---|
| Target search in the top-3 neighbourhoods (East New York–Starrett City 78.5; East Flatbush 75.0; Brownsville–Ocean Hill 74.5). Longlist 5–10; screen each against G2 with a one-paragraph reason per rejection (FR-B1). Shortlist 2–3. | Owner + CPA |
| Lender feedback collected in writing | CPA |
| **Updated written moratorium opinion obtained** (G1 re-confirmed) | Attorney |
| PIC search deepened; PSAO/wholesaler conversations continued before a target is found | Owner + PIC |

**Acceptance criteria:**
- Given a longlist of 5–10 targets, when screening completes, then a shortlist of 2–3 remains, each with a written pass against every G2 criterion (FR-B1).
- Given the lender round, when it is reviewed, then at least one lender confirms the *structure* is financeable in principle.
- Given the moratorium, when the updated opinion is reviewed, then it is a written letter dated within the phase.

**Definition of done:** screened shortlist (2–3) with rejection reasons; lender feedback in writing; updated written moratorium opinion on file.

**Go / No-go gate → P3 (THE HARD PAUSE):** **NO LOI is signed, no deposit is paid, and no closing date is set unless the updated opinion clears Gate G1.** If the moratorium is still in force at Day 60 and the structure is caught: **WAIT.** Use the time to complete Phases P0–P1 work and keep the target screen warm; the 180-day clock **restarts from Stage 3 (Phase P3) when the gate clears**. Do not switch to a startup — it is equally caught for a new enrolment. **Re-plan trigger:** moratorium extended with no structure outside it → quarterly re-check posture (§6.3); do not relax the target screen under time pressure.

### Phase P3 — LOI & exclusivity (Days 61–75) · PRD M4 · Epic E3

**Objective:** lock one target under a non-binding LOI with diligence access and a defined transition.

| Work | Owner |
|---|---|
| Non-binding LOI: price range at U.S. multiples, asset-purchase structure, exclusivity, diligence access, seller transition, escrow/holdback principle, closing conditions | Attorney + CPA |
| Lender application pack assembled | CPA + owner |
| Written PIC confirmation **for this target** (named PIC, full-time, one pharmacy only) | Owner + PIC |

**Acceptance criteria:**
- Given the LOI, when it is reviewed, then it is signed, the exclusivity clock is running, and the price range sits inside 2.5–3.5× adjusted EBITDA / 2.5–4.5× SDE + inventory at cost, or any excess is justified in writing with documented reasons (FR-B2).
- Given the PIC, when it is checked, then the PIC is confirmed in writing for this target (G3).

**Definition of done:** signed LOI; exclusivity running; lender application pack complete; written PIC confirmation on file.

**Go / No-go gate → P4:** GO only if the LOI is signed *and* the PIC is confirmed in writing. NO-GO if the seller will not grant diligence access or exclusivity, or the PIC will not confirm — walk away from the target, return to the P2 shortlist. **Re-plan trigger:** seller demands a price above the U.S. range with no documented justification → discard that target (PRD §5.2 edge case 1).

### Phase P4 — Diligence, valuation, financing, filings (Days 76–120) · PRD M5 · Epics E2–E4

**Objective:** find every deal-killer before the purchase agreement, price on earnings a new owner can keep, secure the money, and file inside the NYSED window.

| Work | Owner |
|---|---|
| Full diligence checklist A–I (PRD §9.4): 3-year financials + script counts **from the dispensing system** (not a broker summary); GP/script by payer; DIR-fee accruals; PBM audit history; lease; licences/compliance; inventory; staffing; systems; structure/protections | CPA + attorney |
| Valuation memo: normalisation line by line — add back owner compensation above a market-rate pharmacist-manager salary, personal expenses, genuine one-offs; subtract costs a new owner must pay (e.g. market rent); owner-pharmacist's labour expensed at replacement cost (~$140,000 fully loaded in the report's illustration) (FR-B3) | CPA |
| Written lender commitment obtained (G4) | CPA + owner |
| PH200 filed inside the 10–14-week window ($345) — for a closing on ~Day 175, file by ~Day 80–105; DEA Form 224 filed ($888/3 yrs); NPI/NCPDP/Medicare (CMS-855B, $750)/Medicaid filings; PBM recredentialing started with written confirmations (FR-B5) | Attorney + PIC |
| PMS selection completed: written 3-year quotes from ≥3 vendors on the same demo script; 11-item checklist compared; data ownership/export/exit in writing (FR-D7). Wholesaler account opened; insurance binders obtained | PIC + owner |
| BNE question answered in writing: confirm whether any DOH-4330 licence is needed for this retail pharmacy (FR-A11) | Attorney |

**Acceptance criteria:**
- Given the LOI, when diligence completes, then every ★ item (script trend, GP/script by payer, DIR accruals, PBM audit history, lease, licences/compliance, PIC intentions) has a written finding and a quantified price adjustment or a walk-away recommendation (FR-B4).
- Given the seller's reported earnings, when normalisation is complete, then every add-back is documented or it does not count (FR-B3).
- Given the material payer list, when closing approaches, then every material PBM/PSAO has answered in writing and the recredentialing applications are filed (FR-B5).
- Given a target closing date, when the PH200 package is filed, then the filing date is ≥10 weeks before closing and the receipt is on file (FR-A1).
- Given three written PMS quotes, when they are compared, then each covers the 11-item selection checklist (FR-D7).

**Definition of done:** diligence report with red-flag list; valuation memo; written lender commitment; PH200 receipt; DEA/NPI/NCPDP/Medicare filings evidenced; PBM written confirmations; PMS contract signed (or shortlisted to one with exit terms in writing); wholesaler account + insurance binders.

**Go / No-go gate → P5:** **Walk away if any ★ item fails and the price does not reflect the quantified exposure** — quantification in writing from the accountant. No purchase agreement without a financing commitment. **Re-plan triggers:** diligence reveals material PBM audit/recoupment exposure, DIR under-accrual, short lease, single-prescriber concentration, or loss of PIC the price does not reflect → walk away from that target (PRD §19.5). Diligence runs long → the closing date moves, never the PH200 10–14-week rule. PBM rejects or delays recredentialing → do not promise a closing date that assumes a PBM moves faster; address-level history must have been checked in diligence.

### Phase P5 — Purchase agreement & closing conditions (Days 121–150) · PRD M6 · Epics E3–E4

**Objective:** convert diligence into a signed, conditioned agreement with the location and the money secured.

| Work | Owner |
|---|---|
| Signed purchase agreement: **asset purchase by default**, with escrow/holdback sized to the audit exposure, seller indemnity, representations and warranties with a survival period, and closing conditions (NYSED registration, landlord consent, material PBM confirmations, financing commitment) (FR-B7) | Attorney |
| Written landlord consent to lease assignment (or surrender-and-regrant of a new longer lease) as a closing condition; confirm whether seller/guarantors are released (FR-B6) | Attorney |
| Seller transition + non-compete/non-solicit agreements (enforceability confirmed under NY law); joint seller+buyer patient letter drafted (FR-B9) | Attorney + owner |
| Escrow funded; inventory-count plan agreed (joint count, independent stocktaker — FR-B8); pre-closing compliance check signed off | CPA + PIC |
| All five gates re-verified before closing | Owner + attorney + CPA |

**Acceptance criteria:**
- Given the purchase agreement, when it is reviewed, then it is an asset purchase (unless counsel documents why an entity purchase is better for this target), with escrow, indemnity, and all closing conditions listed (FR-B7). *Note: an entity purchase may preserve the existing Medicaid enrollment — this is a structure-specific legal conclusion only counsel can confirm in writing; never assume it (PRD §5.1 edge case 3).*
- Given the lease, when closing is approached, then written landlord consent (or a new lease) is in hand and the remaining term/renewal position satisfies Gate G2 (FR-B6).
- Given the five gates, when they are re-verified, then G1–G5 each have current written evidence.

**Definition of done:** signed purchase agreement; written landlord consent; transition + non-compete agreements; escrow funded; inventory-count plan; pre-closing compliance check signed off; gates G1–G5 re-verified in writing.

**Go / No-go gate → P6:** GO only if landlord consent is in writing — **do not close on a promise to seek consent** — and all five gates are verified. NO-GO if landlord refuses consent: the closing condition fails. **Re-plan trigger:** any closing condition unmet at Day 150 → move the closing date; do not waive a condition to hold a date.

### Phase P6 — Closing & first 30 days (Days 151–180) · PRD M7 · Epics E4–E5

**Objective:** transfer ownership without a billing gap and prove the file is trading at its diligence baseline.

| Work | Owner |
|---|---|
| Bill of sale signed; inventory counted jointly at/near closing with an independent stocktaker, valued at the seller's actual acquisition cost from wholesaler invoices; short-dated/slow-moving/discontinued stock priced separately; controlled substances reconciled separately with an opening inventory under the new DEA registration; Schedule II on Form 222 (FR-B8, FR-A4) | CPA + PIC |
| Seller transition delivered in-store; joint seller+buyer patient letter sent before closing (FR-B9) | Owner + seller + PIC |
| Post-closing notices filed: PB327 within 30 days of the change; NPPES update within 30 days of any change; Medicare CHOW within 30 days; PIC change within 7 days if applicable (FR-A9, FR-A10); BNE notified of the transfer; outstanding controlled-substance data-submission errors corrected 30 days before closing (FR-A5) | Attorney + PIC |
| PMS live; Surescripts live; DSCSA solution live; HCS/PMP configured; compliance calendar live (FR-A12) | PIC |
| Week-1 and week-4 trading reports vs. diligence baseline; month-1 management pack from the CPA; daily cash close and daily controlled-substance reconciliation from day one (FR-D4, FR-D5) | CPA + PIC + owner |

**Acceptance criteria:**
- Given the closing count, when the count sheets are reconciled, then the counted value matches invoices, controlled substances reconcile, and any short-dated/slow stock is haircut or excluded per the agreement (FR-B8).
- Given closing, when the new DEA registration is checked, then it is issued to the new entity at the store address and the opening controlled-substance inventory is recorded under it (FR-A4).
- Given closing, when 30 days elapse, then PB327, the NPPES update, and the Medicare CHOW report are all filed with receipts (FR-A10).
- Given the first 30 days of trading, when they are reviewed, then the seller transition was delivered, the joint letter was sent, and weekly script counts are tracked against the diligence baseline (FR-B9).
- Given a trading day, when the close is reviewed, then it is signed by two people and any over/short above threshold has an investigation entry (FR-D5); controlled-substance perpetual shows zero unexplained variance (FR-D4).

**Definition of done:** bill of sale; counted inventory reconciled; post-closing notices filed with receipts; **no billing gap**; trading stable; retention tracking started; cash position known weekly; compliance calendar live.

**Go / No-go gate → P7:** GO if week-4 trading is at or near the diligence baseline and cash is known weekly. NO-GO (escalate, do not "trade through it") if script count falls materially in the first 4 weeks, the PIC/staff depart, or a prescriber disengages — these are the PRD's early-warning churn signals (§9.4): activate the retention plan (seller visibility, prescriber visits by the PIC, delivery reliability) and the relief pool. **Re-plan trigger:** large PBM recoupment in month 6 → escrow sized to audit exposure; audit-response procedure; attorney + PSAO same day (PRD §6.3).

### Phase P7 — First 90 days of ownership, stabilisation (Days 181–270) · PRD §6.5, §13.1, §19.7 Horizon 1

**Objective:** stabilise the acquired file and stand up the service revenue that makes dispensing viable.

| Work | Owner |
|---|---|
| Prescriber visits by the PIC (FQHCs, clinics, physician offices within 0.5 miles — prescriber map is a pre-lease site-search task, PRD §4.7); hours/delivery/phone unchanged | PIC |
| First immunisation clinic only if certified and the SOP is complete (FR-E2) | PIC |
| Med-sync enrolment drive for chronic patients (FR-E3); delivery reliability tracked (FR-E6) | PIC + owner |
| Weekly script-count and GP/script reporting vs. diligence baseline; first monthly management packs; compliance calendar discipline; monthly PIC self-audit (prescription records, controlled-substance perpetual, signature logs, PMP checks, DSCSA data, expiry, temperature logs, cash reconciliation) | CPA + PIC |
| Front-store range set and tracked separately from prescription gross profit (FR-E5); cash prices/U&C set with the CPA and reviewed quarterly (FR-E4) | Owner + CPA |

**Acceptance criteria:**
- Given the patient base, when med sync is reviewed monthly, then the share of chronic patients synchronised and the will-call backlog are tracked (FR-E3).
- Given month-end, when the management pack is produced, then it contains the inventory report, GP/script by payer, and the remittance reconciliation with every short-pay investigated the same week (FR-C6).
- Given an immunisation session, when it is audited, then the order, consent, screening, administration, observation, registry report, and billing benefit are all documented (FR-E2).
- Given the monthly pack, when it is reviewed, then front-store and prescription gross profit are separate lines (FR-E5).

**Definition of done:** three consecutive monthly management packs on schedule; GP/script by payer positive and stable on the material contracts (or a written CPA plan to exit below-cost contracts); med sync and immunisation SOPs operating; retention tracked weekly vs. baseline with **no percentage target set** (no verified rate exists).

**Go / No-go gate → Horizon 2 (Years 2–3):** advance to adherence packaging/MTM at scale, LTC contracts (written contract first, PRD FR-E7), and delivery-radius expansion only if GP/script by payer is positive and stable — and only with the CPA's written sign-off. A second store needs a second PIC, a second registration, and a second DEA number, and is out of scope until the first store's GP/script by payer is positive and stable for two quarters (ASSUMPTION threshold — for the CPA to set, PRD §19.3).

### Startup-branch variant (only if a PRD §19.5 flip condition triggers)

If no suitable target exists at a U.S.-multiple price after a genuine search, the startup branch is available **only if** the owner has a specific underserved location or prescriber relationship plus capital for an 18–24-month ramp; otherwise **do neither yet**. Startup phases (PRD §14): Days 1–30 team + site selection in the top neighbourhoods + lease negotiation; Days 31–60 lease signed, contractor quotes, build-out begins, PH200 filed; Days 61–120 build-out, fixtures, software selection/implementation, hiring, wholesaler account, insurance; Days 121–150 NYSED inspection, DEA, NPI, Medicare/Medicaid enrollment (moratorium applies), PBM/PSAO credentialing from zero; Days 151–180 soft opening, prescriber outreach, patient-transfer campaign, first immunisation clinic (if certified). The 180 days end at **opening**, not revenue maturity — the startup then faces the 18–24-month ramp with Year 1 EBITDA-negative in every scenario (startup capital Lean $435,230 / Standard $791,010 / Larger $1,309,273; break-even 68 / 111 / 171 Rx/day).

---

## 4. Team and vendor map — who does what

### 4.1 Roles (R = responsible, A = accountable, C = consulted, I = informed)

| Role | Person / party | Does | RACI highlights |
|---|---|---|---|
| **Owner-operator** (green card holder, non-pharmacist unless App. B input 4 says otherwise) | The owner | Business manager, employer of record, capital, hiring, pricing decisions with the CPA; **must not** counsel, verify, receive oral prescriptions, or supervise pharmacy practice (FR-F4) | A: gates G1–G5, financing, closing. R: inputs, entity, lender round, target screen sign-off |
| **Supervising pharmacist (PIC)** | NY-licensed pharmacist, full-time 30+ hrs/week, this pharmacy only | Practice of pharmacy: final verification, counselling, controlled substances, DSCSA, PMP, immunisations, SOPs, rosters, PIC self-audit; may not assign responsibility (PRD §11.1) | A: all clinical/compliance execution. R: PH200, DEA, SOPs, PMS demo script, daily reconciliations |
| **Relief pharmacist pool** | Licensed pharmacists, from day one | Covers every open hour when the PIC is unavailable; never open without a pharmacist | R: cover. A (PIC): pool maintained |
| **Healthcare/pharmacy attorney** | NY attorney (hired) | Moratorium opinion, entity choice, LOI/purchase agreement, lease/landlord consent, PBM contract review, anti-kickback review, employment matters, Medicaid compliance programme, all 10 attorney questions (App. C) | A: G1, G5. C: every filing and contract before execution |
| **Pharmacy-savvy CPA** | CPA (hired) | Normalisation, valuation memo, financing stack, lender round, monthly management pack, GP/script-by-payer model, inventory/cash reporting, tax/entity modelling | A: G2 (evidence), G4. R: diligence financials, management pack |
| **Bookkeeper** (part-time, from opening) | Hired | Posts payments, assists monthly inventory count with the PIC; **must not** dispense, handle controlled-substance ordering/receipt alone, or reconcile the controlled-substance perpetual; the bookkeeper who posts a payment does not approve it (FR-D6) | R: bookkeeping. Never: dispensing, controlled-substance reconciliation |
| **RPhTs** | NY-licensed Registered Pharmacy Technicians | Lawful tasks only, under direct personal supervision of a licensed pharmacist; ≤2 per pharmacist on duty, ≤4 total at one time | R: filling (pharmacist verifies), data entry. Never: interpret/evaluate a prescription, receive oral prescriptions, counsel |
| **Front-store staff / delivery driver** | Hired as volume requires | Front store; delivery (sealed, logged out, proof of delivery, undelivered items returned same day). Driver must not counsel, take new prescription orders by phone, or decide substitutions (FR-F4) | R: front store / delivery |
| **PMS vendor** | PioneerRx / PrimeRx / Liberty / WinRx (one, by demo script) | PMS, Surescripts, DSCSA solution, PMP/I-STOP, CIR reporting, med sync, POS (or integration), Part B roster billing, reporting, support; data ownership/export/exit in writing | R: system uptime, data export. A (PIC): acceptance via demo script |
| **PSAO** | Hired | Network contracting, audit support, PBM confirmations | R: contracting leverage. C: every PBM answer before closing |
| **Wholesalers** | Cardinal Health / McKesson / Cencora (primary + secondary) | Drug supply with full DSCSA transaction data; secondary kept active with small regular orders | R: supply, DSCSA data |
| **Lenders** | 2 conventional banks + CDFI/non-SBA community lenders (Accompany Capital, Pursuit, ESD via Pursuit) + SBS/Funds Finder | Debt tranches; **no SBA programme** | R: term sheets / commitment letter |
| **Seller** | Outgoing owner/pharmacist | Transition in-store for a defined period; joint patient letter; non-compete/non-solicit; inventory count cooperation | R: transition. A (owner): retention tracking |
| **Insurance broker** | Hired | Professional liability, general liability, property, business interruption, cyber/privacy, workers' comp, auto coverages and limits (quote required — no premium stated) | R: binders before closing |
| **Trade associations** | NCPA, CPANY (membership) | Market intelligence, reform engagement, contract support | I: ongoing |

### 4.2 Hiring sequence

Attorney + CPA first → PIC before any NYSED filing → RPhTs only after the PIC is in post and the training/competency programme exists → front-store and delivery as volume requires. (PRD §14.)

### 4.3 Separation of business and practice (written into every job description, FR-F4)

The owner manages the business; the PIC controls the practice of pharmacy. No job description may blur that line, and no "paper PIC" — a named supervisor who is not genuinely full-time, on-site, and in active control — is permitted (PRD §7.5).

---

## 5. KPIs, events, and the operating dashboard

### 5.1 KPI table (PRD §9.2)

| KPI | Target / threshold | Phase first measured |
|---|---|---|
| Rx/day vs. break-even | ≥111/day (Scenario B base); 68 (A) / 171 (C) | P6 (week 1) |
| Rx/day vs. steady-state target | 80 (A) / 150 (B) / 220 (C) | P7 |
| Gross margin | Base 20.9% (VERIFIED 2025); conservative 18.2% (VERIFIED 2024) — never model 20.9% as a floor | P6 |
| Gross profit per Rx | $14.57 national average (2024) vs. $15.00 cost to dispense — the store must beat the national average | P6 |
| Monthly EBITDA positive | Month 8 (B) / 9 (C) / 10 (A) of Year 1 (startup-model reference; acquisition measured from the target's actuals) | P7 |
| PBM remittance reconciliation | 100% of claims matched weekly; every short-pay investigated the same week | P6 |
| Controlled-substance variance | Zero unexplained, daily | P6 |
| Inventory: dead stock, shrinkage, turns | Monthly report; targets set by the CPA from the store's first-quarter data (no verified Brooklyn benchmark exists — **do not invent one**) | P7 |
| Patient retention | Tracked weekly vs. diligence baseline; **no percentage target set** (no verified rate exists) | P6 |

### 5.2 PMS dashboard (one screen, PRD §7.2)

Today's script count vs. diligence baseline; GP/script by payer (today and trailing 30 days); claims pending adjudication/rejected (worked same day); will-call ageing; controlled-substance perpetual variance (must be zero unexplained); PBM remittance reconciliation status; inventory alerts (short-dated, dead stock, top-50 stock-outs); immunisation session schedule. **The FR-D7 demo script is the acceptance test for this dashboard.**

### 5.3 Minimum event tracking (20 events, PRD §9.3)

Prescription received (eRx/written/oral) · DUR run · pharmacist verification · PMP check · claim adjudicated (paid/rejected) · claim reversed · fill completed · final verification · counselling offered/accepted/refused · pickup (two-ID check) · delivery dispatched / proof of delivery / undelivered return · will-call return to stock · refill request · PA initiated/resolved · MAC appeal filed · immunisation administered + registry reported · inventory receipt / count adjustment / return / recall actioned · controlled-substance order/receipt/reconciliation · cash close signed · incident/near-miss logged · PBM remittance matched / short-pay flagged · audit letter received / appeal filed.

---

## 6. Risks that would force a re-plan

Risk register from PRD §15.1 (likelihood/impact are the report author's judgement on the evidence cited). Each risk names its re-plan action — "monitor closely" is not a mitigation.

| # | Risk | Likelihood | Impact | Mitigation | Re-plan trigger |
|---|---|---|---|---|---|
| R1 | Below-cost reimbursement — PBM rate-setting + opaque MACs; GP/Rx $14.57 vs. cost $15.00 | H (already occurring) | H | Know the rate before filling; batch MAC appeals with invoices; PSAO; model every network; do not stock below-cost drugs; build non-dispensing revenue | GP/script by payer negative on a material contract for 2 consecutive months → exit or renegotiate that contract; do not grow volume on it |
| R2 | Retroactive adjustments, audits, clawbacks — GER/BER, inventory audits, OMIG/MFCU | H | H | Complete records from day one; daily reconciliation; audit-response procedure; attorney + PSAO on call; escrow sized to audit exposure | Audit letter received → procedure activates; material recoupment → escrow drawn, SOP changed, CPA re-forecasts |
| R3 | Working capital / inventory carrying cost — wholesaler paid in 14–30 days, PBM pays in 30–60 days; specialty refund delays >21 days | H | H | Full working-capital reserve (do not cut it); tight par levels + FEFO; no high-cost stock without written authorisation + confirmed reimbursement; secondary wholesaler; monthly inventory report | Cash runway < 4 weeks → owner + CPA emergency review; no new high-cost stock; renegotiate wholesaler terms |
| R4 | Labour cost / pharmacist scarcity — cost to dispense $13.67 (2023) → $15.00 (2024) while GP/Rx fell; NYC wages; PIC full-time | H | M | Roster to safe capacity; RPhTs for lawful tasks; price clinical services so pharmacist time earns revenue | PIC vacancy > 2 weeks → relief pool + recruitment escalation; if no PIC can be secured, the store cannot trade |
| R5 | PBM concentration / vertical integration — Big 3 ~79% of claims; affiliated pharmacies reimbursed higher; closure wave (net −3,062 US pharmacies 2022–2024) | H (structural) | H | No store-level mitigation beyond R1–R2; enter only if the CPA's forecast shows viability *without* assuming PBM reform or a rate increase; engage NCPA/CPANY | CPA forecast fails without assuming reform → do not proceed |
| R6 | **Medicaid moratorium** — new enrollments, reinstatements, CHOWs suspended 27 Jul 2026 through at least 27 Jan 2027, extendable; pending applications discontinued | Certain (in force) | H | **Gate G1** — written attorney opinion before any LOI/deposit; wait if caught; do not switch to startup | Moratorium still in force at Day 60 → hard pause; clock restarts from P3 when it clears; quarterly re-checks while waiting |
| R7 | **SBA ineligibility** — any LPR ownership bars 7(a)/504/Microloan since 1 Mar 2026 | Certain (rule in force) | H | **Gate G4** — finance without SBA; re-check SOP at application; naturalisation restores eligibility | Lender proposes an SBA tranche → reject it; re-price the stack without SBA |
| R8 | No supervising pharmacist — PIC resigns, ill, or loses licence; pharmacy cannot open without a pharmacist | M | H | **Gate G3** — PIC secured in writing; relief pool from day one; SOPs + succession plan | PIC lost with no relief cover → store does not open/trade as a pharmacy; Board notified within 7 days (PH-205) |
| R9 | Target diligence failure — declining scripts, audit exposure, DIR under-accrual, short lease, single-prescriber concentration, loss of PIC | M | H | PRD §9.4 checklist; walk away if any ★ item fails and price does not reflect quantified exposure; escrow + indemnity | Any ★ item fails unpriced → walk away from that target; return to P2 shortlist |
| R10 | Lease / landlord — consent refused or renegotiated; short remaining term guts goodwill; seller/guarantors not released | M | H | Landlord consent as a closing condition in writing; lease reviewed before LOI; consider surrender-and-regrant | Consent refused → closing condition fails; do not close on a promise |
| R11 | Patient retention after purchase — no verified retention rate exists | M | M | Retain incumbent PIC + staff; keep location/phone/hours; seller transition; joint patient letter; seller note/earn-out tied to retained volume | Script count falls materially in first 4 weeks → retention plan activates (seller visibility, prescriber visits, delivery reliability) |
| R12 | Theft, shrinkage, diversion — no verified shrinkage rate found; controlled-substance diversion is a DEA/Board criminal and licensing risk | M | H | PRD §7.7 controls in full; daily controlled-substance reconciliation; variance investigated same week | Any unexplained controlled-substance variance → same-week investigation; confirmed loss reported as counsel advises (Form 106) |
| R13 | Regulatory change — DSCSA exemption date uncertain; immunisation bills pending; PBM-reform timeline not verified; NYRx changed the auditor overnight in 2023 | M | M | Compliance calendar; attorney on retainer; compliance budget line not cut when cash is tight | New rule published → attorney assesses within 30 days; calendar and SOPs updated |
| R14 | Single-payer / single-prescriber concentration | M | H | Diversify payer mix from the start; no single payer above a share the CPA sets (no percentage stated — for the CPA to set); diligence top-10 prescribers | Concentration above the CPA's cap → diversification plan before signing the next contract |

### 6.1 Black swans (PRD §15.2)

1. **Medicaid moratorium extended indefinitely + no entity-purchase structure available at a fair price.** Both routes are gated; the correct move is to wait (quarterly re-checks, target screen warm, PIC and lender relationships deepened). A purchase made under a freeze, or a startup launched into one, strands the largest revenue line.
2. **A federal PBM settlement or cost-plus mandate lands, but the store's contracts exclude it or demand wholesaler invoices to verify "dead-net" cost.** The store's economics do not improve and its confidential pricing is exposed. Mitigation: do not forecast any benefit from reform that has not taken effect in a written contract; attorney + CPA model any cost-plus offer on the store's actual invoices before accepting.

### 6.2 Dependencies (hard)

Attorney's written moratorium opinion → LOI. PIC secured in writing → PH200 filing and closing. Lender commitment → purchase agreement. Landlord consent in writing → closing. Medicare enrollment → Medicaid enrollment (sequential). NYSED registration → DEA → PBM credentialing (sequential). Owner's 12 inputs → financing sizing, target screen, entity decision.

### 6.3 Waiting posture (if gated — a legitimate outcome)

While waiting: (i) confirm the Medicaid moratorium position quarterly; (ii) build the supervising-pharmacist relationship and the PSAO/wholesaler conversations *before* a target is found, so diligence can move fast; (iii) line up the healthcare attorney, accountant, and lender so a good target is not lost to a slow process; (iv) keep the written target screen and do not relax it under time pressure. A first pharmacy purchase made in haste at the wrong multiple, with the wrong lease, or under a Medicaid freeze is worse than a delayed purchase.

---

## 7. Traceability — every phase back to the PRD

| PRD2Pro phase | PRD sections implemented | PRD requirements implemented (primary) | PRD milestones |
|---|---|---|---|
| P0 — Inputs & team | §4.3 (G1, G5), §14 (M0–M1), §19.6, App. B, App. C | FR-C4 | M0, M1 |
| P1 — Finance pre-work, PIC search, screen | §4.3 (G3, G4 in progress), §5.3, §5.6, §14 (M2), §13.3 | FR-C1, FR-C2, FR-C5, FR-F1–F6 (recruitment) | M2 |
| P2 — Search & HARD PAUSE | §4.3 (G1 re-confirmed), §5.2, §14 (M3), §6.3 | FR-B1 | M3 |
| P3 — LOI & exclusivity | §5.2, §14 (M4) | FR-B2, FR-B7 (principles), FR-B9 (transition principle) | M4 |
| P4 — Diligence, valuation, financing, filings | §5.1, §5.2, §5.3, §5.4 (FR-D7/D8), §8, §14 (M5) | FR-A1, A4–A8, A11; FR-B2–B5; FR-C1–C4; FR-D7, D8 | M5 |
| P5 — Purchase agreement & closing conditions | §5.2, §14 (M6) | FR-B6, FR-B7, FR-B8 (plan), FR-B9 | M6 |
| P6 — Closing & first 30 days | §5.1, §5.2, §5.4, §6.2, §6.5, §14 (M7) | FR-A4, A5, A9, A10; FR-B8, B9; FR-D1–D6 (live); FR-E8 (procedure live) | M7 |
| P7 — First 90 days, stabilisation | §5.3, §5.4, §5.5, §5.6, §6.5, §9, §12, §13.1, §19.7 H1 | FR-C6; FR-D1–D8 (operating); FR-E1–E6; FR-F1–F6 | Post-roadmap |
| Cross-cutting (all phases) | §1–§3 (vision, market, sizing), §4 (principles, flywheel), §7 (UX/store + PMS dashboard), §10 (AI/automation, human-in-the-loop), §11 (security & compliance), §15 (risks), §16 (financial model), §17 (owner perspective), §18 (epics, stories, RICE, MoSCoW, backlog), §19 (recommendations, flip conditions), §20 (out of scope) | All FR-A1–A12, B1–B9, C1–C6, D1–D8, E1–E8, F1–F6 | — |

**Epic mapping (PRD §18.1):** E1 Gates & team → P0–P1; E2 Financing without SBA → P1, P4; E3 Target acquisition → P2–P5; E4 Licensing & enrollment → P4–P6; E5 Trading operations → P6–P7.

**Backlog mapping (PRD §18.5, 20 items):** items 1–5 → P0; 6–10 → P1; 11–13 → P2; 14 → P3; 15–17 → P4; 18–19 → P4–P5; 20 → P5–P6.

**User-story mapping (PRD §18.2, 10 stories):** stories 1–2 → P0–P1; story 3 → P4; stories 4–5 → P4; stories 6–8 → P6–P7; story 9 → P5–P6; story 10 → P7.

---

## 8. What is explicitly NOT built (PRD §20 out of scope)

| Item | Why it is out of scope |
|---|---|
| **Any SBA financing route** — 7(a), 504, Microloan, Community Advantage | Barred for this owner (Policy Notice 5000-876441, eff. 1 Mar 2026; SOP 50 10 8.1). Never to be included in the stack, the budget, or a lender conversation as an available option. Re-check the SOP at application; naturalisation is the only route back, and financing must not be planned around a future naturalisation date. |
| **A dispensing-only business model** | Loses money at the national average (−$0.43/Rx). The product must include service and front-store revenue and GP/script-by-payer discipline. |
| **Medicaid revenue before enrollment is active** | Moratorium gates new enrollments and changes of ownership; do not count Medicaid revenue until enrollment is active. |
| **Startup as the default route** | Acquisition is the verdict; startup is a conditional fallback only (PRD §19.5 flip conditions). |
| **The Canadian 4–6× EBITDA valuation multiple** | Canadian market range (PharmacyBroker.ca); using it on a U.S. store overpays by ~1–2 turns of EBITDA. |
| **A nominal U.S.-citizen co-owner to restore SBA eligibility** | A serious compliance problem; must not be attempted without counsel. |
| **LTC, 340B, specialty, and sterile compounding at launch** | Each needs a separate feasibility and legal review; LTC is Phase 3 only, contract first; **do not pursue 340B without a separate feasibility and legal review**. |
| **Second store / multi-store expansion** | Needs a second PIC, registration, and DEA number; not modelled in this PRD. |
| **Any grant-funded budget line** | No standing grant funds a new Brooklyn pharmacy; every programme that provides money here is repayable debt. |
| **Bhupesh's background, resume, or STEM OPT situation** | The owner is a green card holder, not Bhupesh. Nothing in this plan applies Bhupesh's employment, visa, or OPT position to the owner. |
| **No software prototype / no new pharmacy software built** | The PMS, POS, and switch are bought (see §2); no custom dispensing software is built. The skill's software-prototype sections are adapted, not delivered as code. |
| **No A/B testing, no ML at launch** | Sample sizes do not support A/B testing and patient safety is not an experiment (PRD §9.5). ML (demand forecasting, MAC alerting, adherence-risk flagging) is a Phase 3 opportunity requiring the PMS data export and CPA/PIC sign-off. |

---

## 9. Assumptions register

Every assumption this plan depends on, with its basis and how it is validated. An assumption is not a fact until the named validator replaces it in writing.

| # | Assumption | Basis | Risk if wrong | How to validate | Owner | Due |
|---|---|---|---|---|---|---|
| A1 | Lease ≥5 years remaining or renewal options the buyer controls (Gate G2) | PRD §4.3 — no published minimum found | Goodwill paid for a location that can be lost | Lease review before LOI; landlord consent in writing | Attorney | P3 |
| A2 | Short-dated stock flagged at expiry within 90 days; dead stock = no dispense in 90 days | PRD FR-D2 — ASSUMPTION, set with the PIC | Expired or dead stock on the shelf / in the valuation | PIC sets the thresholds in writing at P4 | PIC | P4 |
| A3 | Daily-close over/short threshold e.g. $10 | PRD FR-D5 — ASSUMPTION, set with the CPA | Cash leakage below the threshold unnoticed | CPA sets the threshold in writing at P4 | CPA | P4 |
| A4 | Legal-fees planning envelope $12,000–$25,000 | PRD App. D item 10 — ASSUMPTION (no verified NYC pharmacy-specific fee schedule found) | Budget underrun/overrun | Written fee schedules from attorney/CPA/valuer/stocktaker/recruiter | Owner | P0 |
| A5 | CDFI loans $5K–$250K typical; rates commonly 8–18% | PRD §5.3 edge case — ASSUMPTION | Stack shortfall if CDFI tranche is smaller or dearer | Written term sheets from each CDFI | CPA | P1 |
| A6 | Delivery-vehicle purchase $25K–$45K (if a vehicle is bought) | Master report §5.2 — ASSUMPTION | Capital understatement | Written quote before any vehicle purchase | Owner | P7 |
| A7 | Personal capital 30–50% of initial capital as the planning envelope; illustrative stack 25–30% personal + 55–65% bank + 10–15% seller note | PRD FR-C1, §16.4 — ASSUMPTION (illustrative) | Deal unfundable on actual terms | Owner's 12 inputs + written lender commitments | CPA + owner | P4 |
| A8 | Illustrative acquisition cash to close and trade ~$650,000–$1.1M for a median-sized store | PRD §1.4/§16.4 — ASSUMPTION from BizBuySell medians | Real target costs materially more or less | Target's normalised earnings, counted inventory, receivables cycle | CPA | P4 |
| A9 | Second store only after first store's GP/script by payer is positive and stable for two quarters | PRD §19.3 — ASSUMPTION threshold, for the CPA to set | Premature expansion | CPA sets the threshold in writing | CPA | P7 |
| A10 | No single payer above a share the CPA sets (no percentage stated) | PRD §15.1 R14 — for the CPA to set | Concentration risk unpriced | CPA sets the cap from the target's payer mix | CPA | P4 |
| A11 | Owner-as-PIC (if the owner is a NY-licensed pharmacist) cuts opex ~$14K–$16K/month and break-even ~30 Rx/day | PRD §16.2 — report illustration | Break-even understated if the owner is not the PIC | App. B input 4 answered in writing | Owner | P0 |
| A12 | RPhT ratio ≤2 per pharmacist, ≤4 total — confirm current 8 NYCRR §63.14 / §29.7 text in writing | PRD FR-F2 — stated in Regents amendment text found in research | Unlawful rostering | Attorney/CPA confirm current text in writing | Attorney | P1 |

---

## 10. Carried-forward open items — do not silently resolve

### 10.1 The 12 owner inputs (PRD Appendix B — must be supplied; nothing substitutes for these)

1. Available capital (total cash investable — savings, family funds, home equity).
2. Credit profile (FICO band, U.S. credit-history length, bankruptcies/liens/judgments, existing debts — supply to the lender directly; the adviser needs only the band).
3. Target neighbourhood(s) / site; acceptable rent ceiling; buy or lease the premises.
4. Are they a NY-licensed pharmacist? (Yes/No; if yes, licence number and whether they will act as PIC — this cuts ~$14K–$16K/month from opex.)
5. Pharmacy experience (years, PBM/wholesaler relationships, prior ownership).
6. Business structure intended; partners and their citizenship/ownership % (citizenship of *every* owner matters for SBA re-checks and NYSED disclosure).
7. Immigration timeline — naturalisation planned/underway, and when? (Determines whether SBA eligibility could be restored; do not plan financing around it.)
8. Income needs during ramp (monthly draw needed; how many months the owner can live without a draw — the model assumes $0 owner draw).
9. Risk tolerance / scenario choice (Lean, Standard, Larger) and whether acquisition is on the table.
10. Tax position (entity preference, CPA engaged or not, personal tax returns available — lenders require 2–3 years).
11. Delivery/clinical-service ambition (delivery radius, vehicle, clinical services — compounding changes licensing and cost materially).
12. Timeline — target opening date (drives the licensing critical path and the financing timetable).

### 10.2 The 10 attorney questions (PRD Appendix C — do not proceed without answers)

1. Entity selection (LLC vs. business corporation) — liability, tax, NYC Unincorporated Business Tax, S-election, governance keeping professional control with the PIC.
2. BNE licence — definitive written answer on whether this retail pharmacy (no ADS, no institutional contracts) needs any DOH-4330 licence.
3. Ownership-change reporting deadline — exact deadline and form (statute states no day count; secondary materials cite 30 days, Form PB327).
4. Anti-kickback / prescriber arrangements — review of any payment, discount, delivery, or marketing arrangement involving prescribers, clinics, nursing homes, or manufacturers.
5. PBM contracts — review of the first PBM/PSAO contracts (reimbursement, audit/clawback, termination, DIR-like fees, network adequacy) before execution.
6. SBA alternatives and any citizen co-owner structure — a nominal citizen owner to satisfy the SBA rule would be a serious compliance problem.
7. Lease and premises — use clause permitting pharmacy use, assignment, NYSED-inspection access, signage rights, contingency if NYSED registration is denied or delayed.
8. Employment matters — PIC employment agreement (duties, hours, non-compete/non-solicit enforceability in NY, termination, PIC-succession provisions), technician scope, wage/hour compliance.
9. Medicaid compliance programme — whether a small independent needs a full OMIG compliance programme or a scaled one, and what it must contain.
10. Naturalisation timing (if ever relevant to financing) — only an immigration attorney can advise; do not build the financing plan around a future naturalisation date.

Plus the acquisition-specific attorney questions (PRD §9.7 / App. C): current moratorium status and scope by structure; asset vs. entity structure incl. successor-liability (de facto merger) risk, NY bulk-sale rules, tax treatment; whether the ownership entity/immigration status raises any issue for NYSED, DEA, or lender underwriting; enforceability of the seller's non-compete/non-solicit and transition obligations; the specific lease (assignment vs. surrender-and-regrant, landlord consent, release of seller/guarantors); any ambiguous PBM recredentialing answer; employment, workers' comp, and insurance tail/run-off for retained staff and pre-closing acts.

### 10.3 The 23 unverified items (PRD Appendix D — carried forward visibly)

From master report Appendix A.9 — each is labelled UNVERIFIED or "quote required" where it appears in this plan:

1. NCPDP first-ID fee and processing time (only the $400 *additional*-ID fee is in NCPDP's FAQ).
2. Medicare/Medicaid and PBM processing times (industry estimates 60–90 days Medicare, 30–90 days Medicaid, 90–180 days PBM — estimates, not published commitments).
3. NYSED re-inspection and PIC-change fees.
4. NYC DOB/FDNY permit fees and timelines.
5. NY prescription-record retention period (exact period not verified — confirm with counsel; do not assume a period).
6. Employer-registration fees and timing.
7. Workers' compensation, disability, and Paid Family Leave premiums.
8. Whether the MATE 8-hour training attestation applies to a pharmacy-entity DEA registration.
9. Exact ownership-change reporting deadline (see §10.2, Q3).
10. Attorney / CPA / valuation / stocktaking / recruiting fee schedules (no verified NYC pharmacy-specific schedule found — "quote required"; the §5.2 legal-fees line of $12,000–$25,000 is an ASSUMPTION planning envelope).
11. Per-neighbourhood independent-vs-chain pharmacy counts (Gap G1).
12. Per-neighbourhood physician-office / prescriber counts (Gap G2).
13. PUMA Medicaid/Medicare splits for 7 of 12 neighbourhoods (Gap G3).
14. Neighbourhood-level rent series (Gap G5).
15. Current block-level foot-traffic data (Gap G6 — evidenced only for Flatbush).
16. Current NYRx dispensing-fee / ingredient-cost schedule (obtain the eMedNY schedule before forecasting Medicaid revenue).
17. 2026 Part B immunisation administration fee ($34.62 in one secondary source — not verified from a CMS fee schedule).
18. DSCSA small-dispenser exemption date (27 Nov 2026 vs. 27 Nov 2027).
19. Pending NY immunisation-expansion bills (A.8383, A.4346, S.8496 — not enacted; do not plan on them).
20. February 2026 federal PBM-reform provisions — implementation timeline not verified.
21. Cost-plus PBM offer terms and availability to a new independent in NY (not verified).
22. Senior (65+) shares not retrieved for 7 of 12 neighbourhoods (Gap G7).
23. Neighbourhood-level prescription-volume, script-count, or reimbursement data (Gap G8 — the model assumes volume scales with population × senior share × public-payer share, stated not evidenced).

None of these changes the verdict, but any of them can change a specific target's numbers — which is why the verdict is CONDITIONAL and the first action is to engage the attorney and CPA.

### 10.4 Market data gaps G1–G12 (PRD Appendix E)

| Gap | Consequence |
|---|---|
| G1 — No per-neighbourhood independent-vs-chain pharmacy counts | Competition factor scored on borough chain counts + closure reporting only, capped at 7 |
| G2 — No per-neighbourhood physician-office or prescriber counts | Clinical proximity scored on documented anchors only, capped at 7–8 |
| G3 — No PUMA coverage split for 7 of 12 neighbourhoods | Payer factor capped at 6–7 for those areas, rests on borough proxies |
| G4 — No neighbourhood-level Medicaid or Medicare enrollment counts | Payer concentration measured as share of residents with coverage type (ACS), not enrollee counts |
| G5 — No neighbourhood-level commercial-rent series | Rent factor rests on borough range + 4–5 individual listings + Furman rent-rank |
| G6 — No current block-level foot-traffic data | Foot traffic evidenced only for Flatbush |
| G7 — Senior (65+) shares not retrieved for 7 of 12 neighbourhoods | Factor 2 uses hypertension rates and HEIA proxies where direct shares are missing |
| G8 — No prescription-volume, script-count, or reimbursement data by neighbourhood | Model assumes volume scales with population × senior share × public-payer share — stated, not evidenced |
| G9 — Geography mismatches (Furman ≠ PUMAs ≠ Community Districts ≠ Point2Homes) | Figures from different geographies shown side-by-side, never averaged |
| G10 — Furman poverty rates not captured for Bushwick and Sheepshead Bay; Furman rent rank not captured for Flatbush/Midwood and Sunset Park | Those factor scores marked ‡/†, rest on secondary evidence |
| G11 — Pharmacy directory counts are not audited censuses | None used as "the number of pharmacies in Brooklyn" (spread 982–1,423) |
| G12 — No vacancy data newer than 2021–22 for most corridors | Vacancy cited only for Flatbush |

---

## 11. Numbers reconciliation (verification checklist)

Checked against the PRD and master report before delivery:

| Figure | Value in this document | Source |
|---|---|---|
| Startup capital A / B / C | $435,230 / $791,010 / $1,309,273 | PRD §16.1; report §5.2 |
| Break-even Rx/day (base) A / B / C | 68 / 111 / 171 | PRD §16.1; report §5.5 |
| Monthly opex A / B / C | $30,641 / $51,050 / $80,083 | PRD §16.1 |
| Working capital A / B / C | $122,564 / $255,250 / $480,498 | PRD §16.1 |
| GP/Rx vs. cost to dispense | $14.57 vs. $15.00 (−$0.43/Rx) | PRD §1.2; report §1.1 (NCPA 2025 Digest) |
| Margin base / conservative; revenue per Rx | 20.9% / 18.2%; $79.20 | PRD §12.2 (NCPA 2026 Digest, VERIFIED) |
| 5-yr ROI A / B / C | ~105% / ~172% / **~135%** (not ~150%) | PRD §16.1; report §5.6 + correction note (report line 1501: spreadsheet computes 134.6% at +5%/yr) |
| Payback A / B / C | ~3.8 / ~2.5 / ~3.1 yrs | PRD §16.1 |
| First EBITDA-positive month A / B / C | Month 10 / 8 / 9 | PRD §16.1 |
| 3-yr cumulative EBITDA B base / conservative | +$567,879 / +$50,289 | PRD §1.6, §16.1 |
| SBA bar | Policy Notice 5000-876441, eff. 1 Mar 2026; SOP 50 10 8.1, eff. 1 Oct 2026 | PRD §4.3 G4; report §1.3/§6.2 |
| Medicaid moratorium | CMS-approved 27 Jul 2026, through 27 Jan 2027, extendable in 6-month periods | PRD §1.2; report §9.2.5 |
| PH200 fee / window; renewal | $345; 10–14 weeks; renewal $260 | PRD §5.1 FR-A1/A12 |
| DEA fee | $888 / 3 years | PRD §5.1 FR-A4 |
| Medicare / Medicaid fees | $750 (2026); $750 total (Medicaid waived if Medicare paid) | PRD §5.1 FR-A7/A8 |
| LLC / corp formation | $200 / $125; EIN free | PRD §14 M2 |
| RPhT fees; ratio | $175 initial / $100 triennial; ≤2 per pharmacist, ≤4 total | PRD §5.6 FR-F2 |
| Valuation multiples | 2.5–3.5× adj. EBITDA / 2.5–4.5× SDE + inventory at cost; BizBuySell avg 2.79×, 2025 median sale $600,000 | PRD §1.3, §5.2 FR-B2, §16.4 |
| Canadian multiple — NOT used | 4–6× EBITDA (Canadian) — excluded | PRD §1.3, §20 |
| Neighbourhood scores | 78.5 / 75.0 / 74.5 / 72.5 / 70.5 | PRD §1.2/App. E |
| PIC salary benchmark | $140,910 (BLS May 2025 median) | PRD App. A |
| Day-60 hard pause; 180-day clock restarts from Stage 3 | Preserved in P2 (§3) | PRD §14 |
| No SBA-eligible claim anywhere in this document | Verified by read-back | — |
| No Medicaid revenue counted before enrollment | Stated in §0.1, §8, and P2/P4 | PRD §4.4 principle 4 |

---

## 12. Final outputs checklist

| # | Deliverable | Status | Section |
|---|---|---|---|
| 1 | Verdict + hard facts (SBA closed, moratorium, PIC, fees, economics) | ✅ | §0 |
| 2 | Build-vs-buy decision matrix (26 capabilities) + summary | ✅ | §2 |
| 3 | Phased delivery plan P0–P7 with acceptance criteria, DoD, and go/no-go gates per phase | ✅ | §3 |
| 4 | Team and vendor map (RACI, hiring sequence, separation of business/practice) | ✅ | §4 |
| 5 | KPIs, PMS dashboard spec, 20-event tracking | ✅ | §5 |
| 6 | Risk register (R1–R14) + black swans + dependencies + waiting posture | ✅ | §6 |
| 7 | Traceability matrix (phases → PRD sections/requirements/milestones; epics, backlog, stories) | ✅ | §7 |
| 8 | Explicitly NOT built (PRD §20 + skill adaptations) | ✅ | §8 |
| 9 | Assumptions register (A1–A12) | ✅ | §9 |
| 10 | Carried-forward open items: 12 owner inputs, 10 attorney questions, 23 unverified items, gaps G1–G12 | ✅ | §10 |
| 11 | Numbers reconciliation checklist | ✅ | §11 |

**IMPLEMENTATION PLAN COMPLETE — READY FOR THE OWNER, ATTORNEY, AND CPA TO EXECUTE PHASE P0.**

*End of PRD2Pro. Research date: 9 November 2026. Prepared for a U.S. Green Card holder (Lawful Permanent Resident) as prospective owner/operator; Bhupesh Chandra Dimri asked on the owner's behalf. No owner name, capital amount, credit score, or preferred neighbourhood was supplied, and none is assumed anywhere in this document. Nothing has been submitted to any agency, no one has been contacted, and no money has been spent.*
