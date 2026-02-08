# main.py
from tripdata import get_trip_data
from datetime import datetime
import json

trips = [
    get_trip_data("Paris", "15-05-2023", "Visited the Eiffel Tower"),
    get_trip_data("Rome", "22-08-2023", "Ancient history everywhere"),
    get_trip_data("Tokyo", "10-11-2024", "Great food and culture")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date_visited"], "%d-%m-%Y")
    trip["date_visited"] = date_obj.strftime("%B %d, %Y")

print(json.dumps(trips, indent=4))
