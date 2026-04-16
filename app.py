from flask import Flask, render_template, request
import aiml
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# AIML setup
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

def process_input(user_input):
    user_input = user_input.upper()   # 🔥 VERY IMPORTANT

    response = kernel.respond(user_input)

    if response == "":
        return "Sorry, I didn’t understand that."

    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = process_input(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)