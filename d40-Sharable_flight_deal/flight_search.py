import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import time
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.access_token = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.API_KEY = os.environ.get('API_FLIGHT_KEY')
        self.API_SECRET =  os.environ.get('API_FLIGHT_SECRET')
        self.token = self.get_token()

    def get_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }

        r = requests.post(self.access_token, headers=header, data=body)
        data = r.json()

        return data["access_token"]

    def get_destination_code(self, city_name):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        header = {
            "Authorization": "Bearer " + self.token
        }

        body = {
            "keyword": city_name,
            "max": 2
        }

        r = requests.get(url, headers=header, params=body)
        data = r.json()

        try:
            iatacode = data["data"][0]["iataCode"]
        except IndexError:
            print("No airport code found for ", city_name)
            return "N/A"
        except KeyError:
            print("Iata code not found")
            return "Not Found"

        return iatacode

    def get_flights(self, origin, destination, departure_date, return_date, is_direct=True):
        url_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer " + self.token
        }

        body = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        r = requests.get(url_endpoint, headers=header, params=body)

        if r.status_code != 200:
            print("Error getting flight offers")
            print(r.text)
            return "None"

        data = r.json()

        return data