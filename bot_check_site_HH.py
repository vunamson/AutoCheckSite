import requests
import time

# URL website của bạn
URLS = [
    "https://clomic.com/",
    "https://printpear.com/",
    "https://davidress.com/"
]

# Token của Telegram Bot và Chat ID của bạn
TELEGRAM_TOKEN = '7483107768:AAGBE-i-csf6Tcish3jshRE_GVFyXdopLVA'
TELEGRAM_CHAT_ID = '1791691428'

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
        except requests.exceptions.RequestException:
            send_telegram_message(f"Website {url} không thể truy cập!")

# Kiểm tra các website mỗi 5 phút
while True:
    check_websites()
    time.sleep(300)  # Kiểm tra mỗi 5 phút
