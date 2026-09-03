class Person:
    def __init__(self, name):
        self.name = name

#single level inheritance
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

#multi-level inheritance
class CollegeStudent(Student):
    def __init__(self, name, course):
        super().__init__(name, course)


student = CollegeStudent("Sadanand", "Python")

print(student.name)
print(student.course)