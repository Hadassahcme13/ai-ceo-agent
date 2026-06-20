import pandas as pd
import ollama

# Load your collected documents
df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

# Use latest 20 documents as context
context = "\n".join(
    df["title"]
    .fillna("")
    .head(20)
    .tolist()
)

prompt = f"""
You are a Strategic Intelligence Analyst.

Analyze the following NVIDIA-related information.

INFORMATION:
{context}

Based ONLY on this information:

1. Identify the top opportunities.
2. Identify the top risks.
3. Recommend actions for NVIDIA's CEO.

Use evidence from the information provided.
"""

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])