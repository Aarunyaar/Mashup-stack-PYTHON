n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    marks.append(int(input(f"Enter marks of student {i+1}: ")))

average = sum(marks) / n
print("Average Marks:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))