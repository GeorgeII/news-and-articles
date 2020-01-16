import requests
import json

from model.article import Article


def send_message(model: Article):
    with open("resources/telegram-config.json") as f:
        telegram_conf = json.load(f)

    bot_token = telegram_conf["bot-token"]
    chat_id = telegram_conf["chat-id"]

    url = "https://api.telegram.org/bot" + bot_token + "/sendMessage"

    params = {"chat_id": chat_id, "text": model.headline + "\n\n" + model.full_article, "disable_web_page_preview": "false"}

    req = requests.get(url=url, params=params)
    print(req.json())

