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
        df.to_sql(table_name, engine, if_exists='replace', index = False)
        print(f"Data successfully loaded into table '{table_name}'")
    except ValueError as e:
        print(f"Error loading data: {e}")

    # Assert row count in DB matches CSV
    with engine.connect() as connection:
        from sqlalchemy import text
        result = connection.execute(text('SELECT COUNT(*) FROM raw_transactions'))
        db_count = result.scalar()
        csv_count = len(df)
        assert db_count == csv_count, f"Row count mismatch: DB has {db_count}, CSV has {csv_count}"
        print(f"Assertion passed. DB rows: {db_count}, CSV rows: {csv_count}")
    
main()

