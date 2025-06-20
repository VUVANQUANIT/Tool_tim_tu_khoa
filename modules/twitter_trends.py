import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('X_BEARER_TOKEN')

TWITTER_TRENDS_URL = 'https://api.twitter.com/1.1/trends/place.json'


def fetch_twitter_trends(woeid=23424984, top_n=20):
    if not BEARER_TOKEN:
        raise Exception('Chưa có X_BEARER_TOKEN trong file .env')
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }
    params = {
        'id': woeid  # WOEID for Vietnam
    }
    r = requests.get(TWITTER_TRENDS_URL, headers=headers, params=params)
    trends = r.json()[0]['trends']
    keywords = [t['name'] for t in trends if t['name'].startswith('#') or t['name'].isalpha()][:top_n]
    save_to_db('twitter', keywords)
    return keywords

def save_to_db(platform, keywords):
    engine = create_engine('sqlite:///db/trends.db')
    df = pd.DataFrame({
        'platform': platform,
        'keyword': keywords,
        'timestamp': datetime.now()
    })
    df.to_sql('trends', engine, if_exists='append', index=False)

if __name__ == '__main__':
    print(fetch_twitter_trends()) 