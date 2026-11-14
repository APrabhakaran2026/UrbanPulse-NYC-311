
import pandas as pd
from sqlalchemy import create_engine, URL, Text, String, DateTime, Float
from getpass import getpass

# Read the cleaned NYC 311 dataset
df = pd.read_csv(
    "cleaned_311_data.csv",
    dtype={
        "unique_key": str,
        "incident_zip": str,
        "council_district": str,
        "police_precinct": str,
        "bbl": str
    }
)

# Convert date columns into datetime format
date_columns = [
    "created_date",
    "closed_date",
    "due_date",
    "resolution_action_updated_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

# Connect to the UrbanPulse MySQL database
password = getpass("Enter UrbanPulse database password: ")

connection_url = URL.create(
    "mysql+pymysql",
    username="urbanpulse_user",
    password=password,
    host="localhost",
    port=3306,
    database="urbanpulse_db"
)

engine = create_engine(connection_url)

# Define MySQL column data types
column_types = {
    "unique_key": String(30),
    "created_date": DateTime(),
    "closed_date": DateTime(),
    "due_date": DateTime(),
    "incident_zip": String(20),
    "council_district": String(20),
    "police_precinct": String(20),
    "latitude": Float(),
    "longitude": Float(),
    "bbl": String(30)
}

# Store the cleaned records in MySQL
for column in df.columns:
    if column not in column_types:
        column_types[column] = Text()

df.to_sql(
    name="nyc311_data",
    con=engine,
    if_exists="fail",
    index=False,
    chunksize=500,
    dtype=column_types
)

# Verify the total number of inserted records
with engine.connect() as connection:
    total_records = connection.exec_driver_sql(
        "SELECT COUNT(*) FROM nyc311_data"
    ).scalar()

print("Data successfully stored in MySQL!")
print("Total Records Inserted:", total_records)

engine.dispose()
