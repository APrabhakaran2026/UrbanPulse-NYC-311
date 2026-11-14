
import pandas as pd

# Load the cleaned NYC 311 dataset
df = pd.read_csv("cleaned_311_data.csv")

# Check duplicate unique keys
print("DUPLICATE UNIQUE KEYS:")
print(df["unique_key"].duplicated().sum())

# Inspect date column values
date_columns = [
    "created_date",
    "closed_date",
    "due_date",
    "resolution_action_updated_date"
]

print("\nDATE COLUMN SAMPLES:")

for column in date_columns:
    print(f"\n{column}:")
    print(df[column].dropna().head(3).tolist())

# Check maximum text length
text_columns = df.select_dtypes(include="object").columns

print("\nMAXIMUM TEXT LENGTH:")

for column in text_columns:
    max_length = df[column].dropna().astype(str).str.len().max()
    print(column, ":", max_length)
