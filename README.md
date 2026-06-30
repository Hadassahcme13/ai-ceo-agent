<div align="center">

# 🤖 AI CEO Strategic Intelligence Agent

### Autonomous Multi-Agent AI System for Executive Strategic Decision Intelligence

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-Qwen2.5-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-purple?style=for-the-badge)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-bge--small--en--v1.5-orange?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Dashboard-blueviolet?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

### 🧠 Planner • Executor • Semantic Search • Multi-Agent AI • Strategic Intelligence • RAG • Executive Decision Support

Transform business news into **CEO-ready strategic intelligence reports** using **Autonomous AI Agents**, **Semantic Retrieval**, **Retrieval-Augmented Generation (RAG)** and **Local Large Language Models**.

</div>

---

# 📖 Project Overview

The **AI CEO Strategic Intelligence Agent** is an autonomous **Multi-Agent Artificial Intelligence System** that assists executive leadership in making evidence-based strategic decisions from large collections of business news.

Instead of asking a single Large Language Model to solve everything, the system divides the task into multiple specialized AI agents that collaborate through a **shared memory architecture**.

Each AI agent performs one specific responsibility:

- 🔍 Retrieve relevant information
- 🚀 Identify strategic opportunities
- ⚠ Analyze business risks
- 📈 Detect emerging trends
- 😊 Assess market sentiment
- ✔ Validate all findings
- 👔 Generate an executive strategic intelligence report

The final output is presented through an interactive **Streamlit Dashboard** designed for executive decision support.

---

# ✨ Key Features

| Category | Capability |
|-----------|------------|
| 🧠 Autonomous Planner | Dynamically creates an execution plan based on the user's strategic goal |
| ⚙ AI Executor | Executes every tool in sequence using shared memory |
| 🔍 Semantic Search | Retrieves relevant documents using FAISS vector similarity |
| 🚀 Opportunity Analysis | Identifies strategic business opportunities |
| ⚠ Risk Analysis | Detects operational and strategic risks |
| 📈 Trend Detection | Discovers emerging technologies and market trends |
| 😊 Sentiment Analysis | Evaluates article-level market sentiment |
| ✔ Validation Engine | Ensures all AI findings are evidence-based |
| 👔 Strategic Intelligence Engine | Produces CEO-ready intelligence reports |
| 📊 Executive Dashboard | Interactive visualization using Streamlit |

---

# 🎯 End-to-End AI Workflow

```mermaid
flowchart TD

A([👤 User Strategic Goal])

A --> B

B["🧠 AI Planner
Analyze Goal
Generate Execution Plan"]

B --> C["📋 Execution Plan"]

C --> D["⚙️ AI Executor"]

D --> E["🔍 Semantic Retriever"]

E --> F[("📚 FAISS Knowledge Repository")]

F --> G["📄 Retrieved Documents"]

G --> H["🚀 Opportunity Analyzer"]

G --> I["⚠️ Risk Analyzer"]

G --> J["📈 Trend Analyzer"]

G --> K["😊 Sentiment Analyzer"]

H --> L["🧠 Shared Agent Memory"]

I --> L

J --> L

K --> L

L --> M["✔️ Validation Engine"]

M --> N["👔 Strategic Intelligence Engine"]

N --> O["📑 CEO Strategic Intelligence Report"]

O --> P["📊 Interactive Streamlit Dashboard"]

style A fill:#1976D2,color:#fff,stroke:#0D47A1,stroke-width:2px
style B fill:#673AB7,color:#fff
style C fill:#9575CD,color:#fff
style D fill:#0097A7,color:#fff
style E fill:#3949AB,color:#fff
style F fill:#3F51B5,color:#fff
style G fill:#90CAF9,color:#000
style H fill:#43A047,color:#fff
style I fill:#E53935,color:#fff
style J fill:#FB8C00,color:#fff
style K fill:#26C6DA,color:#fff
style L fill:#8E24AA,color:#fff
style M fill:#7CB342,color:#fff
style N fill:#D81B60,color:#fff
style O fill:#283593,color:#fff
style P fill:#00897B,color:#fff
```

---

# 💡 Why a Multi-Agent Architecture?

Traditional Retrieval-Augmented Generation (RAG) systems retrieve documents and ask a single Large Language Model to generate an answer.

This project instead adopts a **Multi-Agent AI Architecture**, where independent AI agents collaborate to solve different aspects of a strategic intelligence problem.

### Benefits

- 🧠 Specialized reasoning by dedicated AI agents
- 🔄 Shared memory for inter-agent collaboration
- ✔ Evidence validation before reporting
- 📊 Explainable and transparent decision making
- 📈 Modular and extensible architecture
- 👔 Executive-focused intelligence generation

The result is a scalable and explainable AI system capable of producing high-quality strategic recommendations for executive decision makers.

---
# 🏗️ System Architecture

The AI CEO Strategic Intelligence Agent follows a **modular Multi-Agent Architecture**, where each component performs a specialized task while collaborating through a shared memory system.

The architecture is divided into five logical layers:

| Layer | Responsibility |
|--------|----------------|
| 👤 User Layer | Accepts strategic business goals from executives |
| 🧠 Planning Layer | Generates an intelligent execution plan using the Planner Agent |
| ⚙️ Execution Layer | Executes specialized AI agents sequentially |
| 🧠 Intelligence Layer | Validates insights and generates executive intelligence |
| 📊 Presentation Layer | Displays CEO-ready reports through the Streamlit dashboard |

---

## High-Level System Architecture

```mermaid
flowchart TB

%% ======================
%% User Layer
%% ======================

subgraph USER["👤 User Layer"]
A["CEO / Business User"]
end

%% ======================
%% Planning Layer
%% ======================

subgraph PLAN["🧠 Planning Layer"]

B["Planner Agent"]

C["Goal Analysis"]

D["Tool Registry"]

E["Execution Plan"]

B --> C

C --> D

D --> E

end

%% ======================
%% Execution Layer
%% ======================

subgraph EXEC["⚙️ Execution Layer"]

F["Executor"]

G["Semantic Retriever"]

H["Opportunity Analyzer"]

I["Risk Analyzer"]

J["Trend Analyzer"]

K["Sentiment Analyzer"]

end

%% ======================
%% Shared Memory
%% ======================

subgraph MEMORY["🧠 Shared Agent Memory"]

M["Documents"]

N["Opportunities"]

O["Risks"]

P["Trends"]

Q["Sentiment"]

end

%% ======================
%% Intelligence Layer
%% ======================

subgraph INTEL["👔 Intelligence Layer"]

R["Validation Engine"]

S["Strategic Intelligence Engine"]

T["CEO Strategic Report"]

end

%% ======================
%% Dashboard Layer
%% ======================

subgraph DASH["📊 Presentation Layer"]

U["Streamlit Dashboard"]

V["Interactive Visualizations"]

end

%% ======================
%% Connections
%% ======================

A --> B

E --> F

F --> G

G --> H

G --> I

G --> J

G --> K

H --> N

I --> O

J --> P

K --> Q

G --> M

M --> R

N --> R

O --> R

P --> R

Q --> R

R --> S

S --> T

T --> U

U --> V

%% ======================
%% Colors
%% ======================

style A fill:#1976D2,color:#fff

style B fill:#673AB7,color:#fff
style C fill:#7E57C2,color:#fff
style D fill:#9575CD,color:#fff
style E fill:#B39DDB,color:#000

style F fill:#0097A7,color:#fff
style G fill:#3949AB,color:#fff
style H fill:#43A047,color:#fff
style I fill:#E53935,color:#fff
style J fill:#FB8C00,color:#fff
style K fill:#26C6DA,color:#fff

style M fill:#C5CAE9,color:#000
style N fill:#A5D6A7,color:#000
style O fill:#EF9A9A,color:#000
style P fill:#FFCC80,color:#000
style Q fill:#80DEEA,color:#000

style R fill:#8BC34A,color:#fff
style S fill:#D81B60,color:#fff
style T fill:#3F51B5,color:#fff

style U fill:#00897B,color:#fff
style V fill:#26A69A,color:#fff
```

---

# 🧩 System Components

## 👤 User Layer

The interaction begins when an executive enters a strategic business objective through the Streamlit dashboard.

Example:

```text
Analyze NVIDIA's strategic opportunities in the AI chip market.
```

---

## 🧠 Planning Layer

The Planner Agent transforms the user's objective into a structured execution workflow.

Responsibilities:

- Analyze user intent
- Load the Tool Registry
- Select appropriate AI agents
- Generate an execution plan
- Validate workflow integrity

---

## ⚙️ Execution Layer

The Executor Agent dynamically loads and executes each AI tool.

Responsibilities:

- Import tool modules
- Execute agents sequentially
- Maintain shared memory
- Store intermediate results
- Handle execution failures

---

## 🧠 Shared Agent Memory

Instead of each AI agent working independently, all agents communicate through a centralized memory object.

Stored information includes:

- Retrieved Documents
- Strategic Opportunities
- Business Risks
- Emerging Trends
- Market Sentiment
- Validation Results
- Executive Report

This architecture enables seamless collaboration between autonomous AI agents.

---

## 👔 Intelligence Layer

The Validation Engine verifies that every generated insight is supported by retrieved evidence.

After validation, the Strategic Intelligence Engine synthesizes all validated findings into a comprehensive CEO report containing:

- Executive Summary
- Strategic Opportunities
- Strategic Risks
- Emerging Trends
- Market Sentiment
- Strategic Recommendations
- CEO Briefing

---

## 📊 Presentation Layer

The Streamlit Dashboard presents all AI-generated intelligence in an executive-friendly format.

The dashboard includes:

- Interactive KPI Cards
- Opportunity Analysis
- Risk Analysis
- Trend Analysis
- Market Sentiment
- Strategic Recommendations
- CEO Briefing
- Executive Intelligence Report

---
# 🤖 Multi-Agent Architecture

Unlike traditional Retrieval-Augmented Generation (RAG) systems that rely on a single Large Language Model, this project adopts a **Multi-Agent AI Architecture**.

Each AI agent is responsible for a specialized task while collaborating through a centralized **Shared Agent Memory**.

This modular design improves:

- 🎯 Specialization
- 🔄 Collaboration
- 📚 Explainability
- ⚡ Scalability
- ✔ Evidence-based reasoning

---

# 🧠 Multi-Agent Collaboration

```mermaid
flowchart LR

Planner["🧠 Planner Agent"]

Executor["⚙️ Executor Agent"]

Retriever["🔍 Semantic Retriever"]

Opportunity["🚀 Opportunity Analyzer"]

Risk["⚠️ Risk Analyzer"]

Trend["📈 Trend Analyzer"]

Sentiment["😊 Sentiment Analyzer"]

Memory["🧠 Shared Memory"]

Validator["✔️ Validation Engine"]

Intelligence["👔 Strategic Intelligence Engine"]

Dashboard["📊 Streamlit Dashboard"]

Planner --> Executor

Executor --> Retriever

Retriever --> Opportunity

Retriever --> Risk

Retriever --> Trend

Retriever --> Sentiment

Opportunity --> Memory

Risk --> Memory

Trend --> Memory

Sentiment --> Memory

Memory --> Validator

Validator --> Intelligence

Intelligence --> Dashboard

style Planner fill:#5E35B1,color:#fff
style Executor fill:#039BE5,color:#fff
style Retriever fill:#3949AB,color:#fff
style Opportunity fill:#43A047,color:#fff
style Risk fill:#E53935,color:#fff
style Trend fill:#FB8C00,color:#fff
style Sentiment fill:#26C6DA,color:#fff
style Memory fill:#8E24AA,color:#fff
style Validator fill:#7CB342,color:#fff
style Intelligence fill:#D81B60,color:#fff
style Dashboard fill:#00897B,color:#fff
```

---

# 🧠 Shared Agent Memory

The system uses a centralized **Shared Agent Memory** that enables communication between independent AI agents.

Instead of passing data directly between tools, each agent stores its output inside a common memory object.

Every subsequent agent reads only the information it requires.

---

## Memory Structure

```mermaid
flowchart TD

Memory["🧠 Shared Agent Memory"]

Memory --> Goal["🎯 Goal"]

Memory --> Docs["📄 Retrieved Documents"]

Memory --> Opp["🚀 Opportunities"]

Memory --> Risks["⚠️ Risks"]

Memory --> Trends["📈 Trends"]

Memory --> Sentiment["😊 Sentiment"]

Memory --> Validation["✔️ Validation"]

Memory --> Report["👔 Executive Report"]

style Memory fill:#673AB7,color:#fff

style Goal fill:#42A5F5,color:#fff

style Docs fill:#5C6BC0,color:#fff

style Opp fill:#43A047,color:#fff

style Risks fill:#E53935,color:#fff

style Trends fill:#FB8C00,color:#fff

style Sentiment fill:#26C6DA,color:#fff

style Validation fill:#7CB342,color:#fff

style Report fill:#D81B60,color:#fff
```

---

# 🔄 Agent Execution Sequence

Every AI agent contributes one specialized capability before handing control to the next stage.

```mermaid
sequenceDiagram

participant User

participant Planner

participant Executor

participant Retriever

participant Opportunity

participant Risk

participant Trend

participant Sentiment

participant Validator

participant Intelligence

participant Dashboard

User->>Planner: Strategic Goal

Planner->>Executor: Execution Plan

Executor->>Retriever: Retrieve Documents

Retriever-->>Opportunity: Relevant Articles

Retriever-->>Risk: Relevant Articles

Retriever-->>Trend: Relevant Articles

Retriever-->>Sentiment: Relevant Articles

Opportunity->>Validator: Opportunities

Risk->>Validator: Risks

Trend->>Validator: Trends

Sentiment->>Validator: Sentiment

Validator->>Intelligence: Validated Results

Intelligence->>Dashboard: CEO Report
```

---

# ⚙️ AI Agents

| AI Agent | Responsibility | Output |
|-----------|---------------|--------|
| 🧠 Planner Agent | Analyzes the user's goal and creates an execution plan | Execution Plan |
| ⚙️ Executor Agent | Dynamically executes each AI tool | Updated Shared Memory |
| 🔍 Semantic Retriever | Retrieves relevant documents using FAISS | Relevant Articles |
| 🚀 Opportunity Analyzer | Detects strategic business opportunities | Opportunities |
| ⚠️ Risk Analyzer | Identifies strategic and operational risks | Risks |
| 📈 Trend Analyzer | Detects emerging technologies and market trends | Trends |
| 😊 Sentiment Analyzer | Classifies article-level market sentiment | Sentiment |
| ✔️ Validation Engine | Verifies every insight using supporting evidence | Validated Intelligence |
| 👔 Strategic Intelligence Engine | Generates executive strategic intelligence | CEO Report |

---

# 🎯 Why Multiple AI Agents?

Instead of assigning one Large Language Model every task, the workload is divided among specialized AI agents.

This approach offers several advantages:

| Traditional Single-Agent AI | Multi-Agent AI System |
|-----------------------------|-----------------------|
| One prompt performs every task | Specialized agents perform dedicated tasks |
| Difficult to validate outputs | Validation engine verifies every insight |
| Limited explainability | Each agent has a transparent responsibility |
| Hard to extend | New agents can be added easily |
| Monolithic architecture | Modular and scalable design |
| Single reasoning pathway | Collaborative reasoning across agents |

---

# ⭐ Key Architectural Advantages

✅ Modular AI architecture

✅ Dynamic planning and execution

✅ Shared memory communication

✅ Explainable reasoning

✅ Evidence-based validation

✅ Easy extensibility

✅ Retrieval-Augmented Generation (RAG)

✅ Executive-focused intelligence generation

---
# 🧠 AI Planning & Execution Engine

One of the distinguishing features of this project is its **Autonomous Planning and Execution Framework**.

Instead of hardcoding the workflow, the system dynamically determines **which AI agents to execute** based on the user's strategic goal.

The framework consists of two autonomous components:

- 🧠 **Planner Agent**
- ⚙️ **Executor Agent**

Together they orchestrate the complete strategic intelligence pipeline.

---

# 🧠 Planner Architecture

The Planner Agent transforms a natural language business objective into a structured execution workflow.

Responsibilities include:

- Understanding the user's intent
- Loading the Tool Registry
- Selecting appropriate AI agents
- Generating an execution plan using Qwen
- Validating the generated workflow
- Passing the validated plan to the Executor

---

## Planner Workflow

```mermaid
flowchart TD

A["👤 User Goal"]

A --> B["🧠 Goal Analysis"]

B --> C["📚 Load Tool Registry"]

C --> D["🤖 Qwen Planning Agent"]

D --> E["📋 Generate Execution Plan"]

E --> F["✔ Validate Plan"]

F --> G["⚙️ Executor"]

style A fill:#1976D2,color:#fff
style B fill:#673AB7,color:#fff
style C fill:#3949AB,color:#fff
style D fill:#8E24AA,color:#fff
style E fill:#5E35B1,color:#fff
style F fill:#7CB342,color:#fff
style G fill:#0097A7,color:#fff
```

---

# 📋 Execution Plan Example

For the strategic goal:

```text
Analyze NVIDIA's strategic position in the AI market.
```

The Planner automatically generates:

```text
1. SemanticRetriever

2. OpportunityAnalyzer

3. RiskAnalyzer

4. TrendAnalyzer

5. SentimentAnalyzer

6. Validator

7. StrategicIntelligenceEngine
```

Each step includes:

- Tool Name
- Purpose
- Reason
- Expected Output

before execution begins.

---

# 🛠 Tool Registry

The Tool Registry acts as the knowledge base of available AI agents.

Each tool contains:

| Property | Description |
|----------|-------------|
| Name | Tool Identifier |
| Description | Purpose of the tool |
| Module | Python module location |
| Function | Function executed |
| Input | Expected input |
| Output | Produced output |

---

## Tool Registry Architecture

```mermaid
flowchart LR

Registry["📚 Tool Registry"]

Planner["🧠 Planner"]

Executor["⚙️ Executor"]

Modules["📦 Python Modules"]

Registry --> Planner

Planner --> Executor

Executor --> Modules

Modules --> Retriever["🔍 Retriever"]

Modules --> Opportunity["🚀 Opportunity"]

Modules --> Risk["⚠ Risk"]

Modules --> Trend["📈 Trend"]

Modules --> Sentiment["😊 Sentiment"]

Modules --> Validator["✔ Validator"]

Modules --> Intelligence["👔 Intelligence"]

style Registry fill:#3949AB,color:white
style Planner fill:#673AB7,color:white
style Executor fill:#0097A7,color:white
style Modules fill:#5C6BC0,color:white
style Retriever fill:#42A5F5,color:white
style Opportunity fill:#43A047,color:white
style Risk fill:#E53935,color:white
style Trend fill:#FB8C00,color:white
style Sentiment fill:#26C6DA,color:white
style Validator fill:#8BC34A,color:white
style Intelligence fill:#D81B60,color:white
```

---

# ⚙️ Executor Architecture

The Executor Agent is responsible for carrying out the execution plan generated by the Planner.

Unlike traditional workflows with hardcoded function calls, the Executor dynamically imports and executes Python modules at runtime.

Responsibilities:

- Read execution plan
- Dynamically import modules
- Execute tools sequentially
- Update shared memory
- Handle execution errors
- Produce the final intelligence report

---

## Executor Workflow

```mermaid
flowchart TD

A["📋 Execution Plan"]

A --> B["⚙️ Executor"]

B --> C["📦 Import Module"]

C --> D["🔧 Load Function"]

D --> E["▶ Execute Tool"]

E --> F["🧠 Update Shared Memory"]

F --> G{"More Steps?"}

G -->|Yes| C

G -->|No| H["👔 Final Report"]

style A fill:#3949AB,color:white
style B fill:#0097A7,color:white
style C fill:#5C6BC0,color:white
style D fill:#42A5F5,color:white
style E fill:#43A047,color:white
style F fill:#8E24AA,color:white
style G fill:#FB8C00,color:white
style H fill:#D81B60,color:white
```

---

# 🔄 Dynamic Module Loading

One of the key engineering features of the system is **dynamic module execution**.

Rather than hardcoding individual AI agents, the Executor imports each module during runtime based on the execution plan.

This enables:

- Modular development
- Easy addition of new AI agents
- Low coupling between components
- Flexible execution workflows

---

# 📊 Planning vs Execution

| Planner | Executor |
|----------|----------|
| Understands user goals | Executes AI tools |
| Generates execution plan | Follows execution plan |
| Chooses required agents | Loads Python modules |
| Validates workflow | Updates shared memory |
| Uses Qwen for reasoning | Uses Python for orchestration |

---

# 🚀 Engineering Advantages

✅ Dynamic execution planning

✅ Runtime module loading

✅ Decoupled software architecture

✅ Easily extensible tool registry

✅ Modular AI components

✅ Reusable execution engine

✅ Maintainable codebase

✅ Scalable multi-agent framework

---
