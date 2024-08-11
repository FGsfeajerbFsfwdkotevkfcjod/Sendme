import requests
from bs4 import BeautifulSoup
from config import PHONEPE_EMAIL, PHONEPE_PASSWORD

def scrape_transactions():
    with requests.Session() as session:
        # Log in to PhonePe
        login_url = 'https://business.phonepe.com/login'
        login_data = {
            'email': PHONEPE_EMAIL,
            'password': PHONEPE_PASSWORD
        }
        session.post(login_url, data=login_data)

        # Scrape transaction history page
        transactions_page = session.get('https://business.phonepe.com/transactions')
        soup = BeautifulSoup(transactions_page.text, 'html.parser')

        # Extract transaction details (update selectors as necessary)
        transactions = []
        for transaction in soup.select('.transaction-row'):
            transaction_id = transaction.select_one('.transaction-id').text
            amount = transaction.select_one('.transaction-amount').text
            status = transaction.select_one('.transaction-status').text
            transactions.append({
                'id': transaction_id,
                'amount': amount,
                'status': status
            })

        return transactions
