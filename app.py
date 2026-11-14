
import streamlit as st
import pymysql
import pandas as pd

st.set_page_config(
    page_title="UrbanPulse NYC 311 Dashboard",
    page_icon="🏙️",
    layout="wide"
)

st.title("UrbanPulse – NYC 311 Analytics")
st.subheader("New York City 311 Service Request Analysis")

st.sidebar.header("Database Connection")

password = st.sidebar.text_input(
    "MySQL Password",
    type="password"
)

if st.sidebar.button("Connect to Database"):

    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password=password,
            database="urbanpulse_db",
            port=3306
        )

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                unique_key,
                created_date,
                closed_date,
                complaint_type,
                status,
                borough
            FROM nyc311_data
        """)

        records = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        df = pd.DataFrame(records, columns=columns)

        cursor.close()
        connection.close()

        st.session_state["complaints_df"] = df

        st.success("MySQL Connection Successful!")

    except Exception as error:
        st.error(f"Database Connection Failed: {error}")

if "complaints_df" in st.session_state:

    df = st.session_state["complaints_df"]

    total_complaints = len(df)

    closed_complaints = (
        df["status"].astype(str).str.lower() == "closed"
    ).sum()

    open_complaints = (
        df["status"].notna().sum() - closed_complaints
    )

    st.header("NYC 311 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Complaints", f"{total_complaints:,}")
    col2.metric("Open Complaints", f"{open_complaints:,}")
    col3.metric("Closed Complaints", f"{closed_complaints:,}")

    st.info("UrbanPulse data loaded successfully from MySQL.")


    st.header("Complaint Analysis Filters")

    borough_options = sorted(
        df["borough"].dropna().unique().tolist()
    )

    complaint_options = sorted(
        df["complaint_type"].dropna().unique().tolist()
    )

    selected_boroughs = st.multiselect(
        "Select Borough",
        options=borough_options,
        default=borough_options
    )

    selected_complaints = st.multiselect(
        "Select Complaint Type",
        options=complaint_options,
        default=complaint_options
    )

    filtered_df = df[
        (df["borough"].isin(selected_boroughs)) &
        (df["complaint_type"].isin(selected_complaints))
    ]

    st.write("Filtered Records:", f"{len(filtered_df):,}")

    st.header("NYC 311 Data Visualizations")

    # Borough-wise Complaint Analysis
    st.subheader("1. Borough-wise Complaints")

    borough_data = (
        filtered_df.groupby("borough")
        .size()
        .sort_values(ascending=False)
    )

    st.bar_chart(borough_data)

    # Top 10 Complaint Types
    st.subheader("2. Top 10 Complaint Types")

    complaint_data = (
        filtered_df.groupby("complaint_type")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(complaint_data)

    # Monthly Complaint Trend
    st.subheader("3. Monthly Complaint Trend")

    monthly_df = filtered_df.copy()

    monthly_df["created_date"] = pd.to_datetime(
        monthly_df["created_date"],
        errors="coerce"
    )

    monthly_df = monthly_df.dropna(
        subset=["created_date"]
    )

    monthly_df["month"] = (
        monthly_df["created_date"].dt.to_period("M").astype(str)
    )

    monthly_data = (
        monthly_df.groupby("month")
        .size()
        .sort_index()
    )

    st.line_chart(monthly_data)

else:
    st.info("Enter your MySQL password and connect to load dashboard data.")
