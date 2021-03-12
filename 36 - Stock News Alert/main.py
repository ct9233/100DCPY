import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
import json
from twilio.rest import Client


load_dotenv("C:/data/.env")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api = os.getenv("ALPHA_VANT_API")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api = os.getenv("NEWS_API")
account_sid = os.getenv("TWI_ACC_SID")
auth_token = os.getenv("TWI_AUTH_TOK")
twilio_from = os.getenv("TWI_FROM_NUM")
twilio_to = os.getenv("TWI_TO_NUM")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
stock_data_list = [value for (key, value) in stock_data.items()]

yesterdays_close = stock_data_list[0]['4. close']
day_before_yesterday_close = stock_data_list[1]['4. close']

price_change = abs(float(yesterdays_close) - float(day_before_yesterday_close))
percent_change = price_change/float(yesterdays_close) * 100
print(percent_change)

if percent_change > 4:
    news_params = {
        "apiKey": news_api,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    if len(news_data) > 3:
        news_data = news_data[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_data]
    print(formatted_articles)

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_=f"{twilio_from}",
            to=f"{twilio_to}"
        )