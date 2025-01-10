from data_manager import DataManager
from flight_data import FlightData, get_cheap_flight
from datetime import datetime, timedelta
from flight_search import FlightSearch
import time
from pprint import pprint
data_manager = DataManager()
sheet_data = data_manager.get_rows()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for sheet in sheet_data:
        sheet["iataCode"] = flight_search.get_destination_code(sheet["city"])

    data_manager.get_distanations = sheet_data
    data_manager.put_ia_code()


tomorrow_date = datetime.now() + timedelta(days=1)
in_six_month = tomorrow_date + timedelta(days=6*30)

for destination in sheet_data:
    print("We getting the data for the flight at :", destination["city"])
    flight_data = flight_search.get_flights("LON", destination["iataCode"], tomorrow_date, in_six_month)
    chepeast_flight = get_cheap_flight(flight_data)
    pprint(f"{destination['city']}: £{chepeast_flight.price}")
    data_manager.change_flight_price(destination, chepeast_flight.price)
    time.sleep(2)

