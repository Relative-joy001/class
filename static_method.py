# Static method

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance methods
    def get_info(self):
        return f"{self.name} is a {self.position}."
    

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions
    
employee1 = Employee("John Doe", "Developer")
employee2 = Employee("Jane Smith", "Manager")
employee3 = Employee("Tom Johnson", "Designer")

print(Employee.is_valid_position("cook"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())