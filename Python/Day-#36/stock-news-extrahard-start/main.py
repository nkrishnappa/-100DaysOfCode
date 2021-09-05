import requests

# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"

STOCK = "ITC.BSE"
COMPANY_NAME = "ITC Limited"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Welcome to Alpha Vantage! Your API key is: 1XVM0IE1YW2ZQZCB. Please record this API key at a safe place for future data access.
ALPA_API_KEY = "1XVM0IE1YW2ZQZCB"

#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey=1XVM0IE1YW2ZQZCB
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=full&apikey=1XVM0IE1YW2ZQZCB
ALPA_API_PARAM = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : ALPA_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=ALPA_API_PARAM)
response.raise_for_status()
time_series_data = response.json()["Time Series (Daily)"]

stock_data = dict(list(time_series_data.items())[:2])

# stock_close = []
# for day,values in stock_data.items():
#     # stock_close.append(float(values["4. close"]))
#     stock_close_day = {}
#     stock_close_day["close"] = float(values["4. close"])
#     stock_close_day["date"] = day
#     stock_close.append(stock_close_day)

stock_close = [{'close': 800, 'date': '2021-09-03'}, {'close': 650, 'date': '2021-09-02'}]
#  increase = Increase ÷ Original Number × 100.

change_in_percent = ((stock_close[0]["close"] - stock_close[1]["close"]) /  stock_close[0]["close"]) * 100
if change_in_percent <= -5:
    symbol = "🔻"
elif change_in_percent >= 5:
    symbol = "🔼"

if change_in_percent <= -5 or change_in_percent >= 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    # Your API key is: 06b9ec90f6da402aaf00aa8ddea7a889

    NEWS_API_KEY = "06b9ec90f6da402aaf00aa8ddea7a889"
    # https://newsapi.org/v2/everything?q=apple&from=2021-09-04&to=2021-09-04&sortBy=popularity&apiKey=06b9ec90f6da402aaf00aa8ddea7a889
    NEWS_API_URL = "https://newsapi.org/v2/everything"

    NEWS_API_PARAMS = {
        "q" : "tesla",
        "from" : stock_close[1]["date"],
        "to" : stock_close[0]["date"],
        "sortBy" : "popularity",
        "apiKey" : NEWS_API_KEY
    }

    response = requests.get(url=NEWS_API_URL, params=NEWS_API_PARAMS)
    response.raise_for_status()
    NEWS_RESPONSE = response.json()["articles"][:3]

    for article in NEWS_RESPONSE:
        title = article["title"]
        desc = article["description"]
        url = article["url"]
        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number. 
        from twilio.rest import Client
        import os

        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']

        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=f"{COMPANY_NAME}: {symbol}{change_in_percent} \nHeadline: {title}\nBrief : {desc}\nurl: {url}",
                            from_='+17402058238',
                            to='+918892865544'
                        )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

"""
NOTES:
{
    "Meta Data": {
        "1. Information": "Daily Time Series with Splits and Dividend Events",
        "2. Symbol": "ITC.BSE",
        "3. Last Refreshed": "2021-09-03",
        "4. Output Size": "Full size",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2021-09-03": {
            "1. open": "209.75",
            "2. high": "211.25",
            "3. low": "209.75",
            "4. close": "210.55",
            "5. adjusted close": "210.55",
            "6. volume": "931214",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2021-09-02": {
            "1. open": "209.5",
            "2. high": "211.5",
            "3. low": "209.25",
            "4. close": "209.75",
            "5. adjusted close": "209.75",
            "6. volume": "454233",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
"""

