from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your API endpoint
API_URL = "https://api.on-demand.io/chat/v1/sessions"  # Replace with actual endpoint
API_KEY = "x9CoufWLKn5qxfsSOYOl8k1Pec55ZzkU"  # Replace with your actual API key
AGENT_ID = "plugin-1712327325"  # Replace with your chatbot agent ID

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    user_message = request.json.get('message')  # Message from user

    # Headers me API key bhejte hain
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Data mein agent ID aur user message bhejte hain
    data = {
        "agent_id": AGENT_ID,       # Agent ID ko data mein include karo
        "query": user_message
    }

    # POST request API ko bhejein
    response = requests.post(API_URL, headers=headers, json=data)
    
    # API se response ko JSON mein parse karo aur user ko return karo
    if response.status_code == 200:
        bot_response = response.json().get("response", "Sorry, I didn't understand that.")
    else:
        bot_response = "There was an error with the chatbot service."

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
