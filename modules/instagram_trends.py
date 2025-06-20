import pandas as pd
import httpx
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from datetime import datetime

INSTAGRAM_EXPLORE_URL = 'https://www.instagram.com/explore/tags/'

# Lấy một số hashtag phổ biến từ trang explore (giả lập crawl)
def fetch_instagram_trends(top_n=20):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    # Instagram chặn mạnh, chỉ demo crawl các hashtag phổ biến
    hashtags = ['love', 'instagood', 'fashion', 'photooftheday', 'beautiful', 'art', 'happy', 'cute', 'tbt', 'like4like', 'followme', 'picoftheday', 'follow', 'me', 'selfie', 'summer', 'instadaily', 'friends', 'repost', 'nature', 'girl']
    save_to_db('instagram', hashtags[:top_n])
    return hashtags[:top_n]

def save_to_db(platform, keywords):
    engine = create_engine('sqlite:///db/trends.db')
    df = pd.DataFrame({
        'platform': platform,
        'keyword': keywords,
        'timestamp': datetime.now()
    })
    df.to_sql('trends', engine, if_exists='append', index=False)

if __name__ == '__main__':
    print(fetch_instagram_trends()) 