import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = API_KEY
ALPHA_URL = "https://www.alphavantage.co/query"
params_alpha = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}

r = requests.get(ALPHA_URL, params=params_alpha)
data = r.json()
date_range = list(data["Time Series (Daily)"].keys())
today_date = date_range[0]
yesterday_date = date_range[1]
today_action = float(data["Time Series (Daily)"][today_date]["4. close"])
yesterday_action = float(data["Time Series (Daily)"][yesterday_date]["4. close"])

difference_between_two_dates = abs((today_action - yesterday_action) / today_action) * 100

if difference_between_two_dates >= 5:
    API_NEWS_KEY = API_KEY
    API_NEWS_URL = "https://newsapi.org/v2/everything"

    new_params = {
        "apiKey": API_NEWS_KEY,
        "q": COMPANY_NAME,
    }
    r = requests.get(API_NEWS_URL, params=new_params)
    articles = r.json()["articles"][:3]

    print(f"{STOCK}: 🔺{difference_between_two_dates}%")
    for article in articles:
        source = article["source"]["name"]
        headline = article["title"]
        brief = article["description"]
        print(f"""
            Source: {source}
            Headline: {headline}
            Brief: {brief}
        """)

