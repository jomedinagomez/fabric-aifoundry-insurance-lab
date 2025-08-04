# Life Insurance Underwriting Guidelines
## AI-Powered Underwriting Assistant - Prudential Standards

### Overview
These guidelines enable rapid, data-driven underwriting decisions by combining historical performance data, competitive market analysis, and multi-factor risk assessment to deliver optimal customer outcomes and business value.

---

## Policy Types & Basic Requirements

### Term Life Insurance
- **Age Range**: 18-75 years
- **Coverage Limits**: $25,000 - $10,000,000
- **Term Options**: 10, 15, 20, 30 years
- **Medical Exam Required**: Coverage > $500,000
- **Maximum Coverage**: 25x annual income (30x for high earners)

### Whole Life Insurance  
- **Age Range**: 0-75 years
- **Coverage Limits**: $10,000 - $5,000,000
- **Cash Value Component**: Yes
- **Medical Exam Required**: Coverage > $250,000
- **Maximum Coverage**: 20x annual income

### Universal Life Insurance
- **Age Range**: 0-75 years
- **Coverage Limits**: $50,000 - $15,000,000
- **Flexible Premiums**: Yes
- **Medical Exam Required**: Coverage > $500,000
- **Maximum Coverage**: 30x annual income

---

## Risk Assessment Framework

### Primary Risk Factors

#### Age-Based Risk Scoring
| Age Range | Risk Score | Premium Multiplier |
|-----------|------------|-------------------|
| 18-30     | 1-2        | 1.0x              |
| 31-45     | 2-4        | 1.1x              |
| 46-60     | 4-7        | 1.3x              |
| 61-75     | 7-10       | 1.8x              |

#### Occupation Risk Categories
| Risk Level | Occupations | Score | Premium Impact |
|------------|-------------|-------|----------------|
| **Low Risk** | Office workers, teachers, engineers | 1-2 | No adjustment |
| **Medium Risk** | Construction, truck drivers, police | 3-5 | +15% premium |
| **High Risk** | Pilots, miners, offshore workers | 6-8 | +50% premium |
| **Extreme Risk** | Stunt performers, bomb disposal | 9-10 | Decline or +100% |

#### Health & Lifestyle Factors
- **BMI**: Normal (18.5-24.9) = 0 points, Overweight = +1, Obese = +3
- **Smoking**: Current smoker = +5 points, Quit <2 years = +3, Quit >2 years = +1
- **Family History**: Heart disease/cancer = +2 points
- **Exercise**: Regular (3x/week) = -1 point

### Financial Underwriting

#### Income Verification Requirements
- **Coverage ≤ 5x income**: Salary verification only
- **Coverage 6-15x income**: Tax returns + employer verification
- **Coverage 16-25x income**: Full financial review + net worth analysis

#### Debt-to-Income Ratios
- **Acceptable**: ≤ 40% total debt-to-income
- **Review Required**: 41-55% debt-to-income  
- **Decline**: > 55% debt-to-income

---

## Competitive Market Analysis

### Premium Benchmarking
Use historical market data to ensure competitive positioning:

- **Target Position**: Within 5% of top 3 competitors for similar risk profiles
- **Price Leadership**: 2-5% below market for preferred risk customers
- **Value Proposition**: Match competitors for standard risk, exceed benefits

### Market Rate Adjustments
| Customer Segment | Strategy | Target Position |
|------------------|----------|-----------------|
| **Preferred Plus** | Aggressive pricing | 5-10% below market |
| **Preferred** | Competitive pricing | Within 3% of market |
| **Standard Plus** | Value-focused | Match market leaders |
| **Standard** | Selective pricing | 5-10% above market |

---

## Decision Matrix & Automation Rules

### Instant Approval Criteria (No Human Review)
- Age 18-50
- Non-smoker
- Low-risk occupation (Class 1-2)
- Coverage ≤ 15x income
- Clean medical history
- Total risk score ≤ 3.5

### Conditional Approval (Automated with Conditions)
- Medical exam required
- Financial documentation needed
- Rate class adjustment
- Coverage amount modification

### Manual Review Required
- Age > 65
- High-risk occupation
- Coverage > 20x income
- Total risk score > 7
- Complex medical history

### Automatic Decline
- Age outside policy limits
- Extreme risk occupation without mitigation
- Debt-to-income > 55%
- Total risk score > 9
- Insufficient income for coverage amount

---

## Business Value Metrics

### Speed Optimization
- **Target Processing Time**: < 24 hours for 80% of applications
- **Instant Decisions**: 40% of applications
- **Same-Day Decisions**: 70% of applications

### Revenue Optimization
- **Premium Accuracy**: Within 2% of actuarial targets
- **Win Rate vs Competitors**: > 65% for preferred risks
- **Policy Retention**: > 95% year 1 retention rate

### Customer Experience
- **Application Completion Rate**: > 85%
- **Customer Satisfaction**: > 4.5/5.0 rating
- **Time to Policy Issue**: < 7 days average

---

## AI Decision Explanations

### Required Explanation Elements
1. **Primary Risk Factors**: Top 3 factors influencing decision
2. **Historical Data Comparison**: Similar customer outcomes
3. **Competitive Context**: Market position analysis
4. **Recommendation Confidence**: Statistical confidence level
5. **Alternative Options**: Other suitable products if applicable

### Sample Decision Framework
```
Risk Assessment: APPROVED - PREFERRED RATE CLASS
- Age: 35 (Low Risk - 2 points)
- Occupation: Software Engineer (Low Risk - 1 point)  
- Health: Non-smoker, Normal BMI (Low Risk - 0 points)
- Total Risk Score: 3/10

Historical Performance: 
- Similar profiles show 98.5% policy completion rate
- Claims rate: 0.3% annually for this segment

Market Analysis:
- Our rate: $34.80/month (Term 20, $500k)
- Market average: $37.20/month (6.5% competitive advantage)

Recommendation: Approve at Preferred Plus rate class
Confidence Level: 94%
```

---

## Integration with Historical Data

### Required Data Queries
1. **Claims Analysis**: Similar age/occupation/coverage combinations
2. **Policy Performance**: Retention rates for comparable customers
3. **Pricing Effectiveness**: Win/loss rates at different price points
4. **Risk Validation**: Actual vs. predicted outcomes for risk scores

### Key Performance Indicators
- **Underwriting Accuracy**: Predicted vs. actual claims experience
- **Portfolio Profitability**: Revenue per policy by risk segment
- **Market Competitiveness**: Win rates by competitor comparison
- **Process Efficiency**: Decision time and manual review rates

---

*Last Updated: August 2025*
*Version: 2.1 - AI-Enhanced Underwriting*
