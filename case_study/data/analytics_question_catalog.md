# Insurance Analytics Question Catalog

Comprehensive, domain-aligned question set for exercising the Fabric Data Agent and downstream Foundry orchestration. Organized by analytical theme. Use these to test retrieval, aggregation, reasoning, rule alignment, anomaly detection, and multi-agent collaboration.

---
## 1. Portfolio Composition & Mix
- What is the distribution of active policies by risk rating for calendar year 2024, and how did Q4 2024 compare to Q3 2024?
- What percentage of total coverage (sum of coverage_amount) is concentrated in the top 10% largest policies?
- How does policy count and total coverage differ by region?
- What is the share of policies in each policy_status (Active, Lapsed, Terminated, Suspended)?
- Which 5 application channels account for the majority of in-force premiums?
- What is the average coverage and premium by product_type (if present) or risk_rating?
- What portion of total 2024 premium revenue is contributed by aviation policies vs the rest of the portfolio (and specifically in Q4 2024)?

## 2. Policy Lifecycle & Retention
- What is the lapse rate in calendar year 2024 by region, and (if 2023 data exists) how does it compare to 2023; otherwise note unavailability of prior-year comparison.
- What are termination reasons (if encoded) or inferred patterns near termination vs lapsed policies?
- Are policies issued in the last 90 days of 2024 (Oct–Dec 2024) exhibiting above-average lapse tendencies vs earlier 2024 issuances?
- What is the average time-in-force for terminated vs lapsed policies?

## 3. Risk Segmentation & Pricing Alignment
- Are premiums generally monotonic with risk_rating (A through E)? Identify any inversions.
- Which policies have a premium_to_coverage_ratio above 2× the median for their risk band?
- How does average coverage differ between adjacent risk bands (A vs B, B vs C, etc.)?
- Are there clusters of high coverage with low risk ratings suggesting potential underpricing?

## 4. Coverage Adequacy & Financial Suitability
- For each policy, is coverage within appropriate income multiple guidelines (by age bracket)?
- What percent of policies breach upper income multiple thresholds?
- Are there demographics (e.g., occupation class) where coverage adequacy is systematically low?
- Which policies are borderline (±5%) around income adequacy thresholds and may need review?

## 5. Channel & Distribution Performance
- How does average premium differ by application_channel?
- Which channel has the highest lapse rate adjusted for policy age?
- Are current channel shares deviating >5 percentage points from target distribution?
- What is conversion (issued vs submitted if available) by channel?

## 6. Underwriter & Agent Productivity
- Which underwriters had the highest total coverage issued in Q4 2024 and how does that differ from Q3 2024?
- Are any underwriters producing unusually high concentrations of a single risk_rating?
- Which agents have above-average lapse rates among their issued policies?
- What is the median premium per policy per agent vs portfolio median?

## 7. Claims Performance & Severity
- What is the 2024 claim approval vs denial vs pending rate overall and by underlying policy risk_rating?
- What is average claim amount (if available) by cause_of_death or claim category?
- Are denial rates trending upward month-over-month within 2024 (show Jan–Dec 2024 series)?
- What is the 2024 time-to-approval distribution and are there outliers (p95 / p99) by quarter?
- Do repeat claims (if identifiable) cluster around certain risk bands?

## 8. Aviation Segment Deep Dive
- How does the aviation claim approval rate for full-year 2024 compare to the non-aviation portfolio, and specifically in Q4 2024?
- What are the top causes of aviation claims and their respective approval ratios?
- Are aviation premiums aligned with elevated risk ratings (B–E subset)?
- Are aviation policies over-represented in Q4 2024 terminations vs their share of in-force policies at the start of Q4 2024?
- Is there a seasonal pattern in 2024 aviation claim frequency (quarterly or monthly variation)?

## 9. Compliance & Guideline Adherence
- Which policies breach occupation class multiplier expectations (if baseline defined)?
- Are any underwriting decisions inconsistent with the risk assessment matrix weightings?
- What percent of claims decisions diverge from guideline-expected approval bands?
- Are suspended policies concentrated in specific regions or channels beyond expectation?

## 10. Anomaly & Outlier Detection
- Which policies have z-score > 3 for annual_premium within their risk band?
- Are there clusters of unusually low premiums for high-risk ratings (D/E)?
- Which channels show any week-over-week volume spikes during 2024 exceeding +25% vs the prior week?
- Are any 2024 monthly approval rates outside 2 standard deviations of the 2024 monthly mean?
- Which underwriters exhibit statistically significant deviation from portfolio average denial rate?

## 11. Trend & Time-Series Analysis
- How has monthly new policy issuance trended over calendar year 2024 (Jan–Dec 2024)?
- What is the rolling 3-month lapse rate within 2024 (e.g., Oct–Dec vs Jul–Sep 2024)?
- Are average premiums rising or falling across 2024 (compare Q1 vs Q4 2024 and intra-year slope)?
- Is claim severity (average payout) trending upward across 2024 months and quarters?

## 12. Cross-Dataset Linkage
- What is the claim frequency per 1,000 policies by risk band?
- Do policies that later lapse in 2024 show early (first 90 days) claim activity at a different rate than those remaining active through Dec 31 2024?
- Are higher coverage tiers correlated with slower claim resolution time?
- Does channel of acquisition correlate with claim denial probability?

## 13. Data Quality & Integrity
- Are there missing or null fields in critical columns (coverage_amount, annual_premium, risk_rating)?
- Any duplicate policy_id or claim_id values?
- Are there invalid risk ratings outside expected domain (A–E)?
- Are premiums or coverage amounts negative or implausibly high outside business rules?
- Are there policies with policy_issue_date in the future?

## 14. Scenario / What-If & Stress Testing
- What is the projected 2025 premium impact (using 2024 baseline data) if the 2024 lapse rate increases by 2 percentage points?
- How would a modeled 10% reduction in 2024 high-risk (D/E) new issuance have affected expected 2024 claim payouts (counterfactual)?
- What is the sensitivity of total 2024 coverage to a hypothetical +5pp shift toward the online channel (holding conversion constant)?
- If aviation policy count doubled relative to 2024 levels, what would the modeled approval rate impact be assuming 2024 claim severity distributions?

## 15. Multi-Agent Collaboration Prompts
- Medical Risk Agent: Which risk bands show health-profile inconsistencies vs guidelines?
- Financial Suitability Agent: Which top 5 cases require income multiple recalibration?
- Compliance Agent: List policies violating two or more guideline dimensions simultaneously.
- Senior Underwriter: Provide a prioritized queue of borderline suitability cases.
- Cross-Agent Synthesis: Summarize disagreements between agents on the last 20 reviewed policies.

## 16. Executive Summary Generators
- Provide an executive snapshot: top 5 KPIs, anomalies, and recommended actions.
- Summarize 2024 quarter-over-quarter claim volume trend and risk distribution shift (Q1→Q4 2024).
- Give a 2024 board-level briefing: retention metrics, risk mix drift across quarters, and compliance exceptions count.

## 17. Enrichment & Next Data Steps
- Which additional fields (e.g., customer tenure, policy rider details) would most reduce uncertainty in pricing fairness?
- What external data could improve aviation risk stratification?
- Which data quality issues most erode confidence in current lapse analysis?

---
## Recommended Metric Definitions (Reference)
- lapse_rate = lapsed_policies / active_policies_start_period
- claim_approval_rate = approved_claims / total_claims
- premium_to_coverage_ratio = annual_premium / coverage_amount
- channel_share = channel_policy_count / total_policies

## Suggested Anomaly Thresholds
- Channel share drift: >5 percentage points vs target
- Denial rate anomaly: >2 percentage points vs guideline expectation or >2 SD from mean
- Premium outlier: z-score > 3 within risk band

---
## Top 10 Diverse Test Questions
Use these (temporal scope explicit for 2024 data coverage) for a holistic agent capability evaluation:
1. Portfolio Mix: What is the distribution of active policies and total coverage by risk rating in 2024, and how did Q4 2024 differ from Q3 2024?
2. Pricing Alignment: Are 2024 premiums monotonic with risk rating; list any inversions with supporting 2024 examples.
3. Coverage Adequacy: Which 2024 policies exceed recommended income multiple thresholds by >10% (flag borderline ±5%)?
4. Channel Performance: Which application channels show the highest lapse-adjusted premium loss in the second half of 2024 (Jul–Dec) vs first half (Jan–Jun)?
5. Claims Quality: How does the aviation claim approval rate in full-year 2024 compare to non-aviation (and specifically in Q4 2024)?
6. Compliance: Identify 2024 policies simultaneously breaching occupation class multiplier rules and income adequacy guidelines.
7. Anomaly Detection: Which underwriters have 2024 denial rates statistically different (p<0.05) from the 2024 portfolio average?
8. Trend Analysis: Is average claim amount trending upward across 2024; report Q1 vs Q4 change and rolling 3-month Oct–Dec vs Jul–Sep.
9. Cross-Linkage: In 2024, does acquisition channel correlate with claim denial probability after controlling for risk rating (include effect size)?
10. Data Quality & Impact: Which 2024 data quality issues (missing / invalid values) most impact confidence in lapse rate calculations; quantify affected records and % of total.

---
## Usage Notes
- Pair questions 1–4 for baseline posture; 5–7 for risk & compliance depth; 8–10 for operational resilience and data integrity.
- For each question, log query plan, data sources, and calculation steps for auditability.

---
Generated: (auto) Comprehensive question catalog for Fabric Data Agent & Foundry orchestration.
