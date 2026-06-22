# 🚀 NVIDIA AI CEO Strategic Intelligence Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![NLP](https://img.shields.io/badge/NLP-RAG-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-orange?style=for-the-badge)
![Qwen](https://img.shields.io/badge/LLM-Qwen_2.5-red?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-ff4b4b?style=for-the-badge\&logo=streamlit)

### 🎓 Master's Final Examination Project

**AI-Powered Strategic Intelligence Platform for Executive Decision Support**

Transforming NVIDIA Industry Intelligence into Evidence-Based Strategic Recommendations

</div>

---

# 📌 Project Overview

Modern organizations face an overwhelming amount of information from:

* 📰 Industry News
* 📈 Investor Relations Announcements
* 🤝 Strategic Partnerships
* ⚔️ Competitor Activities
* 🧠 AI Technology Developments

This project builds an **AI Strategic Intelligence Agent** capable of:

✅ Collecting Industry Intelligence

✅ Building a Knowledge Repository

✅ Performing Semantic Search

✅ Generating Strategic Insights

✅ Producing Evidence-Based Recommendations

✅ Supporting Executive Decision Making

---

# 🎯 Project Objectives

| Objective                 | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| 📥 Information Collection | Gather NVIDIA-related intelligence from multiple sources |
| 🧠 Knowledge Creation     | Create a searchable intelligence repository              |
| 🔍 Semantic Retrieval     | Retrieve relevant information using embeddings           |
| 🤖 Strategic Analysis     | Generate executive-level insights                        |
| 📊 Recommendations        | Produce evidence-based recommendations                   |
| 🖥 Dashboard              | Provide an interactive decision-support interface        |

---

# 🏗 System Architecture

```text
┌─────────────────────┐
│   NVIDIA Newsroom   │
└──────────┬──────────┘
           │

┌─────────────────────┐
│    Google News      │
└──────────┬──────────┘
           │

┌─────────────────────┐
│ Investor Relations  │
└──────────┬──────────┘
           │

┌─────────────────────┐
│ Competitor News     │
└──────────┬──────────┘
           │
           ▼

┌────────────────────────────┐
│     Data Collection Layer  │
└────────────┬───────────────┘
             ▼

┌────────────────────────────┐
│ Knowledge Repository       │
│ (313 Documents)            │
└────────────┬───────────────┘
             ▼

┌────────────────────────────┐
│ BGE Small Embeddings       │
└────────────┬───────────────┘
             ▼

┌────────────────────────────┐
│ FAISS Vector Database      │
└────────────┬───────────────┘
             ▼

┌────────────────────────────┐
│ Semantic Retrieval Engine  │
└────────────┬───────────────┘
             ▼

┌────────────────────────────┐
│ Qwen 2.5 via Ollama        │
└────────────┬───────────────┘
             ▼

┌────────────────────────────┐
│ Strategic Intelligence     │
└────────────┬───────────────┘
             ▼

┌────────────────────────────┐
│ CEO Recommendations        │
└────────────────────────────┘
```

---

# 🔄 RAG Workflow

```text
User Question
      │
      ▼
Convert Query to Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Retrieve Relevant Articles
      │
      ▼
Qwen 2.5 LLM
      │
      ▼
Strategic Analysis
      │
      ▼
Evidence-Based Recommendation
```

---

# 🛠 Technology Stack

| Layer           | Technology                          |
| --------------- | ----------------------------------- |
| Programming     | Python                              |
| Data Processing | Pandas, NumPy                       |
| Data Collection | Feedparser, Requests, BeautifulSoup |
| Embeddings      | BAAI/bge-small-en-v1.5              |
| Vector Search   | FAISS                               |
| LLM             | Qwen 2.5                            |
| Local Inference | Ollama                              |
| Dashboard       | Streamlit                           |
| Version Control | Git & GitHub                        |

---

# 📂 Project Structure

```text
ai-ceo-agent/
│
├── collectors/
│   ├── nvidia_collector.py
│   ├── nvidia_google_news.py
│   ├── competitor_news.py
│   ├── nvidia_ir_collector.py
│   └── merge_data.py
│
├── embeddings/
│   └── embed.py
│
├── rag/
│   ├── build_index.py
│   └── retrieve.py
│
├── intelligence/
│   ├── strategic_engine.py
│   └── recommendations.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── requirements.txt
└── README.md
```

---

# 📊 Data Sources

| Source             | Purpose                |
| ------------------ | ---------------------- |
| NVIDIA Newsroom    | Product announcements  |
| Investor Relations | Corporate intelligence |
| Google News        | Industry developments  |
| Competitor News    | Competitive analysis   |

### 📈 Dataset Statistics

| Metric              | Value     |
| ------------------- | --------- |
| Documents Collected | 313       |
| Sources             | 4         |
| Embedding Model     | BGE Small |
| Vector Dimensions   | 384       |
| Vector Database     | FAISS     |
| LLM                 | Qwen 2.5  |

---

# 🧠 NLP Concepts Implemented

| NLP Technique                  | Usage                       |
| ------------------------------ | --------------------------- |
| Text Processing                | Knowledge preparation       |
| Embeddings                     | Semantic representation     |
| Semantic Similarity            | Document retrieval          |
| Information Retrieval          | Knowledge search            |
| Vector Search                  | FAISS indexing              |
| Retrieval-Augmented Generation | Context-grounded generation |
| Large Language Models          | Strategic reasoning         |

---

# 🎯 Strategic Intelligence Engine

The system generates:

### ✅ Strategic Opportunities

Identify growth opportunities and market expansion potential.

### ⚠ Strategic Risks

Identify threats, competition, and business risks.

### 📈 Emerging Trends

Detect new developments and industry shifts.

### 👨‍💼 CEO Recommendations

Generate executive-level action plans.

---

# 📋 Evidence-Based Recommendation Framework

Every recommendation contains:

| Component           | Description            |
| ------------------- | ---------------------- |
| Recommendation      | Strategic action       |
| Supporting Evidence | Article-based evidence |
| Expected Impact     | Business value         |
| Risk Assessment     | Potential risks        |

### Example

```text
Recommendation:
Expand AI Infrastructure Investments

Supporting Evidence:
- NVIDIA & LG AI Factory
- HPE AI Factory
- SK Telecom AI Partnership

Expected Impact:
- Revenue Growth
- Market Differentiation
- Customer Acquisition

Risk Assessment:
- Financial Risk
- Operational Risk
- Strategic Risk
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-repository/ai-ceo-agent.git

cd ai-ceo-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

### Collect Data

```bash
python collectors/nvidia_collector.py
python collectors/nvidia_google_news.py
python collectors/competitor_news.py
python collectors/nvidia_ir_collector.py
```

### Merge Data

```bash
python collectors/merge_data.py
```

### Generate Embeddings

```bash
python embeddings/embed.py
```

### Build Vector Database

```bash
python rag/build_index.py
```

### Run Strategic Intelligence Engine

```bash
python intelligence/strategic_engine.py
```

### Run Recommendation Engine

```bash
python intelligence/recommendations.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

✅ Natural Language Processing

✅ Embeddings

✅ Vector Databases

✅ Information Retrieval

✅ Retrieval-Augmented Generation (RAG)

✅ Large Language Models

✅ Strategic Intelligence Systems

✅ Executive Decision Support

---

# 👨‍💻 Author

### Hadassah Mercy Gottemukula

Master's Final Examination Project NLP

NVIDIA AI CEO Strategic Intelligence Agent

Built using NLP, RAG, FAISS, Qwen 2.5 and Streamlit 🚀
