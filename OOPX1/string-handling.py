# isupper()
# islower()
# upper()
# lower()
# isalpha()
# split()
# len()


a = "Hello! Welcome to Syed Murad’s OOP Class."  
b = "What is Syed’s fuel?"
c = "Coffee! Coffee!!"
d = "COFFEE"
e = "coffee"

print(a) 
print(b)
print("Hello! Welcome to Syed Murad’s OOP Class")  # the escape character \', for apostrophe 

# Check if all the characters in the text are in upper case
x = a.isupper()
print(x)
x = d.isupper()
print(x)

# Check if all the characters in the text are in lower case
x = a.islower()
print(x)
x = e.islower()
print(x)

x = b.upper()
print(x)
x = c.lower()
print(x)

x = d.isalpha() # Check if all the characters in the text are letters
print(x)

x = c.split() # Split a string into a list where each word is a list item
print(x)

x = c.split(", ") 
print(x)

x = c.split("!") 
print(x)


x = len(d) 
print(x)

name = ['Tom', 'Ali', 'Alex']

x = len(name) 
print(x)