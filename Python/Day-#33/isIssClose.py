import requests  
import datetime
import smtplib
import time

API_END_POINT = r"https://api.sunrise-sunset.org/json"

# Raguttahalli
# https://api.sunrise-sunset.org/json?lat=13.4758433&lng=78.0527685
MY_LAT = 13.4758433
MY_LONG = 78.0527685

# parameters = {
#     "lat" : MY_LAT,
#     "lng" : MY_LONG,
#     "formatted" : 0
# }
parameters = {
    "formatted" : 0
}

iss_response  = requests.get(url=r"http://api.open-notify.org/iss-now.json")
# {
#   "iss_position": {
#     "latitude": "-27.8295",
#     "longitude": "-63.5224"
#   },
#   "message": "success",
#   "timestamp": 1630545600
# }

iss_response.raise_for_status()
data = iss_response.json()

langitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (langitude, latitude)

day_response = requests.get(url=API_END_POINT, params=parameters) # , params=parameters not working - getting invalid information about the sunrise and sunset
day_response.raise_for_status()

data = day_response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

now = datetime.datetime.now()

def send_mail():
    print("ISS is close to you...")
    my_email = "nandishakrishnappa186@gmail.com"
    password = "Nandish@123"
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()
        quote_of_the_day = "The International Space Station is above you in the sky"
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="www.nandishraina@gmail.com",
                            msg=f"Subject:Look Up in the SKY\n\n {quote_of_the_day}"
            )

while True:
    print(f"--------------------------------------------------------------")
    print(f"My current locations sunrise/sunset time : {sunrise}/{sunset}")
    print(f"ISS location langitude/latitude          : {langitude}/{latitude}")
    print(f"My current location langitude/latitude   : {MY_LONG}/{MY_LAT}")
    print(f"My current day hour                      : {now.hour}")
    print(f"--------------------------------------------------------------")
    
    if now.hour >= sunset or now.hour <= sunrise: 
        if (langitude - 5) <= MY_LONG <= (langitude + 5) and (latitude - 5) <= MY_LAT <= (latitude + 5):
            send_mail()
            continue
    print("ISS is not close to you...")
    # send_mail()
    print(f"--------------------------------------------------------------")
    time.sleep(60)