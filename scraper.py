import requests
from bs4 import BeautifulSoup
import os

urls = [
    "https://debales.ai/",
]

os.makedirs("data", exist_ok=True)

all_text = ""

for url in urls:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator="\n", strip=True)
        all_text += text + "\n"

        print(f"Scraped: {url}")

    except Exception as e:
        print(f"Error scraping {url}: {e}")

with open("data/debales_content.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Scraping complete!")