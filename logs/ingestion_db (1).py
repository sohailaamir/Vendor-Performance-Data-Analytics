import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Set up logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Create database engine
engine = create_engine('sqlite:///inventory.db')

# Function to ingest DataFrame into SQLite DB
def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Function to load and ingest all CSV files
def load_raw_data():
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join('data', file))
            logging.info(f'Ingesting {file} into DB')
            ingest_db(df, file[:-4], engine)
    
    end = time.time()
    total_time = (end - start) / 60
    logging.info('Ingestion Complete')
    logging.info(f'Total time taken: {total_time:.2f} minutes')

# Entry point
if __name__ == '__main__':
    load_raw_data()
