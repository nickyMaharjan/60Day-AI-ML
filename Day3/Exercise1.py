class Student:
    def __init__(self, name, student_id, english, nepali, maths, science, social):
        self.name = name
        self.student_id = student_id
        self.english = english
        self.nepali = nepali
        self.maths = maths
        self.science = science
        self.social = social

    def calculate_average(self):
        total = self.english + self.nepali + self.maths + self.science + self.social
        return total / 5

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

student1 = Student("Bikash", "1", 85, 78, 92, 88, 80)
print(f"{student1.name}'s average marks: {student1.calculate_average()}")
print(f"{student1.name}'s grade: {student1.calculate_grade()}")

student1 = Student("Suman", "2", 88, 69, 85, 80, 84)
print(f"{student1.name}'s average marks: {student1.calculate_average()}")
print(f"{student1.name}'s grade: {student1.calculate_grade()}")