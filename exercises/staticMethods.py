# Static Methods = A method that belong to a class rather than any object from that class (instance)
#       Usually used for genreal utility functions
# Instance methods = Baest for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self): #instance method
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manger", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene", "Manager")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())