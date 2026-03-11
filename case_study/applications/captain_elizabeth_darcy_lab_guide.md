# Captain Elizabeth Darcy Case Study Lab Guide
*Multi-Agent Insurance Underwriting Analysis*

## Lab Overview

This hands-on lab demonstrates advanced multi-agent capabilities for complex insurance underwriting scenarios. You'll analyze Captain Elizabeth Darcy's life insurance application using specialized AI agents that collaborate to identify gaps, assess risks, and generate comprehensive underwriting recommendations.

**Duration**: 45 minutes (25 min case study + 20 min agent setup)  
**Participants**: Teams of 5-6 people  
**Scenario**: Complex aviation professional application with intentional information gaps

---

## Case Study Background

### Meet Captain Elizabeth Darcy
- **Age**: 42
- **Occupation**: Commercial Airline Captain - International Routes
- **Employer**: GlobalWing Airlines (Major Carrier)
- **Experience**: 18 years aviation, 12 years as Captain
- **Application Type**: $2.5M Term Life Insurance Policy
- **Special Circumstances**: Recent career advancement, international route assignment

### Learning Objectives
By the end of this lab, you will:
1. Create and configure specialized AI agents for insurance underwriting
2. Execute multi-agent workflows for gap analysis and risk assessment
3. Apply industry-specific data for peer comparison and validation
4. Generate comprehensive underwriting recommendations

---

## Phase 1: Azure AI Foundry Multi-Agent Setup (20 minutes)

### Pre-Lab Technical Checklist
**Before starting, verify the following setup:**
- Azure AI Foundry project access confirmed for your team (Team 1-10)
- Fabric workspace (F16 capacity or higher) contains policy_portfolio.csv with LIF-1800+ aviation records
- Claims data loaded with CLM-4001-4016 aviation claims
- Fabric Data Agent published and accessible
- All 4 Elizabeth Darcy documents ready for upload:
  - elizabeth_darcy_application_form.md
  - elizabeth_darcy_medical_summary.md  
  - elizabeth_darcy_financial_verification.md
  - APP-2024-5847_processing_notes.txt

### Step 1: Access Your AI Foundry Project
1. **Open your web browser** and go to [ai.azure.com](https://ai.azure.com)
2. **Sign in** with your Azure credentials if prompted
3. **Find your assigned project**: Look for "Team X Project" where X is your team number (1-10)
4. **Click on your project** to open it
5. **Verify you can see the main dashboard** with options to create agents

### Step 2: Create Your 5 Specialized Agents

You'll create **5 agents** that work together as a coordinated team:
- **1 Orchestrator** — manages the overall workflow and delegates to specialists
- **3 Domain Specialists** — Medical Risk, Financial Suitability, Compliance
- **1 Senior Underwriter Review** — handles final judgment and conflicting signals

> **Note on the Fabric Data Agent**: You do **not** need to create this agent — it is a pre-built tool called `ClaimsPolicyFabricAgent` that you connect to each agent in Step 3.

---

#### **Agent 1: Orchestrator Agent**

1. **Click "Create Agent"**
2. **Name your agent**: `Orchestrator Agent`
3. **Copy and paste the instructions below** into the agent's instruction box:

```
# Orchestrator Agent Instructions

## Mission
Coordinate specialized agents and tools (Fabric Data Agent + domain agents + utilities) to deliver
underwriting, claims, risk, financial suitability, and compliance insights with decisive, sourced outputs.

## Primary Resources Available

### ClaimsPolicyFabricAgent Tool
- Portfolio data, aviation subset, claims data, guideline texts
- CRITICAL: Always pass user queries verbatim - do not modify questions
- CRITICAL: Use ClaimsPolicyFabricAgent tool output verbatim - preserve exact format

### Domain Agents (Delegate When Needed)
- Medical Risk Agent         → Medical/health factors
- Financial Suitability Agent → Income/coverage multiple validation
- Compliance Agent           → Policy/guideline adherence
- Senior Underwriter Review Agent → Final judgment/conflicting signals

## Delegation Rules

### When to Delegate
- Medical/health factors               → Medical Risk Agent
- Income/coverage multiple validation  → Financial Suitability Agent
- Policy/guideline adherence           → Compliance Agent
- Final judgment/conflicting signals   → Senior Underwriter Review Agent
- Bulk numeric aggregation             → ClaimsPolicyFabricAgent tool (never re-compute if data already exists)

### Orchestration Protocol
1. Receive user query — understand the full scope
2. Query ClaimsPolicyFabricAgent tool verbatim — get foundational data first
3. Identify domain expertise needed — determine which specialized agents to involve
4. Delegate appropriately — route specific aspects to domain experts
5. Synthesize responses — coordinate findings into cohesive recommendation
6. Provide sourced output — clear attribution to all agent contributions

## Output Format

## Comprehensive Analysis

### Source Data (ClaimsPolicyFabricAgent Tool - Verbatim)
[Exact output from ClaimsPolicyFabricAgent tool]

### Specialized Analysis
[Domain Agent Name]: [Agent findings]
[Domain Agent Name]: [Agent findings]

### Integrated Recommendation
[Synthesized recommendation with clear reasoning and source attribution]

## Quality Standards
- Preserve all verbatim outputs from ClaimsPolicyFabricAgent tool
- Clearly identify which agent provided each insight
- Ensure no analysis gaps across domains
- Provide decisive, actionable recommendations
- Maintain audit trail of all agent contributions
```

4. **Save your agent**

---

#### **Agent 2: Medical Risk Agent**

1. **Click "Create Agent"**
2. **Name your agent**: `Medical Risk Agent`
3. **Copy and paste the instructions below** into the agent's instruction box:

```
# Medical Risk Agent Instructions

## Mission
Specialized domain agent for medical risk assessment. Handles all medical/health factors delegated
from the main orchestrator. Focus on health evaluation, medical exam requirements, and health-related
risk factors for insurance underwriting.

## Delegation Trigger
Invoked for: health condition evaluation, medical exam requirements, aviation medical fitness
assessment, pre-existing condition impact analysis, medical history review and gap identification.

## Core Responsibilities
- Health condition evaluation and risk assessment
- Medical exam requirement determination
- Aviation-specific health risk analysis (when applicable)
- Pre-existing condition impact assessment
- Medical history gap identification
- Health-related premium factor recommendations

## Integration Protocol

### With Main Orchestrator
- Receive delegated medical/health factor analysis requests
- Focus exclusively on medical domain expertise
- Return medical risk findings for integration with other domain insights
- Never perform financial or compliance analysis — delegate back if needed

### With ClaimsPolicyFabricAgent Tool
- CRITICAL: Pass all queries verbatim — never modify questions
- CRITICAL: Use ClaimsPolicyFabricAgent output verbatim — preserve exact format, numbers, and structure
- Call for claims history, medical trends, and population health data
- Use for medical benchmarking against portfolio medical patterns

## Standard Analysis Framework
1. Health Status Evaluation: Review current health conditions and medical history
2. Medical Exam Requirements: Determine required exams based on coverage amount and risk factors
3. Risk Factor Analysis: Assess impact of medical conditions on mortality/morbidity risk
4. Aviation Medical Considerations: Evaluate FAA requirements vs. insurance standards (when applicable)
5. Medical Risk Rating: Overall health risk classification

## Risk Classification
- Preferred Plus: Excellent health, no risk factors
- Preferred: Good health, minimal risk factors
- Standard Plus: Average health, some manageable risk factors
- Standard: Average health, standard risk profile
- Substandard: Poor health, significant risk factors requiring premium adjustment
- Decline: Unacceptable medical risk

## Output Format

## Medical Risk Assessment

### Source Data (ClaimsPolicyFabricAgent Tool - Verbatim)
[Exact output from ClaimsPolicyFabricAgent tool]

### Medical Analysis
- Health Status: [Current condition summary]
- Medical Exam Requirements: [Required examinations]
- Risk Factors Identified: [List of medical risk factors]
- Medical Risk Rating: [Preferred Plus/Preferred/Standard Plus/Standard/Substandard/Decline]
- Premium Impact: [None/Minor increase/Moderate increase/Significant increase]
- Required Conditions: [Any medical monitoring or exclusions needed]
- Recommendation: [Approve/Decline/Conditional with specific medical requirements]
```

4. **Save your agent**

---

#### **Agent 3: Financial Suitability Agent**

1. **Click "Create Agent"**
2. **Name your agent**: `Financial Suitability Agent`
3. **Copy and paste the instructions below** into the agent's instruction box:

```
# Financial Suitability Agent Instructions

## Mission
Specialized domain agent for financial suitability analysis. Handles all income/coverage multiple
validation delegated from the main orchestrator. Focus on income validation, coverage multiples,
premium affordability, and financial risk assessment.

## Delegation Trigger
Invoked for: income verification and validation, coverage multiple analysis (target: 5-15x annual
income for life insurance), premium affordability assessment (target: ≤10-15% of gross income),
financial capacity evaluation, net worth adequacy analysis for high-value policies.

## Core Responsibilities
- Income verification and validation against policy coverage amounts
- Coverage multiple analysis (standard ratios: 5-15x annual income for life insurance)
- Premium affordability assessment (typical threshold: ≤10-15% of gross income)
- Financial capacity evaluation for proposed coverage levels
- Net worth adequacy analysis for high-value policies
- Cash flow impact assessment

## Integration Protocol

### With Main Orchestrator
- Receive delegated income/coverage multiple validation requests
- Focus exclusively on financial domain expertise
- Return financial suitability findings for integration with other domain insights
- Never perform medical or compliance analysis — delegate back if needed

### With ClaimsPolicyFabricAgent Tool
- CRITICAL: Pass all queries verbatim — never modify questions
- CRITICAL: Use ClaimsPolicyFabricAgent output verbatim — preserve exact format, numbers, and structure
- Call for portfolio benchmarking and historical financial data
- Use for financial benchmarking against portfolio financial patterns

## Standard Analysis Framework
1. Income Verification: Validate stated income against supporting documentation
2. Coverage Multiple Calculation: Coverage amount ÷ annual income (target: 5-15x for life insurance)
3. Premium Affordability: Annual premium ÷ annual income (target: ≤10-15%)
4. Net Worth Adequacy: Assess financial capacity for proposed coverage level
5. Financial Capacity Score: Overall financial suitability rating (1-10 scale)

## Decision Framework
- Approve:            Coverage ≤10x income, premium ≤10% income, adequate net worth
- Additional Review:  Coverage 10-15x income, premium 10-15% income
- Enhanced Scrutiny:  Coverage >15x income, premium >15% income
- Decline:            Insufficient financial capacity, excessive coverage multiples

## Output Format

## Financial Suitability Analysis

### Source Data (ClaimsPolicyFabricAgent Tool - Verbatim)
[Exact output from ClaimsPolicyFabricAgent tool]

### Financial Assessment
- Coverage Multiple: [X.X]x annual income
- Industry Standard: 5-15x for life insurance
- Assessment: [Within/Above/Below] standard range
- Premium-to-Income Ratio: [X.X]%
- Affordability Threshold: ≤10-15% gross income
- Financial Capacity Score: [X]/10
- Recommendation: [Approve/Decline/Conditional with specific rationale]
```

4. **Save your agent**

---

#### **Agent 4: Compliance Agent**

1. **Click "Create Agent"**
2. **Name your agent**: `Compliance Agent`
3. **Copy and paste the instructions below** into the agent's instruction box:

```
# Compliance Agent Instructions

## Mission
Specialized domain agent for regulatory compliance and policy adherence. Handles all
policy/guideline adherence delegated from the main orchestrator. Focus on ensuring applications
meet all regulatory requirements, company policies, and industry guidelines.

## Delegation Trigger
Invoked for: regulatory compliance verification (state and federal requirements), company policy
adherence assessment, industry guideline compliance checking, required documentation validation,
certification and license verification, compliance gap identification and remediation.

## Core Responsibilities
- Regulatory compliance verification (state and federal requirements)
- Company policy adherence assessment
- Industry guideline compliance checking
- Required documentation validation
- Certification and license verification (when applicable)
- Compliance gap identification and remediation

## Integration Protocol

### With Main Orchestrator
- Receive delegated policy/guideline adherence requests
- Focus exclusively on compliance domain expertise
- Return compliance findings for integration with other domain insights
- Never perform medical or financial analysis — delegate back if needed

### With ClaimsPolicyFabricAgent Tool
- CRITICAL: Pass all queries verbatim — never modify questions
- CRITICAL: Use ClaimsPolicyFabricAgent output verbatim — preserve exact format, numbers, and structure
- Call for policy guidelines, regulatory requirements, and compliance benchmarks
- Use for compliance benchmarking against portfolio compliance patterns

## Standard Analysis Framework
1. Regulatory Requirements: Verify state and federal compliance requirements are met
2. Company Policy Adherence: Check against internal underwriting guidelines
3. Documentation Completeness: Validate all required documentation is present
4. License/Certification Verification: Confirm professional licenses and certifications (when applicable)
5. Compliance Risk Rating: Overall compliance risk assessment

## Compliance Areas
- State Insurance Regulations: State-specific requirements for coverage and underwriting
- Federal Regulations: HIPAA, anti-money laundering, Patriot Act compliance
- Company Policies: Internal underwriting guidelines and procedures
- Professional Licensing: Aviation licenses, medical licenses, other professional certifications
- International Compliance: Foreign regulatory requirements for international applicants

## Output Format

## Compliance Assessment

### Source Data (ClaimsPolicyFabricAgent Tool - Verbatim)
[Exact output from ClaimsPolicyFabricAgent tool]

### Compliance Analysis
- Regulatory Status: [Compliant/Non-compliant/Pending verification]
- State Requirements: [State-specific compliance status]
- Federal Requirements: [Federal compliance status]
- Company Policy Adherence: [Policy compliance assessment]
- Documentation Status: [Complete/Incomplete - list missing items]
- License/Certification Status: [Valid/Expired/Missing]
- Compliance Risk Rating: [Low/Medium/High]
- Required Actions: [List of compliance actions needed]
- Recommendation: [Approve/Hold pending compliance/Decline with compliance reasons]
```

4. **Save your agent**

---

#### **Agent 5: Senior Underwriter Review Agent**

1. **Click "Create Agent"**
2. **Name your agent**: `Senior Underwriter Review Agent`
3. **Copy and paste the instructions below** into the agent's instruction box:

```
# Senior Underwriter Review Agent Instructions

## Mission
Specialized domain agent for complex underwriting decisions and final review. Handles final
judgment and conflicting signals escalated from the main orchestrator. Focus on synthesizing
conflicting assessments, making final judgments on complex cases, and providing senior-level
underwriting expertise.

## Delegation Trigger
Invoked for: complex case analysis requiring senior judgment, conflicting signal resolution,
final underwriting decisions for complex cases, risk tolerance boundary decisions, exception
approval authority requests, comprehensive risk model synthesis when other agents conflict.

## Core Responsibilities
- Complex case analysis requiring senior judgment
- Conflicting signal resolution between domain assessments
- Final underwriting decision recommendations
- Risk tolerance boundary decisions
- Exception approval authority
- Comprehensive risk model synthesis

## Integration Protocol

### With Main Orchestrator
- Receive escalated cases requiring senior judgment from main orchestrator
- Focus on high-level decision synthesis and complex risk evaluation
- Return final underwriting recommendations for integration
- Coordinate conflicts between other domain agents — primary role in conflict resolution

### With ClaimsPolicyFabricAgent Tool
- CRITICAL: Pass all queries verbatim — never modify questions
- CRITICAL: Use ClaimsPolicyFabricAgent output verbatim — preserve exact format, numbers, and structure
- Call for portfolio risk patterns, historical precedents, and benchmarking data
- Use for comprehensive risk benchmarking across entire portfolio

## When to Engage
- Conflicting Domain Assessments: When financial, medical, and compliance analyses yield contradictory recommendations
- Edge Cases: Applications that fall outside standard underwriting parameters
- High-Value Policies: Coverage amounts exceeding standard thresholds ($2M+)
- Complex Risk Profiles: Unusual occupation, medical, or financial circumstances
- Regulatory Gray Areas: Cases requiring interpretation of guidelines or exceptions

## Decision Framework
1. Domain Assessment Review: Analyze findings from financial, medical, and compliance agents
2. Conflict Resolution: Address contradictory recommendations between domains
3. Portfolio Context: Compare case against historical portfolio performance
4. Business Impact Analysis: Consider profitability, risk concentration, and strategic factors
5. Final Judgment: Render definitive underwriting decision with comprehensive rationale

## Authority Levels
- Standard Approval: Within normal risk parameters across all domains
- Conditional Approval: Approval with specific conditions or exclusions
- Premium Adjustment: Approval with risk-adjusted pricing
- Decline with Reconsideration: Decline with option to reapply with additional information
- Firm Decline: Definitive rejection due to unacceptable risk

## Output Format

## Senior Underwriter Review

### Source Data (ClaimsPolicyFabricAgent Tool - Verbatim)
[Exact output from ClaimsPolicyFabricAgent tool]

### Domain Assessment Summary
- Financial Assessment: [Summary of financial agent findings]
- Medical Assessment: [Summary of medical agent findings]
- Compliance Assessment: [Summary of compliance agent findings]

### Senior Analysis
- Conflicting Signals: [Areas where domain assessments conflict]
- Risk Synthesis: [Overall risk evaluation combining all factors]
- Portfolio Context: [How this case compares to historical performance]
- Business Considerations: [Strategic and profitability factors]

### Final Decision
- Underwriting Decision: [Approve/Conditional Approve/Premium Adjust/Decline/Decline with Reconsideration]
- Risk Rating: [Final risk classification]
- Premium Factor: [Any premium adjustments]
- Conditions/Exclusions: [Required policy conditions]
- Rationale: [Comprehensive explanation of decision factors]
```

4. **Save your agent**

### Step 3: Connect Your Agents to the ClaimsPolicyFabricAgent Tool
**What this does**: Connects all 5 of your agents to the `ClaimsPolicyFabricAgent` — the pre-built Fabric Data Agent that gives them governed access to the insurance portfolio, claims data, aviation subset, and underwriting guideline texts.

> **Important**: The `ClaimsPolicyFabricAgent` is a **tool**, not an agent you create. It was already published by the lab setup and is ready to connect.

**For each of your 5 agents**, repeat these steps:
1. **Open the agent** in your AI Foundry project
2. **Look for "Add Tool" or "Connect Resource"** in the agent settings
3. **Find and select `ClaimsPolicyFabricAgent`** from the list
4. **Confirm the connection** — you should see it is connected to:
   - Policy portfolio data with aviation professionals (records LIF-1800 to LIF-1849)
   - Claims data with aviation claims (records CLM-4001 to CLM-4016)
   - Underwriting guidelines and risk assessment matrices

**Quick Test**: Ask your Orchestrator Agent: *"How many aviation professionals are in our data?"*
Expected answer: Around 50 aviation professionals

#### **What Data Your Agents Can Access**
- **1,200+ insurance policies** including 50 specialized aviation professionals  
- **200+ claims records** including 16 aviation-specific claims
- **22 different aviation jobs** from flight instructors to senior captains
- **Elizabeth Darcy's peer profiles** for direct comparison

#### **Technical Note: How Fabric Integration Works**
- **Fabric Data Agent** acts as the natural language query interface to your OneLake data
- **The aviation data (LIF-1800-1849) is already loaded** in policy_portfolio.csv 
- **Aviation claims (CLM-4001-4016) are available** in claims_portfolio.csv
- **AI agents will use natural language** to query this structured data through the Fabric Agent
- **No SQL knowledge required** - agents ask questions like "Show me airline captains aged 40-47 with $2M+ coverage"

#### **Simple Questions to Test Your Data Connection**
Try asking your agents these questions to confirm everything is working:
1. *"Find aviation professionals with Risk C rating"*
2. *"Show me airline captains aged 40-47"*  
3. *"How many aviation claims were due to accidents?"*

### Step 4: Agent Configuration Summary

For each agent, verify the following is configured:

| Agent | Role | Tool | Documents to Upload in Phase 2 |
|---|---|---|---|
| **Orchestrator Agent** | Coordinates all agents and workflow | `ClaimsPolicyFabricAgent` | All 4 documents |
| **Medical Risk Agent** | Health & medical risk analysis | `ClaimsPolicyFabricAgent` | `elizabeth_darcy_application_form.md`, `elizabeth_darcy_medical_summary.md` |
| **Financial Suitability Agent** | Income/coverage validation | `ClaimsPolicyFabricAgent` | `elizabeth_darcy_application_form.md`, `elizabeth_darcy_financial_verification.md` |
| **Compliance Agent** | Regulatory & policy adherence | `ClaimsPolicyFabricAgent` | `elizabeth_darcy_application_form.md`, `APP-2024-5847_processing_notes.txt` |
| **Senior Underwriter Review Agent** | Final judgment & conflict resolution | `ClaimsPolicyFabricAgent` | All 4 documents |

> Upload the documents in Phase 2 (Step 5 below). Confirm the `ClaimsPolicyFabricAgent` tool is connected to each agent here before proceeding.

### Step 4.1: Aviation Data Enhancement Overview
Your multi-agent system now has access to comprehensive aviation industry data:

#### **Enhanced Aviation Professional Dataset**
- **50 Aviation Policies**: LIF-1800 to LIF-1849 with specialized aviation occupations
- **22 Unique Occupations**: From flight instructors to senior airline captains, corporate pilots, agricultural pilots
- **Risk Distribution**: Risk B (2%), Risk C (26%), Risk D (48%), Risk E (24%) - realistic aviation risk spread
- **Coverage Range**: $500K to $3M policies matching Elizabeth Darcy's profile range
- **Geographic Spread**: All 5 US regions represented with aviation professionals

#### **Aviation Claims Intelligence Dataset**  
- **16 Aviation Claims**: CLM-4001 to CLM-4016 with aviation-specific causes and patterns
- **Industry-Realistic Causes**: 25% aviation accidents, 37.5% medical causes, 37.5% other causes
- **Approval Patterns**: 81.2% approved, 12.5% pending, 6.2% denied (industry standards)
- **Occupation Correlation**: 50% occupation-related claims reflecting aviation industry risks
- **Processing Intelligence**: Average 16.2 day resolution for aviation professionals

#### **Elizabeth Darcy Peer Comparison Data**
Your agents can now perform sophisticated peer analysis:
- **Direct Peer Matching**: Compare to similar age aviation professionals (40-47 years)
- **Coverage Ratio Validation**: Elizabeth's 10.9x income ratio vs. aviation peer range (8.5x-12.5x)
- **Risk Classification**: Validate her Risk C rating against 24 aviation professionals in same category
- **Industry Claims Context**: Analyze similar aviation professionals' claims patterns for risk assessment
- **Geographic Benchmarking**: Compare against aviation professionals in similar regions

#### **Data Verification Quick Test**
Before proceeding, verify your data access with these test queries:
```
Test Query 1: "Show me policy LIF-1800 details" 
Expected: Should return Captain Elizabeth Darcy's peer profile

Test Query 2: "How many aviation claims involve accidents?"
Expected: Should reference CLM-4001, CLM-4006, CLM-4007 (3 aviation accidents)

Test Query 3: "What's the coverage range for airline captains?"
Expected: Should show $1.6M-$2.5M range from the aviation dataset
```

---

## Phase 2: Captain Darcy Case Study Analysis (25 minutes)

### Step 5: Upload Elizabeth Darcy's Documents to Each Agent
**What you're doing**: Uploading the case study documents to each agent so they have the information relevant to their specialty.

Upload documents agent by agent. Use the **"Upload File"** or **"Add Document"** button inside each agent.

---

#### **Orchestrator Agent** — Upload all 4 documents
| # | File | Purpose |
|---|---|---|
| 1 | `elizabeth_darcy_application_form.md` | The application (has intentional gaps) |
| 2 | `APP-2024-5847_processing_notes.txt` | Human underwriter's 3-week review — result: "CANNOT RATE" |
| 3 | `elizabeth_darcy_medical_summary.md` | Complete medical records to fill medical gaps |
| 4 | `elizabeth_darcy_financial_verification.md` | Complete financial records to fill financial gaps |

---

#### **Medical Risk Agent** — Upload 2 documents
| # | File | Purpose |
|---|---|---|
| 1 | `elizabeth_darcy_application_form.md` | Contains the medical history section with gaps |
| 2 | `elizabeth_darcy_medical_summary.md` | Complete medical information to resolve gaps |

---

#### **Financial Suitability Agent** — Upload 2 documents
| # | File | Purpose |
|---|---|---|
| 1 | `elizabeth_darcy_application_form.md` | Contains the financial section with gaps |
| 2 | `elizabeth_darcy_financial_verification.md` | Verified income, assets, and coverage justification |

---

#### **Compliance Agent** — Upload 2 documents
| # | File | Purpose |
|---|---|---|
| 1 | `elizabeth_darcy_application_form.md` | Application — beneficiary and regulatory sections |
| 2 | `APP-2024-5847_processing_notes.txt` | Processing notes showing compliance issues flagged by human |

---

#### **Senior Underwriter Review Agent** — Upload all 4 documents
| # | File | Purpose |
|---|---|---|
| 1 | `elizabeth_darcy_application_form.md` | Full application for final decision context |
| 2 | `APP-2024-5847_processing_notes.txt` | Human review result for comparison |
| 3 | `elizabeth_darcy_medical_summary.md` | Complete medical records |
| 4 | `elizabeth_darcy_financial_verification.md` | Complete financial records |

### Step 6: Start the Analysis
**What happens now**: Your agents will work together to analyze Elizabeth's application.

1. **Ask your Orchestrator Agent**: *"Please analyze Elizabeth Darcy's application and identify any gaps or missing information. Coordinate with the other agents to provide a complete assessment."*

2. **Watch what happens**: 
   - The Orchestrator queries the ClaimsPolicyFabricAgent tool for portfolio benchmarking data
   - Each domain agent examines their specialty area
   - They identify gaps in the application
   - They use the uploaded documents to fill those gaps
   - They compare Elizabeth to similar aviation professionals in our data
   - The Senior Underwriter Review Agent is escalated to if any findings conflict

3. **What to expect**:
   - **Medical Risk Agent** finds health-related gaps and resolves them using `elizabeth_darcy_medical_summary.md`
   - **Financial Suitability Agent** finds income/coverage gaps and resolves them using `elizabeth_darcy_financial_verification.md`
   - **Compliance Agent** finds regulatory gaps and resolves them
   - **Senior Underwriter Review Agent** steps in if domain assessments conflict or escalation is needed
   - **Orchestrator Agent** coordinates everything and synthesizes the final recommendation

**This process should take 5-10 minutes**

### Step 7: Review the Results
**What you should see**: Your agents will provide a complete analysis that includes:

#### **What the Human Underwriter Found (after 3 weeks)**
- Application scored 6.2/10 (too low to process)
- Found gaps in: medical history, financial info, beneficiary details
- **Result**: "CANNOT RATE - Too many gaps"
- **Status**: Application stuck, waiting for more information

#### **What Your AI Agents Should Find (in minutes)**
Each agent will identify the same gaps PLUS additional details:

**Medical Risk Agent Results**:
- ✅ Found the same medical gaps the human found
- ➕ PLUS: Specific aviation medical requirements
- ➕ PLUS: Used `elizabeth_darcy_medical_summary.md` to resolve gaps immediately
- **Result**: Can provide actual medical risk rating

**Financial Suitability Agent Results**:
- ✅ Found the same financial gaps the human found  
- ➕ PLUS: Aviation industry compensation analysis
- ➕ PLUS: Used `elizabeth_darcy_financial_verification.md` to verify coverage needs
- **Result**: Can confirm coverage is appropriate ($2.5M for $229,800 income)

**Compliance Agent Results**:
- ✅ Found the same regulatory gaps the human found
- ➕ PLUS: Colorado-specific requirements
- ➕ PLUS: Aviation-specific compliance needs
- **Result**: Can confirm all requirements are met

**Senior Underwriter Review Agent + Orchestrator Final Recommendation**:
- **Coverage**: $2,500,000 Term Life Insurance - **APPROVED**
- **Risk Level**: Standard Plus 
- **Annual Premium**: Approximately $3,400
- **Reasoning**: All gaps resolved, aviation peer comparison validates coverage amount

---

## What You Just Accomplished

### The Key Difference
- **Human Underwriter**: 3+ weeks → "CANNOT RATE" 
- **AI Multi-Agent System**: 10 minutes → Complete approval with specific terms

### Why This Matters for Your Business
1. **Faster Decisions**: Customers get answers in hours, not weeks
2. **Better Analysis**: AI found gaps humans missed AND resolved them
3. **Consistent Quality**: Every application gets the same thorough review
4. **Competitive Edge**: While competitors are still processing, you're already approving

### Technical Achievement 
You successfully demonstrated:
- Multi-agent AI coordination
- Automated gap detection and resolution
- Industry-specific data integration
- Complete underwriting workflow automation

---

## Expected Results & Learning Outcomes

### Gap Analysis and Resolution Report
Your multi-agent system should demonstrate:

#### **Gap Identification Capabilities**
- **Application Analysis**: Systematic identification of missing information
- **Specialist Expertise**: Each agent finds domain-specific gaps
- **Comprehensive Coverage**: No information gaps overlooked
- **Prioritization**: Gaps ranked by impact on underwriting decision

#### **Information Access and Integration**
- **Supporting Documentation**: Agents access complete medical and financial records
- **Enhanced Fabric Data Integration**: Use comprehensive lakehouse data including 50 aviation professionals and 16 aviation claims for benchmarking and validation
- **Aviation Peer Analysis**: Compare Elizabeth Darcy directly to similar aviation professionals (age 40-47, international routes, major airline captains)
- **Claims Pattern Recognition**: Analyze aviation-specific claims data (aviation accidents, medical emergencies, occupational risks) for risk model validation
- **Industry Coverage Standards**: Apply current aviation underwriting guidelines with peer comparison data from 22 aviation occupation types

#### **Final Assessment Results**
Agents should provide comprehensive evaluation:

#### **Medical Risk Assessment**
- **Health Status**: Hypertension well-controlled, excellent fitness
- **Family History**: Cardiovascular disease and diabetes noted, managed appropriately
- **Aviation Medical**: FAA certification current, no restrictions
- **Risk Rating**: Standard Plus (appropriate for controlled hypertension)

#### **Financial Justification**
- **Income Verification**: $229,800 annual compensation confirmed
- **Coverage Ratio**: 10.9x income (appropriate for aviation professional)
- **Family Needs**: $2.3M calculated need vs $2.5M requested
- **Financial Stability**: Excellent net worth ($713,100) and debt management

#### **Compliance Confirmation**
- **Beneficiary Structure**: Primary (spouse) and contingent (children) designated
- **Trust Arrangements**: Recommended for minor children
- **Aviation Compliance**: Safety records verified, international route risks assessed
- **Regulatory Requirements**: All federal and state requirements met

### Risk Assessment Insights
Agents should provide comprehensive analysis:

#### **Overall Risk Profile**
- **Applicant**: Captain Elizabeth Darcy, age 42, excellent aviation safety record
- **Occupation**: Class F aviation risk, but major airline with excellent safety protocols
- **Health**: Well-controlled hypertension, excellent fitness, strong family support
- **Financial**: Stable high income, appropriate coverage ratio, strong net worth

#### **Final Underwriting Recommendation**
- **Coverage**: $2,500,000 Term Life Insurance - APPROVED
- **Risk Classification**: Standard Plus (validated against 24 similar aviation professionals in Risk C category)
- **Annual Premium**: Approximately $3,400 (competitive for aviation professional, benchmarked against peer data)
- **Policy Conditions**: Standard aviation exclusions, medical monitoring continuation
- **Peer Validation**: Coverage ratio 10.9x income aligns with aviation industry standards (peer range: 8.5x-12.5x)
- **Claims Context**: Risk assessment informed by 16 aviation claims including 4 aviation accidents and 6 medical causes

#### **Decision Rationale**
- **Medical**: Controlled hypertension with excellent compliance meets Standard Plus criteria (validated against 6 aviation medical claims in peer data)
- **Financial**: Coverage fully justified by income and family protection needs (10.9x ratio within aviation industry peer range of 8.5x-12.5x)
- **Aviation Occupation**: Risks mitigated by excellent safety record and major airline employment (peer data shows 25% aviation accident rate among all aviation claims, but lower for major airline captains)
- **Peer Benchmarking**: Elizabeth's profile aligns with approved aviation professionals in similar age range (40-47) and coverage amounts ($2M-$3M)
- **Claims Intelligence**: Aviation claims data shows 81.2% approval rate with 16.2 day average resolution, confirming standard processing expectations
- **Overall**: Well-qualified applicant presenting standard plus risk profile with strong peer validation from comprehensive aviation dataset

### Automation Benefits Demonstrated

#### Accuracy Improvements
- Systematic gap detection with comprehensive regulatory compliance
- Industry-specific expertise application

#### Consistency Benefits
- Standardized review process for every application
- Complete documentation of decision process

---

## Discussion Questions for Your Team

### For Leadership
1. How could this speed up our customer experience?
2. What would faster underwriting mean for our sales team?
3. How does this compare to our current process?
4. What other products could benefit from this approach?

### For Technical Teams  
1. How did the agents coordinate their analysis?
2. What role did the aviation data play in the decision?
3. How could we scale this to hundreds of applications?
4. What additional data would enhance this further?

### For Sales Teams
1. How would customers react to getting decisions in hours vs. weeks?
2. What competitive advantages does this create?
3. How could this help with difficult cases like aviation professionals?
4. What other challenging occupations could this help with?

---

## Lab Success Checklist

By the end of this lab, you should have:

### ✅ Technical Success
- Created 4 specialized AI agents
- Connected them to insurance data  
- Uploaded Elizabeth Darcy's documents
- Received a complete underwriting recommendation

### ✅ Business Understanding  
- Saw AI identify gaps faster than humans
- Understood how aviation data improves decisions
- Recognized the speed advantage (minutes vs. weeks)
- Appreciated the consistency of AI analysis

### ✅ Strategic Value
- Envisioned using this for other complex cases
- Understood competitive advantages
- Recognized customer experience improvements
- Appreciated operational efficiency gains

---

## Next Steps

### Immediate Actions
1. **Share Results**: Discuss findings with your team
2. **Consider Applications**: Think about other use cases in your business
3. **Plan Implementation**: Consider how this could work in production

### Future Possibilities  
1. **Scale Up**: Apply to hundreds of applications daily
2. **Expand Coverage**: Add other insurance products
3. **Enhance Data**: Include more specialized datasets
4. **Integrate Systems**: Connect to core underwriting platforms

---

## Need Help? Quick Troubleshooting

### "I can't find my project"
- Go to [ai.azure.com](https://ai.azure.com) and look for "Team X Project"

### "My agents aren't responding"
- Make sure all 4 agents are created and connected to data
- Try asking the Senior Underwriter to start the analysis

### "No aviation data found"
- Ask an agent: *"How many aviation professionals are in our data?"*
- Expected: Around 50. If not, ask your instructor for help

### "Upload not working"
- Look for "Upload Document" button in the conversation area
- Upload all 4 files before starting analysis

---



---

## INSTRUCTOR GUIDANCE: Strategic Use of Processing Notes

### When to Introduce the Processing Notes
**TIMING**: Introduce `APP-2024-5847_processing_notes.txt` **immediately** when uploading the application form in Step 6.1

### Why This Timing is Critical
1. **Sets realistic context** - Shows this represents a real-world processing scenario with identified gaps
2. **Creates performance benchmark** - Provides baseline for comparing human vs. AI capabilities  
3. **Demonstrates workflow reality** - Shows how applications actually get stuck in traditional processes

### Recommended Instructor Script
```
"Before we let our AI agents analyze this application, let's see what happened 
with traditional human underwriting. This processing notes file shows the current 
status after 3 weeks of human review.

Notice the application scored 6.2/10 - below the threshold for processing. 
The underwriter concluded 'CANNOT RATE - Too many critical gaps' and the 
application is stuck waiting for documentation.

Now let's see if our AI agents can:
1. Identify the same gaps in minutes (not days)
2. Find additional gaps humans missed  
3. Access supporting documentation immediately
4. Provide complete recommendations instead of 'cannot rate'

This demonstrates the transformational impact of multi-agent AI on traditional 
insurance underwriting workflows."
```

### Key Learning Outcomes to Emphasize
- **Speed**: 3 weeks human process vs. 2-3 hours AI process
- **Completeness**: "Cannot rate" vs. complete risk assessment with specific recommendations
- **Accuracy**: Human found major gaps; AI finds same gaps plus aviation-specific requirements
- **Integration**: Human waits for documents; AI accesses all supporting information instantly

### Discussion Points During Analysis
- **Gap Identification**: "The human found these 3 major gaps. Watch as our AI agents identify the same ones plus additional details..."
- **Processing Efficiency**: "The human process is stuck waiting for documentation. Our AI agents access everything immediately..."
- **Decision Quality**: "After 3 weeks, the human could only say 'cannot rate.' Our AI agents will provide specific risk ratings and premium recommendations..."
- **Documentation**: Reference Azure AI Foundry documentation
- **Fallback Plan**: Manual analysis using provided guidelines if needed

---

##  Additional Resources

### Sterling Insurance Guidelines
- [Life Insurance Underwriting Guidelines](../underwriting_guidelines/life_insurance_underwriting_guidelines.md)
- [Special Cases & Exceptions](../underwriting_guidelines/special_cases_exceptions.md)
- [Risk Assessment Matrix](../underwriting_guidelines/risk_assessment_matrix.md)

### Azure AI Foundry Documentation
- [Multi-Agent Systems Guide](https://docs.microsoft.com/azure/ai-foundry/multi-agent)
- [Agent Coordination Patterns](https://docs.microsoft.com/azure/ai-foundry/agent-coordination)
- [Fabric Integration](https://docs.microsoft.com/azure/ai-foundry/fabric-integration)

### Industry Context
- [Aviation Insurance Risks](../underwriting_guidelines/special_cases_exceptions.md#aviation--transportation)
- [Occupation Risk Classifications](../underwriting_guidelines/risk_assessment_matrix.md#occupation-risk-classification)
- [Competitive Intelligence](../underwriting_guidelines/competitive_market_intelligence.md)

---

*This lab demonstrates multi-agent insurance underwriting - where AI agents collaborate to provide faster, more accurate, and more consistent risk assessments.*
