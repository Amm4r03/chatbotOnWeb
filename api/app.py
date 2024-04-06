from flask import Flask, render_template, request, jsonify
from chat import get_response, bot_name

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# Set configuration options
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Print configuration options
print(app.config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    bot_message = get_response(user_message)
    return jsonify({'response': bot_message})

if __name__ == '__main__':
    app.run(debug=True)