# class variables = shared among all instances of a class
#       Defined outside the constructor
#       Allow you to share data among all objects created from that class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Patrick", 30)
student2 = Student("Larry", 26)
student3 = Student("Jerry", 15)

print(student1.name)
print(student1.age)
print(Student.class_year)

print()

print(student2.name)
print(student2.age)
print(Student.class_year)

print()

print(student3.name)
print(student3.age)
print(Student.class_year)

print()

print(f"The total students in the class of {Student.class_year} is: {Student.num_students}")