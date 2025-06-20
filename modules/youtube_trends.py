import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')

YOUTUBE_TRENDING_URL = 'https://www.googleapis.com/youtube/v3/videos'


def fetch_youtube_trends(region_code='VN', max_results=20):
    if not API_KEY:
        raise Exception('Chưa có YOUTUBE_API_KEY trong file .env')
    params = {
        'part': 'snippet',
        'chart': 'mostPopular',
        'regionCode': region_code,
        'maxResults': max_results,
        'key': API_KEY
    }
    r = requests.get(YOUTUBE_TRENDING_URL, params=params)
    items = r.json().get('items', [])
    keywords = [item['snippet']['title'] for item in items]
    save_to_db('youtube', keywords)
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
    print(fetch_youtube_trends()) 