import requests

QUIZZ_API = "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=boolean"
response = requests.get(QUIZZ_API)
question_data = response.json()["results"]
