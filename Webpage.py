from chatbot import chatbot
from flask import Flask, render_template, request
import time

app  = Flask(__name__)

# Your API endpoint
API_URL = "https://api.on-demand.io/chat/v1/sessions"  # Replace with actual endpoint
API_KEY = "x9CoufWLKn5qxfsSOYOl8k1Pec55ZzkU"  # Replace with your actual API key
AGENT_ID = "plugin-1712327325"  # Replace with your chatbot agent ID


@app.route("/")
def home():
    return render_template("Chat.html")
    
@app.route("/test")
def test():
    return render_template("Test.html")

@app.route("/finance")
def finance():
    return render_template("Finance.html")

@app.route("/chatbot")
def chatbotter():
    return render_template("Chatbot.html")

@app.route("/get")
def get_bot_response():
    time.sleep(0.5)
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)