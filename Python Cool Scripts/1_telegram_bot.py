import requests
from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")  # Selecting Timezone as Indian Standard Time
raw_TS = datetime.now(IST)
curr_date = raw_TS.strftime("%d-%m-%Y")
curr_time = raw_TS.strftime("%H-%M-%S")

telegram_auth_token = "1827209721:AAE7uXBqL6-gwaglnoXbZlRvhloEMRuTUEk"  # Authentication token
telegram_group_id = "vaccine_notifier"

msg = f"Message received on {curr_date} at {curr_time}"


def send_msg_on_telegram(message):
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}" \
                       f"&text={message}"
    tel_resp = requests.get(telegram_api_url)

    if tel_resp.status_code == 200:
        print("INFO: Notification has been sent on Telegram")
    else:
        print("Error: Could not send message")


send_msg_on_telegram(msg)
