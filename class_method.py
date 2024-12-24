# Class methods

class Student:

    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    # Class method
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("John Doe", 3.8)
student2 = Student("Jane Smith", 3.9)
student3 = Student("Lary Thompson", 3.7)


print(Student.get_count())
print(Student.get_average_gpa())