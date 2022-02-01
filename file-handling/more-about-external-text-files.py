# readline()
# readlines()
# line.split()


f = open("abc.txt", "r")
print(f.readline())  # the first line of the file

f = open("abc.txt", "r")
print(f.readline(3)) # Return only the three first bytes from the first line:
print(f.readlines()) # Return all lines in the file, as a list where each line is an item in the list object
print(f.readlines(3)) # Do not return the next line if the total number of returned bytes are more than 3


txt = "welcome to the class"
x = txt.split() # Split a string into a list where each word is a list item
print(x)


txt = "welcome,to the class"
x = txt.split(",")
print(x)

txt = "welcome#to#the#class"
x = txt.split("#")
print(x)

txt = "welcome#to#the#class"
x = txt.split("#", 1)
print(x)