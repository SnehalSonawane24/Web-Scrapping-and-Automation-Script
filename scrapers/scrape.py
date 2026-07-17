import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.parse import urljoin


URL = "https://valuenable.in/careers"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

jobs = []

cards = soup.find_all("div", class_="collection-item-3 w-dyn-item")

for card in cards:

    title_tag = card.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else ""

    details = card.find_all("div", class_="text-block-19")

    department = details[0].get_text(strip=True) if len(details) > 0 else ""
    level = details[1].get_text(strip=True) if len(details) > 1 else ""
    location = details[2].get_text(strip=True) if len(details) > 2 else ""

    summary_tag = card.find("div", class_="jobs-summary")
    summary = summary_tag.get_text(strip=True) if summary_tag else ""

    link_tag = card.find("a", href=True)
    link = urljoin(URL, link_tag["href"]) if link_tag else ""

    jobs.append({
        "title": title,
        "department": department,
        "level": level,
        "location": location,
        "summary": summary,
        "link": link,
        "status": "Open"
    })

with open("output/valuenable_jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=4, ensure_ascii=False)

print("JSON file created: valuenable_jobs.json")

with open("output/valuenable_jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "title",
            "department",
            "level",
            "location",
            "summary",
            "link",
            "status"
        ]
    )

    writer.writeheader()
    writer.writerows(jobs)

print("CSV file created: valuenable_jobs.csv")

print(f"\nSuccessfully extracted {len(jobs)} jobs.")