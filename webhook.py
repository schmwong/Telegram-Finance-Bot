
PORT = int(os.environ.get("PORT", 5000))

...


def main() -> None:

    ...

    # Start the Bot
    # `start_polling` for local dev; webhook for production
    # updater.start_polling()
    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN
    )
    updater.bot.setWebhook(
        "https://python-stock-scraper-bot.herokuapp.com/" + TOKEN)

    updater.idle()
