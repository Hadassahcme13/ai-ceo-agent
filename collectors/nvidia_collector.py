import feedparser
import pandas as pd

feed = feedparser.parse(
    "https://nvidianews.nvidia.com/rss.xml"
)

articles = []

for entry in feed.entries:
    articles.append({
        "title": entry.get("title", ""),
        "link": entry.get("link", ""),
        "published": entry.get("published", ""),
        "source": "NVIDIA"
    })

df = pd.DataFrame(articles)

df.to_csv(
    "data/raw/nvidia_news.csv",
    index=False
)

print(f"Collected {len(df)} NVIDIA articles")