attendance = [18, 20, 19, 15, 21]

full_days = 0
totalattendance = 0

for students in attendance:
    if students >= 20:
        print("Attendance is full")
        full_days += 1
    else:
        print("Attendance is not full")

    totalattendance += students

print("No of days", full_days)
print("No of students present in 5 days", totalattendance)















        
