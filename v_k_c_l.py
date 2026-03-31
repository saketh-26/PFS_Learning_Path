'''
Comments -->Comments are the notes in the code for readbility and are
ignored by the Python Interpreter
-->Single Line Comments #
-->Multi Line Comments (single triple quotes / double triple quotes

Variables -->A variable is a named reference to a value stored in
computer memory.Think of it as a labeled container that points to a value

name = "Saketh"  #assigning variable
age = 7
print(name)
print(name,age)

Rules for Naming Variables:
Keep it clean,simple and general
-->Letters (a-z,A-Z)
-->Numbers (0-9)
-->Underscore (_)

Not start with numbers,special characters,keywords

#2swer = 12
#$asdf = 125 #invalid syntax

email_id = "saketh@codegnan.com"
print(email_id)

#Multiple assignments -->Python lets u assign multiple variables in a single line
name,age,place = "Saketh",32,"Hyderabad"
print(name,age,place)
#same value to multiple variables
x=y=z = 25
print(x,y,z)

Keywords -->These are the reserved words in Python which carry a specific usage
Keywords for control block usage,Handling statements,function,class definition and
many more

shortcut use help() -->keywords -->35 keywords

#True = 25 #here we are boolean keyword
#if = 14
class = 45

#Dynamic Typing Conversion
x = 15
print(x)
x = 1.5
print(x)

#Core Built-in datatypes -->Numeric (int,float,complex),boolean
#Integer (int) -->Stores whole numbers,used for counts,quantities,indexes

students = 50
print(type(students))

#Floating Point (float) -->stores decimal value,used for prices,percentages,averages

percentage = 85.5
print(type(percentage))

#Complex (complex) -->stores data in real and imaginary form
#in the form of a + bj
value = 5+3j
print(value)
print(type(value))

value1 = 5+j3
print(value1)
print(type(value1))

#Boolean (bool) -->stores logical values (two possible -->True False)
is_active = True
task_submitted = False
print(type(is_active))


#Type Conversion -->Explicit Type (int,float,complex,bool)
price = 75
print(type(price))
q = float(price)
print(q)
print(type(q))
h = complex(price)
print(h)
print(type(h))
g = bool(price)
print(g)
print(type(g))

#Float -->Rmng types
percentage = 75.5
print(type(percentage))
a = int(percentage)
print(a)
print(type(a))
b = complex(percentage)
print(b)
print(type(b))
c = bool(percentage)
print(c)
print(type(c))

#Complex Type conversion -->int,float (TypeErrors)
value = 5+3j
print(type(value))
#a = int(value)
#print(a)
#b = float(value)
#print(b)
c = bool(value)
print(c)
print(type(c))

#Boolean Type (bool)
students_active = True
codegnan_chennai = False
a = int(students_active)
print(a)
print(type(a))
b = float(codegnan_chennai)
print(b)
print(type(b))
c = complex(students_active)
print(c)
print(type(c))

#input() -->by default it accepts any value but results only in str datatype

#a = input()
a = input("Enter the value:")
print(a)
print(type(a))

name = input("Enter the Organization name:")
print(name)
print(type(name))

#Accept integer input from the user -->int()
age = int(input("Enter the age:"))#raises ValueError if we pass other than int datatype
print(age)
print(type(age)) 

#Accept int/decimal values from the user -->float()
price = float(input("Enter the price of the item:"))
print(price)
print(type(price))

#print() -->display output on the screen

#1.basic output
print('--------------')
print("Hello Codegnan")
print('***************')

#2.Multiple values (include input())
name = input("Enter the name:")
marks = float(input("Enter the marks of the user:"))
print(name,marks)

#3.Using Separator (sep)
print("2018","08","08",sep="-")
print("2018","08","08",sep="/")

#4.Using end parameter
print("Codegnan is in",end=" ")
print("Hyderabad,Vijayawada and Vizag")

#5.Formatted Output (Professional way)

a)f-string (Recommended)

name = "Saketh"
age = 32
print(name,age)
print(f'My name is {name} and age is {age}')
'''
#b)format()
name = "Saketh"
age = 32
print("My name is {} and age is {}".format(name,age))









