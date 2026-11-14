-- ============================================================
-- UrbanPulse Project
-- Module 5: SQL Analyst Investigations
-- Investigations 01 to 12
-- Database: urbanpulse_db
-- Table: nyc311_data
--
-- Run each query separately in MySQL Workbench or MySQL CLI.
-- Dataset: 100,000 NYC 311 records.
-- ============================================================


-- ------------------------------------------------------------
-- Investigation 01: Top 10 Complaint Types
-- Business question: Which complaint types are reported most?
-- ------------------------------------------------------------
SELECT
    complaint_type,
    COUNT(*) AS total_complaints
FROM nyc311_data
GROUP BY complaint_type
ORDER BY total_complaints DESC
LIMIT 10;


-- ------------------------------------------------------------
-- Investigation 02: Borough-wise Complaint Distribution
-- Business question: Which borough receives the most complaints?
-- ------------------------------------------------------------
SELECT
    borough,
    COUNT(*) AS total_complaints
FROM nyc311_data
WHERE borough IS NOT NULL
GROUP BY borough
ORDER BY total_complaints DESC;


-- ------------------------------------------------------------
-- Investigation 03: Agency-wise Complaint Distribution
-- Business question: Which agencies receive the most complaints?
-- ------------------------------------------------------------
SELECT
    agency,
    agency_name,
    COUNT(*) AS total_complaints
FROM nyc311_data
GROUP BY agency, agency_name
ORDER BY total_complaints DESC
LIMIT 10;


-- ------------------------------------------------------------
-- Investigation 04: Monthly Complaint Trends
-- Business question: How are complaints distributed by month?
-- Note: The current dataset contains records from October and
-- November 2026 only; do not interpret this as a yearly trend.
-- ------------------------------------------------------------
SELECT
    DATE_FORMAT(created_date, '%Y-%m') AS complaint_month,
    COUNT(*) AS total_complaints
FROM nyc311_data
WHERE created_date IS NOT NULL
GROUP BY complaint_month
ORDER BY total_complaints DESC;


-- ------------------------------------------------------------
-- Investigation 05: Average Resolution Time by Agency
-- Business question: Which agencies take longer to resolve cases?
-- ------------------------------------------------------------
SELECT
    agency,
    COUNT(*) AS resolved_complaints,
    ROUND(
        AVG(TIMESTAMPDIFF(HOUR, created_date, closed_date)) / 24,
        2
    ) AS avg_resolution_days
FROM nyc311_data
WHERE created_date IS NOT NULL
  AND closed_date IS NOT NULL
GROUP BY agency
ORDER BY avg_resolution_days DESC;


-- ------------------------------------------------------------
-- Investigation 06: Complaint Status Distribution
-- Business question: What is the current status distribution?
-- ------------------------------------------------------------
SELECT
    status,
    COUNT(*) AS total_complaints
FROM nyc311_data
GROUP BY status
ORDER BY total_complaints DESC;


-- ------------------------------------------------------------
-- Investigation 07: Complaint Type by Borough
-- Business question: How many complaints of each type occur
-- in each borough?
-- ------------------------------------------------------------
SELECT
    borough,
    complaint_type,
    COUNT(*) AS total_complaints
FROM nyc311_data
WHERE borough IS NOT NULL
  AND complaint_type IS NOT NULL
GROUP BY borough, complaint_type
ORDER BY borough, total_complaints DESC;


-- ------------------------------------------------------------
-- Investigation 08: Complaint Distribution by Day of Week
-- Business question: Which weekday receives the most complaints?
-- ------------------------------------------------------------
SELECT
    DAYNAME(created_date) AS complaint_day,
    COUNT(*) AS total_complaints
FROM nyc311_data
WHERE created_date IS NOT NULL
GROUP BY
    DAYOFWEEK(created_date),
    DAYNAME(created_date)
ORDER BY total_complaints DESC;


-- ------------------------------------------------------------
-- Investigation 09: Complaint Distribution by Hour
-- Business question: At which hour are most complaints reported?
-- ------------------------------------------------------------
SELECT
    HOUR(created_date) AS complaint_hour,
    COUNT(*) AS total_complaints
FROM nyc311_data
WHERE created_date IS NOT NULL
GROUP BY HOUR(created_date)
ORDER BY total_complaints DESC;


-- ------------------------------------------------------------
-- Investigation 10: Average Resolution Time by Complaint Type
-- Business question: Which complaint types take longest to resolve?
-- Only complaint types with at least 100 resolved records are
-- included to reduce the effect of very small sample sizes.
-- ------------------------------------------------------------
SELECT
    complaint_type,
    COUNT(*) AS resolved_complaints,
    ROUND(
        AVG(TIMESTAMPDIFF(HOUR, created_date, closed_date)) / 24,
        2
    ) AS avg_resolution_days
FROM nyc311_data
WHERE created_date IS NOT NULL
  AND closed_date IS NOT NULL
  AND complaint_type IS NOT NULL
GROUP BY complaint_type
HAVING COUNT(*) >= 100
ORDER BY avg_resolution_days DESC
LIMIT 10;


-- ------------------------------------------------------------
-- Investigation 11: Borough-wise Average Resolution Time
-- Business question: Which borough has the longest average
-- complaint resolution time?
-- ------------------------------------------------------------
SELECT
    borough,
    COUNT(*) AS resolved_complaints,
    ROUND(
        AVG(TIMESTAMPDIFF(HOUR, created_date, closed_date)) / 24,
        2
    ) AS avg_resolution_days
FROM nyc311_data
WHERE created_date IS NOT NULL
  AND closed_date IS NOT NULL
  AND borough IS NOT NULL
GROUP BY borough
HAVING COUNT(*) >= 100
ORDER BY avg_resolution_days DESC;


-- ------------------------------------------------------------
-- Investigation 12: Top 10 Complaint Types in Each Borough
-- Business question: What are the most common complaint types
-- within each borough?
-- DENSE_RANK assigns the same rank to tied complaint counts.
-- ------------------------------------------------------------
WITH borough_complaints AS (
    SELECT
        borough,
        complaint_type,
        COUNT(*) AS total_complaints,
        DENSE_RANK() OVER (
            PARTITION BY borough
            ORDER BY COUNT(*) DESC
        ) AS complaint_rank
    FROM nyc311_data
    WHERE borough IS NOT NULL
      AND complaint_type IS NOT NULL
    GROUP BY borough, complaint_type
)
SELECT
    borough,
    complaint_type,
    total_complaints,
    complaint_rank
FROM borough_complaints
WHERE complaint_rank <= 10
ORDER BY borough, complaint_rank;


-- ============================================================
-- End of UrbanPulse SQL Analyst Investigations 01 to 12
-- ============================================================
