from st import Student

Student1=Student("Tom","IT",3.5)
Student2=Student("Syed","IT",3.9)

print (Student1.gpa)
print(Student1.has_goodgpa())

print (Student2.name, "-", Student2.major, "-",Student2.gpa, "-", Student2.has_goodgpa())
