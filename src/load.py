from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

def main():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db = os.getenv('DB_NAME')
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')
    # with engine.connect() as connection:
    #     print("Successfully connected")

    df = pd.read_csv('..\\data\\cleaned\\transactions_clean.csv')
    
    table_name = 'raw_transactions'
    try:
        df.to_sql(table_name, engine, if_exists='append', index = False)
        print(f"Data successfully loaded into table '{table_name}'")
    except ValueError as e:
        print(f"Error loading data: {e}")
    
main()

