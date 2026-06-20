import pandas as pd
import ollama

print("=" * 60)
print("Evidence-Based Recommendation Engine")
print("=" * 60)

# Load collected intelligence
df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

print(f"\nLoaded {len(df)} documents")

# Use recent documents as context
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

==================================================

Recommendation:

Supporting Evidence:
- Cite the EXACT article titles from the information.
- Minimum 3 evidence sources.

Expected Impact:
- Revenue Growth (High/Medium/Low)
- Market Differentiation (High/Medium/Low)
- Customer Acquisition (High/Medium/Low)

Risk Assessment:
- Financial Risk (High/Medium/Low)
- Operational Risk (High/Medium/Low)
- Strategic Risk (High/Medium/Low)

==================================================

IMPORTANT RULES:

1. Use ONLY the supplied information.
2. Do NOT use outside knowledge.
3. Do NOT invent article titles.
4. Quote article titles exactly as they appear.
5. If evidence is insufficient, state:
   "No evidence found in retrieved documents."
6. Be concise and executive focused.
7. Focus on:
   - AI Infrastructure
   - Data Centers
   - Enterprise AI
   - Partnerships
   - Competition
   - Growth Opportunities

Return the report in professional executive format.
"""

print("\nGenerating recommendations...\n")

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
print("EVIDENCE-BASED RECOMMENDATIONS")
print("=" * 60 + "\n")

print(
    response["message"]["content"]
)

print("\n" + "=" * 60)
print("END OF REPORT")
print("=" * 60)