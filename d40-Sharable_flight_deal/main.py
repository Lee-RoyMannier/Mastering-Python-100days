from data_manager import DataManager
from flight_data import FlightData, get_cheap_flight
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
import time
from pprint import pprint
data_manager = DataManager()
sheet_data = data_manager.get_rows()
flight_search = FlightSearch()

for i in range(0, len(sheet_data)):
    if sheet_data[i]["iataCode"] == "":
        for sheet in sheet_data:
            sheet["iataCode"] = flight_search.get_destination_code(sheet["city"])

        data_manager.get_distanations = sheet_data
        data_manager.put_ia_code()


tomorrow_date = datetime.now() + timedelta(days=1)
in_six_month = tomorrow_date + timedelta(days=6*30)
user_mails = data_manager.get_customer_emails()

for destination in sheet_data:
    print("We getting the data for the flight at :", destination["city"])
    flight_data = flight_search.get_flights("LON", destination["iataCode"], tomorrow_date, in_six_month)
    chepeast_flight = get_cheap_flight(flight_data)
    if chepeast_flight.price == "N/A":
        flight_data = flight_search.get_flights("LON", destination["iataCode"], tomorrow_date, in_six_month,
                                                is_direct=False)
        chepeast_flight = get_cheap_flight(flight_data)

    pprint(f"{destination['city']}: £{chepeast_flight.price}")
    data_manager.change_flight_price(destination, chepeast_flight.price)
    
    if chepeast_flight.price != "N/A":
        notification_manager = NotificationManager()
        if chepeast_flight.stop == 0:
            message = f"Low price alert! Only GBP {chepeast_flight.price} to fly direct "\
                      f"from {chepeast_flight.origin_airport} to {chepeast_flight.destination_airport}, "\
        else:
            message = f"Low price alert! Only GBP {chepeast_flight.price} to fly "\
                      f"from {chepeast_flight.origin_airport} to {chepeast_flight.destination_airport}, "\
                      f"with {chepeast_flight.stops} stop(s) "\
                      f"departing on {chepeast_flight.out_date} and returning on {chepeast_flight.return_date}."
        
        print("Please check your email")
        notification_manager.send_notification(user_mails, message)
    time.sleep(2)

