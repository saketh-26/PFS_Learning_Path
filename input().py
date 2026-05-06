'''
input() -->used to accept input from the user
int,float,str,list,tuple,set,dict

#String input
name = input("Enter the name:")
print(name)
print(type(name))
print(len(name))

#Integer input ->quantity,age,number of items ...

quantity = int(input("Enter the quantity:"))
print(quantity)
print(type(quantity))

#Float input -->price,temperature,discount...
price = float(input("Enter the price:"))
print(price)
print(type(price))

#Multiple string values -->input() with split()
name,place,gender = input("Enter the details:").split()
print(name)
print(place)
print(gender)
name,place,gender = input("Enter the details:").split(',')
print(name)
print(place)
print(gender)

#Input as List (space separated) -->List of names,IDs or marks
names = input("Enter the student names:").split()
print(names)
print(type(names))

#Input as List (comma separated) -->tags,emails,product categories
categories = input("Enter the student names:").split(',')
print(categories)

#List of Integers -->marks,product prices...
marks = list(map(int,input().split(',')))
print(marks)
print(type(marks))

#list of float values -->sensor readings..
readings = list(map(float,input("Enter the values:").split(',')))
print(readings)
print(type(readings))

#tuple as input -->dimensions (length,width,height)
dimensions = tuple(map(float,input("Enter the values:").split(',')))
print(dimensions)

#Set input() -->Selected Image IDs(removing duplicates from it)

image_ids = set(map(int,input('Enter the Image IDs').split(',')))
print(image_ids)
'''
#Dict as input -->eval() -->structured data (map user details)
details = eval(input("Enter the details:"))
print(details)























