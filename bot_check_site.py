import requests
import time

# URL website của bạn
URLS = [
    "https://clomic.com/",
    "https://luxinshoes.com/",
    "https://clothguy.com/",
    "https://lobreve.com/",
    "https://noaweather.com/",
    "https://printpear.com/"
]

# Token của Telegram Bot và Chat ID của bạn
TELEGRAM_TOKEN = '7997037067:AAG7jRrrJAAiilYeK8hv7i8iYTQzpc8EnA8'
TELEGRAM_CHAT_ID = '5929770035'

# Gửi thông báo qua Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

# Kiểm tra tình trạng website
def check_websites():
    for url in URLS:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                send_telegram_message(f"Website {url} gặp sự cố! Mã trạng thái: {response.status_code}")
            # else : send_telegram_message(f"✅ Website {url} đang hoạt động bình thường")
        except requests.exceptions.RequestException:
            send_telegram_message(f"Website {url} không thể truy cập!")

# Kiểm tra các website mỗi 5 phút
while True:
    check_websites()
    time.sleep(300)  # Kiểm tra mỗi 5 phút
