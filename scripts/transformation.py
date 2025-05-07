import pandas as pd
import logging



def transform(data):
    df = pd.read_csv(f"{data}", index_col='id')
    df.drop(['frozen', 'freezeDurationSeconds', 'relativeTimeSeconds'], axis=1, inplace=True)
    df['startTime'] = pd.to_datetime(df['startTimeSeconds'], unit='s')
    df.drop('startTimeSeconds', axis=1, inplace=True)
    df.to_csv(f"data/contests_transformed.csv", index='id')
    logging.info("The Contests transformed successfully")



transform("data/contests.csv")