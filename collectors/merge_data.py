import pandas as pd

files = [
    "data/raw/nvidia_news.csv",
    "data/raw/google_nvidia_news.csv",
    "data/raw/competitor_news.csv",
    "data/raw/nvidia_ir.csv"
]

all_data = []

for file in files:
    print(f"Loading {file}")
    df = pd.read_csv(file)

   
    df.dropna(                 # Remove rows with missing titles
        subset=["title"],
        inplace=True
    )
  
    df["title"] = (       # Remove extra spaces
        df["title"]
        .astype(str)
        .str.strip()
    )

    all_data.append(df)

master_df = pd.concat(
    all_data,
    ignore_index=True
)

master_df.drop_duplicates(   # Remove duplicates
    subset=["title"],
    inplace=True
)

master_df.to_csv(
    "data/processed/master_dataset.csv",
    index=False
)

print("\nMerge Complete")
print(f"Total Documents: {len(master_df)}")
print("Saved: data/processed/master_dataset.csv")
