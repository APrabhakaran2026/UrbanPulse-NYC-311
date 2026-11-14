
import pandas as pd

# Load the cleaned NYC 311 dataset
df = pd.read_csv("cleaned_311_data.csv")

# Display basic dataset information
print("NYC 311 Dataset Loaded Successfully!")

print("\nTotal Records:", len(df))
print("Total Columns:", len(df.columns))
print("Dataset Shape:", df.shape)

# Display the first five records
print("\nFirst 5 Records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()



# Analyze the most common complaint types

complaint_counts = df["complaint_type"].value_counts()

print("\nTop 10 Complaint Types:")
print(complaint_counts.head(10))

# Calculate complaint percentages
complaint_percentages = (
    df["complaint_type"].value_counts(normalize=True) * 100
)

print("\nTop 10 Complaint Percentages:")
print(complaint_percentages.head(10).round(2))

# Display total number of unique complaint types
print("\nTotal Unique Complaint Types:", df["complaint_type"].nunique())



# Analyze complaints by borough

print("\nBorough-wise Complaint Analysis:")

borough_counts = df["borough"].value_counts()

print("\nComplaint Counts:")
print(borough_counts)

# Calculate complaint percentages by borough
borough_percentages = (
    df["borough"].value_counts(normalize=True) * 100
).round(2)

print("\nComplaint Percentages:")
print(borough_percentages)



# Analyze complaints by agency

print("\nAgency-wise Complaint Analysis:")

agency_counts = df["agency"].value_counts()

print("\nComplaint Counts by Agency:")
print(agency_counts)

# Calculate agency-wise complaint percentages
agency_percentages = (
    df["agency"].value_counts(normalize=True) * 100
).round(2)

print("\nAgency-wise Complaint Percentages:")
print(agency_percentages)




# Analyze complaint status distribution

print("\nComplaint Status Analysis:")

status_counts = df["status"].value_counts()

print("\nComplaint Counts by Status:")
print(status_counts)

# Calculate status percentages
status_percentages = (
    df["status"].value_counts(normalize=True) * 100
).round(2)

print("\nComplaint Status Percentages:")
print(status_percentages)



# Convert date columns into datetime format
df["created_date"] = pd.to_datetime(
    df["created_date"], errors="coerce"
)

df["closed_date"] = pd.to_datetime(
    df["closed_date"], errors="coerce"
)

# Calculate complaint resolution time in days
df["resolution_days"] = (
    df["closed_date"] - df["created_date"]
).dt.total_seconds() / 86400

# Keep only valid, non-negative resolution durations
valid_resolution = df[
    df["resolution_days"].notna() &
    (df["resolution_days"] >= 0)
]

print("\nComplaint Resolution Time Analysis:")

print("Closed Complaints with Valid Resolution Time:",
      len(valid_resolution))

print("\nResolution Time Statistics (Days):")
print(valid_resolution["resolution_days"].describe().round(2))



import matplotlib.pyplot as plt
import os

# Create a folder to store analysis charts
os.makedirs("visualizations", exist_ok=True)

# Chart 1: Top 10 Complaint Types
top_complaints = df["complaint_type"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_complaints.sort_values().plot(kind="barh")
plt.title("Top 10 NYC 311 Complaint Types")
plt.xlabel("Number of Complaints")
plt.ylabel("Complaint Type")
plt.tight_layout()
plt.savefig("visualizations/top_10_complaints.png")
plt.show()

# Chart 2: Borough-wise Complaints
borough_counts = df["borough"].value_counts()

plt.figure(figsize=(9, 5))
borough_counts.plot(kind="bar")
plt.title("NYC 311 Complaints by Borough")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/borough_analysis.png")
plt.show()

# Chart 3: Agency-wise Complaints
agency_counts = df["agency"].value_counts().head(10)

plt.figure(figsize=(10, 6))
agency_counts.sort_values().plot(kind="barh")
plt.title("Top 10 Agencies by Complaint Count")
plt.xlabel("Number of Complaints")
plt.ylabel("Agency")
plt.tight_layout()
plt.savefig("visualizations/agency_analysis.png")
plt.show()

# Chart 4: Complaint Status Distribution
status_counts = df["status"].value_counts()

plt.figure(figsize=(8, 5))
status_counts.plot(kind="bar")
plt.title("NYC 311 Complaint Status Distribution")
plt.xlabel("Complaint Status")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/status_analysis.png")
plt.show()

# Chart 5: Complaint Resolution Time
plt.figure(figsize=(9, 5))
valid_resolution["resolution_days"].plot(
    kind="hist", bins=30, edgecolor="black"
)
plt.title("Complaint Resolution Time Distribution")
plt.xlabel("Resolution Time (Days)")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.savefig("visualizations/resolution_time.png")
plt.show()

print("\nAll Visualization Charts Saved Successfully!")



# Analyze daily complaint trends

df["created_date"] = pd.to_datetime(
    df["created_date"], errors="coerce"
)

# Group complaints by creation date
daily_complaints = (
    df.groupby(df["created_date"].dt.date)
    .size()
    .sort_index()
)

print("\nDaily Complaint Trend Analysis:")
print(daily_complaints)

# Create a daily complaint trend chart
plt.figure(figsize=(12, 6))

daily_complaints.plot(
    kind="line",
    marker="o"
)

plt.title("Daily NYC 311 Complaint Trend")
plt.xlabel("Date")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the daily trend chart
plt.savefig("visualizations/daily_complaint_trend.png")

plt.show()

print("\nDaily Complaint Trend Chart Saved Successfully!")



# Analyze complaint submission channels

channel_counts = df["open_data_channel_type"].value_counts()

print("\nComplaint Submission Channel Analysis:")

print("\nComplaint Counts by Channel:")
print(channel_counts)

# Calculate channel-wise percentages
channel_percentages = (
    df["open_data_channel_type"].value_counts(normalize=True) * 100
).round(2)

print("\nChannel-wise Complaint Percentages:")
print(channel_percentages)

# Create a submission channel chart
plt.figure(figsize=(9, 5))

channel_counts.plot(kind="bar")

plt.title("NYC 311 Complaint Submission Channels")
plt.xlabel("Submission Channel")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=30)

plt.tight_layout()

# Save the chart
plt.savefig("visualizations/submission_channel_analysis.png")

plt.show()

print("\nSubmission Channel Chart Saved Successfully!")



# Analyze complaint types across different boroughs

borough_complaint_table = pd.crosstab(
    df["borough"],
    df["complaint_type"]
)

# Select the top 5 complaint types across the dataset
top_5_complaints = (
    df["complaint_type"].value_counts().head(5).index
)

# Filter the table to show only the top 5 complaint types
borough_top_complaints = borough_complaint_table[
    top_5_complaints
]

print("\nComplaint Type by Borough Analysis:")
print(borough_top_complaints)

# Create a comparison chart
borough_top_complaints.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Top 5 Complaint Types Across NYC Boroughs")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=30)
plt.legend(title="Complaint Type")
plt.tight_layout()

# Save the chart
plt.savefig(
    "visualizations/complaint_type_by_borough.png"
)

plt.show()

print("\nComplaint Type by Borough Chart Saved Successfully!")


