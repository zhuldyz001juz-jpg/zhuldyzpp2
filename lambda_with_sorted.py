students = [
    ("Aliya", 85),
    ("Zhuldyz", 95),
    ("Dana", 78)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(sorted_students)