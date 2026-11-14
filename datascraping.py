import requests
import pandas as pd
import time

# NYC Open Data API connection
url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

# Select the required 25 fields
selected_fields = [
    "unique_key", "created_date", "closed_date", "due_date",
    "agency", "agency_name", "complaint_type", "descriptor",
    "descriptor_2", "location_type", "incident_zip",
    "incident_address", "street_name", "city", "status",
    "resolution_description", "resolution_action_updated_date",
    "community_board", "council_district", "police_precinct",
    "borough", "latitude", "longitude",
    "open_data_channel_type", "bbl"
]


# Base API parameters
params = {
    "$select": ",".join(selected_fields),
    "$where": "created_date >= '2020-01-01T00:00:00'",
    "$order": "created_date DESC, unique_key DESC"
}

# Extract NYC 311 records using API pagination
page_size = 10000
target_records = 100000
offset = 0
all_records = []

while offset < target_records:

    page_params = params.copy()
    page_params["$limit"] = min(page_size, target_records - offset)
    page_params["$offset"] = offset

    max_retries = 3
    batch = None

    for attempt in range(1, max_retries + 1):
        try:
            print(f"Requesting records from offset: {offset}")

            response = requests.get(
                url,
                params=page_params,
                timeout=(15, 180)
            )

            response.raise_for_status()
            batch = response.json()
            break

        except requests.RequestException as error:
            print(f"Request failed: {error}")

            if attempt == max_retries:
                raise

            wait_time = 10 * attempt
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

    if not batch:
        print("No more records available.")
        break

    all_records.extend(batch)

    print("Records fetched:", len(all_records))

    offset += len(batch)

    if len(batch) < page_params["$limit"]:
        print("API returned fewer records than requested.")
        break

    time.sleep(1)

# Create the raw DataFrame
df_raw = pd.DataFrame(all_records, columns=selected_fields)

# Display final dataset information
print("\nFinal Total Records:", len(df_raw))
print("Rows and Columns:", df_raw.shape)
print("Total Columns:", len(df_raw.columns))
print("Duplicate IDs:", df_raw["unique_key"].duplicated().sum())

print("\nMissing Values:")
print(df_raw.isnull().sum())

# Save the raw dataset
df_raw.to_csv("raw_311_data.csv", index=False)

print("\nRaw dataset saved successfully!")
