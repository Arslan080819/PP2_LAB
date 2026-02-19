class University:
    university_name = "KazNU"

    def __init__(self, student_name):
        self.student_name = student_name

student1 = University("Arslan")
student2 = University("Ali")

print(student1.student_name)
print(student1.university_name)
print(student2.university_name)
