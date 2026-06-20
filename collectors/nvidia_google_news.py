import feedparser
import pandas as pd

RSS_URL = (
    "https://news.google.com/rss/search?"
    "q=NVIDIA&hl=en-US&gl=US&ceid=US:en"
)

feed = feedparser.parse(RSS_URL)

articles = []

for entry in feed.entries:
    articles.append({
        "title": entry.title,
        "link": entry.link,
        "published": entry.get("published", ""),
        "source": "Google News"
    })

df = pd.DataFrame(articles)

df.to_csv(
    "data/raw/google_nvidia_news.csv",
    index=False
)

print(f"Collected {len(df)} NVIDIA news articles")