# "a" - Append - will append to the end of the file
ow = open(r"abc.txt", "a")
ow.write("I can write whatever I want!")
ow.close()

#open and read the file after the appending:
ow = open(r"abc.txt", "r")
print(ow.read())

ow.close()
