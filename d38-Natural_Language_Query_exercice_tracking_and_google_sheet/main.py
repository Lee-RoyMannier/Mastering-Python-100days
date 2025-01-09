import os
from datetime import datetime

import requests

API_KEY_NUTRI = os.environ.get('API_NUTRI')
host_url = "https://trackapi.nutritionix.com"
endpoint_nutri = "/v2/natural/exercise"

headers = {
    'Content-Type': 'application/json',
    "x-app-id": "f9476a6a",
    'x-app-key': API_KEY_NUTRI
}
params = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "age": "18",
    "weight_kg": "90",
    "height_cm": "180",
}
r = requests.post(host_url + endpoint_nutri, headers=headers, json=params)
nutrition_result = r.json()["exercises"]

google_sheet_url = "https://api.sheety.co/b6a63b6b22cad029b2304b6e5fa05bb7/copieDeMyWorkouts/workouts"
headers = {
    'Content-Type': 'application/json',
    "Authorization": Authorisation,
}
for ex in nutrition_result:
    params_google_sheet = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": ex["name"],
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"],
        }

    }
    r = requests.post(google_sheet_url, headers=headers, json=params_google_sheet)

# test for user input ->  ran 45K and make 7 pull-ups