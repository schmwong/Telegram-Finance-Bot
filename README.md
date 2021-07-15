# Telegram-Finance-Bot

Written in Python, deployed on Heroku.

## Step 1: Clone scripts

Scraper: https://gist.github.com/davidcjw/422300a1ddc360e3b892bc9866a32005#file-ticker-py

Bot: https://gist.github.com/davidcjw/208b23f78b3da7ace7c1790a0b4b0930#file-telegram_bot_app-py

## Step 2: Create telegram bot with BotFather
https://t.me/BotFather
![Screen Shot 2021-07-15 at 10 01 19 AM](https://user-images.githubusercontent.com/79643071/125716371-6d592e9b-3622-4307-b03e-12dfbf7edda5.png)

## Step 3: Export bot token to access API

Run " export TELEGRAM_BOT_TOKEN=<YOUR_BOT_TOKEN_HERE> " in Terminal

## Step 4: Add command to bot on Telegram

Select the bot on BotFather, navigate to add command and input:
get_px_change
![Screen Shot 2021-07-15 at 9 59 21 AM](https://user-images.githubusercontent.com/79643071/125716200-59421aba-57fb-4064-a452-b362489a8776.png)


## Step 5: Create files needed for Heroku deployment

- Procfile
- requirements.txt

## Step 6: Create Workflow

- YAML file
- GitHub repo secrets: bot token & Heroku email

## Step 7: Create project and add bot token on Heroku
Install Heroku CLI if not yet done so.
- heroku create <project_name>
- heroku config:set TELEGRAM_BOT_TOKEN=<YOUR_BOT_TOKEN_HERE>
