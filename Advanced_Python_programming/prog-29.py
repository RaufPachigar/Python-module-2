#What relationship is appropriate for Student and Person?


# The relationship between Student and Person is an inheritance relationship.
# A Student is a specific type of Person, so the Student class can inherit from the Person class. 
# This represents an "is-a" relationship.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person): 
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id