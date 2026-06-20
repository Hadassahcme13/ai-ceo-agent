from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

print("Loading dataset...")

df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

# Create text for embedding
texts = []

for _, row in df.iterrows():

    title = str(row.get("title", ""))
    source = str(row.get("source", ""))

    text = f"{title}. Source: {source}"

    texts.append(text)

print(f"Documents loaded: {len(texts)}")

print("Loading BGE model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    show_progress_bar=True
)

np.save(
    "data/processed/embeddings.npy",
    embeddings
)

print("Embeddings saved!")
print(f"Shape: {embeddings.shape}")