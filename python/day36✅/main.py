import requests
from twilio.rest import Client



STOCK_NAME = "NVIDIA"
COMPANY_NAME = "NVIDIA Corporation"



STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters ={
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,
    'apikey' : STOCK_API
}
response = requests.get(STOCK_ENDPOINT, params=parameters)
print(response.json())
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday = data_list[0]
yesterday_close = yesterday['4. close']
before_yesterday = data_list[1]
before_yesterday_close = before_yesterday['4. close']

diff = abs(float(yesterday_close) - float(before_yesterday_close))

diff_percent = (diff / float(yesterday_close)) * 100
result = "⬆️" if diff_percent > 0 else "⬇️"
print(diff_percent)
if diff_percent > 1:
    print("in If Statement")
    new_parameters = {
        'apiKey' : NEWS_API,
        'qInTitle' : COMPANY_NAME
    }
    new_response = requests.get(NEWS_ENDPOINT,params=new_parameters)
    article = new_response.json()['articles']
    print(article)
    three_article = article[:1]
    print(three_article)
    formatted_msg = [f"{COMPANY_NAME} {result} {diff_percent} Headline: {article_line['title']} \n Brief: {article_line['description']}" for article_line in three_article]
    client = Client(sid,token)
    msg = client.messages.create(body = formatted_msg, from_ = "+12702136976", to = "+973 3722 5951")