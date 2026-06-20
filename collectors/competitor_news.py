import feedparser
import pandas as pd

companies = [
    "AMD",
    "Intel"
]

all_articles = []

for company in companies:

    url = (
        f"https://news.google.com/rss/search?"
        f"q={company}&hl=en-US&gl=US&ceid=US:en"
    )

    feed = feedparser.parse(url)

    for entry in feed.entries:

        all_articles.append({
            "company": company,
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", ""),
            "source": "Google News"
        })

df = pd.DataFrame(all_articles)

df.to_csv(
    "data/raw/competitor_news.csv",
    index=False
)

print(f"Collected {len(df)} competitor articles")