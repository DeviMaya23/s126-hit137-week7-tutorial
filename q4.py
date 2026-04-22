class Student:
    """
    A class representing a student.
    Has attributes for name, roll number, age, marks.
    """
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

    def Display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")


john = Student("John", "S123123")
john.setAge(20)
john.setMarks(85)
john.Display()
