import requests
from dotenv import load_dotenv
import os
load_dotenv()
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url_sheety_flights = "https://api.sheety.co/b6a63b6b22cad029b2304b6e5fa05bb7/copieDeFlightDeals/prices"
        self.header = {
           "Authorization": "Bearer "+ os.environ["AUTH_GOOGLE_SHEETY"],
        }
        self.get_distanations = {}

    def get_rows(self):
        r = requests.get(self.url_sheety_flights, headers=self.header)
        data = r.json()
        self.get_distanations = data["prices"]

        return self.get_distanations

    def put_ia_code(self):
        for city in self.get_distanations:
            body = {
                'price':{
                    "iataCode": city["iataCode"],
                }
            }
            id_row = city['id']
            r = requests.put(f"{self.url_sheety_flights}/{id_row}", headers=self.header, json=body)
            print(r.text)

    def change_flight_price(self, destination, price):
        body = {
            'price':{
                "lowestPrice": price,
            }
        }
        id_row = destination['id']
        r = requests.put(f"{self.url_sheety_flights}/{id_row}", headers=self.header, json=body)
        print(r.text)