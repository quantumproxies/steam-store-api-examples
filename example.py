"""Minimal Steam game data API call — one typed row per app.

Docs & schema: https://quanticdata.io/collectors/steam-store-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/steam/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "portal",
        "max_results": 10
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("app_id"), row.get("name"), row.get("type"))
print(f"{len(data['results'])} apps, cost ${data['cost']}")
