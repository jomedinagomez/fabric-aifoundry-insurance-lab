# Lab Planning Session Insights & Decisions
*Session Date: August 4, 2025*

## Lab Overview
- **Duration**: 90 minutes
- **Participants**: 50 attendees in-person
- **Teams**: 10 teams (5-6 people each)
- **Focus**: Microsoft Fabric OneLake + Data Agents + Azure AI Foundry integration
- **Business Context**: Insurance policy underwriting evaluation

---

## Final Lab Structure

### Timing Decisions Made
**Original vs. Final Structure:**
- Stage 1: Data Upload & Agent Creation: 30 minutes (10-40 min)
- Stage 2: Azure AI Foundry Integration: **30 minutes** (40-70 min) ✅
- Stage 3: Policy Review Case Study: **25 minutes** (70-85 min) ✅
- Wrap-up: 5 minutes (85-90 min)

**Key Decision**: Extended Stage 2 to 30 minutes and Stage 3 to 25 minutes to allow more time for practical scenario demonstration.

---

## Dataset Strategy

### Data Architecture Decision
**Structured Data (for Fabric Data Agent - CSV/Tables):**
1. **Claims History Table** - Historical claim patterns for risk assessment
2. **Policy Portfolio Table** - Current active policies for comparison  
3. **Customer Demographics** - Demographic factors influencing underwriting
4. **Risk Factors Table** - Lookup table for risk calculations

**Unstructured Data (for Policy Review):**
- Policy applications in multiple formats (PDF, TXT, DOCX)
- Medical exam notes
- Financial statements
- Interview notes

**Guidelines Format:**
- Markdown files for easy reading and reference
- Focus on life insurance (Prudential's core business)

---

## Business Context: Prudential Profile

### Company Focus
- **Primary Business**: Life insurance (core competency since 1875)
- **Product Types**: Term life, whole life, universal life policies
- **Secondary Products**: Disability insurance, long-term care
- **Brand**: "Rock of Gibraltar" - stability and reliability

### Insurance Types Chosen
- **Primary**: Life Insurance underwriting (most complex and valuable demo)
- **Secondary**: Disability insurance (supporting guidelines)
- **Rationale**: Complex enough for meaningful AI analysis, realistic business scenarios

---

## Value Proposition Strategy

### Dual Focus Decision: Technical + Business Value

**Technical Capabilities Showcase:**
- **Data Integration**: Structured lakehouse data + unstructured policy documents
- **Complex Reasoning**: Multi-factor risk analysis across datasets
- **Real-time Recommendations**: Dynamic pricing and coverage suggestions
- **Explainable AI**: Clear reasoning for decisions

**Business Value Demonstration:**
- **Speed**: Manual underwriting (2-3 days) → AI analysis (minutes)
- **Accuracy**: Risk prediction with confidence scores
- **Revenue**: Optimal pricing vs. competitors  
- **Customer Experience**: Instant pre-approval/conditional offers

### Enhanced Scenario: "AI-Powered Underwriting Assistant"
- Multi-dimensional analysis combining risk assessment, competitive pricing, and customer experience
- Clear ROI demonstration through speed, accuracy, and revenue optimization
- Real-world business impact that resonates with diverse audience

---

## Key Design Principles

### User Experience
- **Engagement**: Enhanced from basic underwriting to comprehensive AI assistant
- **Wow Factor**: Instant decisions with detailed explanations
- **Relatability**: Focus on customer experience and business outcomes

### Technical Demonstration
- **Integration Complexity**: Multiple data sources and formats
- **AI Sophistication**: Pattern recognition, competitive analysis, explainable decisions
- **Real-world Applicability**: Industry-standard processes and metrics

### Time Management
- **25-minute case study**: Sufficient time for meaningful analysis
- **Multi-dimensional demo**: Risk + pricing + customer experience
- **Clear outcomes**: Specific business metrics and technical capabilities

---

## Success Metrics Defined

### Phase 1: Data Foundation (30 min)
- Successful lakehouse creation and data upload
- Working Fabric Data Agent with query capabilities
- Published agent ready for AI Foundry integration

### Phase 2: AI Integration (30 min)  
- Connected Fabric Data Agent to AI Foundry
- Enhanced agent with advanced reasoning capabilities
- Successfully tested multi-source data analysis

### Phase 3: Business Value Demo (25 min)
- **Speed Demo**: Instant underwriting decisions
- **Accuracy Demo**: Risk scoring with historical validation
- **Revenue Demo**: Competitive pricing recommendations
- **Explanation Demo**: Clear AI decision reasoning

---

## File Structure Created

```
case_study/
└── underwriting_guidelines/
    ├── life_insurance_underwriting_guidelines.md
    ├── disability_insurance_guidelines.md
    ├── risk_assessment_matrix.md
    ├── competitive_market_intelligence.md
    └── special_cases_exceptions.md
```

### Content Highlights
- **Comprehensive Risk Framework**: Age, occupation, health, financial factors
- **Competitive Market Analysis**: Pricing strategies and positioning with realistic 2025 rates
- **Decision Automation Rules**: Instant approval, conditional, manual review criteria
- **Business Value Metrics**: Speed, revenue, customer experience KPIs
- **AI Explanation Framework**: Required elements for decision transparency
- **Multi-File Integration**: 5 interconnected documents requiring cross-referencing
- **Realistic Data**: Industry-standard premiums, coverage limits, and risk factors

### Realistic Data Standards Applied
- **Term Life Premiums**: $32.50/month (Male 30, $500k) - industry-accurate rates
- **Coverage Limits**: Up to $10M term life, $15M universal life - realistic maximums
- **Medical Exam Thresholds**: $500k for term life, $250k for whole life
- **Disability Benefits**: Up to $30k/month maximum - industry standard
- **Risk Scoring**: Refined instant approval criteria (age 18-50, ≤15x income)
- **Competitive Positioning**: Accurate relative pricing vs. major competitors

---

## Key Takeaways for Lab Execution

### Critical Success Factors
1. **Data Quality**: Ensure sample datasets demonstrate clear patterns
2. **Agent Instructions**: Pre-built prompts that showcase multi-dimensional analysis
3. **Case Study Selection**: Choose policy applications that highlight AI capabilities
4. **Business Context**: Emphasize real-world impact and ROI throughout

### Potential Challenges & Mitigations
- **Time Constraints**: Pre-populate some data if needed to stay on schedule
- **Technical Issues**: Have backup scenarios and troubleshooting guides ready
- **Engagement**: Use competitive pricing and instant decisions as "wow moments"
- **Mixed Audience**: Balance technical depth with business value throughout

### Next Steps Required
1. Create sample structured datasets (CSV files) - **READY FOR CREATION**
2. Develop sample policy applications (unstructured documents) - **READY FOR CREATION**
3. Write step-by-step participant guides
4. Prepare instructor notes with troubleshooting tips
5. Design sample agent prompts/instructions

### Files Created & Validated
✅ **5 Comprehensive Guidelines Files**:
- Life insurance underwriting (main policies, risk framework, decisions)
- Disability insurance (occupation classes, medical requirements)
- Risk assessment matrix (detailed scoring methodology)
- Competitive market intelligence (2025 rates, positioning)
- Special cases & exceptions (edge cases, complex scenarios)

✅ **Data Realism Review Completed**:
- Premium rates updated to 2025 market standards
- Coverage limits aligned with industry maximums
- Medical exam thresholds corrected to realistic levels
- Risk scoring criteria refined for authenticity
- Cross-file consistency validated

---

*This document captures the strategic decisions and insights from the lab planning session to ensure consistent execution and future reference.*
