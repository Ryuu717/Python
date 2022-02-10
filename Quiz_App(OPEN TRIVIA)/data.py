import requests

#Open Trivia
#https://opentdb.com/api_config.php

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 11, #Movie
    "difficulty": "easy"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
