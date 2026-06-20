import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://investor.nvidia.com/news/default.aspx"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

articles = []

for link in soup.find_all("a"):

    title = link.get_text(strip=True)

    href = link.get("href")

    if title and href:

        if "news" in href.lower():

            if not href.startswith("http"):
                href = (
                    "https://investor.nvidia.com"
                    + href
                )

            articles.append({
                "title": title,
                "link": href,
                "source": "NVIDIA Investor Relations"
            })

df = pd.DataFrame(articles)

df.drop_duplicates(
    subset=["title"],
    inplace=True
)

df.to_csv(
    "data/raw/nvidia_ir.csv",
    index=False
)

print(f"Collected {len(df)} IR articles")