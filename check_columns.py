
import pandas as pd

# Load the cleaned NYC 311 dataset
df = pd.read_csv("cleaned_311_data.csv")

# Display column names and data types
print("COLUMN DATA TYPES:")
print(df.dtypes)

# Display missing values in each column
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Display total records and columns
print("\nDATASET SHAPE:", df.shape)
