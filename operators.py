'''
Operators --> An Operator is a symbol or a keyword that performs an operation
on one or more values (operands) that produces a result

7 Categories of Python Operators:
-->Arithmetic Operators
-->Assignment Operators
-->Comparision / Relational Operators
-->Logical Operators (and,or,not)
-->Membership Operators (in,not in)
-->Identity Operators (is,is not)
-->Bitwise Operators

#Arithmetic Operators -->Perform Mathematical operations
#+,-,*,/,//(Floor Division),%(Modulus),**(Exponential)

#Let us include input() and print() with above operators
a = int(input("Enter the first value"))
b = int(input("Enter the second value:"))
print(f'Addition is :{a+b}')
print(f'Subtraction is : {a-b}')
print(f'Multiplication is : {a*b}')
print(f'Division is : {a/b}') #it always returns a float value
print(f'Floor Division : {a//b}')
print(f'Modulus is : {a%b}')
print(f'Power: {a**b}')

#Assignment Operators -->Used to assign/update values to variables
#Assign =             Subtract and Assign -=       Division and Assign /=
#Add and Assign +=    Multiply and Assign *=       Floor Division and Assign //=
#Modulus and Assign %=  Exponential and Assign **=
a = int(input("Enter a value:"))
print(a)
b = int(input("Enter another value:"))
print(b)
a +=b  #a = a+b
print(a)
b -=a #b = b-a
print(a)
print(b)
a *=2
print(a)
a/=3
print(a)
a//=2
print(a)
a%=3
print(a)
a%=4
print(a)
b**=3
print(b)

#Comparision/Relational Operators -->Compare values and return a boolean
#(True / False) result

age = int(input("Enter the age:"))
vote_eligibility = 18
# == Equal to , < less than , > greater than,!= Not Equal to,
# <= Less than equal to, >=Greater than equal to
print(age == vote_eligibility)
print(age != vote_eligibility)
print(age < vote_eligibility)
print(age > vote_eligibility)
print(age <= vote_eligibility)
print(age >= vote_eligibility)


#Logical Operators -->They are used to combine multiple conditions
#and,or,not
#and -->True only if all conditions are satisfied
#or -->True if any one condition is satisfied
#not -->Reverses the boolean result

age = 25 #int datatype 
has_id = True #bool datatype
print(age >= 18 and has_id)
print(age < 20 or has_id)
print(not has_id)

#Membership Operators -->Check whether a value exists in a collection
#in , not in

age = int(input("Enter a value"))
students_age = [15,21,14,20,18]
print(age in students_age)
print('saketh' in ['codegnan','saketh','hyderabad'])
print('c' not in 'apple')

#Identity Operators -->Compare Location,not value (id)
#is,is not
a = 25
b = 25
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = [15,2,3]
b = a
c = [15,2,3]
print(id(a))
print(id(b))
print(a is b)
print(a is c)
print(a == c)
'''
#Bitwise Operators -->Perform binary operations on numbers
#and --> &
#or --> |
#xor --> ^
print(5 & 3) #convert 5 and 3 to binary then the rsult is binary converted to decimal
print(5 | 3)# convert to binary and check Any one condition to be True
print(5 ^ 3) #convert to binary and check only both are differnt 
# << Left shift , >> Right Shift
print(5 << 2) #perform left shift by two bits
print(5 >> 2)
print(bin(5)) #to get binary value






















