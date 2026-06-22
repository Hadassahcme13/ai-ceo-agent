import pandas as pd
import ollama

print("=" * 60)
print("NVIDIA Strategic Intelligence Engine")
print("=" * 60)

# Load collected documents
print("\nLoading dataset...")

df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

print(f"Loaded {len(df)} documents")

# User question
query = input(
    "\nAsk a strategic question: "
)

# Use latest documents as context
context = "\n".join(
    df["title"]
    .fillna("")
    .head(30)
    .tolist()
)

prompt = f"""
You are NVIDIA's Strategic Intelligence Advisor.

QUESTION:
{query}

INFORMATION:
{context}

IMPORTANT RULES:

1. Use ONLY the information provided.
2. Do NOT use outside knowledge.
3. If there is insufficient evidence, write:
   "No evidence found in retrieved documents."
4. Every opportunity, risk, trend, and recommendation MUST cite the article title that supports it.
5. Base all conclusions strictly on the supplied information.

Generate a report with the following sections:

==================================================
STRATEGIC OPPORTUNITIES
==================================================

For each opportunity provide:

Opportunity:
Evidence:
Impact (High/Medium/Low):
Recommendation:

==================================================
STRATEGIC RISKS
==================================================

For each risk provide:

Risk:
Evidence:
Impact (High/Medium/Low):
Recommendation:

==================================================
EMERGING TRENDS
==================================================

For each trend provide:

Trend:
Evidence:
Impact (High/Medium/Low):
Recommendation:

==================================================
CEO ACTION PLAN
==================================================

Provide the Top 3 CEO priorities.

For each priority provide:

Priority:
Supporting Evidence:
Expected Impact:
Recommended Action:

Use a professional executive-report style.
"""

print("\nGenerating strategic intelligence report...\n")

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n" + "=" * 60)
print("STRATEGIC INTELLIGENCE REPORT")
print("=" * 60 + "\n")

print(
    response["message"]["content"]
)

print("\n" + "=" * 60)
print("END OF REPORT")
print("=" * 60)
