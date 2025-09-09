# Three-Question Demo Script for Insurance Underwriting Multi-Agent System

## Overview
This script demonstrates a progressive interaction with the multi-agent underwriting system using the Elizabeth Darcy aviation insurance case. Each question builds upon the previous response, showcasing different aspects of the underwriting workflow.

---

## **TURN 1: Initial Case Assessment**

### **Question to Ask:**
```
"Please analyze the Elizabeth Darcy application for aviation insurance coverage and provide your initial underwriting assessment."
```

### **Expected Agent Flow:**
1. **Senior Underwriter Agent** (Primary) receives the request
2. **Orchestrator Agent** coordinates the analysis
3. **Financial Analysis Agent** reviews financial documents
4. **Medical Risk Assessment Agent** evaluates health factors
5. **Compliance Agent** checks regulatory requirements

### **Expected Response Elements:**
- Initial risk classification (Standard/Substandard/Declined)
- Key risk factors identified
- Financial capacity assessment
- Medical concerns flagged
- Compliance status overview
- Preliminary premium indication

### **What This Demonstrates:**
- Complete multi-agent orchestration
- Comprehensive risk evaluation
- Business-realistic workflow
- Agent specialization and coordination

---

## **TURN 2: Deep Dive Risk Analysis**

### **Question to Ask (based on Turn 1 response):**
```
"What specific risk factors concern you most about Elizabeth Darcy's aviation profile, and how do they impact our underwriting decision?"
```

### **Expected Agent Focus:**
1. **Senior Underwriter Agent** provides executive perspective
2. **Medical Risk Assessment Agent** elaborates on health concerns
3. **Financial Analysis Agent** details financial risk factors
4. **Compliance Agent** highlights regulatory considerations

### **Expected Response Elements:**
- Detailed risk factor breakdown
- Impact assessment for each concern
- Risk mitigation strategies
- Premium adjustments or exclusions
- Comparative analysis with underwriting guidelines

### **What This Demonstrates:**
- Agent specialization depth
- Risk quantification capabilities
- Business logic application
- Decision-making transparency

---

## **TURN 3: Final Decision and Recommendations**

### **Question to Ask:**
```
"Based on your complete analysis, what is your final underwriting decision for Elizabeth Darcy's aviation insurance application, including specific terms and conditions?"
```

### **Expected Agent Response:**
1. **Senior Underwriter Agent** delivers final decision
2. **Orchestrator Agent** summarizes complete analysis
3. **All Specialized Agents** provide final input in their areas

### **Expected Response Elements:**
- **FINAL DECISION:** Approve/Decline/Conditional Approval
- **Premium Quote:** Specific dollar amount with justification
- **Policy Terms:** Coverage limits, deductibles, exclusions
- **Special Conditions:** Additional requirements or restrictions
- **Documentation:** Required follow-up items
- **Risk Management:** Ongoing monitoring recommendations

### **What This Demonstrates:**
- Executive decision-making authority
- Complete underwriting process
- Business outcome delivery
- Professional documentation
- Risk management planning

---

## **Demo Success Criteria**

### **Technical Validation:**
- ✅ All 5 agents participate appropriately
- ✅ Agent hierarchy is respected (Senior Underwriter authority)
- ✅ File references work correctly
- ✅ Orchestration flows smoothly

### **Business Validation:**
- ✅ Realistic insurance terminology used
- ✅ Proper underwriting logic applied
- ✅ Professional communication style
- ✅ Actionable business outcomes delivered

### **User Experience Validation:**
- ✅ Responses build logically across turns
- ✅ Information depth increases appropriately
- ✅ Clear decision rationale provided
- ✅ Professional industry standards demonstrated

---

## **Tips for Best Demo Results:**

### **Agent Setup:**
- Ensure all agents have access to Elizabeth Darcy case files
- Verify ClaimsPolicyFabricAgent tool is properly configured
- Confirm agent hierarchy is correctly established

### **Question Timing:**
- Wait for complete responses before asking next question
- Allow agents to fully coordinate in each turn
- Give time for comprehensive analysis

### **Follow-up Options:**
If you want to extend beyond 3 questions:
- "How would this decision change if Elizabeth's medical condition improved?"
- "What would be the impact if she wanted to increase coverage limits?"
- "Show me the claims data analysis that supports this decision"

---

## **Expected Demo Duration:**
- **Turn 1:** 2-3 minutes (comprehensive initial analysis)
- **Turn 2:** 1-2 minutes (focused risk deep dive)
- **Turn 3:** 1-2 minutes (final decision delivery)
- **Total:** 4-7 minutes for complete demonstration

---

## **Backup Questions (if needed):**

### **If agents need more direction:**
- "Focus specifically on the aviation risk factors in Elizabeth's case"
- "What does our claims data tell us about similar pilot profiles?"
- "Walk me through your decision matrix for this case"

### **If you want to show data integration:**
- "Show me how the claims portfolio data influences this decision"
- "What does our historical data say about similar cases?"
- "How does this compare to our risk assessment matrix?"

---

*This script is designed to showcase the full capabilities of your multi-agent insurance underwriting system in a structured, business-realistic demonstration.*
