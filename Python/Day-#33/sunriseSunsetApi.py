# API documentation
# Ours is a very simple REST api, you only have to do a GET request to https://api.sunrise-sunset.org/json.

# Parameters
# lat (float): Latitude in decimal degrees. Required.
# lng (float): Longitude in decimal degrees. Required.
# date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.
# callback (string): Callback function name for JSONP response. Optional.
# formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.


API_END_POINT = r"https://api.sunrise-sunset.org/json"

"""
// 20210902073524
// https://api.sunrise-sunset.org/json

{
  "results": {
    "sunrise": "5:55:10 AM",
    "sunset": "6:04:02 PM",
    "solar_noon": "11:59:36 AM",
    "day_length": "12:08:52",
    "civil_twilight_begin": "5:35:23 AM",
    "civil_twilight_end": "6:23:49 PM",
    "nautical_twilight_begin": "5:11:09 AM",
    "nautical_twilight_end": "6:48:03 PM",
    "astronomical_twilight_begin": "4:46:55 AM",
    "astronomical_twilight_end": "7:12:17 PM"
  },
  "status": "OK"
}
"""

# Raguttahalli
MY_LAT = 13.4758433
MY_LONG = 78.0527685

# https://api.sunrise-sunset.org/json?lat=13.4758433&lng=78.0527685

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

import requests 
import datetime

response = requests.get(url=API_END_POINT, params=parameters)
response.raise_for_status()

data = response.json()


sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


print(sunrise, sunset)

# with format enabled  - "formatted" : 1
# print(sunrise, sunset) # 12:35:22 AM 12:59:33 PM

now = datetime.datetime.now()
# print(now) # 2021-09-02 07:59:01.225981
print(now.hour)

# without format enabled - "formatted" : 0
# print(sunrise, sunset) # 2021-09-02T00:35:22+00:00 2021-09-02T12:59:33+00:00