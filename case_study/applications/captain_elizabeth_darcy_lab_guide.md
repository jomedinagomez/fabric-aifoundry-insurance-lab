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

### Step 2: Create Your First Agent (Medical Risk Analyzer)
You'll create 4 specialized agents. Let's start with the first one:

1. **Click "Create Agent"** (or similar button on your dashboard)
2. **Name your agent**: Type "Medical Risk Analyzer"  
3. **Copy and paste the instructions below** into the agent's instruction box:

#### **Medical Risk Assessment Agent Instructions**
```yaml
Name: Medical Risk Analyzer
Role: Identify medical information gaps and assess health risks
Capabilities:
  - Detect missing medical information in applications
  - Analyze family history and genetic risk factors
  - Apply medical underwriting guidelines
  - Cross-reference aviation medical requirements
  - Access supporting medical documentation
Instructions: |
  You are a medical underwriting specialist. Your primary tasks are:
  
  1. GAP IDENTIFICATION: Analyze applications to identify insufficient medical information:
     - Look for vague responses about family medical history
     - Identify incomplete health condition details
     - Find missing medical documentation references
     - Spot unclear medication or treatment information
     
  2. RISK ASSESSMENT: When gaps are identified, use available supporting documentation to:
     - Evaluate genetic risk factors from complete family history
     - Assess current health status and controlled conditions
     - Review aviation medical requirements and compliance
     - Determine appropriate medical risk ratings
     
  3. AVIATION-SPECIFIC ANALYSIS: For aviation professionals:
     - Verify FAA medical certificate compliance and details
     - Assess fitness for international duty requirements
     - Evaluate occupational health risks and management
     - Review stress and fatigue management capabilities
     
  4. RECOMMENDATIONS: Provide clear medical underwriting recommendations with risk ratings and any conditions based on complete medical information.
```

4. **Save your agent** when done
5. **Repeat this process** for the other 3 agents below:

#### **Financial Analysis Agent Instructions** 
(Create a second agent called "Financial Underwriter")
```yaml
Name: Financial Underwriter
Role: Identify financial gaps and verify coverage justification
Capabilities:
  - Detect missing financial documentation
  - Analyze income-to-coverage ratios
  - Assess financial stability and justification
  - Review asset/liability positions
  - Access complete financial records
Instructions: |
  You are a financial underwriting expert. Your primary responsibilities are:
  
  1. GAP DETECTION: Identify insufficient financial information in applications:
     - Look for vague income descriptions without specific amounts
     - Find missing or incomplete asset and liability details
     - Identify unclear coverage justification reasoning
     - Spot missing documentation references
     
  2. FINANCIAL ANALYSIS: Use supporting documentation to:
     - Verify specific income levels and stability from complete records
     - Calculate appropriate coverage multiples using verified data
     - Assess debt-to-income ratios from detailed financial statements
     - Evaluate family financial needs based on complete information
     
  3. OCCUPATION-SPECIFIC EVALUATION: For aviation professionals:
     - Understand airline industry compensation structures and verify details
     - Assess career stability and longevity using employment records
     - Consider industry-specific financial risks and benefits
     - Evaluate international work considerations and compensation
     
  4. COVERAGE JUSTIFICATION: Using complete financial documentation, determine if requested coverage is:
     - Appropriate for verified income level
     - Justified by documented family financial needs
     - Within industry guidelines for the occupation
     - Financially sustainable based on complete financial picture
```

#### **Regulatory Compliance Agent Instructions**
(Create a third agent called "Compliance Officer")
```yaml
Name: Compliance Officer
Role: Identify compliance gaps and ensure regulatory adherence
Capabilities:
  - Detect missing regulatory documentation
  - Verify beneficiary designation completeness
  - Check state-specific requirements
  - Ensure aviation occupation compliance
  - Access regulatory guidelines
Instructions: |
  You are a regulatory compliance specialist. Your key functions are:
  
  1. COMPLIANCE GAP IDENTIFICATION: Find insufficient regulatory information:
     - Look for incomplete beneficiary designations and missing details
     - Identify vague or missing trust arrangement information
     - Find unclear estate planning coordination
     - Spot missing required regulatory documentation
     
  2. BENEFICIARY ANALYSIS: When beneficiary information is incomplete or vague:
     - Recommend proper primary/contingent structure using complete information
     - Identify trust needs for minor children based on family details
     - Ensure proper legal designations are complete and accurate
     - Verify estate planning coordination using available documentation
     
  3. AVIATION OCCUPATION COMPLIANCE: For airline professionals:
     - Verify safety record documentation completeness
     - Check international route risk assessments and requirements
     - Ensure proper aviation risk disclosures are adequate
     - Validate FAA compliance requirements using detailed records
     
  4. REGULATORY ADHERENCE: Using all available documentation, ensure applications meet:
     - Federal insurance regulations and requirements
     - State insurance law requirements specific to Colorado
     - Aviation-specific regulatory compliance needs
     - Anti-money laundering compliance standards
```

#### **Main Orchestrator Agent Instructions**
(Create a fourth agent called "Senior Underwriter")
```yaml 
Name: Senior Underwriter
Role: Coordinate analysis and synthesize final recommendations
Capabilities:
  - Coordinate multi-agent gap analysis
  - Synthesize specialist recommendations
  - Access all supporting documentation
  - Make final underwriting decisions
  - Generate comprehensive reports
Instructions: |
  You are a senior underwriter who orchestrates the complete underwriting process. Your responsibilities include:
  
  1. GAP COORDINATION: Manage gap identification across all specialists:
     - Collect gap reports from medical, financial, and compliance agents
     - Prioritize gaps by impact on underwriting decision
     - Coordinate access to supporting documentation
     - Track gap resolution progress
     
  2. INFORMATION SYNTHESIS: When agents find and fill gaps:
     - Integrate medical risk assessments
     - Combine financial justification analysis
     - Incorporate compliance requirements
     - Resolve any conflicting recommendations
     
  3. AVIATION EXPERTISE: Apply specialized knowledge of aviation risks:
     - Understand airline industry dynamics
     - Assess international route exposure
     - Evaluate aviation safety factors
     - Apply aviation-specific underwriting guidelines
     
  4. FINAL DECISION MAKING: Generate comprehensive recommendations:
     - Provide final risk classification
     - Determine appropriate premium pricing
     - Identify any policy conditions or exclusions
     - Explain reasoning and decision rationale
     
  5. PROCESS EFFICIENCY: Demonstrate automation benefits:
     - Show faster processing compared to manual review
     - Highlight systematic gap identification
     - Prove consistency in decision-making
     - Document complete audit trail
```

### Step 3: Connect Your Agents to Data
**What this does**: This connects your agents to the insurance data they need to make decisions.

1. **Look for "Add Resource" or "Connect Data"** in your project
2. **Find and select "Fabric Data Agent"** from the list
3. **Confirm the connection** - you should see it's connected to:
   - Policy data with aviation professionals (records LIF-1800 to LIF-1849)
   - Claims data with aviation claims (records CLM-4001 to CLM-4016)

**Quick Test**: Ask one of your agents: *"How many aviation professionals are in our data?"*
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

### Step 4: Agent Configuration
For each agent, configure:
- **Data Access**: Connect to enhanced Fabric Data Agent resource with aviation datasets
- **Instructions**: Use the role-specific instructions above
- **Capabilities**: Enable file analysis, data querying, and aviation peer comparison
- **Collaboration**: Ensure agents can coordinate with each other
- **Aviation Intelligence**: Access to 50 aviation professionals and 16 aviation claims for benchmarking

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

### Step 4: Upload Elizabeth Darcy's Documents
**What you're doing**: Giving your agents the insurance application to analyze.

You have 4 documents to upload. **Upload them in this order**:

#### **Document 1: Upload the Application** 
- **File**: `elizabeth_darcy_application_form.md`
- **What it is**: Elizabeth's life insurance application (has gaps on purpose)
- **How to upload**: Look for "Upload File" or "Add Document" button and select this file

#### **Document 2: Upload the Processing Notes**
- **File**: `APP-2024-5847_processing_notes.txt` 
- **What it is**: Shows what a human underwriter found after 3 weeks of work
- **Why important**: This shows the human said "CANNOT RATE" - let's see if AI can do better

#### **Document 3: Upload Medical Records**
- **File**: `elizabeth_darcy_medical_summary.md`
- **What it is**: Complete medical information that fills in the gaps

#### **Document 4: Upload Financial Records** 
- **File**: `elizabeth_darcy_financial_verification.md`
- **What it is**: Complete financial information that fills in the gaps

### Step 5: Start the Analysis
**What happens now**: Your agents will work together to analyze Elizabeth's application.

1. **Ask your Senior Underwriter agent**: *"Please analyze Elizabeth Darcy's application and identify any gaps or missing information. Coordinate with the other agents to provide a complete assessment."*

2. **Watch what happens**: 
   - Each agent will examine their specialty area
   - They'll identify gaps in the application
   - They'll use the complete documents to fill those gaps
   - They'll compare Elizabeth to similar aviation professionals in our data

3. **What to expect**:
   - **Medical Agent** finds health-related gaps and resolves them
   - **Financial Agent** finds income/coverage gaps and resolves them  
   - **Compliance Agent** finds regulatory gaps and resolves them
   - **Senior Underwriter** coordinates everything and makes final recommendation

**This process should take 5-10 minutes**

### Step 6: Review the Results
**What you should see**: Your agents will provide a complete analysis that includes:

#### **What the Human Underwriter Found (after 3 weeks)**
- Application scored 6.2/10 (too low to process)
- Found gaps in: medical history, financial info, beneficiary details
- **Result**: "CANNOT RATE - Too many gaps"
- **Status**: Application stuck, waiting for more information

#### **What Your AI Agents Should Find (in minutes)**
Each agent will identify the same gaps PLUS additional details:

**Medical Agent Results**:
- ✅ Found the same medical gaps the human found
- ➕ PLUS: Specific aviation medical requirements
- ➕ PLUS: Used complete medical records to resolve gaps immediately
- **Result**: Can provide actual medical risk rating

**Financial Agent Results**:
- ✅ Found the same financial gaps the human found  
- ➕ PLUS: Aviation industry compensation analysis
- ➕ PLUS: Used complete financial records to verify coverage needs
- **Result**: Can confirm coverage is appropriate ($2.5M for $229,800 income)

**Compliance Agent Results**:
- ✅ Found the same regulatory gaps the human found
- ➕ PLUS: Colorado-specific requirements
- ➕ PLUS: Aviation-specific compliance needs
- **Result**: Can confirm all requirements are met

**Senior Underwriter Final Recommendation**:
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
