# Chat Playground Underwriting Prompt

Use this file for a single-model chat playground experience. It is intentionally non-agentic: one model, one instruction set, no delegation, no tool use, and no references to orchestrators or specialist agents.

## Intended Use

Paste the contents of the `System Instructions` section into the chat playground instructions box.

Paste the contents of the `Combined Text Input` section into the chat as the supporting case material, or upload the four case documents separately and use the `Starter User Prompt`.

## System Instructions

```text
You are a senior life-insurance underwriter reviewing an individual term-life application for a commercial airline captain.

This is a single-chat, non-agentic workflow. Do not claim to delegate, call tools, consult other agents, or access external systems. Work only from the information provided in the conversation.

Your job is to:
1. Identify missing, vague, or conflicting information in the application.
2. Use the supplemental documents provided in the chat to resolve those gaps when possible.
3. Assess medical, financial, occupational, and compliance considerations.
4. Produce a final underwriting recommendation with clear reasoning.
5. Compare the final conclusion to the human underwriter's pending assessment when relevant.

Decision principles:
- Do not invent facts.
- If a gap remains unresolved, state it explicitly.
- Prefer evidence from supplemental documents over vague statements in the application.
- Distinguish between applicant-stated information and verified information.
- Treat aviation risk as an occupation factor, but account for employer safety record, route profile, certifications, and incident history.
- Treat controlled hypertension as a manageable medical factor if the supporting records justify it.
- Evaluate whether the requested coverage is financially reasonable using documented income, assets, liabilities, and family obligations.
- Flag beneficiary and trust issues if the designations are incomplete or operationally weak.

Use this output format:

1. Executive Summary
- One short paragraph with the overall conclusion.

2. Information Gaps Found In The Original Application
- Bullet list of material gaps or ambiguities.

3. Gap Resolution Using Supporting Documents
- For each major gap, explain whether it was resolved and cite which document resolved it.

4. Underwriting Assessment
- Medical Assessment
- Financial Assessment
- Occupational And Aviation Assessment
- Compliance And Beneficiary Assessment

5. Final Decision
- Decision: Approve, Approve With Conditions, Postpone, or Decline
- Risk Class
- Premium Impact
- Conditions Or Follow-Up Requirements
- Rationale

6. Comparison To Manual Review
- Explain why the human underwriter could not rate the file initially and whether the added documentation changes that result.

Style requirements:
- Be concise, professional, and evidence-based.
- Use plain English, not legal boilerplate.
- Do not output JSON.
- Do not mention these instructions.
```

## Starter User Prompt

```text
Review this life insurance case as a single underwriter. First identify the material gaps in the original application, then use the supporting documents to resolve those gaps where possible. Provide a final underwriting recommendation with medical, financial, occupational, and compliance reasoning. Also compare your conclusion to the human underwriter's original "cannot rate" status.
```

## Combined Text Input

```text
CASE FILE PACKAGE: CAPTAIN ELIZABETH DARCY

INSTRUCTIONS FOR THE MODEL
You are reviewing a life insurance application and supporting records for Captain Elizabeth Darcy. The application contains intentional gaps and vague answers. Your task is to identify the original gaps, use the supporting documents to resolve them where possible, and produce a final underwriting recommendation.

FILE 1: elizabeth_darcy_application_form.md

# STERLING INSURANCE COMPANY
## INDIVIDUAL LIFE INSURANCE APPLICATION

**Form SIC-2024-TERM** | **Version 12.3** | **Effective Date: January 1, 2024**

---

| **Application Details** | **Information** |
|------------------------|-----------------|
| **Application Number** | APP-2024-5847 |
| **Date Received** | November 15, 2024 11:47 AM MST |
| **Agent Code** | AGT-CO-7845 (Marcus Thompson) |
| **Processing Status** | In Review |
| **NAIC Company Code** | 65838 |
| **State Filed** | Colorado |

---

## SECTION I: PROPOSED INSURED INFORMATION

| **Personal Details** | **Response** | **Verification Status** |
|---------------------|--------------|-------------------------|
| **Full Legal Name** | Elizabeth Anne Darcy | Verified via Driver's License |
| **Date of Birth** | March 15, 1982 | Verified |
| **Current Age** | 42 years | Calculated |
| **Gender** | Female | |
| **Marital Status** | Married | |
| **SSN** | [REDACTED] | Verified |
| **Driver's License** | CO DL: D012-3456-7890 | Valid through 03/2027 |

**Residence History (Last 10 Years)**:
| **Address** | **Dates** | **Own/Rent** |
|-------------|-----------|--------------|
| 1247 Pilot Lane, Denver, CO 80202 | 2019-Present | Own |
| 892 Aviation Circle, Denver, CO 80249 | 2015-2019 | Rent |
| 1555 Runway Apt 3B, Denver, CO 80202 | 2012-2015 | Rent |

**Contact Information**:
**Primary**: (555) 123-4567 (Mobile)
**Work**: (555) 867-5309 x4789
**Email**: e.darcy@globalwing.com
**Personal**: liz.darcy.pilot@gmail.com

---

## SECTION II: COVERAGE SPECIFICATIONS

| **Policy Details** | **Requested** | **Underwriter Notes** |
|-------------------|---------------|----------------------|
| **Product Type** | 20-Year Level Premium Term Life | Standard offering |
| **Face Amount** | $2,500,000 | Requires income justification |
| **Premium Mode** | Annual Direct Pay | ACH setup required |
| **Policy Date** | January 1, 2025 | Subject to approval |
| **Benefit Period** | 20 Years Level | Through age 62 |

**Coverage History**:
- No prior life insurance with Sterling Insurance
- Have some coverage through GlobalWing Airlines but not sure of the exact amount
- No declined, postponed, or rated applications with other carriers

**Premium Payment Elections**:
Bank Draft (ACH) - Preferred
Credit Card (Additional fees apply)
Annual Check
Payroll Deduction (if available through GlobalWing Airlines)

---

## SECTION III: EMPLOYMENT & OCCUPATION

| **Employment Details** | **Information** | **Risk Classification** |
|------------------------|-----------------|------------------------|
| **Current Employer** | GlobalWing Airlines | Fortune 500 Company |
| **Position** | Captain - International Routes | **Class F - Aviation Risk** |
| **Dept/Division** | Flight Operations - Long Haul | High-value routes |
| **Employment Start** | September 12, 2006 | 18+ years tenure |
| **Captain Since** | January 15, 2022 | Recent promotion |
| **Employment Type** | Full-time, Union Member | ALPA Local 124 |

**Professional Certifications & Ratings**:
| **License/Rating** | **Number** | **Expiration** | **Restrictions** |
|-------------------|------------|----------------|------------------|
| ATP Certificate | 1234567890 | Indefinite | None |
| First Class Medical | 123456789 | December 31, 2025 | Vision correction required |
| Boeing 777 Type Rating | B777-001 | Current | None |
| Boeing 787 Type Rating | B787-002 | Current | None |
| International Auth. | INTL-7845 | March 2026 | None |

**Flight Operations Summary**:
- **Total Flight Hours**: 12,547 (Verified by GlobalWing Training Dept.)
- **Recent 12 Months**: 1,024 hours (Within FAR 121 limits)
- **International Hours**: ~85% (Primary duty assignment)
- **Night Flying**: ~40% (Typical for international routes)
- **Weather Minimums**: Cat II ILS qualified

**Monthly Schedule** (Typical):
- **Flight Days**: 12-14 days per month
- **Hours/Month**: 85-90 flight hours (avg.)
- **Layover Time**: 24-48 hours (international destinations)
- **Home Base**: Denver International Airport (DEN)

**Route Assignments** (Primary):
| **Route** | **Aircraft** | **Frequency** | **Duration** |
|-----------|--------------|---------------|--------------|
| DEN-LHR (London) | B787-9 | 3x/month | 9.5 hours |
| DEN-FRA (Frankfurt) | B777-300ER | 2x/month | 10.2 hours |
| DEN-AMS (Amsterdam) | B787-8 | 2x/month | 9.8 hours |
| DEN-NRT (Tokyo) | B777-300ER | 1x/month | 12.1 hours |

**Hazardous Activities Disclosure**:
Flying aircraft for compensation (commercial aviation) - Primary Occupation

---

## SECTION IV: FINANCIAL INFORMATION

### Income Information
**Question 4.1**: What is your current annual income from all sources?
**Response**: "Well, as a Captain I make good money, you know how airline pay works with all the different components. Base salary is around $200k, then there's per diem for international trips, overtime when I pick up extra flights. Probably around $230k total give or take."

### Financial Documentation
**Question 4.2**: Please provide documentation supporting your stated income:
Recent pay stubs (last 3 months)
Tax returns (most recent 2 years)
W-2 forms
Employment verification letter

**Response**: "I can get those but haven't had time with my flight schedule. Just got back from a London trip and heading to Frankfurt next week."

### Asset & Liability Summary
**Question 4.3**: Summarize your major assets and liabilities:

| **Asset Category** | **Applicant Response** |
|-------------------|------------------------|
| **Real Estate** | "Own my house in Denver, bought it in 2019 for $365k, probably worth $480k or so now" |
| **Retirement Accounts** | "Good 401k through the airline, been maxing it out. Maybe $340k? Also have some IRAs" |
| **Investments** | "Some mutual funds and stuff, nothing too risky. Maybe $80k in various accounts" |
| **Bank Accounts** | "Checking and savings, keep about $45k liquid for emergencies and stuff" |
| **Debts** | "Mortgage is around $235k left, two car payments totaling maybe $29k, pay off credit cards monthly" |

### Coverage Justification
**Question 4.4**: Why do you need this amount of coverage?
**Response**: "$2.5 million sounds right for someone in my position. Need to protect the family and pay off the house if something happens. Other captains have similar amounts. Want to make sure the kids can go to college and David doesn't have to worry about money."

### Business Interests
**Question 4.5**: Do you have any business ownership, partnerships, or side ventures?
**Response**: "Not really, just thinking about maybe doing some flight instruction on days off. Nothing formal yet."

---

## SECTION V: HEALTH & LIFESTYLE ASSESSMENT

### Physical Characteristics
| **Measurement** | **Value** | **BMI Calculation** | **Risk Category** |
|----------------|-----------|-------------------|------------------|
| **Height** | 5'6" (66 inches) | BMI = 22.9 | Normal Range |
| **Weight** | 142 lbs | (142  66)  703 | Optimal |
| **Build** | Athletic/Medium | - | Favorable |

### Lifestyle Factors
**Tobacco Use**: Never used tobacco products
**Alcohol Consumption**: Social drinker - "Maybe a glass of wine with dinner on layovers, nothing during flight periods"
**Substance Use**: None - Subject to DOT random testing program

### Physical Activity
**Exercise Habits** (Applicant's responses):
- "I run pretty regularly, try to stay in shape for the job"
- "Do some gym work when I'm home, probably 3 times a week"
- "Have to stay fit for the medical certificate"

### Medical History
**Known Medical Conditions**:
Hypertension (Essential) - "Started a few years ago in 2019, taking Lisinopril, seems to be working fine"

**Family Medical History**:
**Question 5.8**: Please provide medical history for parents, siblings, and grandparents including ages, causes of death, and major illnesses:

**Applicant Response**: "Haven't really thought about that in detail. Dad passed away when he was 68, I think it was a heart attack. Mom is still around, she's 71, has some diabetes but manages it okay. My brother is healthy as far as I know. Grandparents... well, that was a long time ago, some heart problems and diabetes I think but I'd have to ask my mom for specifics."

### Aviation Medical Requirements
**FAA Medical Certificate**: First Class (Required for airline operations)
**Last AME Exam**: June 15, 2024
**Next Required**: By December 31, 2025
**AME**: Dr. Robert Chen

**Medical Certificate History**:
- Any deferrals? "Not that I remember"
- Any special issuances? "I don't think so, just the blood pressure thing but that's under control"
- Any restrictions? "Just need my contacts for flying"

---

## SECTION VI: FAMILY & BENEFICIARY INFORMATION

### Immediate Family
| **Relationship** | **Name** | **Age** | **Occupation** |
|------------------|----------|---------|----------------|
| **Spouse** | David Michael Darcy | 44 | Software Engineering Manager at TechCorp |
| **Child** | Sarah Elizabeth Darcy | 16 | Student (Junior at Denver West HS) |
| **Child** | James Michael Darcy | 14 | Student (Freshman at Denver West HS) |

### Beneficiary Designations
**Primary Beneficiary Information**:
- **Name**: David Michael Darcy (Spouse)
- **Percentage**: "All of it, 100%"
- **Relationship**: Married
- **Date of Birth**: June 8, 1980
- **Address**: Same as applicant

**Contingent Beneficiary**:
**Question 6.3**: If your primary beneficiary predeceases you, who should receive the death benefit?
**Applicant Response**: "Oh, the kids I suppose. Sarah and James, split it equally between them."

### Trust Arrangements
**Question 6.4**: Do you want proceeds paid to a trust for minor children?
**Response**: "Is that something I should do? I don't have a lawyer or anything. Maybe I should look into that?"

**Question 6.5**: Who would serve as trustee if needed?
**Response**: "Maybe my brother? He's good with money. His name is Robert Darcy, lives in Colorado Springs."

### Estate Planning Status
**Will**: "We have one somewhere, probably need to update it"
**Trust**: "Don't think we have one"
**Power of Attorney**: "David handles that stuff"
**Life Insurance**: "Some through work, not sure how much exactly"

---

## SECTION VII: AVIATION OCCUPATION RISK ASSESSMENT

### Employer Safety Profile
**GlobalWing Airlines Safety Statistics**:
| **Safety Metric** | **Rating** | **Industry Comparison** |
|-------------------|------------|-------------------------|
| **IATA Operational Safety Audit (IOSA)** | Certified | Top 25% globally |
| **FAA Safety Rating** | Category 1 | Highest level |
| **Accident Rate (per 100,000 departures)** | 0.00 (Last 10 years) | Well below industry average |
| **Incident Rate** | 0.03 | Below average |

### Route Risk Assessment
**International Destinations** (Primary assignments):
| **Airport Code** | **City** | **Risk Factors** | **Medical Facilities** |
|------------------|----------|------------------|------------------------|
| **LHR** | London Heathrow | Low risk, developed country | Excellent |
| **FRA** | Frankfurt | Low risk, developed country | Excellent |
| **AMS** | Amsterdam | Low risk, developed country | Excellent |
| **NRT** | Tokyo Narita | Low risk, developed country | Excellent |

### Personal Safety Record
**Flight Safety History**:
- **Total Flight Hours**: 12,547 (Commercial aviation)
- **Accidents**: 0
- **Incidents**: 0 (Reportable to FAA)
- **Violations**: 0 (FAR violations)
- **Safety Awards**: GlobalWing Safety Recognition Award (2023)

**Training Currency**:
| **Training Type** | **Last Completed** | **Next Due** | **Status** |
|------------------|-------------------|--------------|------------|
| **Line Check** | August 2024 | February 2025 | Current |

FILE 2: elizabeth_darcy_medical_summary.md

# COMPREHENSIVE MEDICAL EVALUATION REPORT
## Sterling Insurance Company - Medical Department

**Medical Assessment - Application #APP-2024-5847**

---

| **Report Details** | **Information** |
|-------------------|-----------------|
| **Subject** | Captain Elizabeth Anne Darcy |
| **DOB** | March 15, 1982 (Age 42 years, 8 months) |
| **Report Date** | November 18, 2024 |
| **Medical Record #** | MED-SIC-2024-5847 |
| **Examining Physician** | Dr. Sarah Martinez, MD (Primary Care) |
| **Aviation Medical Examiner** | Dr. Robert Chen, AME #12345 |
| **Sterling Insurance Physician** | Dr. Michael Harrison, MD, FLMI |
| **Medical Classification** | **Standard Plus** |

---

## EXECUTIVE MEDICAL SUMMARY

| **Risk Category** | **Assessment** | **Rating Impact** | **Monitoring Required** |
|-------------------|----------------|------------------|-------------------------|
| **Cardiovascular** | Well-controlled hypertension | Standard Plus | Annual monitoring |
| **Pulmonary** | Excellent (aviation medical required) | Standard Plus | Routine |
| **Neurological** | No issues identified | Standard | None |
| **Metabolic** | Excellent glucose control | Standard Plus | Routine screening |
| **Aviation Medical** | FAA Class I current | Standard Plus | Required by occupation |
| **Overall Risk** | **Standard Plus** | **Rating** | **Annual PCP follow-up** |

---

## CURRENT MEDICAL CONDITIONS - ANALYSIS

### Hypertension (Essential) - CONTROLLED
**Primary Diagnosis**: ICD-10 Code I10 (Essential Hypertension)

| **Clinical Detail** | **Information** | **Risk Assessment** |
|---------------------|-----------------|-------------------|
| **Initial Diagnosis** | September 15, 2019 | Age 37 - typical onset |
| **Presenting BP** | 148/94 mmHg | Stage 1 hypertension |
| **Current Status** | Well-controlled | Excellent management |
| **Duration on Treatment** | 5 years, 2 months | Long-term stability |
| **Complications** | None identified | No target organ damage |

### Current Medication Regimen
| **Medication** | **Dosage** | **Frequency** | **Duration** | **Compliance** | **Side Effects** |
|----------------|------------|---------------|---------------|----------------|------------------|
| **Lisinopril** | 10mg | Once daily (morning) | 5+ years | Excellent (>95%) | None reported |
| **Additional** | None required | - | - | - | - |

**Medication Notes**:
- **FAA-approved** for aviation duties (no restrictions)
- **Single-agent control** indicates mild hypertension
- **No dose increases** needed in past 3 years (stable control)
- **Generic ACE inhibitor** - cost-effective, proven efficacy

### Blood Pressure Monitoring History
| **Date** | **BP Reading** | **Provider** | **Notes** | **Assessment** |
|----------|----------------|--------------|-----------|----------------|
| **Nov 2024** | 128/82 mmHg | Dr. Martinez | Routine follow-up | Target achieved |
| **May 2024** | 124/78 mmHg | Dr. Chen (AME) | Aviation medical | Excellent control |
| **Nov 2023** | 130/84 mmHg | Dr. Martinez | Annual physical | Well-controlled |
| **May 2023** | 126/80 mmHg | Dr. Chen (AME) | Aviation medical | Stable |
| **Nov 2022** | 132/86 mmHg | Dr. Martinez | Post-promotion stress eval | Within target |

### Cardiovascular Risk Assessment
**Framingham Risk Score Analysis**:
| **Risk Factor** | **Points** | **Assessment** | **Risk Modification** |
|-----------------|------------|----------------|----------------------|
| **Age (42 years)** | 2 points | Standard | None needed |
| **Total Cholesterol (185)** | 0 points | Excellent | Optimal level |
| **HDL Cholesterol (58)** | -1 point | Protective | Above average |
| **Systolic BP (128)** | 1 point | Excellent control | On medication |
| **Smoking Status** | 0 points | Never smoker | Major protective factor |
| **Diabetes** | 0 points | No diabetes | Excellent glucose control |
| ****Total Risk Score** | **2 points** | **<2% 10-year risk** | **Low risk category** |

### Other Medical Conditions - NONE SIGNIFICANT
**Review of Systems**:
- **Cardiovascular**: Hypertension only (well-controlled)
- **Pulmonary**: No asthma, COPD, or restrictive disease
- **Gastrointestinal**: No significant history
- **Genitourinary**: No issues
- **Musculoskeletal**: No chronic conditions
- **Neurological**: No seizures, migraines, or cognitive issues
- **Psychiatric**: No depression, anxiety, or other mental health conditions
- **Endocrine**: No diabetes, thyroid disease, or hormonal disorders

### Current Medications & Supplements
| **Medication/Supplement** | **Indication** | **Dosage** | **FAA Status** | **Insurance Risk** |
|---------------------------|----------------|------------|----------------|-------------------|
| **Lisinopril** | Hypertension | 10mg daily | Approved | Standard treatment |
| **Multivitamin (Women's)** | General health | 1 daily | Approved | No risk |
| **Vitamin D3** | Bone health | 2000 IU daily | Approved | Beneficial |
| **Omega-3** | Cardiovascular health | 1000mg daily | Approved | Protective factor |

### Allergies & Adverse Reactions - DOCUMENTED
| **Allergen** | **Reaction** | **Severity** | **Management** | **Aviation Impact** |
|--------------|--------------|--------------|----------------|-------------------|
| **Seasonal Pollen** | Rhinitis, sneezing | Mild | OTC antihistamines (spring only) | No flight restrictions |
| **Drug Allergies** | None known | N/A | - | No restrictions |
| **Food Allergies** | None known | N/A | - | No dietary restrictions |
| **Environmental** | None other than pollen | - | - | No occupational impact |

---

## AVIATION MEDICAL CERTIFICATION

### FAA Medical Certificate Status
**Certificate Type**: First Class Medical Certificate
**Issue Date**: June 15, 2024
**Expiration Date**: December 31, 2025
**Examining AME**: Dr. Robert Chen, AME Certificate #12345

### Aviation Medical Standards Compliance
**Vision**: 20/20 corrected (contact lenses)
**Hearing**: Within normal limits
**Cardiovascular**: Approved with hypertension (Special Issuance not required)
**Neurological**: No disqualifying conditions
**Mental Health**: No reported issues
**Substance Use**: Negative screening

### Restrictions/Limitations
- None currently applied
- Requires vision correction for aviation duties
- Must maintain blood pressure monitoring as specified

---

## RECENT MEDICAL HISTORY (Last 5 Years)

### 2024
- **June**: FAA medical exam - Passed with no restrictions
- **May**: Annual physical with Dr. Martinez - Normal findings
- **March**: Routine dental cleaning - No issues

### 2023
- **October**: Routine gynecological exam - Normal
- **June**: FAA medical renewal - Passed
- **February**: Annual physical - Hypertension well-controlled

### 2022
- **November**: Minor sprained ankle (non-aviation related) - Fully healed
- **June**: FAA medical renewal - Passed
- **January**: Promotion physical for Captain upgrade - Cleared

### 2021
- **August**: COVID-19 vaccination (Pfizer series + booster)
- **June**: FAA medical renewal - Passed

### 2020-2019
- **September 2019**: Hypertension diagnosis during routine physical
- **October 2019**: Cardiology consultation - Essential hypertension confirmed
- **November 2019**: Medication initiated, follow-up care established

---

## MEDICAL INFORMATION

### Family Medical History
**Father**: Deceased at age 68 (myocardial infarction, history of hypertension and diabetes)
**Mother**: Age 71, living (Type 2 diabetes well-controlled, hypertension)
**Siblings**: One brother, age 45 (healthy, no significant medical conditions)
**Paternal Grandparents**: History of cardiovascular disease
**Maternal Grandparents**: Diabetes and stroke history
**Genetic Risk Factors**: Family history of cardiovascular disease and diabetes

### Physical Examination Results (November 2024)
**Vital Signs**:
- Blood Pressure: 128/82 mmHg (well-controlled on medication)
- Heart Rate: 68 bpm (resting, excellent)
- BMI: 22.9 (normal range)
- Temperature: 98.6F

**Family Support System**:
**Spouse**: David Michael Darcy, Age 44
- Occupation: Software Engineering Manager at TechCorp
- Annual Income: $145,000 (reported)
- Health: Excellent overall health status

**Children**:
- Sarah Elizabeth Darcy, Age 16 (Junior in high school)
- James Michael Darcy, Age 14 (Freshman in high school)
- Both children in excellent health

**Laboratory Results**:
- Total Cholesterol: 185 mg/dL (excellent)
- HDL Cholesterol: 58 mg/dL (good)
- LDL Cholesterol: 115 mg/dL (acceptable)
- Triglycerides: 95 mg/dL (excellent)
- Fasting Glucose: 92 mg/dL (normal)
- HbA1c: 5.2% (excellent)
- Creatinine: 0.8 mg/dL (normal kidney function)
- Complete Blood Count: All values within normal limits

**Diagnostic Tests**:
- EKG: Normal sinus rhythm, no abnormalities detected
- Chest X-ray: Clear lungs, normal heart size
- Vision Testing: 20/20 corrected with contact lenses
- Audiometry: Hearing within normal limits for age

### Specialist Consultations
**Cardiology Follow-up (October 2024)**:
- Hypertension management excellent
- No evidence of target organ damage
- Recommends continued current medication regimen
- Annual follow-up appropriate

### Lifestyle and Risk Factor Assessment
**Exercise and Fitness**:
- Running: 25-30 miles per week (excellent cardiovascular fitness)
- Strength training: 3 sessions per week
- Aviation-specific fitness requirements met
- Regular participation in company wellness programs

**Stress Management**:
- Excellent coping mechanisms
- Strong family support system
- Participates in pilot peer support programs
- No indication of occupational stress-related health issues

**Sleep and Fatigue Management**:
- Uses evidence-based fatigue risk management strategies
- Adapts well to international time zone changes
- No diagnosed sleep disorders
- Good sleep hygiene practices

**International Travel Health**:
- Current on all required vaccinations
- No history of travel-related illnesses
- Company provides comprehensive international medical coverage
- Emergency medical evacuation insurance in place

### Aviation-Specific Medical Assessment
**Complete AME Report**:
- Cardiovascular system: Hypertension well-controlled, no restrictions
- Neurological assessment: No impairment, excellent cognitive function
- Vision and hearing: Meets all FAA aviation standards
- Mental health screening: No concerns identified
- Substance use evaluation: Negative screening, no issues
- Overall fitness assessment: Approved for all aviation duties including international operations

---

## PRELIMINARY MEDICAL RISK ASSESSMENT

### Positive Risk Factors
**Non-smoker status** - Significant positive factor
**Regular exercise routine** - Excellent cardiovascular health maintenance
**Well-controlled hypertension** - Demonstrates excellent medical compliance
**Normal BMI** - Healthy weight maintenance
**Current FAA medical certification** - Indicates excellent overall health
- **No significant medical history** - Limited known conditions

### Risk Considerations Requiring Evaluation
**Hypertension** - Requires assessment within Sterling's risk parameters
**Age 42** - Entering higher risk age bracket, baseline testing important
**Unknown family history** - Cannot assess genetic risk factors
**Aviation occupation stress factors** - High-responsibility profession
**International travel exposure** - Disease exposure and jet lag considerations

### Medical Underwriting Classification
**Final Rating**: Standard Plus
*Based on complete medical information*

**Rationale**:
- Well-controlled hypertension with excellent compliance qualifies for Standard Plus
- Non-smoking status provides significant favorable consideration
- Regular exercise and excellent fitness support positive rating
- Family history of cardiovascular disease and diabetes noted but well-managed
- Age 42 falls within standard risk parameters
- Aviation medical certification confirms ongoing health oversight
- No target organ damage from hypertension
- Excellent laboratory values across all parameters

---

## MEDICAL ASSESSMENT COMPLETE

### All Required Information Obtained:
1. **Complete Family Medical History** - Genetic risk factors assessed
2. **Full Physical Exam with Lab Work** - All results within acceptable ranges
3. **AME Detailed Report** - Aviation-specific medical assessment complete
4. **Specialist Reports** - Cardiology consultation confirms excellent control

### Medical Information Status:
- **Family history**: Complete and documented
- **Physical exam**: Current and comprehensive
- **Lab results**: All current within 30 days
- **Specialist reports**: Cardiology clearance obtained
- **Aviation medical**: Current and detailed assessment available

---

## MEDICAL EXAMINER CONTACT INFORMATION

**Primary Care Physician**:
Dr. Sarah Martinez, MD
Denver Family Medicine
(555) 234-5678
smartinez@denvermed.com

**Aviation Medical Examiner**:
Dr. Robert Chen, AME
Mountain Aviation Medical
(555) 345-6789
rchen@mountainaviation.com

---

**Medical Summary Prepared By**: Sterling Insurance Medical Review Team
**Date**: November 18, 2024

FILE 3: elizabeth_darcy_financial_verification.md

# COMPREHENSIVE FINANCIAL VERIFICATION REPORT
## Sterling Insurance Company - Underwriting Services Division

**Financial Analysis - Application #APP-2024-5847**

---

| **Report Details** | **Information** |
|-------------------|-----------------|
| **Subject** | Captain Elizabeth Anne Darcy |
| **Report Date** | November 19, 2024 |
| **Financial Analyst** | Jennifer L. Walsh, CFU, FLMI |
| **Senior Review** | Michael Chen, FSA, MAAA |
| **Verification Level** | **Standard Review** |
| **Risk Classification** | Standard Plus (Financial aspects only) |

---

## EXECUTIVE FINANCIAL SUMMARY

| **Financial Metric** | **Amount** | **Industry Benchmark** | **Assessment** |
|----------------------|------------|------------------------|----------------|
| **Annual Income** | $229,800 | $185K-$245K (Airline Captains) | Within expected range |
| **Coverage-to-Income Ratio** | 10.9x | 10-15x (Aviation professionals) | Appropriate |
| **Net Worth** | $621,100 | $450K-$800K (Age 42, profession) | Within range |
| **Debt-to-Income Ratio** | 10.0% | <28% (Acceptable) | Excellent |
| **Liquid Assets** | $45,200 | 3-6 months expenses | Adequate emergency fund |

---

## EMPLOYMENT VERIFICATION - COMPREHENSIVE ANALYSIS

### Primary Employment Profile
**GlobalWing Airlines** - Fortune 500 Airline (NYSE: GWA)
Corporate Headquarters: 5000 Airport Blvd, Denver, CO 80249
**HR Contact**: November 18, 2024 by Lisa Rodriguez, Senior HR Business Partner

| **Employment Detail** | **Verified Information** | **Risk Assessment** |
|----------------------|--------------------------|-------------------|
| **Employee ID** | GW-4789-CAP | Active employee |
| **Hire Date** | September 12, 2006 | 18.2 years tenure |
| **Position** | Captain, International Division | Senior management level |
| **Department** | Flight Operations - Long Haul | High-value route assignment |
| **Employment Status** | Active, Full-Time, Union (ALPA) | Job security excellent |
| **Performance Rating** | "Exceeds Expectations" (2024) | Above average performer |

### Career Progression Analysis
| **Position** | **Dates** | **Base Salary** | **Promotion Basis** |
|--------------|-----------|-----------------|-------------------|
| **First Officer** | Sep 2006 - Dec 2015 | $65K-$125K | Normal progression |
| **Senior First Officer** | Jan 2016 - Dec 2021 | $135K-$165K | Merit-based advancement |
| **Captain** | Jan 2022 - Present | $198,500 | Seniority + performance |

**Analysis**: Steady career progression typical for major airline. Captain promotion at 15.3 years service demonstrates strong performance and leadership capabilities.

### Professional Aviation Credentials
**Federal Aviation Administration Check** (Conducted November 19, 2024):

| **Certificate/Rating** | **Certificate #** | **Issue Date** | **Status** | **Restrictions** |
|------------------------|------------------|----------------|------------|------------------|
| **ATP Certificate** | ATP-1234567890 | March 12, 2015 | Valid | None |
| **First Class Medical** | 123456789 | June 15, 2024 | Valid until 12/31/25 | Vision correction only |
| **B777 Type Rating** | TR-777-001 | January 8, 2018 | Current | None |
| **B787 Type Rating** | TR-787-002 | March 15, 2022 | Current | None |
| **International Authorization** | INTL-7845 | January 22, 2022 | Valid until 03/2026 | None |

### Safety & Performance Record
**Flight Operations Safety Summary**:
- **Total Flight Hours**: 12,547 (via GlobalWing Training Records)
- **Hours Last 12 Months**: 1,024 (Within FAR Part 117 limits)
- **Safety Incidents**: Zero (Career total)
- **Check Ride History**: 47 successful, zero failures or unsatisfactory ratings
- **Company Recognition**:
  * GlobalWing Safety Excellence Award (2023)
  * 15-Year Service Recognition (2021)
  * Pilot Mentor Program Instructor (2020-Present)

**Risk Assessment**: Exceptional safety record significantly reduces occupational risk profile for insurance purposes.

**International Route Assignment**:
- Primary Routes: Denver to London Heathrow (3x monthly), Denver to Frankfurt (2x monthly), Denver to Amsterdam (2x monthly)
- Occasional Tokyo and Seoul flights
- All routes to developed countries with excellent medical facilities
- Company provides comprehensive international medical coverage and emergency evacuation insurance

**Industry Risk Context**:
- GlobalWing Airlines maintains excellent safety ratings
- All destinations are low-risk developed countries
- Company provides comprehensive crew medical and evacuation coverage
- No high-risk route assignments or conflict zone operations

---

## COMPREHENSIVE INCOME ANALYSIS

### 2024 Income Breakdown
**Documentation Sources**: Pay stubs (Jan-Oct 2024), HR salary information, union contract analysis

| **Income Component** | **Amount** | **Frequency** | **Annual Total** | **Source** |
|---------------------|------------|---------------|------------------|------------|
| **Base Captain Salary** | $16,541.67 | Monthly | $198,500 | HR information |
| **International Per Diem** | $1,866.67 | Monthly avg | $22,400 | Pay stub analysis |
| **Overtime Premium** | $741.67 | Monthly avg | $8,900 | Flight ops records |
| ****TOTAL 2024 INCOME** | **$19,150** | **Monthly** | **$229,800** | **Multiple sources** |

### Income Stability Analysis (2019-2024)
| **Year** | **Base Salary** | **Total Compensation** | **% Change** | **Notes** |
|----------|-----------------|------------------------|--------------|-----------|
| **2024** | $198,500 | $229,800 | +2.3% | Current year projection |
| **2023** | $194,000 | $224,650 | +2.8% | Regular step increase |
| **2022** | $188,500 | $218,400 | +15.7% | **Captain promotion** |
| **2021** | $165,000 | $188,800 | +3.2% | Senior F/O final year |
| **2020** | $160,000 | $182,900 | -8.2% | COVID impact (reduced flying) |
| **2019** | $160,000 | $199,200 | +4.1% | Pre-pandemic normal |

**Analysis**: Income shows consistent growth with significant increase upon Captain promotion. COVID-19 impact was temporary and below industry average reduction.

### Additional Income Sources
| **Source** | **Type** | **Annual Amount** | **Status** | **Risk Factor** |
|------------|----------|-------------------|------------|-----------------|
| **Flight Instruction** | Part-time (weekends) | $3,200 | Occasional | Low - recreational instruction |
| **Union Rep Stipend** | ALPA Local 124 | $1,800 | Annual | Low - stable union position |
| **Speaking Engagements** | Aviation safety | $2,400 | Variable | Low - professional expertise |
| ****TOTAL ADDITIONAL** | | **$7,400** | | **Modest, stable sources** |

**Combined Total Annual Income**: $237,200 (Primary + Additional)

### Tax Analysis
**2023 Tax Return Analysis** (Most recent filed):
| **Tax Category** | **Amount** | **Rate** | **Assessment** |
|------------------|------------|----------|----------------|
| **Adjusted Gross Income** | $224,650 | - | Matches employment records |
| **Federal Income Tax** | $45,200 | 20.1% | Appropriate for income level |
| **State Tax (Colorado)** | $11,800 | 5.3% | Standard CO rate |
| **FICA/Medicare** | $17,196 | 7.65% | Correct calculation |
| ****Effective Tax Rate** | **$74,196** | **33.0%** | **Reasonable for income bracket** |

**2022 Tax Return Analysis**:
- **AGI**: $218,400 (Matches first year as Captain)
- **Effective Rate**: 31.8% (Consistent with 2023)
- **Refund**: $2,847 (Indicates proper withholding)

### Income Assessment Conclusion
**Status**:
- Income documented through multiple independent sources
- Stable employment with major airline (18+ years tenure)
- Career progression demonstrates strong performance
- Tax returns consistent with reported income
- Additional income sources are modest and low-risk

---

## COMPLETE ASSET & LIABILITY ANALYSIS

### Real Estate Holdings
**Primary Residence**: 1247 Pilot Lane, Denver, CO 80202

| **Property Detail** | **Information** | **Source** | **Assessment** |
|---------------------|-----------------|------------|----------------|
| **Purchase Date** | March 2019 | Public records | 5.7 years ownership |
| **Purchase Price** | $365,000 | Deed records | Original investment |
| **Current Value** | $485,000 | Recent appraisal (Oct 2024) | 32.9% appreciation |
| **Property Type** | Single-family, 4BR/3BA | MLS records | Family-appropriate |
| **Square Footage** | 2,847 sq ft | County assessor | Above average for area |
| **Lot Size** | 0.31 acres | Survey records | Good-sized lot |

**Property Tax Analysis**:
- **2024 Assessment**: $472,100 (Mill levy: 7.512)
- **Annual Property Tax**: $3,546 (Current, no delinquencies)
- **Insurance**: $1,847/year (USAA - adequate coverage)

### Investment Portfolio Analysis
**Documentation**: Statements as of October 31, 2024

#### Retirement Accounts
| **Account Type** | **Provider** | **Current Balance** | **Contribution Rate** | **Risk Assessment** |
|------------------|--------------|-------------------|-------------------|-------------------|
| **401(k)** | GlobalWing Airlines Plan | $342,000 | 15% + 6% match | Excellent savings rate |
| **Traditional IRA** | Charles Schwab | $45,200 | $6,500 annually | Max contribution |
| **Roth IRA** | Charles Schwab | $33,300 | $6,500 annually | Tax diversification |
| ****Total Retirement** | | **$420,500** | **27% of income** | **Above average** |

#### Investment Accounts (Taxable)
| **Account** | **Provider** | **Balance** | **Investment Strategy** | **Risk Level** |
|-------------|--------------|-------------|------------------------|----------------|
| **Brokerage Account** | Charles Schwab | $48,200 | Index funds (80%), Bonds (20%) | Conservative |
| **Education Savings (529)** | Colorado CollegInvest | $30,300 | Age-based portfolio | Appropriate |
| ****Total Investments** | | **$78,500** | **Diversified strategy** | **Low-moderate risk** |

#### Liquid Assets
| **Account Type** | **Institution** | **Balance** | **Purpose** | **Assessment** |
|------------------|-----------------|-------------|-------------|----------------|
| **Primary Checking** | USAA Federal | $18,400 | Daily expenses | Adequate |
| **High-Yield Savings** | Marcus Online | $16,800 | Emergency fund | 3.2 months expenses |
| **Money Market** | USAA Federal | $10,000 | Short-term goals | Good liquidity |
| ****Total Liquid Assets** | | **$45,200** | **Emergency preparedness** | **Sufficient** |

### Liability Analysis
**Documentation**: Current statements and loan documents

#### Real Estate Debt
| **Mortgage Detail** | **Information** | **Terms** | **Assessment** |
|---------------------|-----------------|-----------|----------------|
| **Original Loan Amount** | $292,000 | 30-year fixed | Conventional loan |
| **Current Balance** | $298,000 | 3.2% APR | Excellent rate (2019) |
| **Monthly Payment** | $1,271 | P&I only | 19.5% of gross income |
| **Remaining Term** | 24.3 years | 292 payments left | On schedule |
| **LTV Ratio** | 48.6% | Significant equity | Low risk |

#### Vehicle Loans
| **Vehicle** | **Year/Make/Model** | **Balance** | **Payment** | **Term** |
|-------------|-------------------|-------------|-------------|----------|
| **Primary** | 2022 Toyota Highlander | $18,400 | $347/month | 2.9% APR, 4.2 years left |
| **Secondary** | 2020 Honda Civic | $10,200 | $298/month | 1.9% APR, 2.8 years left |
| ****Total Auto Debt** | | **$28,600** | **$645/month** | **Reasonable vehicles** |

#### Other Debts
| **Debt Type** | **Balance** | **Terms** | **Risk Assessment** |
|---------------|-------------|-----------|-------------------|
| **Credit Cards** | $3,247 | Various (paid monthly) | Low utilization (12%) |
| **Student Loans** | $0 | Paid off 2021 | No education debt |
| ****Total Other Debt** | **$3,247** | | **Minimal consumer debt** |

### Net Worth Calculation
| **Category** | **Amount** | **Percentage** |
|--------------|------------|----------------|
| ****TOTAL ASSETS** | **$950,700** | **100%** |
| Real Estate | $485,000 | 51.0% |
| Retirement Accounts | $342,000 | 36.0% |
| Investment Accounts | $78,500 | 8.3% |
| Liquid Assets | $45,200 | 4.8% |
| | | |
| ****TOTAL LIABILITIES** | **$329,600** | **34.7%** |
| Mortgage | $298,000 | 31.3% |
| Auto Loans | $28,400 | 3.0% |
| Credit Cards | $3,200 | 0.3% |
| | | |
| ****NET WORTH** | **$621,100** | **Strong financial position** |

### Debt-to-Income Analysis
| **Debt Category** | **Monthly Payment** | **Annual Payment** | **% of Income** |
|-------------------|-------------------|-------------------|-----------------|
| **Mortgage** | $1,271 | $15,252 | 6.6% |
| **Auto Loans** | $645 | $7,740 | 3.4% |
| **Credit Cards** | $0 | $0 | 0.0% (paid in full) |
| ****Total Debt Service** | **$1,916** | **$22,992** | **10.0%** |

**Analysis**: Debt-to-income ratio of 10.0% is excellent (industry standard <28%). Conservative debt management demonstrates strong financial discipline.

#### Liabilities (As of November 2024)
**Real Estate Debt**:
- Primary Mortgage: $298,000 (3.2% fixed, 18 years remaining)
- Monthly Payment: $1,271

**Other Debt**:
- Auto Loan #1: $18,400 (2022 Toyota Highlander)
- Auto Loan #2: $10,000 (2020 Honda Civic)
- Credit Cards: $3,200 (low balances, paid monthly)

**Total Liabilities**: $329,600
**Net Worth**: $621,100

### Coverage Justification Analysis

#### Financial Ratios
**Coverage-to-Income Multiple**: 10.9x ($2,500,000  $229,800)
**Debt-to-Income Ratio**: 12.6% (acceptable range)
**Net Worth-to-Coverage Ratio**: 24.8% (adequate financial position)

#### Family Financial Needs Assessment
**Mortgage Balance**: $298,000 (would be covered)
**Children's Education Costs**: Estimated $200,000 (2 children, college expenses)
**Family Living Expenses**: $1,800,000 (10 years at current lifestyle)
**Total Family Protection Need**: $2,235,847
**Requested Coverage**: $2,500,000 **APPROPRIATE**

### Spouse Financial Information
**David Michael Darcy**:
- Occupation: Software Engineering Manager, TechCorp
- Annual Income: $145,000 (reported)
- Employment: 8 years with current employer
- Combined Household Income: $374,800

### Additional Income Sources
**Rental Property**: None
**Business Interests**: None
**Investment Income**: $4,200 annually (from investment accounts)
**Other Income**: Occasional aviation consulting ($2,000-5,000 annually)

---

## VERIFIED FINANCIAL INDICATORS

### Employment Stability Factors
**Positive Indicators**:
- 18+ years with same employer (excellent stability)
- Recent promotion to Captain (career advancement)
- Major airline employment (vs. regional or charter)
- Excellent safety record (job security)
- Union representation (pilot union protections)

### Industry Financial Context
**GlobalWing Airlines - Financial Strength**:
- S&P Rating: A- (Strong financial position)
- Industry Leader: Top 5 US carriers
- Pilot Contract: Recently negotiated favorable terms (2024)
- Job Security: High for senior captains
- Retirement Benefits: Strong pension and 401k matching

### Coverage Request Assessment
**Requested Coverage**: $2,500,000
**Preliminary Analysis**:
- **Industry Standard Range**: 10-15x annual income typical for aviation professionals
- **Estimated Income Multiple**: 10.2x - 12.8x (if income = $195K-$245K)
- **Initial Assessment**: Within reasonable range for occupation
- **Final Determination**: Pending actual income verification

---

## FINANCIAL RISK FACTORS

### Positive Risk Indicators
- **Career Stability**: 18+ years same employer
- **Professional Advancement**: Recent promotion to Captain
- **Industry Position**: Major airline vs. regional/charter
- **Age/Experience**: Peak earning years (age 42)
- **Aviation Career Longevity**: Potential 15+ more years to retirement

### Risk Considerations
- **Industry Cyclicality**: Aviation subject to economic downturns
- **Mandatory Retirement**: FAA requires retirement at age 65
- **Medical Dependency**: Career dependent on maintaining medical certificate
- **Economic Sensitivity**: Travel industry impacts on airlines

### Missing Risk Assessment Data
- **Actual income verification** - Cannot confirm coverage justification
- **Debt levels** - Unknown impact on financial capacity
- **Spouse income** - Unknown additional household income
- **Financial obligations** - Cannot assess family financial needs

---

## COMPREHENSIVE FINANCIAL UNDERWRITING DECISION

### Final Assessment
**Coverage Requested**: $2,500,000
**Financial Justification**: Appears appropriate
**Risk Rating**: Standard (good financial position)

### Coverage Justification Summary
- **Income Multiple**: 10.9x (within guidelines for aviation professionals)
- **Family Need**: $2.3M calculated need vs. $2.5M requested
- **Financial Stability**: Good employment history and asset position
- **Debt Management**: Conservative debt levels, good credit management

### Required Actions

#### INCOME DOCUMENTATION:
1. **Income Package**:
  - Last 6 months pay stubs received and reviewed
  - 2022 and 2023 tax returns analyzed
  - GlobalWing Airlines salary information confirmed

2. **Financial Statement Package**:
  - Asset/liability statement reviewed
  - Bank statements reviewed (6 months)
  - Investment account statements analyzed

3. **Coverage Justification**:
  - Family financial needs analysis completed
  - Debt obligation review finished
  - Estate planning objectives documented

#### ADDITIONAL DOCUMENTATION:
1. **Spouse Financial Information**:
  - David Darcy income reported ($145,000)
  - Joint financial obligations documented
  - Beneficiary financial planning appropriate

2. **Supporting Documentation**:
  - Retirement planning documentation reviewed
  - Existing insurance coverage analyzed

FILE 4: APP-2024-5847_processing_notes.txt

STERLING INSURANCE COMPANY
INTERNAL PROCESSING NOTES - CONFIDENTIAL
Application #APP-2024-5847

Date Created: November 18, 2024 2:15 PM MST
Created By: Janet Martinez, Senior Underwriter
Last Updated: December 1, 2024 10:30 AM MST

=== INITIAL REVIEW ASSESSMENT ===

Application Review Score: 6.2/10 (Below acceptable threshold for immediate processing)

Primary Issues Identified:
- Financial section incomplete (Critical)
- Family medical history missing (Critical)
- Beneficiary designations insufficient (High)
- No supporting documentation provided (High)

=== PROCESSING TIMELINE ===

11/15/2024 11:47 AM - Application received via electronic submission
11/18/2024 2:15 PM - Initial review completed by J. Martinez, UW
11/20/2024 9:30 AM - Requirements letter sent (15-day response time)
11/22/2024 - Agent follow-up call - Applicant traveling internationally
12/01/2024 - Status inquiry from agent M. Thompson - Timeline update requested

=== REQUIRED DOCUMENTATION STATUS ===

Financial Documentation (Priority 1):
[ ] Pay stubs (last 3 months) - Due: Dec 5, 2024
[ ] Tax returns (2022, 2023) - Due: Dec 5, 2024
[ ] Bank statements (6 months) - Due: Dec 5, 2024
[ ] Employment verification letter - Due: Dec 5, 2024
[ ] Financial statement - Due: Dec 5, 2024

Medical Documentation (Priority 1):
[ ] Family medical history form - Due: Dec 5, 2024 (CRITICAL)
[ ] AME detailed report - Requested from Dr. Chen - Due: Dec 10, 2024
[ ] Complete physical exam - To be scheduled - Due: Dec 15, 2024
[ ] Lab work panel - Pending physical - Due: Dec 15, 2024
[ ] Cardiology consultation - May be required - TBD

Regulatory Compliance (Priority 2):
[ ] Beneficiary designation form - Due: Dec 5, 2024
[ ] Colorado disclosure forms - Due: Dec 5, 2024
[X] HIPAA authorization - Complete
[ ] Replacement form - N/A (new coverage)

=== PRELIMINARY RISK ASSESSMENT ===

Age: Standard (42 years)
Occupation: Class F - Aviation (Standard for major airline)
Health: Standard Plus potential (pending complete medical)
Financial: TBD (pending income verification)
Overall: CANNOT RATE - Too many critical gaps

=== UNDERWRITER NOTES ===

This application requires significant additional documentation before proceeding.
The applicant appears to be a good risk based on preliminary information:
- Senior Captain with major airline (18+ years experience)
- Stable employment and career progression
- No obvious red flags in initial disclosure

However, critical gaps prevent proper risk assessment:
1. Financial justification for $2.5M coverage cannot be determined
2. Family medical history essential for hypertension risk assessment
3. Beneficiary designations do not meet regulatory requirements

Recommendation: Hold in pending status until complete documentation received.
Consider expedited processing once gaps filled due to quality of risk profile.

Next Review: Upon receipt of required documentation
Assigned Senior Underwriter: TBD (after information complete)
Target Decision Date: December 20, 2024 (if documentation received by Dec 5)

=== CONTACT LOG ===

Agent: Marcus Thompson, CLU, ChFC
License: CO-LIC-78451
Agency: Mile High Insurance Partners
Phone: (555) 987-6543
Email: m.thompson@milehighinsurance.com

11/20/2024 - Requirements letter emailed to agent and applicant
11/22/2024 - Agent called - applicant on international flight assignment
11/25/2024 - Follow-up email sent to agent with checklist
12/01/2024 - Agent inquiry about timeline - advised 15-day extension possible

=== QUALITY CONTROL FLAGS ===

Red Flags: None identified
Yellow Flags: Large coverage amount relative to disclosed information
Green Flags: Major airline employment, stable career, good preliminary health

Overall QC Status: ACCEPTABLE FOR PROCESSING (pending documentation)

---
CONFIDENTIAL - FOR INTERNAL STERLING INSURANCE USE ONLY
File stored in secure underwriting system
Access restricted to authorized underwriting personnel
```