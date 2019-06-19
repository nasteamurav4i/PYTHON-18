# -*- coding: utf-8 -*-
import flask
import telebot

from time import sleep

from poems import find_rhyme

try:
    import conf
except ImportError:
    import os

    conf = type(
        "conf",
        (),
        {
            "TOKEN": os.environ["TOKEN"],
            "WEBHOOK_HOST": os.environ["WEBHOOK_HOST"],
            "WEBHOOK_PORT": os.environ["WEBHOOK_PORT"],
        },
    )

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN)
sleep(1)
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)

app = flask.Flask(__name__)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Это бот, который подбирает рифму на ваше сообщение. За основу берутся строчки из https://github.com/IlyaGusev/PoetryCorpus.",
    )


@bot.message_handler(func=lambda m: True)
def send_len(message):
    text = message.text
    chat_id = message.chat.id

    rhyme = find_rhyme(text)
    bot.send_message(chat_id, rhyme)


@app.route("/", methods=["GET", "HEAD"])
def index():
    return "ok"


@app.route(WEBHOOK_URL_PATH, methods=["POST"])
def webhook():
    if flask.request.headers.get("content-type") == "application/json":
        json_string = flask.request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ""
    else:
        flask.abort(403)


if __name__ == "__main__":
    import os

    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
