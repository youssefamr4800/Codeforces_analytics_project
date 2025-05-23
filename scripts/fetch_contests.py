import requests
from datetime import datetime
import pandas as pd
import logging
import os

def fetch_contests():
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        raise Exception("Failed to fetch contests")

    contests = data['result']

    data = pd.DataFrame(contests)
    os.makedirs('data', exist_ok=True)
    data.to_csv('data/contests.csv', index=False)
    logging.info("The Contests imported successfully")

    

