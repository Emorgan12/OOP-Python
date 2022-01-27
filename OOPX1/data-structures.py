# lists and arrays
# index()
# append()
# insert()
# remove()
# count()
# pop()
# sort()
# in
# not in
# len()


list1 = ['Tom', 'Ali', 'Alex']
list2 = [1, 5, 7, 9, 3, 33]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

print(list1)
print(list4[2:4])
print(list4[:4])

list1[2]="Katy"
print(list1)

list1[1:3] = ["Ange"] # Change the second and third value by replacing it with one value
print(list1)

# list.index(elmnt)
x = list2.index(3)
print(x)

print(list1)

list5 = ['Tom', 'Ali', 'Alex']
list6= ["Ford", "BMW", "Volvo"]

list5.append("456")
print(list5)

list5.append(list6) # Add an element to the list5 list
print(list5)

list5.insert(3, "Anna") # list.insert(pos, elmnt)
print(list5)

list5.remove(["Ford", "BMW", "Volvo"]) # list.remove(elmnt)
print(list5)

list5.remove("456")
print(list5)

x = list2.count(3) # the number of times the value 3 appears int the list - list.count(value)
print(x)

x = list5.pop(3) # the number of times the value 3 appears int the list - list.count(value)
print(x)

print(list5)

# list.sort(reverse=True|False, key=myFunc)
list5.sort() #  list alphabetically
print(list5) 

# Sort the list descending
list5.sort(reverse=True)
print(list5) 


# A function that returns the 'year' value
def myFu(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFu)

print(cars)

# by length 
def myFu2(e):
  return len(e)
list7= ["Bill", "Steve", "Jeff", "Elon"]
list7.sort(key=myFu2)
print(list7)

# the list by the length of the values and reversed
def myFu3(e):
  return len(e)
list7= ["Bill", "Steve", "Jeff", "Elon"]
list7.sort(reverse=True, key=myFu3)
print(list7)

x = len(list7)
print(x)


list8= [1,2,3,4,5]
string1= "My name is AskPython"
tuple1=(11,22,33,44)
 
print(5 not in list8) #False
print("is" not in string1) #False
print(88 not in tuple1) #True
print(88 in tuple1) #False