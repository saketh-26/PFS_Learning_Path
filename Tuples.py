'''
Tuples -->A tuple is an Immutable,Ordered collection of elements
Tuples are similar to lists,but once tuple is created we cannot modify the
elements in the tuple,we can store any type of data(int,float,str,list etc..,)

We use () for tuples

data = (5,25,'saketh','codegnan')
print(data)
print(type(data))

#even without any braces data is automatically stored in tuple
marks = 75,76,85,45,50
print(marks)
print(len(marks))
print(type(marks))

#we will create an example with any type of data so that we will have a recap\
student_details = ('Saketh',32,[75,85,95],['Python','AI','ML'],
                   'John',24,[70,65,45],['Java','ML','AI'],
                   'Sai',20,[80,85,65],['DS','DL','Python'])

print(student_details)
#print(len(student_details))

#Accessing Tuple elements
#print(student_details[1])
#student_details[1] = 85
#print(student_details[1]) #TypeError as Tuples are Immutable
#print(student_details[-3]) #negative indexing

#print(student_details[1:4]) 
#As we have output with lists we can perform subindxing as below
print(student_details[3])
print(student_details[3][2])
student_details[3][1] = 'GENAI'
print(student_details[3])
print(len(student_details[3]))

#once we have list all list methods can be applicable
print(type(student_details[3]))
student_details[3].extend(['Testing','DSA','GENAI'])
print(student_details[3])

#Overall length of tuple is same
print(len(student_details))

print(student_details[1:8:2])
#print the elements in reverse order
print(student_details[3])
print(student_details[3][::-1])
'''

#Operations on Tuples
#Concatenation -->Combine one or more tuples into a single tuple
'''data = (75,85,14,5,6)
marks = (75,85,65)
names = ('John','Paul','Sonu')
#we want to combine all of them
details = data + marks + names
print(details)

#Repetition --> Repeat the elements in a tuple by using '* operator
age = (18,15,16)
new_data = age * 2
print(new_data)

#Tuple Unpacking
#Assign elements to multiple variables

my_tuple = (45,12,65,48)
a,b,c, = my_tuple
print(a,b,c,d)

#Methods in Tuples
a = (75,45,12,6,5,5)
print(a)
print(dir(a))
#count() & index()
print(a.count(5))
print(a.index(5))
print(a.index(5,5))

#we can use len(),max(),min(),type()
print(len(a))
print(min(a))
print(max(a))
'''
#Every built-in dataype is a built-in function
#int(),float(),complex(),bool(),str(),list(),tuple()...
marks = (75,65,85,95)
print(type(marks))
marks = list(marks)
print(marks)
print(type(marks))

b = tuple('saketh')
print(b)
print(len(b))













