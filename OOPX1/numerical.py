# random()
# randint()
# uniform()
# sample()
# range()
# round()
# math.trunc()
# math.floor()
# math.ceil()
# max()
# min()
# count()

a=2.5
x = 1
y = 35656222554887711
z = -3255522

print(type(a))
print(type(x))
print(type(y))
print(type(z))

import random
print(random.random()) # random number between 0.0 and 1.0

print(random.randint(3, 9)) # a number between 3 and 9, both included

print(random.uniform(10, 70)) # a random number between, and included, 10 and 70

mylist = ["a", "b", "c"]
print(random.sample(mylist, k=2)) #  Return a list that contains any 2 of the items from a list

# range(start, stop, step)
x = range(6) # 0 to 5
for n in x:
  print(n)

x = range(13, 16)
for n in x:
  print(n)

x = range(133, 139, 2)
for n in x:
  print(n)


x = round(2.47474)
print(x)

x = round(2.47474, 2)
print(x)

# Import math Library
import math

# Return the truncated integer parts of different numbers
print(math.trunc(3.85))
print(math.trunc(9.32))
print(math.trunc(-9.29))

# Round numbers down to the nearest integer
print(math.floor(0.6))
print(math.floor(1.4))
print(math.floor(5.6))
print(math.floor(-5.3))

# Round a number upward to its nearest integer
print(math.ceil(2.4))
print(math.ceil(6.3))
print(math.ceil(-6.3))


# max(n1, n2, n3, ...)

a = (6, 5, 3, 9)
x = max(a)
print(x)

a = ("Tom", "Ali", "Alex") # highest value, ordered alphabetically
x = max(a)
print(x)


# min(n1, n2, n3, ...)
a = (6, 5, 3, 9)
x = min(a)
print(x)

a = ("Tom", "Ali", "Alex") # highest value, ordered alphabetically
x = min(a)
print(x)

# list.count(value)
b = ['Tom', 'Ali', 'Alex']
x = b.count("Ali")
print(x)

a = [6, 5, 3, 9, 3]
x = a.count(3)           # Return the number of times the value 3 appears int the list
print(x)

