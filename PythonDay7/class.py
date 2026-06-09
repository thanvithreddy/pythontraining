class Student:
    def __init__(self):
        print("Student Object is created")
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
s1 = Student('scott', 25)
details = s1.display()
s2= Student()
details = s2.display()
#more objects can be created as per the requirement


