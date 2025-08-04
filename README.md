
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
- [ ] Fabric capacity (F2+) provisioned and accessible
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
| 0–10 min   | Introduction & Setup           | Introduce Fabric Data Agents and Azure AI Foundry. Outline the insurance scenario. Ensure access to Fabric workspace, Foundry project, and OneLake. |
| 10–30 min  | Data Upload & Agent Creation   | Upload datasets to OneLake data lake, create lakehouse, then build Fabric Data Agent connected to the underwriting dataset. Add instructions/examples and test queries. |
| 30–40 min  | Publish Fabric Data Agent      | Finalize agent configuration, test with sample queries, and publish the agent to make it available for Foundry integration. |
| 40–70 min  | Azure AI Foundry Integration   | Create a new agent in Foundry, connect the published Fabric Data Agent as a resource, configure instructions to leverage the Fabric tool, and test various underwriting scenarios with refinement. |
| 70–85 min  | Policy Review Case Study       | Use Playground chat to review a sample insurance policy and compare it against underwriting guidelines. Analyze against historical lakehouse data and generate risk assessment recommendations. |
| 85–90 min  | Wrap-Up & Next Steps           | Summarize accomplishments, highlight real-world applications, and gather feedback. |

---

## Team Structure

- 50 participants split into **10 teams** (5–6 people per team)
- Each team has:
  - 1 Microsoft Fabric Workspace
  - 1 Azure AI Foundry Project
- Each participant creates and publishes their own agent

---

## Azure Services Required

| Service                  | Purpose |
|--------------------------|---------|
| Microsoft Fabric (F2+)   | Workspace creation, Data Agent publishing, lakehouse management |
| OneLake                  | Data lake storage for datasets, unified data storage across Fabric |
| Azure AI Foundry         | Agent orchestration, Playground chat, integration with Fabric agents |
| Microsoft Entra          | Identity and access control (RBAC for workspace and project roles) |

---

## Provisioning Strategy

| Resource Type            | Quantity | Notes |
|--------------------------|----------|-------|
| Fabric Workspaces        | 10       | One per team |
| Azure AI Foundry Projects| 10       | One per team |
| Fabric Capacity          | 1 (F2+)  | Shared across all teams |
| Foundry Resource         | 1        | Shared across all teams |

---

## Success Criteria

### Lab Completion Goals
Each participant should successfully:

#### Phase 1: Data Upload & Fabric Data Agent (30 minutes)
- [ ] Connect to assigned Fabric workspace with Contributor role permissions
- [ ] Create a new lakehouse in the workspace
- [ ] Upload sample datasets to OneLake data lake
- [ ] Verify data loading and schema detection
- [ ] Create a new Data Agent
- [ ] Connect agent to uploaded datasets in the lakehouse
- [ ] Add custom instructions for insurance policy evaluation
- [ ] Test agent with sample queries
- [ ] Publish agent successfully

#### Phase 2: AI Foundry Integration (30 minutes)
- [ ] Access assigned AI Foundry project
- [ ] Create new agent in Foundry
- [ ] Connect published Fabric Data Agent as resource
- [ ] Configure agent instructions to leverage the Fabric tool
- [ ] Test various underwriting scenarios
- [ ] Refine agent instructions and validate data lake connections
- [ ] Troubleshoot any integration issues

#### Phase 3: Policy Review Case Study (25 minutes)
- [ ] Query agent about underwriting guidelines
- [ ] Review sample insurance policy using agent
- [ ] Compare policy against underwriting guidelines
- [ ] Analyze against historical lakehouse data
- [ ] Generate risk assessment recommendations
- [ ] Demonstrate understanding of agent capabilities

---