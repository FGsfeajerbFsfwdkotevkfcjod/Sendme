# PhonePe Payment Notification Bot

This is a Flask application that logs into PhonePe, scrapes transaction data, and sends notifications to a Telegram channel.

## How to Deploy

1. Clone this repository.
2. Create a `.env` file with the necessary environment variables.
3. Deploy to Koyeb using the provided Dockerfile.

## Environment Variables

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `CHANNEL_ID`: Your Telegram channel ID.
- `PHONEPE_EMAIL`: Your PhonePe business account email.
- `PHONEPE_PASSWORD`: Your PhonePe business account password.
