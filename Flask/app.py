from flask import Flask, jsonify, request
from flask_cors import CORS

# Our files
from setup import setup_api_keys
from openai_controller import interactive_chat_with_bing_search


openai_api_key, bing_subscription_key = setup_api_keys()

app = Flask(__name__)
CORS(app)

# Select Option for developpment
USE_CHAT_GPT_API = True

if USE_CHAT_GPT_API:
    # OPTION 1: ChatGpt Answer   
    @app.route('/chatbot-ask', methods=['POST'])
    def chatbot_ask():
        data = request.get_json()
        return interactive_chat_with_bing_search(data, use_log=True)

else:
    # OPTION 2: Test Frontend/Backend connection
    # Use this function to send an echo of the received message
    @app.route('/chatbot-ask', methods=['POST'])
    def chatbot_ask():
        user_message = request.json.get('messages')
        return jsonify({'response': f"You said: {user_message}"})


if __name__ == "__main__":
    app.run(debug=True)
