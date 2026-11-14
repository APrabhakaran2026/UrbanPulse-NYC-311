import requests
import pandas as pd

# NYC API connection
url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

# Collect 1,000 records
params = {
    "$select": "unique_key,created_date,closed_date,agency,complaint_type,descriptor,borough,status,latitude,longitude",
    "$limit": 1000,
    "$order": "created_date DESC"
}

# Convert JSON to DataFrame
response = requests.get(url, params=params, timeout=30)

print("Status Code:", response.status_code)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
df.head()

# Save raw data as CSV
df.to_csv("raw_311_data.csv", index=False)

print("Raw data saved successfully!")
