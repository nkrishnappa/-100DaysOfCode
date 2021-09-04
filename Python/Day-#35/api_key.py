import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
OWM_API_KEY = os.environ['OWM_API_KEY']


ONE_CALL_URL = r"https://api.openweathermap.org/data/2.5/onecall"
# http://api.openweathermap.org/data/2.5/weather?q=London&appid=69f04e4613056b159c2761a9d9e664d2
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# https://api.openweathermap.org/data/2.5/onecall?lat=13.4758433&lon=78.0527685&appid=69f04e4613056b159c2761a9d9e664d2

MY_LAT = 13.4758433
MY_LONG = 78.0527685

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : OWM_API_KEY,
    "exclude" : "current,minutely,daily"
}

response = requests.get(url=ONE_CALL_URL, params=parameters)
response.raise_for_status()

# import json
# with open("one_call.json", 'w') as f:
#     json.dump(response.json(), f, indent=4)

hour_json = response.json()["hourly"][:12]

for hour_data in hour_json:
    weather_id = hour_data["weather"][0]["id"]
    # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    if weather_id <= 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body="From: Nandisha Krishnappa \nIt is going to rain🌧 today, Remember to bring an ☔",
                            from_='+17402058238',
                            to='+918892865544'
                        )
        # print(message.sid)
        #print(hour_data["weather"][0]["main"])
        # print("Bring an Umbrella")
        break


