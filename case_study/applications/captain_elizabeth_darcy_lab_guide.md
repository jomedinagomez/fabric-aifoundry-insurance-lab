# Captain Elizabeth Darcy Case Study Lab Guide
*Multi-Agent Insurance Underwriting Analysis*

## Lab Overview

This hands-on lab demonstrates advanced multi-agent capabilities for complex insurance underwriting scenarios. You'll analyze Captain Elizabeth Darcy's life insurance application using specialized AI agents that collaborate to identify gaps, assess risks, and generate comprehensive underwriting recommendations.

**Duration**: 45 minutes (25 min case study + 20 min multi-agent setup)  
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
1. **Experience Multi-Agent Coordination** - See how specialized agents collaborate
2. **Understand Gap Detection** - Learn how AI identifies missing information
3. **Apply Industry Knowledge** - Use underwriting guidelines for real decisions
4. **Demonstrate Automation Benefits** - Compare AI vs. manual processing

---

## Phase 1: Azure AI Foundry Multi-Agent Setup (20 minutes)

### Step 1: Access Your AI Foundry Project
1. **Navigate to Azure AI Foundry** ([ai.azure.com](https://ai.azure.com))
2. **Select Your Project**: Use project assigned to your team (Team 1-10)
3. **Verify Permissions**: Ensure you can create agents and access resources

### Step 2: Create Specialized Agent System
You'll create **4 specialized agents** that work together:

#### **Medical Risk Assessment Agent**
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

#### **Financial Analysis Agent**
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

#### **Regulatory Compliance Agent**
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

#### **Master Orchestrator Agent**
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

### Step 3: Connect Fabric Data Agent
1. **Add Resource**: Connect your published Fabric Data Agent
2. **Configure Access**: Ensure all agents can query the lakehouse data
3. **Test Connection**: Verify agents can access policy and claims data

### Step 4: Agent Configuration
For each agent, configure:
- **Data Access**: Connect to Fabric Data Agent resource
- **Instructions**: Use the role-specific instructions above
- **Capabilities**: Enable file analysis and data querying
- **Collaboration**: Ensure agents can coordinate with each other

---

## Phase 2: Captain Darcy Case Study Analysis (25 minutes)

### Step 5: Upload Application Documents

You'll work with **4 separate document files** that agents must analyze:

#### Document 1: elizabeth_darcy_application_form.md
- **Purpose**: Completed application form with subtle gaps and incomplete information
- **Content**: Application appears complete but contains vague responses, missing details, and insufficient information that agents must identify
- **Agent Task**: Analyze responses to identify where additional information or clarification is needed for proper underwriting

#### Document 2: elizabeth_darcy_medical_summary.md  
- **Purpose**: Complete medical documentation for gap resolution
- **Content**: Comprehensive medical history, family history, physical exam results, and aviation medical certification
- **Agent Task**: Use this complete information to fill medical gaps identified in the application

#### Document 3: elizabeth_darcy_financial_verification.md
- **Purpose**: Complete financial documentation for gap resolution  
- **Content**: Verified income, tax returns, asset/liability statements, and coverage justification analysis
- **Agent Task**: Use this complete information to fill financial gaps identified in the application

#### Document 4: APP-2024-5847_processing_notes.txt
- **Purpose**: Internal underwriting notes showing what documentation is still needed
- **Content**: Processing timeline, required documentation checklist, and underwriter observations
- **Agent Task**: Reference this to understand what specific information gaps need to be filled

### Step 6: Execute Multi-Agent Analysis Workflow

#### 6.1 Initial Gap Detection Phase
1. **Upload elizabeth_darcy_application_form.md** to your multi-agent system
2. **Also provide APP-2024-5847_processing_notes.txt** for context on what gaps need identification
3. **Trigger Gap Analysis**: Each specialist agent analyzes their domain for insufficient information
4. **Monitor Gap Detection**: Watch agents identify where responses are too vague or incomplete for proper underwriting

#### 6.2 Gap Identification Results
Each specialist agent will identify specific gaps from the application form:

**Medical Risk Agent** identifies:
- Vague family medical history responses that need detailed clarification
- Incomplete medical condition details requiring specific information  
- Missing detailed exercise and lifestyle information for risk assessment
- Need for complete medical documentation to make proper risk determination

**Financial Analysis Agent** identifies:
- Approximate income figures that need precise verification
- Vague asset and debt descriptions requiring specific amounts and documentation
- Coverage justification based on peer comparison rather than needs analysis
- Need for detailed financial documentation to verify appropriateness of coverage amount

**Compliance Agent** identifies:
- Incomplete beneficiary designation information missing required details
- Unclear trust arrangements that need proper legal structure
- Vague estate planning status requiring coordination assessment
- Need for complete regulatory compliance documentation

#### 6.3 Information Access and Gap Resolution
Agents then access the supporting documentation files to fill gaps:
- **Medical Agent**: Uses `elizabeth_darcy_medical_summary.md` to provide full health risk assessment
- **Financial Agent**: Uses `elizabeth_darcy_financial_verification.md` to verify coverage justification
- **Compliance Agent**: Uses regulatory information from supporting docs to complete compliance requirements

#### 6.4 Data Integration with Fabric Agent
Simultaneously, agents access the Fabric Data Agent to:
- **Compare similar aviation professional profiles** from the lakehouse
- **Benchmark coverage amounts** against industry data  
- **Analyze claim patterns** for similar occupations and risk factors
- **Validate risk ratings** against historical underwriting data

### Step 7: Collaborative Decision Making

#### 7.1 Agent Coordination and Gap Resolution
Watch as agents collaborate to resolve identified gaps:
```
Medical Agent → Financial Agent: "Family history shows cardiovascular 
risk, but applicant has excellent health management. Medical rating 
Standard Plus appropriate."

Financial Agent → Medical Agent: "Income of $229,800 verified, 
coverage ratio 10.9x is appropriate for aviation professional 
with this risk profile."

Compliance Agent → Master Orchestrator: "All beneficiary designations 
now complete, trust arrangements recommended for minor children."

Master Orchestrator → All Agents: "Gap resolution complete. 
Synthesizing final recommendation based on complete information."
```

#### 7.2 Master Orchestrator Synthesis
The Senior Underwriter agent will:
1. **Compile Gap Resolutions** - Integrate all identified and resolved gaps
2. **Synthesize Risk Assessment** - Combine medical, financial, and compliance findings
3. **Apply Industry Benchmarks** - Use Fabric data for comparative analysis
4. **Generate Final Recommendation** - Provide comprehensive underwriting decision

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
- **Fabric Data Integration**: Use lakehouse data for benchmarking and validation
- **Cross-Reference Analysis**: Compare applicant to similar profiles in database
- **Industry Standards**: Apply current underwriting guidelines and market practices

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
- **Risk Classification**: Standard Plus 
- **Annual Premium**: Approximately $3,400 (competitive for aviation professional)
- **Policy Conditions**: Standard aviation exclusions, medical monitoring continuation

#### **Decision Rationale**
- **Medical**: Controlled hypertension with excellent compliance meets Standard Plus criteria
- **Financial**: Coverage fully justified by income and family protection needs
- **Occupation**: Aviation risks mitigated by excellent safety record and major airline employment
- **Overall**: Well-qualified applicant presenting standard plus risk profile

### Automation Benefits Demonstrated

#### **Speed Comparison**
- **Manual Process**: 2-3 weeks for complete review
- **Multi-Agent Process**: 2-3 hours for gap identification and preliminary assessment

#### **Accuracy Improvements**
- **Systematic Gap Detection**: No overlooked requirements
- **Regulatory Compliance**: Automated compliance checking
- **Risk Correlation**: Data-driven risk pattern analysis

#### **Consistency Benefits**
- **Standardized Analysis**: Same thorough review for every application
- **Audit Trail**: Complete documentation of decision process
- **Quality Assurance**: Multiple agent validation of findings

---

## Discussion Questions

Use these questions for team discussion and reflection:

### Technical Implementation
1. **How did agent specialization improve analysis quality?**
2. **What role did the Fabric Data Agent play in benchmarking?**
3. **How could this system scale to handle hundreds of applications daily?**

### Business Impact
1. **What's the ROI of this multi-agent approach vs. manual processing?**
2. **How does this improve customer experience and satisfaction?**
3. **What compliance benefits does systematic analysis provide?**

### Industry Applications
1. **How could this approach apply to other insurance products?**
2. **What other industries could benefit from similar multi-agent systems?**
3. **How does this position Sterling Insurance competitively?**

---

## 📈 Success Metrics

By the end of this lab, your team should have:

### **Technical Achievements**
- [ ] Successfully created 4 specialized agents
- [ ] Connected agents to Fabric Data Agent resource
- [ ] Executed coordinated gap analysis workflow
- [ ] Generated comprehensive underwriting report

### **Business Understanding**
- [ ] Identified all major information gaps
- [ ] Understood aviation occupation risk factors
- [ ] Appreciated multi-agent coordination benefits
- [ ] Recognized automation value proposition

### **Strategic Insights**
- [ ] Envisioned scaled implementation across Sterling Insurance
- [ ] Understood competitive advantages of AI-powered underwriting  
- [ ] Appreciated customer experience improvements
- [ ] Recognized operational efficiency gains

---

## 🔄 Next Steps & Real-World Application

### Immediate Follow-Up
1. **Complete Application**: Use gap analysis to request missing information
2. **Risk Rating**: Apply findings to determine final risk classification
3. **Premium Calculation**: Use risk assessment for pricing decisions

### Production Implementation
1. **System Integration**: Connect to core underwriting systems
2. **Workflow Automation**: Implement triggered multi-agent analysis
3. **Quality Assurance**: Establish human oversight protocols
4. **Performance Monitoring**: Track accuracy and efficiency metrics

### Continuous Improvement
1. **Agent Training**: Update agents based on new regulations and patterns
2. **Data Enhancement**: Expand lakehouse with additional risk factors
3. **Process Optimization**: Refine workflows based on usage patterns
4. **Regulatory Updates**: Keep compliance agents current with law changes

---

## 🆘 Troubleshooting Guide

### Common Issues

#### **Agents Not Communicating**
- **Check resource connections** - Ensure all agents can access Fabric Data Agent
- **Verify permissions** - Confirm agents have necessary access rights
- **Review instructions** - Make sure agent roles are clearly defined

#### **Gap Detection Incomplete**
- **Document upload issues** - Ensure all 3 documents uploaded successfully
- **Missing context** - Verify agents have underwriting guidelines access
- **Coordination failures** - Check agent-to-agent communication logs

#### **Data Access Problems**
- **Fabric connection** - Test Fabric Data Agent connectivity
- **Query failures** - Verify lakehouse data accessibility
- **Authentication issues** - Check Azure permissions

### Getting Help
- **Lab Facilitators**: Available for technical assistance
- **Team Collaboration**: Work with teammates to solve issues
- **Documentation**: Reference Azure AI Foundry documentation
- **Fallback Plan**: Manual analysis using provided guidelines if needed

---

## 📚 Additional Resources

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

*This lab demonstrates the future of insurance underwriting - where AI agents collaborate to provide faster, more accurate, and more consistent risk assessments while maintaining the human judgment needed for complex cases.*
