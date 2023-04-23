# from flask import Flask, render_template, request
# from chatbot import get_chatbot

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get_chatbot_response")
# def chatbot_response():
#     user_input = request.args.get("msg")
#     response = get_chatbot(user_input)
#     return response

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
from chatbot import get_chatbot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/model")
def model():
    return render_template("model.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/get_chatbot_response")
def chatbot_response():
    user_input = request.args.get("msg")
    response = get_chatbot(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
