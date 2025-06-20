# Tool Tìm Từ Khóa Trend Đa Nền Tảng

## Mục tiêu
- Tự động lấy các từ khóa đang thịnh hành trên Google, YouTube, TikTok, Facebook, X (Twitter), Instagram.
- Giao diện web (Streamlit dashboard).
- Lưu lịch sử trend vào SQLite.

## Công nghệ sử dụng
- Python, Streamlit, pytrends, requests, BeautifulSoup, pandas, SQLAlchemy, httpx

## Cài đặt nhanh
```bash
pip install -r requirements.txt
streamlit run main.py
```

## Cấu trúc project
- `main.py`: Chạy dashboard web
- `modules/`: Code lấy trend từng nền tảng
- `db/`: Lưu file SQLite
- `utils/`: Hàm phụ trợ
- `.env`: Lưu API key (nếu cần)

## Lưu ý
- Một số nền tảng cần API key (YouTube, X). Xem hướng dẫn trong từng module. 