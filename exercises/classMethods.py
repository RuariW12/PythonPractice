# Class methods = Allow operations related to the class itself
#       Take (cls) as the first parameter, which represents the class itself



class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

student1 = Student("Sandy", 3.2)
student2 = Student("Jerry", 3.8)
student3 = Student("Harry", 4.0)

print(Student.get_count())