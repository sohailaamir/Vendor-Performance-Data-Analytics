import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

os.makedirs('logs', exist_ok=True)

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
logging.info(" Logging setup complete in ingestion_db.py")

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine_or_conn):
    df.to_sql(table_name, con=engine_or_conn, if_exists='replace', index=False)

def load_raw_data():
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            file_path = os.path.join('data', file)
            df = pd.read_csv(file_path)

            table_name = os.path.splitext(file)[0]
            ingest_db(df, table_name, engine)

            logging.info(f' Ingested {file} into table "{table_name}"')

    end = time.time()
    total_time = (end - start) / 60
    logging.info(f' Ingestion complete in {total_time:.2f} minutes')


