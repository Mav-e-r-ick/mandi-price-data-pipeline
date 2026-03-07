import requests
import json
import time

url = "https://api.agmarknet.gov.in/v1/price-trend/wholesale-arrivals-weekly"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://agmarknet.gov.in",
    "Referer": "https://agmarknet.gov.in/",
    "User-Agent": "Mozilla/5.0"
}

session = requests.Session()
session.headers.update(headers)

all_data = []

for year in range(2021, 2027):

    if year == 2026:
        months = [1]
    else:
        months = range(1, 13)

    for month in months:
        for week in range(1, 5):

            params = {
                "report_mode": "Marketwise",
                "commodity": 23,   # Onion
                "year": year,
                "month": month,
                "week": week,
                "state": 20,
                "district": 364,
                "export": "false"
            }

            try:

                r = session.get(url, params=params)

                print("Status:", r.status_code)

                if r.status_code == 200 and r.text.strip():

                    data = r.json()

                    all_data.append({
                        "year": year,
                        "month": month,
                        "week": week,
                        "data": data
                    })

                    print(f"Fetched {year} Month {month} Week {week}")

                else:
                    print(f"Blocked {year} Month {month} Week {week}")

            except Exception as e:
                print("Error:", e)

            time.sleep(4)

with open("onion_arrivals_2022_2026.json", "w") as f:
    json.dump(all_data, f, indent=2)

print("Saved: onion_arrivals_2022_2026.json")