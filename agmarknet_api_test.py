import requests
import json
import time

session = requests.Session()

url = "https://api.agmarknet.gov.in/v1/price-trend/wholesale-arrivals-weekly"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://agmarknet.gov.in",
    "Referer": "https://agmarknet.gov.in/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

session.headers.update(headers)

all_data = []

for month in range(1, 13):
    for week in range(1, 6):

        params = {
            "report_mode": "Marketwise",
            "commodity": 65,
            "year": 2021,
            "month": month,
            "week": week,
            "state": 20,
            "district": 364,
            "export": "false"
        }

        try:

            r = session.get(url, params=params)

            print("Status:", r.status_code)

            if r.status_code == 200:
                data = r.json()

                all_data.append({
                    "month": month,
                    "week": week,
                    "data": data
                })

                print(f"Fetched Month {month} Week {week}")

            else:
                print(f"Blocked Month {month} Week {week}")

        except Exception as e:
            print("Error:", e)

        # important delay
        time.sleep(5)

with open("agmarknet_2021_raw.json", "w") as f:
    json.dump(all_data, f, indent=2)

print("Saved JSON")



