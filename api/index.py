from flask import Flask, jsonify, request
from chat import get_response

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    bot_message = get_response(user_message)
    return jsonify({'response': bot_message})

if __name__ == '__main__':
    app.run(debug=True)
