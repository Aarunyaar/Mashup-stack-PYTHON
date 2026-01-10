students = {}

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter name: ")
    mark = int(input("Enter mark: "))
    students[name] = mark

for name, mark in students.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    else:
        grade = "C"
    print(name, "Grade:", grade)