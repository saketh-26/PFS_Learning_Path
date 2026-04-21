'''
Lists : A List is a Python built-in collection used to store multiple values
in a single variable.
A List is used when data count is dynamic,in simple words A list allows us to
group related data together

Real Life Anology : Students Marks -->one list
                    Expenses Tracker -->one list
                    Quiz Questions -->one list
Characteristics : A List is Ordered,Mutable,Indexed & Dynamic
Syntax : it is enclosed in square brackets and values are separated by commas
        data = [element1,element2,......]

#Creation of Lists
a = []
print(a)
print(type(a))
#We can pass same type or different datatypes into alist
age = [32,25,21,18,19]
print(age)
print(len(age))

marks = [75,85.5,45,35]
print(marks)
print(len(marks))
details = ['Saketh',32,'Hyderabad','Male',21.5]
print(details)
print(len(details))

#Nested lists
data = [['Saketh',32,21.5],['Chinnu',26,20],['Sai',34,23.5]]
print(data)
print(len(data))
'''

#Indexing and Slicing on Lists
'''data = [12,5,25]
print(data)
print(type(data))
print(len(data))

#Let us go for indexing
print(data[1])
#print(data[25]) #len(data) -->3 it returns error
print(data[-3])
'''
#Now let us create a Nested list and see all the possibilities
details = [[21,'Sathvik','Vijayawada'],
           [25,'Raju','Hyderabad'],
           'Codegnan',[26,'Chinnu','Karimnagar']]
'''print(len(details))
print(details[0])
print(len(details[0]))
#let us check the subindexing
print(details[0][1])
#Now again we can extract characters from ths string
print(type(details[0][1]))
print(len(details[0][1]))
print(details[0][1][:4])

#Access Raju,Hyderabad from the list
print(details[1])
print(details[1][1:])

print(details[2:])
#print(details[2:[0]]) #raises TypeError
print(details[3])
print(details[3][::2]) #we are using step value
print(details) #original list
print(details[::-1]) #reverses the entire collection   

#Lists are Mutable -->elements can be modified (indexing & slicing)
marks = [78,85,65,45]
print(len(marks))
print(marks[2])
marks[2] = 95
print(marks)
#marks[45] = 100 #IndexError
#print(marks)

#Using Slicing
print(marks[2:])
marks[2:] = [85,75]
print(marks)
marks[:2] = ['Codegnan',25,45]
print(marks)
marks[::3] = ['Saketh','Hyderabad']
print(marks)

#Updating elements into list -->append(),extend(),insert()
#dir(list) -->returns list of available methods
#append() -->Add single element to the end of the list
#Think of using append() as adding one item at a time
data = ['Codegnan','Python',7]
data.append('Saketh')
print(data)
#what if we add a list using append()
#data.append(data)
#print(data)
data.append([25,12]) 
print(data)#creates a nested list


#Create an empty list
data = []
data.append('Saketh')
print(data)
data.append([15,12])
print(data)

#extend() -->add multiple elements to the end of the list
details = ['Saketh','Codegnan',25]
print(details)
details.extend('python')
print(details)
details.append('python')
print(details)
marks = [75,85,65]
#now we will use extend so that all elements will be added from the iterable
details.extend(marks)
print(details)

#insert(object,index) -->Insert object before index
data = ['Saketh','Codegnan','Python','Java','Vjwda','Hyd','Vzg']
print(data)
print(len(data))
data.insert(2,'AI')
print(data)
data.insert(3,[47,58,26,'Testing'])
print(data)
print(len(data))
#what if we go with negative indexing

data.insert(-3,'Selenium')
print(data)
print(len(data))

#remove() -->removes elements by value
#deletes the first occurance of the given value
details = ['Codegnan',26,3,15,14]
print(details)
details.remove(15)
print(details) #as we have single occurance no issue
#details.remove(15) #ValueError just make a note of it
#print(details)

details.extend(['Codegnan',26,2018,'Python'])
print(details)
details.remove('Codegnan')
print(details)

#pop() -->removes element by index
#by default it takes last index if no index given
data= ['Codegnan','Python','Java','Hyd',2023,2018]
print(data)
data.pop()
print(data)
data.pop(3)
print(data)

#we wanted to remove specific group of elements we can use del keyword
data= ['Codegnan','Python','Java','Hyd',2023,2018]
del data[2]
print(data)
del data[-2:]
print(data)
data.extend([14,15,23,6])
print(data)
print(data[::2])
del data[::2]
print(data)

#clear() -->removes all elements from the collection and creates an empty list

data= ['Codegnan','Python','Java','Hyd',2023,2018]
data.clear()
print(data)
print(len(data))
'''
#copy() -->creates a shallow copy of the list
#A shallow copy creates a new list,but it doesnot Copy nested objects
#it just copies references (pointers) to inner elements
'''a = [15,26,36,'Codegnan']
print(a)
b = a.copy()
print(b)
#let us modify new list
b[2] = 'Saketh'
print(b)
print(a)
b.append('Python')
print(b)
print(a)

data=[15,2,3,['Codegnan','Python','Java','Hyd']]
print(data)
details = data.copy()
print(details)
#now let us modify the elements in new list
#details[2] = 'Saketh'
#print(details)
#print(data)
details[-1][2] = 'Vjwda'
print(details)
print(data)

#count() -->returns the count of occurances of values
data = [15,2,3,6,6,'codegnan',14]
print(data)
print(data.count(6))
print(data.count('Saketh')) #it returns 0 as no object in list

#index() -->returns the first occurance of the value
data = [15,2,3,6,6,'codegnan',14]
print(data.index(6))
#as we have index with start and stop we can get next occurances
print(data.index(6,4))
data.append(3)
print(data)
print(data.count(3))
print(data.index(3)) #returns first occurance
print(data.index(3,3))
#print(data.index('Saketh')) #ValueError 
'''

#sort() and reverse()
#sort() -->will arrange the elements (numeric -->ascending order,text ->alphabetical
#order)
'''
marks = [75,45,65,35]
print(marks)
marks.sort()
print(marks)
#print(marks.sort()) #returns None,reverse = True makes the list to be in descendingh order
marks.sort(reverse = True)
print(marks)

data = ['python','java','codegnan','ai']
print(data)
data.sort()
print(data)
data.append('Codegnan')
print(data)
data.sort()
print(data)

data = ['Codegnan',7,'Vjwda',23]
data.sort() 
print(data) #TypeError only similar datatype to be used not mix

#reverse() ->return the elements in reverse order
marks = []
marks.extend([85,95,50,15,35])
print(marks)
marks.reverse()
print(marks) #the original list is modified for that below process is applied
print(marks[::-1]) #it also results elements in reverse order
'''

#len() -->returns the number of items in a container
data = [85,45,65,12,35]
print(len(data))
#to get maximum and minimum values from a collection -->max(),min()
print(max(data))
print(min(data))








