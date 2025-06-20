import streamlit as st
import pandas as pd
from modules import google_trends, youtube_trends, tiktok_trends, facebook_trends, twitter_trends, instagram_trends
from sqlalchemy import create_engine

st.set_page_config(page_title='Tool Tìm Từ Khóa Trend Đa Nền Tảng', layout='wide')
st.title('Tool Tìm Từ Khóa Trend Đa Nền Tảng')

col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Lấy Google Trends mới nhất'):
        keywords = google_trends.fetch_google_trends()
        st.success('Đã lấy và lưu trending Google!')
        st.write(keywords)
    if st.button('Lấy TikTok Trends mới nhất'):
        keywords = tiktok_trends.fetch_tiktok_trends()
        st.success('Đã lấy và lưu trending TikTok!')
        st.write(keywords)
with col2:
    if st.button('Lấy YouTube Trends mới nhất'):
        try:
            keywords = youtube_trends.fetch_youtube_trends()
            st.success('Đã lấy và lưu trending YouTube!')
            st.write(keywords)
        except Exception as e:
            st.error(str(e))
    if st.button('Lấy Facebook Trends mới nhất'):
        keywords = facebook_trends.fetch_facebook_trends()
        st.success('Đã lấy và lưu trending Facebook!')
        st.write(keywords)
with col3:
    if st.button('Lấy Twitter (X) Trends mới nhất'):
        try:
            keywords = twitter_trends.fetch_twitter_trends()
            st.success('Đã lấy và lưu trending Twitter!')
            st.write(keywords)
        except Exception as e:
            st.error(str(e))
    if st.button('Lấy Instagram Trends demo'):
        keywords = instagram_trends.fetch_instagram_trends()
        st.success('Đã lấy và lưu trending Instagram!')
        st.write(keywords)

# Hiển thị lịch sử
st.header('Lịch sử trending keywords')
engine = create_engine('sqlite:///db/trends.db')
df = pd.read_sql('SELECT * FROM trends ORDER BY timestamp DESC LIMIT 100', engine)
st.dataframe(df)
