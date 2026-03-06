import requests
import pandas as pd

url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"

params = {
    "api-key": "DEMO_KEY",
    "format": "json",
    "limit": 1000
}

response = requests.get(url, params=params)
data = response.json()

records = data.get("records", [])

df = pd.DataFrame(records)

df.to_csv("data/mandi_prices.csv", index=False)

print("Mandi data saved successfully")