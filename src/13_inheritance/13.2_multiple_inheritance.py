class Person:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, job):
        self.job = job


class WorkingStudent(Person, Employee):   #multiple inheritance here
    def __init__(self, name, job):
        Person.__init__(self, name)
        Employee.__init__(self, job)


student = WorkingStudent("Sadanand", "Trainee")

print(student.name)
print(student.job)