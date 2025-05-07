import pandas as pd
from sqlalchemy import create_engine
import logging


def load_to_db(data):
    # Create a database connection
    connection_uri = "postgresql+psycopg2://airflow:airflow@localhost:5432/codeforces"
    dbengine = create_engine(connection_uri)
    df = pd.read_csv(data, index_col='id')
    df.to_sql('contests', dbengine, if_exists='replace', index=True)
    logging.info("The Contests loaded to DB successfully")
    print("The Contests loaded to DB successfully")

    
    
load_to_db('data/contests_transformed.csv')

