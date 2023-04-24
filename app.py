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
import joblib
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

@app.route("/get_model_output", methods=['POST'])
def model_output():
    return request.form['twitterPost']

@app.route("/get_survey_prediction", methods=['POST'])
def survey_prediction():
    loaded_model = joblib.load(open('model.joblib', "rb"))

    # request.form['num-employees']
    # request.form['mental-health-benefits']
    # request.form['anonymity-protected']
    # request.form['negative-consequences']
    # request.form['previous-employers']
    # request.form['bring-up-issue']
    # request.form['unsupportive-response']
    # request.form['family-history']
    # request.form['past-disorder']
    # request.form['current-disorder']
    # request.form['seek-treatment']
    # request.form['remote-work']
    # request.form['employer-discussion']
    # request.form['mental-health-resources']
    # request.form['physical-health']
    # request.form['mental-health-disorder']
    # request.form['direct-supervisor']
    # request.form['mental-physical-health']
    # request.form['co-worker-health']

    user_input = [1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0]
    return "You are likely to have depression!" if round(loaded_model.predict([user_input])[0]) == 1 else "You do not seem to have depression!" 

if __name__ == "__main__":
    app.run(debug=True)
