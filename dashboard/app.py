import streamlit as st
import pandas as pd
import ollama

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="NVIDIA AI CEO Strategic Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.big-title {
    font-size: 3rem;
    font-weight: bold;
    color: #76B900;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/master_dataset.csv")

df = load_data()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🚀 NVIDIA AI Agent")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Strategic Analysis",
        "Recommendations",
        "Architecture"
    ]
)

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if page == "Dashboard":

    st.markdown(
        '<p class="big-title">NVIDIA AI CEO Strategic Intelligence Platform</p>',
        unsafe_allow_html=True
    )

    st.write(
        "Strategic intelligence powered by Retrieval-Augmented Generation (RAG), FAISS, and Qwen 2.5."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Documents Collected", len(df))

    with col2:
        st.metric("Sources", df["source"].nunique())

    with col3:
        st.metric("Articles Displayed", min(50, len(df)))

    st.divider()

    st.subheader("Latest Intelligence")

    st.dataframe(
        df[["title", "source"]],
        use_container_width=True,
        height=500
    )

# --------------------------------------------------
# STRATEGIC ANALYSIS
# --------------------------------------------------

# --------------------------------------------------
# STRATEGIC ANALYSIS
# --------------------------------------------------

elif page == "Strategic Analysis":

    st.header("📊 Strategic Intelligence Engine")

    question = st.text_input(
        "Ask a strategic question:",
        "What competitive threats should NVIDIA monitor?"
    )

    if st.button("Generate Strategic Report"):

        context = "\n".join(
            df["title"]
            .fillna("")
            .head(50)
            .tolist()
        )

        prompt = f"""
You are the Chief Strategic Advisor to NVIDIA's CEO.

QUESTION:
{question}

RETRIEVED INTELLIGENCE:
{context}

Analyze the intelligence and generate an executive report.

Provide:

# Strategic Opportunities

For each opportunity provide:
- Opportunity
- Supporting Evidence (exact article title)
- Business Impact (High/Medium/Low)

# Strategic Risks

For each risk provide:
- Risk
- Supporting Evidence (exact article title)
- Risk Severity (High/Medium/Low)

# Emerging Trends

For each trend provide:
- Trend
- Supporting Evidence (exact article title)
- Strategic Importance (High/Medium/Low)

# CEO Action Plan

For each recommendation provide:
- Recommendation
- Supporting Evidence
- Expected Outcome

IMPORTANT RULES:

1. Use ONLY the supplied information.
2. Never invent evidence.
3. Quote article titles exactly.
4. Be concise and executive-focused.
5. Focus on:
   - AI Infrastructure
   - Enterprise AI
   - Data Centers
   - Partnerships
   - Competition
   - Growth Opportunities

Write like a Fortune 500 strategic consultant.
"""

        with st.spinner("Generating strategic intelligence report..."):

            response = ollama.chat(
                model="qwen2.5:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.success("Analysis Complete")

        st.markdown(response["message"]["content"])
# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

elif page == "Recommendations":

    st.header("🎯 Evidence-Based Recommendations")

    if st.button("Generate Recommendations"):

        context = "\n".join(
            df["title"]
            .fillna("")
            .head(50)
            .tolist()
        )

        prompt = f"""
You are NVIDIA's Chief Strategic Advisor.

Analyze ONLY the information provided.

INFORMATION:
{context}

Generate EXACTLY 3 strategic recommendations.

For EACH recommendation provide:

Recommendation

Supporting Evidence
- Minimum 3 evidence sources

Expected Impact
- Revenue Growth
- Market Differentiation
- Customer Acquisition

Risk Assessment
- Financial Risk
- Operational Risk
- Strategic Risk

IMPORTANT:
- Use ONLY supplied information.
- Do NOT invent article titles.
"""

        with st.spinner("Generating recommendations..."):

            response = ollama.chat(
                model="qwen2.5:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.success("Recommendations Generated")

        st.markdown(response["message"]["content"])

# --------------------------------------------------
# ARCHITECTURE
# --------------------------------------------------

elif page == "Architecture":

    st.header("🏗️ System Architecture")

    architecture = """
NVIDIA News
Google News
Investor Relations
Competitor News
        ↓
Data Collection
        ↓
CSV Knowledge Repository
        ↓
Embeddings (BGE Small)
        ↓
FAISS Vector Database
        ↓
Semantic Retrieval
        ↓
Qwen 2.5 (Ollama)
        ↓
Strategic Intelligence Engine
        ↓
Evidence-Based Recommendations
        ↓
CEO Decision Support
"""

    st.code(architecture)

    st.subheader("Technologies Used")

    st.write("""
• Python  
• Pandas  
• BeautifulSoup  
• Feedparser  
• Sentence Transformers  
• BGE Small Embeddings  
• FAISS  
• Ollama  
• Qwen 2.5  
• Streamlit
""")

    st.subheader("Project Statistics")

    st.write(f"Documents Collected: {len(df)}")
    st.write(f"Unique Sources: {df['source'].nunique()}")

    st.success(
        "Strategic Intelligence Platform Successfully Operational"
    )