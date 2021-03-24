from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

origin_city_iata = "ORD"

for row in sheet_data:
    if row["iataCode"] == "":
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_iata,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_now
    )