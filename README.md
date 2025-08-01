
# Insurance Policy Review Hands-On Lab

This README provides setup instructions and resources for a 90-minute hands-on lab where 50 participants will create and publish Microsoft Fabric Data Agents and integrate them with Azure AI Foundry to evaluate insurance policies against underwriting guidelines.

---

## 🗓️ Lab Agenda

| Time       | Segment                        | Description |
|------------|--------------------------------|-------------|
| 0–10 min   | Introduction & Setup           | Introduce Fabric Data Agents and Azure AI Foundry. Outline the insurance scenario. Ensure access to Fabric workspace, Foundry project, and datasets. |
| 10–30 min  | Build & Publish Fabric Data Agent | Each participant creates a Fabric Data Agent, connects to the underwriting dataset, adds instructions/examples, tests queries, and publishes the agent. |
| 30–50 min  | Azure AI Foundry Integration   | Create a new agent in Foundry, connect the Fabric Data Agent as a resource, and configure instructions to leverage the Fabric tool. |
| 50–60 min  | Query the Integrated Agent     | Use Foundry Playground chat to ask underwriting-related questions. Observe results from Fabric data and troubleshoot query behavior. |
| 75–85 min  | Policy Review Case Study       | Use Playground chat to review a sample insurance policy and compare it against underwriting guidelines. Encourage custom questions and refine agent behavior. |
| 85–90 min  | Wrap-Up & Next Steps           | Summarize accomplishments, highlight real-world applications, and gather feedback. |

---

## 👥 Team Structure

- 50 participants split into **10 teams** (5–6 people per team)
- Each team has:
  - 1 Microsoft Fabric Workspace
  - 1 Azure AI Foundry Project
- Each participant creates and publishes their own agent

---

## 🧰 Azure Services Required

| Service                  | Purpose |
|--------------------------|---------|
| Microsoft Fabric (F2+)   | Workspace creation, OneLake storage, Data Agent publishing |
| Azure AI Foundry         | Agent orchestration, Playground chat, integration with Fabric agents |
| Microsoft Entra          | Identity and access control (RBAC for AI Developer and Contributor roles) |

---

## 🛠️ Provisioning Strategy

| Resource Type            | Quantity | Notes |
|--------------------------|----------|-------|
| Fabric Workspaces        | 10       | One per team |
| Azure AI Foundry Projects| 10       | One per team |
| Fabric Capacity          | 1 (F2+)  | Shared across all teams |
| Foundry Resource         | 1        | Shared across all teams |

---

## 🧪 Setup Timeline (1 Month)

| Week | Tasks |
|------|-------|
| Week 1 | Finalize agenda and team structure. Create Fabric workspaces and Foundry projects. Assign roles. |
| Week 2 | Load datasets into OneLake. Create sample agent templates. Validate access and permissions. |
| Week 3 | Test agent creation and publishing. Refine instructions. Prepare onboarding materials. |
| Week 4 | Conduct dry run with 1–2 teams. Finalize support plan. Set up Teams channel or Viva Learning for live help. |

---

## 📘 Onboarding Guide

Includes:
- Lab agenda
- Setup instructions for Fabric and Foundry
- Dataset preparation
- Sample agent instructions
- Support recommendations

📄 File: `onboarding_guide.pdf`

---

## 🗂️ Provisioning Template

Includes:
- Team IDs
- Workspace and project names
- Member emails
- Assigned roles

📄 File: `provisioning_template.json`

---

## 📄 Sample Datasets

- [insurance_policy_sample.csv](insurance_policy_sample.csv)
- [underwriting_guidelines.csv](underwriting_guidelines.csv)

Upload these to OneLake and connect them to your Fabric Data Agent.

---

## ✅ Next Steps

- Distribute onboarding guide and team assignments
- Upload datasets to OneLake
- Conduct dry run with 1–2 teams
- Prepare support channel for live help during the lab