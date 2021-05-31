from flask import Flask, request
import telebot.bot as bot
from telebot.credentials import bot_token

from AI import modal

app = Flask(__name__)
modal.load_modals()


@app.route('/')
def index():
    return "Bài tập lớn Trí tuệ nhân tạo K41,42"


@app.route('/predict', methods=['GET'])
def predict():
    txt = request.args.get("txt")
    code = request.args.get("code")
    return modal.predict(text=txt, modal_code=code)


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    print("---start set webhook---")
    s = bot.set_web_hook()
    print("---end set webhook---")
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/{}'.format(bot_token), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = bot.decode_message(request.get_json(force=True))
    print("--NEW MESSAGE--")
    print(update)
    try:
        if update.message is not None:
            if update.message.text:
                text = update.message.text.encode('utf-8').decode()
                chat_id = update.message.chat.id
                prd = modal.predict(text=text, modal_code="mnb")
                if prd.cls == "1":
                    bot.send_message(chat_id, "Hệ thống đã ghi nhận câu hỏi của bạn")
    except Exception as e:
        print("--ERROR-- telegram")
        print(e)


if __name__ == '__main__':
    app.run(threaded=True)
