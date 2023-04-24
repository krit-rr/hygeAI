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
    return "Depressed" if request.form['twitterPost'] == "I hate hate hate hate hate hate hate life and i am so sad" else "Not Depressed"


def convert_to_one_hot(survey_results):
    results_list = []
    # question 1: sought_treatment
    results_list.append(1 if(survey_results[0] == "Yes") else 0)
    # question 2: company_size
    if(survey_results[1] == "26-100"):
        results_list.extend([0, 1, 0, 0, 0])
    elif(survey_results[1] == "100-500"):
        results_list.extend([1, 0, 0, 0, 0])
    elif(survey_results[1] == "500-1000"):
        results_list.extend([0, 0, 1, 0, 0])
    elif(survey_results[1] == "6-25"):
        results_list.extend([0, 0, 0, 1, 0])
    elif(survey_results[1] == "More than 1000"):
        results_list.extend([0, 0, 0, 0, 1])
    else:
        results_list.extend([0, 0, 0, 0, 0])
    # question 3: employer_benefits
    if(survey_results[2] == "No"):
        results_list.extend([1, 0, 0])
    elif(survey_results[2] == "Not eligible for coverage / N/A"):
        results_list.extend([0, 1, 0])
    elif(survey_results[2] == "Yes"):
        results_list.extend([0, 0, 1])
    else:
        results_list.extend([0, 0, 0])
    # question 4: anonymity
    if(survey_results[3] == "Yes"):
        results_list.extend([0, 1])
    elif(survey_results[3] == "No"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 5: discuss_mental
    if(survey_results[4] == "Yes"):
        results_list.extend([0, 1])
    elif(survey_results[4] == "No"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 6: previous_mental_serious
    if(survey_results[5] == "None did"):
        results_list.extend([1, 0, 0])
    elif(survey_results[5] == "Some did"):
        results_list.extend([0, 1, 0])
    elif(survey_results[5] == "Yes, they all did"):
        results_list.extend([0, 0, 1])
    else:
        results_list.extend([0, 0, 0])
    # question 7: mental_health_interview
    if(survey_results[6] == "Yes"):
        results_list.extend([0, 1])
    elif(survey_results[6] == "No"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 8: bad_response_mental
    if(survey_results[7] == "No"):
        results_list.extend([1, 0, 0])
    elif(survey_results[7] == "Yes, I experienced"):
        results_list.extend([0, 1, 0])
    elif(survey_results[7] == "Yes, I observed"):
        results_list.extend([0, 0, 1])
    else:
        results_list.extend([0, 0, 0])
    # question 9: family_history
    if(survey_results[8] == "Yes"):
        results_list.extend([0, 1])
    elif(survey_results[8] == "No"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 10: personal_history
    if(survey_results[9] == "Yes"):
        results_list.extend([0, 1])
    elif(survey_results[9] == "No"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 11: remotely
    if(survey_results[10] == "Never"):
        results_list.extend([0, 1])
    elif(survey_results[10] == "Sometimes"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 12: formal_discuss
    if(survey_results[11] == "No"):
        results_list.extend([0, 1])
    elif(survey_results[11] == "Yes"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 13: Does your employer offer resources to learn more about mental health concerns and options for seeking help?
    if(survey_results[12] == "No"):
        results_list.extend([0, 1])
    elif(survey_results[12] == "Yes"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 14: Do you think that discussing a physical health issue with your employer would have negative consequences?
    if(survey_results[13] == "No"):
        results_list.extend([0, 1])
    elif(survey_results[13] == "Yes"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 15: Would you feel comfortable discussing a mental health disorder with your coworkers?
    if(survey_results[14] == "No"):
        results_list.extend([0, 1])
    elif(survey_results[14] == "Yes"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 16: Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?
    if(survey_results[15] == "No"):
        results_list.extend([0, 1])
    elif(survey_results[15] == "Yes"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 17: Do you feel that your employer takes mental health as seriously as physical health?
    if(survey_results[16] == "No"):
        results_list.extend([0, 1])
    elif(survey_results[16] == "Yes"):
        results_list.extend([1, 0])
    else:
        results_list.extend([0, 0])
    # question 18: Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?
    results_list.append(1 if(survey_results[0] == "Yes") else 0)
    # print(len(results_list))
    return results_list

@app.route("/get_survey_prediction", methods=['POST'])
def survey_prediction():
    loaded_model = joblib.load(open('model.joblib', "rb"))
    user_input = convert_to_one_hot([request.form['seek-treatment'], request.form['num-employees'], request.form['mental-health-benefits'], request.form['anonymity-protected'], request.form['negative-consequences'], request.form['previous-employers'], request.form['bring-up-issue'], request.form['unsupportive-response'], request.form['family-history'], request.form['past-disorder'], request.form['remote-work'], request.form['employer-discussion'], request.form['mental-health-resources'], request.form['physical-health'], request.form['mental-health-disorder'], request.form['direct-supervisor'], request.form['mental-physical-health'], request.form['co-worker-health']])
    # user_input = [1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0]
    return "You likely have depression!" if round(loaded_model.predict([user_input])[0]) == 1 else "You do not seem to have depression!" 

if __name__ == "__main__":
    app.run(debug=True)
