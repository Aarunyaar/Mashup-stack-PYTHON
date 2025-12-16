from datetime import datetime
import json

def get_trip(city, date_str, comment):
    return {
        "city": city,
        "date": date_str,
        "comment": comment
    }


trips = [
    get_trip("Delhi", "15-05-2023", "Amazing historical places"),
    get_trip("Goa", "10-12-2023", "Beautiful beaches"),
    get_trip("Jaipur", "20-01-2024", "Loved the forts and culture")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)

print(json_data)