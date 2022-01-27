# "a" - Append - will append to the end of the file
ow = open("abc.txt", "a")
ow.write("I can write whatever I want!")
ow.close()

# "w" - Write - will overwrite any existing content
# ow = open("abc.txt", "w")
# ow.write("I can write whatever I want! W.")
# ow.close()

#open and read the file after the appending:
ow = open("abc.txt", "r")
print(ow.read())

ow.close()


