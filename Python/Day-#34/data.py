import requests

OPEN_TRIVIA_DATABASE = r"https://opentdb.com/api.php"

parameters = {
    "amount" : 10,
    "type" : "boolean",
    "category" : 18
}

response = requests.get(url=OPEN_TRIVIA_DATABASE, params=parameters)
response.raise_for_status()

question_data  = response.json()['results']