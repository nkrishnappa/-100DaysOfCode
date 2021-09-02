import requests 

response  = requests.get(url=r"http://api.open-notify.org/iss-now.json")
# {
#   "iss_position": {
#     "latitude": "-27.8295",
#     "longitude": "-63.5224"
#   },
#   "message": "success",
#   "timestamp": 1630545600
# }

# print(response) # <Response [200]>
# print(response.status_code) # 200
status = response.status_code
response.raise_for_status()
data = response.json()

langitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (langitude, latitude)

print(iss_position) # ('-17.2791', '29.3702')

# '''
# Traceback (most recent call last):
#   File "c:/Users/nkrishnappa/Desktop/100DaysOfCode/Python/Day-#33/main.py", line 9, in <module>
#     response.raise_for_status()
#   File "C:\Users\nkrishnappa\AppData\Local\Programs\Python\Python38-32\lib\site-packages\requests\models.py", line 953, in raise_for_status
#     raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/iss-now.jon
# '''


# if status != 200:
#     raise Exception("Unable to get the response!")
#     """
#     # url="http://api.open-notify.org/iss-now.jon

#     Traceback (most recent call last):
#     File "c:/Users/nkrishnappa/Desktop/100DaysOfCode/Python/Day-#33/main.py", line 10, in <module>
#         raise Exception("Unable to get the response!")
#     Exception: Unable to get the response!
#     """

