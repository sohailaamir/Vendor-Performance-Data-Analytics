import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db


logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"

    def create_vendor_summary(conn):
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS (
    SELECT
    VendorNumber,
    SUM(Freight) AS FreightCost
    FROM vendor_invoice
    GROUP BY VendorNumber
    ),

    PurchaseSummary AS(
    SELECT 
    p.VendorNumber,
    p.VendorName,
    p.Brand,
    p.Description,
    pp.Price AS ActualPrice,
    pp.Volume
    SUM(p.Quantity) AS TotalPurchaseQuantity,
    SUM(p.Dollars) AS TotalPurchaseDollars
From purchases p
JOIN purchase_prices pp
ON p.Brand=pp.Brand
where p.PurchasePrice>0
Group BY p.VendorNumber,p.VendorName,p.Brand,p.Description,p.PurchasePrice,pp.Price,pp.Volume
),
SalesSummary AS(
Select
VendorNo,
Brand,
SUM(SalesQuantity) AS TotalSalesQuantity,
SUM(SalesDollars) AS TotalSalesDollars,
SUM(SalesPrice) AS TotalSalesPrice,
SUM(ExciseTax) AS TotalExciseTax
FROM sales
Group BY VendorNo,Brand
)
Select
ps.VendorNumber,
ps.VendorName,
ps.Brand,
ps.Description,
ps.PurchasePrice,
ps.ActualPrice,
ps.Volume,
ps.TotalPurchaseQuantity,
ps.TotalPurchaseDollars,
ss.TotalSalesQuantity,
ss.TotalSalesDollars,
ss.TotalSalesPrice,
ss.TotalExciseTax,
fs.FreightCost
FROM PurchaseSummary ps
LEFT JOIN SalesSummary ss
ON ps.VendorNumber=ss.VendorNO
AND ps.Brand=ss.Brand
LEFT JOIN FreightSummary fs
ON ps.VendorNumber = fs.VendorNumber
ORDER BY ps.TotalPurchaseDollars DESC""",conn)

return vendor_sales_summary

def clean_data(df):
    df['Volume'] = df['Volume'].astype('float')

    #filling missing values with 0
    df.fillna(0,inplace = True)

    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    vendor_sales_summary['GrossProfit']= vendor_sales_summary['TotalSalesDollars']- vendor_sales_summary['TotalPurchaseDollars']
    vendor_sales_summary['ProfitMargin']= (vendor_sales_summary['GrossProfit'] / vendor_sales_summary['TotalSalesDollars'])*100
    vendor_sales_summary['StockTurnover']= vendor_sales_summary['TotalSalesQuantity'] / vendor_sales_summary['TotalPurchaseQuantity']
    vendor_sales_summary['SalesToPurchseRatio']= vendor_sales_summary['TotalSalesDollars'] / vendor_sales_summary['TotalPurchaseDollars']

    return df

    if __name__ == '__main__':
        conn = sqlite3.connect('inventory.db')

        logging.info('Creating Vendor summary table...')
        summary_df = create_vendor_summary(conn)
        logging.info(summary_df.head())

        logging.info('cleaning Data...')
        clean_df = clean_data(summary_df)
        logging.info(clean_df.head())

        logging.info('Ingesting data...')
        ingest_db(clean_df,'vendor_sales_summary',conn)
        logging.info('Connected')
    
    