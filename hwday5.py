frontend_students = {"Alice", "Bob", "Charlie", "Diana"}
backend_students = {"Charlie", "Evan", "Fiona", "Bob"}

backend_students.add("George")

frontend_students.remove("Diana")

both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)

only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)

unique_students = frontend_students | backend_students
print("Total unique students:", len(unique_students))

course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

for course, count in course_counts.items():
    print(f"{course} has {count} students")

course_counts_with_fullstack = {
    **course_counts,
    "Fullstack": len(unique_students)
}

print("Courses with Fullstack added:", course_counts_with_fullstack)