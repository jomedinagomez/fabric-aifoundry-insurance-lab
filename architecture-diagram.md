# Lab Architecture Flow Diagram

## High-Level Architecture Overview

```mermaid
graph TB
    subgraph "LAB INFRASTRUCTURE"
        subgraph "MICROSOFT FABRIC"
            F2[Single F2+ Capacity<br/>Shared Resource]
            F2 --> WS[10 Workspaces<br/>1 per team]
        end
        
        subgraph "AZURE AI FOUNDRY"
            AF[Single Foundry Instance<br/>Shared Resource]
            AF --> PROJ[10 Projects<br/>1 per team]
        end
    end
    
    style F2 fill:#e1f5fe
    style AF fill:#f3e5f5
    style WS fill:#e8f5e8
    style PROJ fill:#fff3e0
```

## Detailed Team Structure

```mermaid
graph TB
    subgraph "TEAM X - 5 Participants"
        subgraph "FABRIC WORKSPACE X"
            LH[LAKEHOUSE X]
            LH --> ID[Insurance Data]
            LH --> CD[Claims Data]
            LH --> PT[Policy Templates]
            LH --> SP[Sample Policies]
            
            LH --> DA[DATA AGENTS]
            DA --> AG1[Agent A Team]
            DA --> AG2[Agent B Team]
            DA --> AG3[Agent C Team]
        end
        
        subgraph "FOUNDRY PROJECT X"
            AI[AI AGENTS]
            AI --> P1[Agent 1 - Participant 1]
            AI --> P2[Agent 2 - Participant 2]
            AI --> P3[Agent 3 - Participant 3]
            AI --> P4[Agent 4 - Participant 4]
            AI --> P5[Agent 5 - Participant 5]
            
            INT[INTEGRATION]
            INT --> CONN[Foundry Agents connect to<br/>Published Fabric Data Agents]
        end
    end
    
    DA -.->|Integration| AI
    P1 -.-> DA
    P2 -.-> DA
    P3 -.-> DA
    P4 -.-> DA
    P5 -.-> DA
    
    style LH fill:#e1f5fe
    style AI fill:#f3e5f5
    style DA fill:#e8f5e8
    style INT fill:#fff3e0
```

## Lab Process Flow

```mermaid
flowchart TD
    subgraph "Step 1: FABRIC SETUP (10-30 minutes)"
        A1[Access Team<br/>Workspace] --> B1[Create Team<br/>Lakehouse]
        B1 --> C1[Upload Data to<br/>OneLake Lake]
        C1 --> D1[Create Fabric Data Agents<br/>Connect to lakehouse data]
        D1 --> E1[Publish Data Agents<br/>1+ per team]
    end
    
    subgraph "Step 2: FOUNDRY INTEGRATION (40-75 minutes)"
        A2[Access Team<br/>Project Foundry] --> B2[Create AI Agents<br/>1 per participant]
        B2 --> C2[Connect to Published<br/>Fabric Data Agents]
        C2 --> D2[Configure Agent Instructions<br/>Policy evaluation logic]
        D2 --> E2[Test & Evaluate<br/>Insurance Policies]
    end
    
    E1 -.->|Integration| C2
    
    style A1 fill:#e1f5fe
    style A2 fill:#f3e5f5
    style E1 fill:#e8f5e8
    style E2 fill:#fff3e0
```

**Team Allocation:** 50 Participants → 10 Teams (5 participants each)

## Resource Allocation Matrix

```mermaid
graph TB
    subgraph "SHARED INFRASTRUCTURE"
        FC[Fabric Capacity F2+<br/>Shared across all teams]
        FI[Foundry Instance<br/>Shared across all teams]
    end
    
    subgraph "TEAM RESOURCES"
        subgraph "Teams 1-3"
            T1[Team 1<br/>Workspace: fabric-ws-01<br/>Lakehouse: lakehouse-01<br/>Project: foundry-proj-01]
            T2[Team 2<br/>Workspace: fabric-ws-02<br/>Lakehouse: lakehouse-02<br/>Project: foundry-proj-02]
            T3[Team 3<br/>Workspace: fabric-ws-03<br/>Lakehouse: lakehouse-03<br/>Project: foundry-proj-03]
        end
        
        subgraph "Teams 4-6"
            T4[Team 4<br/>Workspace: fabric-ws-04<br/>Lakehouse: lakehouse-04<br/>Project: foundry-proj-04]
            T5[Team 5<br/>Workspace: fabric-ws-05<br/>Lakehouse: lakehouse-05<br/>Project: foundry-proj-05]
            T6[Team 6<br/>Workspace: fabric-ws-06<br/>Lakehouse: lakehouse-06<br/>Project: foundry-proj-06]
        end
        
        subgraph "Teams 7-10"
            T7[Team 7<br/>Workspace: fabric-ws-07<br/>Lakehouse: lakehouse-07<br/>Project: foundry-proj-07]
            T8[Team 8<br/>Workspace: fabric-ws-08<br/>Lakehouse: lakehouse-08<br/>Project: foundry-proj-08]
            T9[Team 9<br/>Workspace: fabric-ws-09<br/>Lakehouse: lakehouse-09<br/>Project: foundry-proj-09]
            T10[Team 10<br/>Workspace: fabric-ws-10<br/>Lakehouse: lakehouse-10<br/>Project: foundry-proj-10]
        end
    end
    
    FC -->|Supports| T1
    FC -->|Supports| T2
    FC -->|Supports| T3
    FI -->|Hosts| T1
    FI -->|Hosts| T2
    FI -->|Hosts| T3
    
    style FC fill:#e1f5fe
    style FI fill:#f3e5f5
    style T1 fill:#e8f5e8
    style T2 fill:#e8f5e8
    style T3 fill:#e8f5e8
```

**Resource Summary:**
- **Total Participants:** 50 (5 participants per team)
- **Total Teams:** 10
- **Fabric Workspaces:** 10 (1 per team)
- **Foundry Projects:** 10 (1 per team)
- **Shared Capacity:** 1 Fabric F2+ instance
- **Shared Foundry:** 1 instance

## Integration Architecture

```mermaid
flowchart LR
    subgraph FABRIC["FABRIC SIDE"]
        subgraph DATA["Team Lakehouse Data"]
            ID[Insurance Data]
            CH[Claims History]
            PR[Policy Rules]
            TMP[Templates]
        end
        
        PDA[Published Data Agents]
        
        subgraph CAP["Agent Capabilities"]
            QI[Query Data]
            AP[Analyze Policies]
            RA[Risk Assessment]
        end
    end
    
    subgraph FOUNDRY["FOUNDRY SIDE"]
        subgraph AGENTS["Participant Agents"]
            A1[Agent 1]
            A2[Agent 2]
            A3[Agent 3]
            A4[Agent 4]
            A5[Agent 5]
        end
        
        subgraph TEST["Testing Environment"]
            PC[Playground Chat]
            EX[Policy Review Queries]
        end
    end
    
    %% Data flows to agents
    ID --> PDA
    CH --> PDA
    PR --> PDA
    TMP --> PDA
    
    %% Agent capabilities
    PDA --> QI
    PDA --> AP
    PDA --> RA
    
    %% Integration connections
    PDA -.->|Integration| A1
    PDA -.->|Integration| A2
    PDA -.->|Integration| A3
    PDA -.->|Integration| A4
    PDA -.->|Integration| A5
    
    %% Testing flows
    A1 --> PC
    A2 --> PC
    A3 --> PC
    A4 --> PC
    A5 --> PC
    PC --> EX
    
    %% Styling
    style PDA fill:#e8f5e8
    style PC fill:#fff3e0
    style FABRIC fill:#e1f5fe
    style FOUNDRY fill:#f3e5f5
```

**Integration Flow:**
1. **Data Sources** → Published Data Agents (Fabric side)
2. **Published Agents** → Participant Agents (Foundry side)
3. **Participant Agents** → Playground Testing
4. **Testing** → Policy evaluation and refinement

This architecture ensures:
- **Scalability**: Single capacity serves all teams efficiently
- **Isolation**: Each team has their own workspace and project
- **Collaboration**: Teams can share insights while maintaining separation
- **Integration**: Seamless connection between Fabric and Foundry components

---

## Infrastructure Provisioning Summary

> **For Infrastructure Teams**: This section outlines the Azure services and configurations required to support the lab environment.

```mermaid
graph TB
    subgraph AZURE["Azure Subscription"]
        subgraph ENTRA["Microsoft Entra ID"]
            RBAC[Role-Based Access Control]
            USERS[50 Lab Participants]
            GROUPS[Team Groups 1-10]
        end
        
        subgraph FABRIC_INFRA["Microsoft Fabric Infrastructure"]
            FC[Fabric Capacity F2+<br/>Shared Resource]
            WS1[Workspace 1<br/>fabric-ws-01]
            WS2[Workspace 2<br/>fabric-ws-02]
            WS_ETC[... 8 more workspaces]
            LH[OneLake Storage<br/>Lakehouses 1-10]
        end
        
        subgraph FOUNDRY_INFRA["Azure AI Foundry Infrastructure"]
            FI[Foundry Hub Instance<br/>Shared Resource]
            PROJ1[Project 1<br/>foundry-proj-01]
            PROJ2[Project 2<br/>foundry-proj-02]
            PROJ_ETC[... 8 more projects]
            MODELS[AI Models<br/>GPT-4o, etc.]
        end
        
        subgraph NETWORK["Networking & Security"]
            VNET[Virtual Network<br/>Optional: Private endpoints]
            NSG[Network Security Groups]
            PRIVEP[Private Endpoints<br/>For enhanced security]
        end
    end
    
    %% Access Control
    RBAC --> FABRIC_INFRA
    RBAC --> FOUNDRY_INFRA
    USERS --> GROUPS
    GROUPS --> WS1
    GROUPS --> PROJ1
    
    %% Infrastructure Dependencies
    FC --> WS1
    FC --> WS2
    FC --> WS_ETC
    WS1 --> LH
    WS2 --> LH
    
    FI --> PROJ1
    FI --> PROJ2
    FI --> PROJ_ETC
    FI --> MODELS
    
    %% Integration Communication
    LH -.->|Data Agent Publishing| MODELS
    MODELS -.->|Agent Integration| LH
    
    %% Security
    VNET --> FABRIC_INFRA
    VNET --> FOUNDRY_INFRA
    NSG --> VNET
    PRIVEP --> FOUNDRY_INFRA
    
    %% Styling
    style FC fill:#e1f5fe
    style FI fill:#f3e5f5
    style RBAC fill:#fff3e0
    style LH fill:#e8f5e8
    style MODELS fill:#fce4ec
```

### Infrastructure Requirements Checklist

#### **Core Azure Services**
- [ ] **Microsoft Fabric Capacity** (F2 or higher)
  - Supports concurrent workload for 50 users
  - Enables lakehouse and data agent capabilities
  - Estimated cost: ~$8,000-12,000/month for F2
  
- [ ] **Azure AI Foundry Hub**
  - Single shared instance
  - Model deployment capabilities (GPT-4o, GPT-35-turbo)
  - Supports 10 projects with isolation
  
- [ ] **Microsoft Entra ID**
  - 50 user accounts with appropriate licenses
  - 10 security groups for team assignments
  - RBAC configuration for Fabric and Foundry access

#### **Resource Configuration**
- [ ] **Fabric Workspaces**: 10 workspaces (fabric-ws-01 through fabric-ws-10)
- [ ] **Lakehouses**: 10 lakehouses (lakehouse-01 through lakehouse-10)
- [ ] **Foundry Projects**: 10 projects (foundry-proj-01 through foundry-proj-10)
- [ ] **OneLake Storage**: Sufficient capacity for sample datasets (~1GB per team)

#### **Permissions & Access**
- [ ] **Fabric Permissions**: Contributor role for all participants
- [ ] **Foundry Permissions**: Azure AI Developer role for all participants
- [ ] **Team Assignments**: Participants mapped to specific workspace/project pairs
- [ ] **Data Access**: OneLake permissions configured for team isolation

#### **Optional Enhancements**
- [ ] **Private Endpoints**: For enhanced security (enterprise environments)
- [ ] **Virtual Network**: Custom VNET with controlled access
- [ ] **Monitoring**: Application Insights for usage tracking
- [ ] **Backup**: Data retention policies for lab artifacts

### Communication Flows

1. **Authentication**: Entra ID → Fabric/Foundry services
2. **Data Upload**: Participants → OneLake via Fabric workspaces  
3. **Agent Publishing**: Fabric Data Agents → Foundry integration endpoints
4. **Model Access**: Foundry projects → Shared AI model deployments
5. **Cross-Service Integration**: Published agents accessible across Fabric/Foundry boundary

### Estimated Costs (Monthly)
- **Fabric F2 Capacity**: $8,000 - $12,000
- **Azure AI Foundry**: $500 - $1,500 (depends on model usage)
- **Storage (OneLake)**: $50 - $200
- **Networking**: $0 - $500 (if private endpoints used)
- **Total**: ~$8,550 - $14,200/month during lab period

### Post-Lab Cleanup
- [ ] Deprovision Fabric capacity to avoid ongoing costs
- [ ] Archive or delete OneLake data
- [ ] Remove Foundry model deployments
- [ ] Retain project structures for future labs (optional)
