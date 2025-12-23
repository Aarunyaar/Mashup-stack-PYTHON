students = [
    {"id": 1, "name": "rajesh"},
    {"id": 2, "name": "rahul"},
    {"id": 3, "name": "sruthi"}
]

search_id = int(input("Enter student id: "))

found = False
for student in students:
    if student["id"] == search_id:
        print("Student name:", student["name"])
        found = True
        break

if not found:
    print("Student not found")