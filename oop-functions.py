def sayHi():  # def is for Functions
    print("Hello") # need to be indented

sayHi() # to call

print("--------------------------------------------------------")

def sayHi(name):
    print("Hello " + name)

sayHi("Syed")

print("--------------------------------------------------------")

def sayHi(name, age):
    print("Hello " + name + " you are " + age)

sayHi("Tom", "24")
sayHi("Syed", "99")

print("--------------------------------------------------------")

def sayHi(name,age):
    print("Hello " + name + " you are " + str(age))

sayHi("Syed", 94)
