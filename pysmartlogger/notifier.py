import requests


class Notifier:
    @staticmethod
    def send_telegram_alert(token, chat_id, message):
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        response = requests.post(url, data=data)
        return response.json()

    @staticmethod
    def send_discord_alert(webhook_url, message):
        data = {"content": message}
        response = requests.post(webhook_url, json=data)
        return response.json()


if __name__ == "__main__":
    telegram_token = "SEU_TOKEN"
    telegram_chat_id = "SEU_CHAT_ID"
    discord_webhook = "SEU_WEBHOOK_URL"

    Notifier.send_telegram_alert(telegram_token, telegram_chat_id, "🚨 Critical error detected!")
    Notifier.send_discord_alert(discord_webhook, "🚨 Critical error detected!")
