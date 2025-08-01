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
    subgraph "SHARED RESOURCES"
        FC[1x Fabric Capacity F2+<br/>Supports all 10 workspaces]
        FI[1x Foundry Instance<br/>Hosts all 10 projects]
    end
    
    subgraph "TEAM ALLOCATION"
        subgraph "Teams 1-5"
            T1[Team 1<br/>fabric-ws-01 | lakehouse-01<br/>1+ agents | foundry-proj-01]
            T2[Team 2<br/>fabric-ws-02 | lakehouse-02<br/>1+ agents | foundry-proj-02]
            T3[Team 3<br/>fabric-ws-03 | lakehouse-03<br/>1+ agents | foundry-proj-03]
            T4[Team 4<br/>fabric-ws-04 | lakehouse-04<br/>1+ agents | foundry-proj-04]
            T5[Team 5<br/>fabric-ws-05 | lakehouse-05<br/>1+ agents | foundry-proj-05]
        end
        
        subgraph "Teams 6-10"
            T6[Team 6<br/>fabric-ws-06 | lakehouse-06<br/>1+ agents | foundry-proj-06]
            T7[Team 7<br/>fabric-ws-07 | lakehouse-07<br/>1+ agents | foundry-proj-07]
            T8[Team 8<br/>fabric-ws-08 | lakehouse-08<br/>1+ agents | foundry-proj-08]
            T9[Team 9<br/>fabric-ws-09 | lakehouse-09<br/>1+ agents | foundry-proj-09]
            T10[Team 10<br/>fabric-ws-10 | lakehouse-10<br/>1+ agents | foundry-proj-10]
        end
    end
    
    FC -.-> T1
    FC -.-> T2
    FC -.-> T3
    FC -.-> T4
    FC -.-> T5
    FC -.-> T6
    FC -.-> T7
    FC -.-> T8
    FC -.-> T9
    FC -.-> T10
    
    FI -.-> T1
    FI -.-> T2
    FI -.-> T3
    FI -.-> T4
    FI -.-> T5
    FI -.-> T6
    FI -.-> T7
    FI -.-> T8
    FI -.-> T9
    FI -.-> T10
    
    style FC fill:#e1f5fe
    style FI fill:#f3e5f5
```

**Allocation Summary:** 50 Participants → 10 Teams (5 participants each)

## Integration Architecture

```mermaid
graph LR
    subgraph "FABRIC SIDE"
        subgraph "Team Lakehouse"
            ID[Insurance Data]
            CH[Claims History]
            PR[Policy Rules]
            TMP[Templates]
        end
        
        PDA[Published Data Agents<br/>1+ per team]
        
        subgraph "Agent Capabilities"
            QI[Query insurance data]
            AP[Analyze policies]
            RA[Risk assessment]
        end
        
        ID --> PDA
        CH --> PDA
        PR --> PDA
        TMP --> PDA
        
        PDA --> QI
        PDA --> AP
        PDA --> RA
    end
    
    subgraph "FOUNDRY SIDE"
        subgraph "Team Project"
            subgraph "Participant Agents"
                A1[Agent 1]
                A2[Agent 2]
                A3[Agent 3]
                A4[Agent 4]
                A5[Agent 5]
            end
            
            subgraph "Playground Testing"
                PC[Playground Chat Testing]
                EX[Example Query:<br/>"Review this policy against guidelines..."]
            end
        end
    end
    
    PDA -.->|Integration Connection| A1
    PDA -.->|Connect to Published<br/>Fabric Data Agents| A2
    PDA -.-> A3
    PDA -.-> A4
    PDA -.-> A5
    
    A1 --> PC
    A2 --> PC
    A3 --> PC
    A4 --> PC
    A5 --> PC
    
    PC --> EX
    
    style PDA fill:#e8f5e8
    style A1 fill:#f3e5f5
    style A2 fill:#f3e5f5
    style A3 fill:#f3e5f5
    style A4 fill:#f3e5f5
    style A5 fill:#f3e5f5
    style PC fill:#fff3e0
```

This architecture ensures:
- **Scalability**: Single capacity serves all teams efficiently
- **Isolation**: Each team has their own workspace and project
- **Collaboration**: Teams can share insights while maintaining separation
- **Integration**: Seamless connection between Fabric and Foundry components
