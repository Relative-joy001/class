class student:

    class_year = 2024
    num_students = 0
    def __init__(self, name, age, grade, subjects):
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects
        student.num_students += 1

student1 = student("John Doe", 18, "A", ["Math", "Science", "English"])
student2 = student("Jane Smith", 17, "B", ["History", "Geography", "French"])
student3 = student("Bob Johnson", 19, "C", ["Computer Science", "Physics", "Chemistry"])
student4 = student("Alice Brown", 20, "D", ["Biology", "Physics", "Chemistry"])

#print(f"Student 1: {student1.name}, Age: {student1.age}, Grade: {student1.grade}, Subjects: {student1.subjects}")
#print(student.class_year)
print(student.num_students)

print(f"my graduating class of {student.class_year} has {student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
