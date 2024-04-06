from flask import Flask, render_template, request, jsonify
from chat import get_response, bot_name
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# Set configuration options
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Print configuration options
print(app.config)

# Handle UnicodeDecodeError
@app.errorhandler(UnicodeDecodeError)
def handle_unicode_decode_error(error):
    return "An error occurred while decoding the request data.", 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_message = request.form['message']
        bot_message = get_response(user_message)
        return jsonify({'response': bot_message})
    except UnicodeDecodeError:
        return jsonify({'response': 'An error occurred while decoding the request data.'}), 500

if __name__ == 'main':
    app.run(debug=True)