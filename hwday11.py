from datetime import datetime
import json


def create_record(city, comment, date_str):
    return {
        "city": city,
        "comment": comment,
        "date": date_str
    }


records = [
    create_record("Paris", "Visited Eiffel Tower", "05-06-2022"),
    create_record("Rome", "Explored ancient ruins", "18-09-2023"),
    create_record("Tokyo", "Enjoyed local food", "12-03-2024")
]


for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")


json_data = json.dumps(records, indent=4)
print("JSON Data:\n")
print(json_data)


parsed_records = json.loads(json_data)


print("\nTravel Records:")
for record in parsed_records:
    print(f"{record['city']} | {record['date']} | {record['comment']}")