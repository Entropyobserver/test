class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def display_student(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    # Class Method
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        return f"average gpa is {cls.total_gpa / cls.count}"
    
    @classmethod
    def get_count(cls):
        return f"total count is {cls.count}"

    # Static Method
    @staticmethod
    def is_honor_roll(gpa):
        return gpa >= 3.5

# Creating instances of Student
student1 = Student("Alice", 3.8)
student2 = Student("Bob", 3.2)
student3 = Student("Charlie", 3.5)

# Using instance method
print(student1.display_student())  # Output: Name: Alice, GPA: 3.8 
print(student2.display_student())  # Output: Name: Bob, GPA: 3.2
print(student3.display_student())  # Output: Name: Charlie, GPA: 3.5

# Using class method
print(Student.get_count())  # Output: 3
print(Student.average_gpa())  # Output: 3.5

# Using static method
print(Student.is_honor_roll(3.8))  # Output: True
print(Student.is_honor_roll(3.2))  # Output: False