x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("--------------------------------------------------------")


y = "awesome"

def myfunc():
  y = "fantastic"
  print("Python is " + y)

myfunc()

print("Python is " + y)

print("--------------------------------------------------------")


def myfunc():
  global z
  z = "fantastic"

myfunc()

print("Python is " + z)


print("--------------------------------------------------------")

t = "awesome"

def myfunc():
  global t
  t = "fantastic"

myfunc()

print("Python is " + t)