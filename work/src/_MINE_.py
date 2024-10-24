import sys
import requests
from _CONFIG_ import WEBHOOK_URL

def send_to_discord(message):
    if not message:
        return

    data = {
        "content": message
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("Сообщение успешно отправлено!")
        else:
            print(f"Ошибка при отправке сообщения. Код ошибки: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")

if __name__ == "__main__":
    message = " ".join(sys.argv[1:])
    send_to_discord(message)