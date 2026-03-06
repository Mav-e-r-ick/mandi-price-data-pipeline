import requests
import pandas as pd
import os

# API endpoint
url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"

api_key = "DEMO_KEY"

all_records = []
offset = 0
limit = 1000

while True:
    params = {
        "api-key": api_key,
        "format": "json",
        "limit": limit,
        "offset": offset
    }

    response = requests.get(url, params=params)
    data = response.json()
    records = data.get("records", [])

    if not records:
        break

    all_records.extend(records)
    offset += limit
    print(f"Downloaded {len(all_records)} records...")

df = pd.DataFrame(all_records)

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Save file
df.to_csv("data/mandi_prices_full.csv", index=False)

print("All mandi data saved successfully")