python_students = {"Aarav", "Diya", "Kiran"}
data_science_students = {"Diya", "Meera", "Rohan"}

python_students.add("Sanjay")

data_science_students.remove("Meera")

both_courses = python_students.intersection(data_science_students)
print("Students in both courses:", both_courses)

only_python = python_students.difference(data_science_students)
print("Only in Python:", only_python)

all_students = python_students.union(data_science_students)
print("All students (no duplicates):", all_students)

course_dict = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {course: count * 2 for course, count in course_dict.items()}
print("Expected growth:", expected_growth)
