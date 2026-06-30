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

Transform business news into **CEO-ready strategic intelligence reports** using autonomous AI agents, semantic retrieval, Retrieval-Augmented Generation (RAG), and a local Large Language Model.

</div>

---

## 📖 Overview

The **AI CEO Strategic Intelligence Agent** is an autonomous multi-agent AI system that helps executive leadership make evidence-based strategic decisions from large collections of business news.

Rather than asking a single LLM to do everything, the system splits the work across specialized agents that collaborate through a **shared memory** object. Each agent has one job:

- 🔍 Retrieve relevant information
- 🚀 Identify strategic opportunities
- ⚠️ Analyze business risks
- 📈 Detect emerging trends
- 😊 Assess market sentiment
- ✔️ Validate all findings
- 👔 Generate an executive strategic intelligence report

Results are presented through an interactive **Streamlit dashboard** built for executive decision support.

---

## ✨ Key Features

| Category | Capability |
|-----------|------------|
| 🧠 Autonomous Planner | Dynamically builds an execution plan from the user's strategic goal |
| ⚙️ AI Executor | Runs each tool in sequence, updating shared memory |
| 🔍 Semantic Search | Retrieves relevant documents via FAISS vector similarity |
| 🚀 Opportunity Analysis | Surfaces strategic business opportunities |
| ⚠️ Risk Analysis | Detects operational and strategic risks |
| 📈 Trend Detection | Identifies emerging technologies and market trends |
| 😊 Sentiment Analysis | Scores article-level market sentiment |
| ✔️ Validation Engine | Confirms every finding is evidence-based |
| 👔 Strategic Intelligence Engine | Synthesizes a CEO-ready report |
| 📊 Executive Dashboard | Interactive visualization in Streamlit |

---

## 🎯 End-to-End Workflow

```mermaid
flowchart TD

A([👤 User Strategic Goal]) --> B

B["🧠 AI Planner
Analyze Goal
Generate Execution Plan"] --> C["📋 Execution Plan"]

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

## 💡 Why Multi-Agent Instead of a Single LLM?

Traditional RAG systems retrieve documents and hand them to one LLM to generate an answer. This project instead uses independent, specialized agents that collaborate through shared memory:

- 🧠 Specialized reasoning per agent
- 🔄 Shared memory for inter-agent collaboration
- ✔️ Evidence validation before reporting
- 📊 Explainable, transparent decision-making
- 📈 Modular, extensible architecture

| Traditional Single-Agent AI | Multi-Agent AI System |
|-----------------------------|-----------------------|
| One prompt performs every task | Specialized agents perform dedicated tasks |
| Difficult to validate outputs | Validation engine verifies every insight |
| Limited explainability | Each agent has a transparent responsibility |
| Hard to extend | New agents added easily via Tool Registry |
| Monolithic architecture | Modular, scalable design |

---

## 🏗️ System Architecture

The system is organized into five layers:

| Layer | Responsibility |
|--------|----------------|
| 👤 User Layer | Accepts strategic goals from executives |
| 🧠 Planning Layer | Planner Agent builds an execution plan |
| ⚙️ Execution Layer | Executor runs specialized agents sequentially |
| 🧠 Intelligence Layer | Validates insights, generates executive report |
| 📊 Presentation Layer | Streamlit dashboard displays the CEO-ready report |

```mermaid
flowchart TB

subgraph USER["👤 User Layer"]
A["CEO / Business User"]
end

subgraph PLAN["🧠 Planning Layer"]
B["Planner Agent"] --> C["Goal Analysis"] --> D["Tool Registry"] --> E["Execution Plan"]
end

subgraph EXEC["⚙️ Execution Layer"]
F["Executor"]
G["Semantic Retriever"]
H["Opportunity Analyzer"]
I["Risk Analyzer"]
J["Trend Analyzer"]
K["Sentiment Analyzer"]
end

subgraph MEMORY["🧠 Shared Agent Memory"]
M["Documents"]
N["Opportunities"]
O["Risks"]
P["Trends"]
Q["Sentiment"]
end

subgraph INTEL["👔 Intelligence Layer"]
R["Validation Engine"]
S["Strategic Intelligence Engine"]
T["CEO Strategic Report"]
end

subgraph DASH["📊 Presentation Layer"]
U["Streamlit Dashboard"]
V["Interactive Visualizations"]
end

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

## 🤖 AI Agents

| Agent | Responsibility | Output |
|-----------|---------------|--------|
| 🧠 Planner Agent | Analyzes the user's goal, creates an execution plan | Execution Plan |
| ⚙️ Executor Agent | Dynamically executes each AI tool | Updated Shared Memory |
| 🔍 Semantic Retriever | Retrieves relevant documents using FAISS | Relevant Articles |
| 🚀 Opportunity Analyzer | Detects strategic business opportunities | Opportunities |
| ⚠️ Risk Analyzer | Identifies strategic/operational risks | Risks |
| 📈 Trend Analyzer | Detects emerging technologies and market trends | Trends |
| 😊 Sentiment Analyzer | Classifies article-level market sentiment | Sentiment |
| ✔️ Validation Engine | Verifies every insight using supporting evidence | Validated Intelligence |
| 👔 Strategic Intelligence Engine | Generates executive strategic intelligence | CEO Report |

### Agent Execution Sequence

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

### Planner & Executor

The **Planner** turns a natural-language goal (e.g. *"Analyze NVIDIA's strategic opportunities in the AI chip market"*) into a structured plan by analyzing intent, consulting the Tool Registry, and using Qwen to select and order the needed agents. Example generated plan:

```text
1. SemanticRetriever
2. OpportunityAnalyzer
3. RiskAnalyzer
4. TrendAnalyzer
5. SentimentAnalyzer
6. Validator
7. StrategicIntelligenceEngine
```

The **Executor** then dynamically imports and runs each module in order, updating shared memory after every step, until the final report is produced. Because modules are loaded at runtime from the Tool Registry rather than hardcoded, new agents can be added without touching the Executor.

### Shared Agent Memory

All agents read and write to one shared memory object instead of passing data directly between tools — this is what allows independent agents to collaborate. Stored fields: `goal`, `documents`, `opportunities`, `risks`, `trends`, `sentiment`, `validation`, `report`.

### Validation Engine

Before the final report is generated, every finding is checked for required fields, supporting evidence, valid impact levels, and duplicates — only validated findings reach the report.

---

## 🔍 Knowledge Base & Retrieval (RAG)

All AI-generated insights are grounded in real business news retrieved from a semantic vector database, rather than relying only on the LLM's internal knowledge.

```mermaid
flowchart LR

A["📰 Business News Dataset"] --> B["🧹 Data Cleaning"] --> C["📄 Master Dataset"]
C --> D["🧠 Sentence Transformer<br/>BAAI/bge-small-en-v1.5"] --> E["🔢 Dense Embeddings"] --> F["📚 FAISS Vector Database"]
G["🔍 User Query"] --> H["🧠 Semantic Search"]
H --> F
F --> I["📄 Top-K Relevant Documents"] --> J["🤖 Multi-Agent Analysis"]

style A fill:#1976D2,color:white
style B fill:#00897B,color:white
style C fill:#5C6BC0,color:white
style D fill:#8E24AA,color:white
style E fill:#3949AB,color:white
style F fill:#673AB7,color:white
style G fill:#E53935,color:white
style H fill:#43A047,color:white
style I fill:#FB8C00,color:white
style J fill:#D81B60,color:white
```

**Pipeline stages:** collect & clean articles → generate dense embeddings with `BAAI/bge-small-en-v1.5` (via SentenceTransformers) → index them in FAISS for fast nearest-neighbor search → encode the user's query → retrieve the top-K most similar articles → pass them to the AI agents.

Semantic search retrieves by **meaning**, not just keywords:

| User Query | Retrieved Result |
|------------|------------------|
| AI chip competition | NVIDIA Blackwell architecture |
| GPU demand | Data center infrastructure expansion |
| Semiconductor market | Advanced packaging technologies |

This grounding reduces hallucination, improves relevance, and makes every recommendation explainable and evidence-backed.

---

## 📊 Executive Dashboard

The Streamlit dashboard walks the user from goal entry to final report:

```mermaid
flowchart LR
A["🎯 Strategic Goal"] --> B["🧠 AI Planner"] --> C["⚙️ AI Execution"] --> D["📊 Dashboard"] --> E["👔 CEO Report"]

style A fill:#1976D2,color:white
style B fill:#673AB7,color:white
style C fill:#26A69A,color:white
style D fill:#3949AB,color:white
style E fill:#D81B60,color:white
```

**Sections:** strategic goal input, execution plan, retrieved articles, opportunity/risk/trend analysis, sentiment visualization, validation summary, and the final CEO Strategic Intelligence Report.

**KPIs & visualizations:** total opportunities, total risks, emerging trends, sentiment distribution (pie chart), opportunity/risk/trend counts (bar chart), and expandable detailed findings.

**Final CEO Report contains:**

- 📌 Executive Summary
- 🚀 Strategic Opportunities (with evidence and impact)
- ⚠️ Strategic Risks (with evidence and impact)
- 📈 Emerging Trends
- 😊 Market Sentiment (🟢 Positive / 🟡 Neutral / 🔴 Negative, each with evidence)
- 🎯 Strategic Recommendations
- 👔 CEO Briefing — what happened, why it matters, what to do next

---

## ⚙️ Installation & Usage

### Prerequisites

| Software | Version |
|-----------|----------|
| Python | 3.11+ |
| Ollama | Latest |
| Git | Latest |
| Streamlit | Latest |

### Setup

```bash
git clone https://github.com/<your-username>/AI-CEO-Strategic-Intelligence-Agent.git
cd AI-CEO-Strategic-Intelligence-Agent
```

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

Install [Ollama](https://ollama.com/download), then pull the model:

```bash
ollama pull qwen2.5:3b
ollama run qwen2.5:3b   # verify
```

### Build the Knowledge Base

```bash
python scripts/generate_embeddings.py
python scripts/build_faiss_index.py
```

### Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

Open `http://localhost:8501`

### Example Goal

```text
Analyze NVIDIA's strategic opportunities in the AI chip market.
```

This triggers: Semantic Retrieval → Opportunity Analysis → Risk Analysis → Trend Detection → Sentiment Analysis → Validation → Strategic Intelligence Report.

---

## 📂 Project Structure

```text
AI-CEO-Strategic-Intelligence-Agent
│
├── agent
│   ├── executor.py
│   ├── planner.py
│   ├── retriever.py
│   ├── opportunity.py
│   ├── risk.py
│   ├── trend.py
│   ├── sentiment.py
│   ├── validator.py
│   ├── strategic_intelligence.py
│   ├── llm_helper.py
│   └── tools.py
│
├── dashboard
│   └── app.py
│
├── data
│   ├── processed
│   │     ├── master_dataset.csv
│   │     ├── embeddings.npy
│   │     └── faiss_index.bin
│   └── raw
│
├── scripts
│   ├── generate_embeddings.py
│   └── build_faiss_index.py
│
├── requirements.txt
├── main.py
└── README.md
```

---

## 💻 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.11 |
| Large Language Model | Qwen 2.5 (via Ollama) |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | FAISS (IndexFlatL2) |
| Embedding Library | SentenceTransformers |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| AI Architecture | Multi-Agent AI |
| Retrieval | Retrieval-Augmented Generation (RAG) |

**Other characteristics:** 384-dim embeddings, business news as the knowledge source, local LLM reasoning, structured JSON report output.

---

## 🎯 Design Principles

- **Modularity** — each agent has one well-defined responsibility
- **Separation of Concerns** — planning, execution, retrieval, analysis, validation, and reporting are independent components
- **Evidence-Based Reasoning** — every recommendation must be backed by retrieved evidence
- **Explainability** — findings include evidence, impact, and validation status
- **Extensibility** — new agents register in the Tool Registry without touching the Executor

---

## 📈 Current Capabilities

✅ Semantic document retrieval · ✅ Opportunity analysis · ✅ Risk analysis · ✅ Trend detection · ✅ Sentiment analysis · ✅ AI validation · ✅ Executive report generation · ✅ Interactive dashboard · ✅ Multi-agent architecture



---

## 🏆 Learning Outcomes

Multi-agent AI systems · Retrieval-Augmented Generation (RAG) · Vector databases (FAISS) · Local LLMs · Semantic search · AI planning & execution · Streamlit dashboard development · Explainable AI · Executive decision support systems

---


## 👨‍💻 Author

**Hadassah Mercy Gottemukula**
Master of Applied Data Science and Artificial Intelligence


---

<div align="center">

### ⭐ If you found this project interesting, consider giving it a star!

Built with ❤️ using Python, Ollama, FAISS, Streamlit, and Multi-Agent AI.

</div>
