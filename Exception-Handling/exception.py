a = 10
b = 2

try:
    print(a/b)

except Exception as e:
    print("Wrong")

finally:
    print("Closed")








a = 10
b = 2

try:
    print("Open")
    print(a/b)
    u = int(input("Enter a number"))
    print(u)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero" , e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print("Closed")