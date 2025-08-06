# Insurance Policy Review Hands-On Lab

This README provides setup instructions and resources for a 90-minute hands-on lab where 50 participants will create and publish Microsoft Fabric Data Agents and integrate them with Azure AI Foundry to evaluate insurance policies against underwriting guidelines.

---

## Prerequisites

Before starting the lab, ensure all participants have:

### Required Access
- **Microsoft Fabric workspace** with one of the following roles:
  - **Contributor**: Create data agents, upload to OneLake, manage lakehouse (for participants)
- **Azure AI Foundry project** with one of the following roles:
  - **Azure AI Developer**: Create AI agents, deploy models, access Playground (for participants)
- **Azure subscription** with appropriate permissions for resource creation

### Pre-Lab Setup
- [ ] Participants have logged into both Fabric and AI Foundry platforms
- [ ] Participants have **OneLake access** to upload and manage datasets
- [ ] Sample datasets ready for upload to **OneLake data lake**
- [ ] Fabric capacity (F16) provisioned and accessible
- [ ] AI Foundry projects created and configured with proper role assignments
- [ ] Team assignments distributed with specific workspace/project mappings

### Technical Requirements
- Modern web browser (Chrome, Edge, Firefox)
- Stable internet connection
- Basic understanding of AI agents and data querying concepts

---

## Lab Agenda

| Time       | Segment                        | Description |
|------------|--------------------------------|-------------|
| 010 min   | Introduction & Setup           | Introduce Fabric Data Agents and Azure AI Foundry. Outline the general insurance underwriting scenario. Ensure access to Fabric workspace, Foundry project, and OneLake. |
| 1030 min  | Data Upload & Agent Creation   | Upload general insurance datasets to OneLake data lake, create lakehouse, then build Fabric Data Agent connected to comprehensive underwriting data. Add instructions for general insurance queries and test with industry-wide questions. |
| 3040 min  | Publish Fabric Data Agent      | Finalize agent configuration, test with general underwriting queries (claims analysis, risk assessment, portfolio benchmarking), and publish the agent to make it available for Foundry integration. |
| 4070 min  | Azure AI Foundry Integration   | Create specialized multi-agent system in Foundry, connect the published Fabric Data Agent as a resource, introduce Captain Elizabeth Darcy pilot case study, and configure specialized agents for complex underwriting scenarios. |
| 7085 min  | Multi-Agent Case Study         | Use the multi-agent system to analyze Captain Elizabeth Darcy's application with intentional gaps, demonstrate gap-filling workflow using complete supporting documents, and showcase automation benefits. |
| 8590 min  | Wrap-Up & Next Steps           | Summarize accomplishments, highlight real-world applications, and gather feedback. |

---

## Team Structure

- 50 participants split into **10 teams** (56 people per team)
- Each team has:
  - 1 Microsoft Fabric Workspace
  - 1 Azure AI Foundry Project
- Each participant creates and publishes their own agent

---

## Azure Services Required

| Service                  | Purpose |
|--------------------------|---------|
| Microsoft Fabric (F16)   | Workspace creation, Data Agent publishing, lakehouse management |
| OneLake                  | Data lake storage for datasets, unified data storage across Fabric |
| Azure AI Foundry         | Agent orchestration, Playground chat, integration with Fabric agents |
| Microsoft Entra          | Identity and access control (RBAC for workspace and project roles) |

---

## Provisioning Strategy

| Resource Type            | Quantity | Notes |
|--------------------------|----------|-------|
| Fabric Workspaces        | 10       | One per team |
| Azure AI Foundry Projects| 10       | One per team |
| Fabric Capacity          | 1 (F16)  | Shared across all teams |
| Foundry Resource         | 1        | Shared across all teams |

---

## Dataset Schema & Structure

### Enhanced Policy Portfolio Dataset (23 fields)
The primary dataset contains comprehensive policy information designed for advanced analytics:

#### Core Policy Information (15 fields)
- **policy_id**: Unique identifier (format: LIF-YYYYMMDD-######)
- **occupation**: Policyholder occupation (excludes sensitive occupations)
- **age**: Policyholder age (18-80)
- **coverage_amount**: Policy coverage amount ($25K-$15M)
- **premium**: Monthly premium amount
- **policy_type**: Term Life, Whole Life, Universal Life
- **issue_date**: Policy issue date (2018-2024)
- **risk_rating**: Preferred Plus, Preferred, Standard Plus, Standard, Substandard, Table ratings
- **medical_exam_required**: Yes/No based on coverage amount
- **state**: US state abbreviation
- **annual_income**: Policyholder income ($30K-$2M)
- **health_status**: Excellent, Good, Fair, Poor
- **smoking_status**: Smoker, Non-Smoker
- **beneficiary_relationship**: Spouse, Child, Parent, Other
- **payment_frequency**: Monthly, Quarterly, Annual

#### Enhanced Analytics Fields (8 fields)
- **policy_status**: Active (85%), Lapsed (10%), Terminated (3%), Suspended (2%)
- **underwriter_id**: UW001-UW015 (15 underwriters for performance analysis)
- **agent_id**: AGT001-AGT030 (30 agents for sales analytics)
- **last_premium_paid_date**: Recent payment tracking for lapse prediction
- **policy_value**: Current cash value (0 for term life, variable for permanent)
- **region**: Northeast, Southeast, Midwest, Southwest, West
- **application_channel**: Agent (40%), Online (25%), Broker (20%), Direct Mail (10%), Phone (5%)
- **explanation**: Optional field for high-risk cases and premium adjustments

---

## Success Criteria

### Lab Completion Goals
Each participant should successfully:

#### Phase 1: Data Upload & Fabric Data Agent (30 minutes)
- [ ] Connect to assigned Fabric workspace with Contributor role permissions
- [ ] Create a new lakehouse in the workspace
- [ ] Upload general insurance datasets to OneLake data lake (claims history, policy portfolio, demographics, risk factors)
- [ ] Verify data loading and schema detection
- [ ] Create a new Data Agent
- [ ] Connect agent to uploaded datasets in the lakehouse
- [ ] Add custom instructions for general insurance industry queries
- [ ] Test agent with general underwriting questions (e.g., "What are the claim rates for different age groups?", "How do occupation classes affect risk ratings?")
- [ ] Publish agent successfully

#### Phase 2: AI Foundry Multi-Agent Integration (30 minutes)
- [ ] Access assigned AI Foundry project
- [ ] Create specialized multi-agent system in Foundry
- [ ] Connect published Fabric Data Agent as foundational resource
- [ ] Introduction to Captain Elizabeth Darcy pilot case study
- [ ] Configure specialized agents (Financial Analysis, Medical Risk, Regulatory Compliance, Master Orchestrator)
- [ ] Test multi-agent coordination and data integration
- [ ] Prepare for complex case study analysis

#### Phase 3: Multi-Agent Case Study (25 minutes)
- [ ] Upload Elizabeth Darcy application with intentional gaps
- [ ] Execute multi-agent gap detection workflow
- [ ] Demonstrate specialized agents accessing supporting documents
- [ ] Show agents using general lakehouse data for benchmarking
- [ ] Generate comprehensive underwriting recommendation
- [ ] Compare automation benefits vs. manual process
