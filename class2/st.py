class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def has_goodgpa(self):
         if self.gpa >= 3.5:
               return True
         else:
               return False
