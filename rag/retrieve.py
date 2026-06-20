import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

index = faiss.read_index(
    "data/processed/faiss_index.bin"
)

df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

query = input(
    "Enter your question: "
)

query_embedding = model.encode(
    [query]
).astype("float32")

distances, indices = index.search(
    query_embedding,
    k=5
)

print("\nTop Results:\n")

for idx in indices[0]:

    print("-" * 80)

    print(
        df.iloc[idx]["title"]
    )

    print(
        df.iloc[idx]["source"]
    )