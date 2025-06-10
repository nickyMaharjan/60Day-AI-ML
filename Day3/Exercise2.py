from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self): #role() is now an abstract method
        pass

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #super() --> calls Person's class __init__, just like in Java
        self.student_id = student_id
        self.__marks = {}

    def role(self):
        return "Student"

    def set_marks(self, subject, mark):
        if 0 <= mark <= 100:
            self.__marks[subject] = mark
        else:
            print("Invalid mark")

    def get_marks(self):
        return self.__marks

    def calculate_average(self):
        if self.__marks:
            return sum(self.__marks.values()) / len(self.__marks)
        return 0

    # POLYMORPHISM: Same method name, different behavior
    def introduce(self):
        return f"I am {self.name}, a student."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def role(self):
        return "Teacher"

    # POLYMORPHISM: Same method name, different behavior
    def introduce(self):
        return f"I am {self.name}, and I teach {self.subject}."

# POLYMORPHISM in action
def print_introduction(person):
    print(person.introduce())

# Example Usage
student = Student("Bikash", 18, "12")
teacher = Teacher("Mrs. Sherstha", 35, "Science")

student.set_marks("Math", 85)
student.set_marks("English", 90)

print_introduction(student)
print_introduction(teacher)

print(student.get_marks())
print(f"Average: {student.calculate_average()}")
print(f"Student Role: {student.role()}")
print(f"Teacher Role: {teacher.role()}")
