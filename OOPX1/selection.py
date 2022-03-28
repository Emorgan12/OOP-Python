# selection

# if
# else 
# elif - oop-if-else-1
# case: - also Switcher 

x = 21
y = 210
if y > x:
  print("Y is greater than X")



a = 21
b = 21
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# You can also have an else without the elif
c = 200
d = 33
if b > a:
  print("d is greater than c")
else:
  print("d is not greater than c")
  


def week(i):
    switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
    return switcher.get(i,"Invalid day of week")


    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    
 
# Driver program
if __name__ == "__main__":
    i=0
    print (week(i))



# just for example case 

# http_code = "418"
# match http_code:
#     case "200":
#         print("OK")
#         do_something_good()
#     case "404":
#         print("Not Found")
#         do_something_bad()
#     case "418":
#         print("I'm a teapot")
#         make_coffee()
#     case _:
#         print("Code not found")