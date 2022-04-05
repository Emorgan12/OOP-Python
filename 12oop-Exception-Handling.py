a = 6
b = 8

try:
    print("Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("You cannot divide a Number by Zero" , e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong")

finally:
    print("resource Closed")


# x=input("enter first num: ")
# y=input("enter second num: ")

# try:
#     print(x/y)

# except:
#     print("No Zero")    
