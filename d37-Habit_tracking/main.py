import requests
from datetime import datetime

API_TOKEN = "secrettok3nfdsgfdfgds"
username = "leeroymannier1337"
headers = {
    "X-USER-TOKEN": API_TOKEN,
}
params_graph = {
        "id" : "habit1",
        "name": "working",
        "unit": "commit",
        "type": "int",
        "color": "sora"
    }

def create_user():
    # create my profile -> https://pixe.la/@leeroymannier1337
    pixel_url_api = "https://pixe.la/v1/users/"
    params_pixe_api = {
        "token": API_TOKEN,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    r = requests.post(url=pixel_url_api, json=params_pixe_api)
    response = r.json()
    if not response["isSuccess"]:
        print("User already exist")
    else:
        print(r.text)


def create_new_graph(params_graphique):
    # creation of a new graph
    API_ENDPOINT_URL = f"https://pixe.la/v1/users/{username}/graphs"

    r = requests.post(url=API_ENDPOINT_URL, headers=headers, json=params_graphique)
    response = r.json()
    if not response["isSuccess"]:
        print("Graph already create ! :)")
    else:
        print("Graphique create !")


def create_habit(params_habit, graphique_name):
    url_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graphique_name}"

    r = requests.post(url=url_endpoint, headers=headers, json=params_habit)
    msg = r.json()
    if not msg["isSuccess"]:
        print(msg)
        create_habit(params_habit, graphique_name)
    else:
        print("Habit created")


def update_habit(params_habit, graphique_name, date):
    url_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graphique_name}/{date}"
    r = requests.put(url=url_endpoint, headers=headers, json=params_habit)
    response = r.json()
    if not response["isSuccess"]:
        print("Habit not created")
    else:
        print("Habit updated")

def delete_graph(graphique_name):
    API_ENDPOINT_URL = f"https://pixe.la/v1/users/{username}/graphs/{graphique_name}"
    r = requests.delete(url=API_ENDPOINT_URL, headers=headers)
    response = r.json()
    if not response["isSuccess"]:
        print("Graph not delete")
    else:
        print("graphique deleted")
# Create a new user
create_user()

# Create a graph
create_new_graph(params_graph)

# create a activity in the graph

params_habit = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("Enter your quantity"),
}
print(params_habit)

create_habit(params_habit, "habit1")

if True:
    # update a habit
    params_habit = {
        "quantity": "23",
    }
    update_habit(params_habit, "habit1", datetime.now().strftime("%Y%m%d"))

if True:
    # delete graph
    delete_graph("habit1")