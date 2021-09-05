import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STOCK = "ITC.BSE"
# COMPANY_NAME = "ITC Limited"

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
# UnicodeEncodeError: 'ascii' codec can't encode character '\U0001f53c' in position 20: ordinal not in range(128)
if change_in_percent <= -5:
    # symbol = "🔻"
    symbol = "DOWN"
elif change_in_percent >= 5:
    # symbol = "🔼"
    symbol = "UP"

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
        # from twilio.rest import Client
        # import os

        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']

        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #                 .create(
        #                     body=f"{COMPANY_NAME}: {symbol}{change_in_percent} \nHeadline: {title}\nBrief : {desc}\nurl: {url}",
        #                     from_='+17402058238',
        #                     to='+918892865544'
        # )
        import smtplib

        my_email = "nandishakrishnappa186@gmail.com"
        password = "Nandish@123"
        #- symbol {change_in_percent} \nHeadline: {title}\nBrief : {desc.encode('utf-8')}\nurl: {url.encode('utf-8')}
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="www.nandishraina@gmail.com",
                                msg=f"Subject:{COMPANY_NAME} {symbol} {change_in_percent} \n\nHeadline: {title.encode('utf-8')}\n\nBrief : {desc.encode('utf-8')}\n\nurl: {url.encode('utf-8')}")