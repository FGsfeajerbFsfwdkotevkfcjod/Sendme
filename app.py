from flask import Flask
from scraping import scrape_transactions
from config import TELEGRAM_BOT_TOKEN, CHANNEL_ID
from helper_func import send_to_telegram

app = Flask(__name__)

@app.route('/check_transactions', methods=['GET'])
def check_transactions():
    transactions = scrape_transactions()
    for transaction in transactions:
        message = f"Transaction ID: {transaction['id']}\nAmount: {transaction['amount']}\nStatus: {transaction['status']}"
        send_to_telegram(message)
    return "Transactions checked and notifications sent.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
