import faiss
import numpy as np

print("Loading embeddings...")

embeddings = np.load(
    "data/processed/embeddings.npy"
)

embeddings = embeddings.astype("float32")

print(
    f"Embedding Shape: {embeddings.shape}"
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

faiss.write_index(
    index,
    "data/processed/faiss_index.bin"
)

print(
    f"Indexed {index.ntotal} documents"
)

print("FAISS index saved!")