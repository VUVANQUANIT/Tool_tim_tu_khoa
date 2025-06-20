import pandas as pd
import httpx
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from datetime import datetime

TIKTOK_TRENDING_URL = 'https://www.tiktok.com/trending?lang=vi'


def fetch_tiktok_trends(top_n=20):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    r = httpx.get(TIKTOK_TRENDING_URL, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    keywords = []
    for tag in soup.find_all('a', href=True):
        if '/tag/' in tag['href']:
            kw = tag.text.strip().replace('#', '')
            if kw and kw not in keywords:
                keywords.append(kw)
        if len(keywords) >= top_n:
            break
    save_to_db('tiktok', keywords)
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
    print(fetch_tiktok_trends()) 