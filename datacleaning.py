
import pandas as pd

# Module 2: Data Cleaning

# Load the raw NYC 311 dataset
df = pd.read_csv("raw_311_data.csv")

# Display dataset overview
print("Dataset Loaded Successfully!")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("Dataset Shape:", df.shape)

# Display first five records
print("\nFirst 5 Records:")
print(df.head())

# Display column data types
print("\nColumn Data Types:")
print(df.dtypes)

# Check duplicate records
print("\nDuplicate Rows:", df.duplicated().sum())

# Check duplicate request IDs
print("Duplicate Unique Keys:", df["unique_key"].duplicated().sum())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check date range
dates = pd.to_datetime(df["created_date"], errors="coerce")

print("\nDate Range:")
print("Earliest Date:", dates.min())
print("Latest Date:", dates.max())
print("Invalid Dates:", dates.isna().sum())



# Convert date columns into datetime format
date_columns = [
    "created_date",
    "closed_date",
    "due_date",
    "resolution_action_updated_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

# Verify converted data types
print("\nDate Columns Data Types:")
print(df[date_columns].dtypes)

# Display date conversion results
print("\nDate Conversion Missing Values:")
print(df[date_columns].isnull().sum())



# Convert identifier columns into appropriate data types

# Convert ZIP codes into 5-digit strings
df["incident_zip"] = (
    pd.to_numeric(df["incident_zip"], errors="coerce")
    .astype("Int64")
    .astype("string")
    .str.zfill(5)
)

# Convert council district into nullable integer
df["council_district"] = pd.to_numeric(
    df["council_district"], errors="coerce"
).astype("Int64")

# Convert BBL into 10-digit string identifiers
df["bbl"] = (
    pd.to_numeric(df["bbl"], errors="coerce")
    .astype("Int64")
    .astype("string")
    .str.zfill(10)
)

# Verify converted data types
print("\nIdentifier Data Types:")
print(df[["incident_zip", "council_district", "bbl"]].dtypes)

print("\nIdentifier Sample Values:")
print(df[["incident_zip", "council_district", "bbl"]].head(10))



# Standardize text columns by removing extra spaces

text_columns = [
    "agency",
    "agency_name",
    "complaint_type",
    "descriptor",
    "descriptor_2",
    "location_type",
    "incident_address",
    "street_name",
    "city",
    "status",
    "resolution_description",
    "community_board",
    "police_precinct",
    "borough",
    "open_data_channel_type"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()
    df[column] = df[column].replace("", pd.NA)

# Verify text standardization
print("\nText Standardization Completed!")

print("\nMissing Values in Text Columns:")
print(df[text_columns].isnull().sum())

print("\nSample Complaint Types:")
print(df["complaint_type"].value_counts().head(10))


# Analyze missing values and their percentages

missing_count = df.isnull().sum()

missing_percentage = (
    df.isnull().sum() / len(df)
) * 100

missing_summary = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage.round(2)
})

missing_summary = missing_summary[
    missing_summary["Missing_Count"] > 0
].sort_values(
    by="Missing_Percentage",
    ascending=False
)

print("\nMissing Value Analysis:")
print(missing_summary)



# Validate geographic and numeric values

print("\nGeographic Data Validation:")

# Check valid latitude range
invalid_latitude = df[
    df["latitude"].notna() &
    ~df["latitude"].between(-90, 90)
]

# Check valid longitude range
invalid_longitude = df[
    df["longitude"].notna() &
    ~df["longitude"].between(-180, 180)
]

# Check NYC ZIP code format
invalid_zip = df[
    df["incident_zip"].notna() &
    ~df["incident_zip"].str.fullmatch(r"\d{5}")
]

print("Invalid Latitude Values:", len(invalid_latitude))
print("Invalid Longitude Values:", len(invalid_longitude))
print("Invalid ZIP Codes:", len(invalid_zip))

# Display coordinate summary
print("\nLatitude Summary:")
print(df["latitude"].describe())

print("\nLongitude Summary:")
print(df["longitude"].describe())



# Validate complaint status and category values

print("\nComplaint Status Distribution:")
print(df["status"].value_counts(dropna=False))

print("\nBorough Distribution:")
print(df["borough"].value_counts(dropna=False))

print("\nAgency Distribution:")
print(df["agency"].value_counts().head(10))

print("\nOpen Data Channel Distribution:")
print(df["open_data_channel_type"].value_counts(dropna=False))

# Check unique category counts
print("\nUnique Category Counts:")
print("Complaint Types:", df["complaint_type"].nunique())
print("Agencies:", df["agency"].nunique())
print("Boroughs:", df["borough"].nunique())
print("Statuses:", df["status"].nunique())



# Check complaint status and closed date consistency

print("\nStatus and Closed Date Consistency:")

status_date_check = pd.crosstab(
    df["status"],
    df["closed_date"].isna(),
    margins=True
)

status_date_check.columns = [
    "Closed Date Available",
    "Closed Date Missing",
    "Total"
]

print(status_date_check)

print("\nMissing values are preserved.")
print("No rows or columns have been deleted.")



# Save the cleaned dataset into a new CSV file

df.to_csv("cleaned_311_data.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

# Verify the cleaned dataset
cleaned_df = pd.read_csv("cleaned_311_data.csv")

print("Total Records:", len(cleaned_df))
print("Total Columns:", len(cleaned_df.columns))
print("Dataset Shape:", cleaned_df.shape)

print("\nFirst 5 Cleaned Records:")
print(cleaned_df.head())
