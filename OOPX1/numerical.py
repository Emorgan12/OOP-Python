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


