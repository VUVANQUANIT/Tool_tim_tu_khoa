import pandas as pd
from pytrends.request import TrendReq
from sqlalchemy import create_engine
from datetime import datetime

def fetch_google_trends(top_n=20):
    pytrends = TrendReq(hl='vi-VN', tz=360)
    trending_searches = pytrends.trending_searches(pn='united_states')
    keywords = trending_searches[0].tolist()[:top_n]
    save_to_db('google', keywords)
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
    print(fetch_google_trends()) 