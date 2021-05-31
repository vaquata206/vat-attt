from flask import Flask, request

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


if __name__ == '__main__':
    app.run(threaded=True)
