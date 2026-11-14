# UrbanPulse – NYC 311 Service Request Analysis

## 1. Project Overview

UrbanPulse is a Data Science project that analyzes NYC 311 Service Requests to identify complaint trends, geographic patterns, agency workload, and service resolution performance.

The project uses Python, Pandas, MySQL, SQL, and Streamlit to transform raw service request data into meaningful insights.

## 2. Project Objectives

- Collect 100,000 NYC 311 service request records.
- Clean and preprocess the dataset.
- Perform data quality assessment.
- Analyze complaint patterns and distributions.
- Store processed data in MySQL.
- Perform SQL-based analyst investigations.
- Build an interactive Streamlit dashboard.
- Identify meaningful business insights.

## 3. Dataset Details

- **Dataset:** NYC 311 Service Requests
- **Total Records:** 100,000
- **Raw Dataset:** `raw_311_data.csv`
- **Cleaned Dataset:** `cleaned_311_data.csv`

The raw and cleaned CSV files are retained locally and excluded from Git tracking because of their size.

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Requests
- Matplotlib
- MySQL
- PyMySQL
- SQLAlchemy
- Streamlit
- Visual Studio Code

## 5. Project Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Data Quality Assessment
4. Exploratory Data Analysis
5. Statistical Analysis
6. MySQL Database Integration
7. SQL Analyst Investigations
8. Interactive Dashboard Development
9. Business Insights

## 6. Exploratory Data Analysis

The project includes eight visualizations covering complaint patterns and distributions, including:

- Top complaint types
- Borough-wise complaint distribution
- Agency analysis
- Daily complaint trends
- Complaint status analysis
- Resolution time analysis
- Submission channel analysis
- Complaint types by borough

Visualization files are available in the `visualizations/` folder and as `Figure_1.png` to `Figure_8.png` in the project root.

## 7. SQL Analyst Investigations

Twelve SQL investigations were performed to explore NYC 311 service request data and identify useful patterns.

**SQL file:** `sql/UrbanPulse_Investigations_01_to_12.sql`

## 8. Interactive Dashboard

The Streamlit dashboard provides:

- Total complaint records
- Open complaints
- Closed complaints
- Borough-based filtering
- Complaint-type filtering
- Filtered complaint records

The dashboard retrieves data from the MySQL database.

## 9. Project Setup and Execution

### Prerequisites

- Python
- MySQL Server
- Required Python packages listed in `requirements.txt`

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit dashboard

```bash
streamlit run app.py
```

Make sure the MySQL server is running and the database connection settings in the application are configured correctly. Do not store database passwords in public source code.

## 10. Project Folder Structure

```text
UrbanPulse_Projects_1/
|
|-- app.py
|-- datascraping.py
|-- datascraping_backup.py
|-- datacleaning.py
|-- dataanalysis.py
|-- urbanpulse_nyc.py
|-- create_mysql_table.py
|-- load_cleaned_data_to_mysql.py
|-- test_mysql_connection.py
|-- check_columns.py
|-- check_mysql_schema.py
|
|-- requirements.txt
|-- .gitignore
|-- PROJECT_PLAN.md
|-- README.md
|
|-- Figure_1.png
|-- Figure_2.png
|-- Figure_3.png
|-- Figure_4.png
|-- Figure_5.png
|-- Figure_6.png
|-- Figure_7.png
|-- Figure_8.png
|
|-- visualizations/
|   |-- agency_analysis.png
|   |-- borough_analysis.png
|   |-- complaint_type_by_borough.png
|   |-- daily_complaint_trend.png
|   |-- resolution_time.png
|   |-- status_analysis.png
|   |-- submission_channel_analysis.png
|   |-- top_10_complaints.png
|
|-- sql/
|   |-- UrbanPulse_Investigations_01_to_12.sql
|
|-- raw_311_data.csv
|-- cleaned_311_data.csv
|-- urbanpulse_dev_1000.csv
```

## 11. Project Outcome

UrbanPulse demonstrates an end-to-end Data Science workflow, from collecting and cleaning real-world service request data to performing exploratory analysis, SQL investigations, and interactive dashboard development.