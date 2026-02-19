students = [
    {"name": "Ali", "grade": 85},
    {"name": "Arslan", "grade": 95},
    {"name": "Dana", "grade": 78}
]

sorted_students = sorted(students, key=lambda student: student["grade"])

for student in sorted_students:
    print(student)
