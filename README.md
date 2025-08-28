# Vendor-Performance-Data-Analytics
End-to-end pipeline using Python, SQL, and Power BI to analyze vendor performance, track stock turnover, and optimize purchasing decisions.

This repository offers a complete end-to-end solution to analyze and visualize **vendor performance** using **Python (data ingestion & transformation)** and **Power BI (interactive dashboard)**.

It includes:
- Automated database ingestion pipeline
- Vendor summary generation with key performance metrics
- Exploratory Data Analysis (EDA)
- Power BI dashboard with interactive filters, Top N visuals, and drill-through capabilities

---

## Features

- **Data Pipeline (Python):**
  - Ingests CSV files into SQLite database (`ingestion_db.py`)
  - Creates a vendor sales summary using SQL & Pandas (`get_vendor_summary.py`)
  - Calculates key metrics:
    - Freight Costs
    - Purchase & Sales Summaries
    - Gross Profit & Profit Margin
    - Stock Turnover
    - Sales-to-Purchase Ratio

- **Exploratory Data Analytics (Jupyter):**
  - `Vendor Performance Analysis.ipynb`
  - `Exploratory DataAnalytics.ipynb`
  - Data cleaning, descriptive statistics, and visual exploration.

- **Power BI Dashboard:**
  - **Top 5 Products/Brands** (stacked bar chart)
  - **Low Turnover Vendors** table (Top 10 smallest AvgStockTurnOver)
  - **Vendor Deep Dive Drill-through** (Page 1 → Page 2 navigation)
  - Word wrap, bold column headers, formatted KPIs

---

## Project Structure

.
├── data/ # Raw CSV files (to be ingested)
├── logs/ # Logging outputs
├── ingestion_db.py # Data ingestion script
├── get_vendor_summary.py # Vendor summary & transformation script
├── Vendor Performance Analysis.ipynb # Vendor analytics notebook
├── Exploratory DataAnalytics.ipynb # EDA notebook
├── VendorPerformanceDashboard.pbix # Power BI Dashboard
└── README.md # This file


---

## How to Use

### 1. Clone this Repository

git clone https://github.com/sohailaamir/vendor-performance-data-analytics.git
cd vendor-performance-analytics

## 2. Set up the Environment
pip install -r requirements.txt
(requirements include pandas, sqlalchemy, sqlite3, logging)

## 3. Ingest Data

Place your CSV files in the data/ folder.

Run:
python ingestion_db.py

## 4. Generate Vendor Summary

python get_vendor_summary.py
This will create a table vendor_sales_summary in inventory.db.

## 5. Explore Data

Open Vendor Performance Analysis.ipynb or Exploratory DataAnalytics.ipynb in Jupyter Lab/Notebook.

Run cells for visual exploration and validation.

## 6. Open Power BI Dashboard

Open VendorPerformanceDashboard.pbix in Power BI Desktop.

Refresh data → connect to inventory.db.

Use interactive visuals:

Right-click a vendor → Drillthrough → Vendor Deep Dive

View Low Turnover Vendors table (Top 10 smallest stock turnover)




