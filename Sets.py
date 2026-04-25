'''
Many Real-world problems require unique values only

Examples : Unique StudentIDs,Unique emailids,Unique usernames....
Sets : A Set is an Unordered collection of Unique,Immutable elements
Properties of Sets:Unique Elements,Unordered Collection,Mutable collection,
Elements Immutable (Cannot contains lists or dicts)

#Creation of Sets: set() -->we use {} notation
a = set()
print(a)
print(type(a))

a = {1,5,8,1,5,2,3} #as it has duplicate entries it will reduce the length
print(a)
print(type(a))
print(len(a))

#if you try to go for accessing elements in sets -->Not possible
#print(a[2]) #TypeError 
#No Indexing,Slicing,Step Interval in Sets

#Creation of Sets from Lists,Tuples,strings

details = ['Codegnan','Saketh','Python',25]
d = set(details)
print(d)

e = (14,2,8,5,'code')
f = set(e)
print(f)

d = "Codegnan"
f = set(d)
print(f)

d = {'Saketh',32,[75,25,65],42} #TypeError
print(d)

d = {'Saketh',32,(75,25,65),42}
print(d)

#As Set is an Unordered and a Mutable collection

data = {'codegnan','saketh',2018,2026}
print(data)
print(len(data))
print(type(data))
#print(data[2]) TypeError as we dont have indexing/slicing

#add()-->adds an element to the set,update()-->it updates the original set
#with given objects (string,list,tuple..)
data.add('python')
print(data)

data.add(('vjwda','hyd','vizag'))
print(data)

data.update('Java')
print(data)

data.update(['Code','GENAI'])
print(data)

#remove(),discard(),pop(),clear()
data.remove('codegnan')
print(data)
#If we again try to use remove() for a value which is not existing
#data.remove('sai')
#print(data)
#discard()
data.discard('saketh')
print(data)
data.discard('saketh') #discard() will ignore the error
print(data)

#pop()-->removes an arbitary element and raises KeyError if set is empty
#clear()
data.pop()
print(data)

data.clear()
print(data)
'''
#Operations on sets -->union(),intersection(),difference(),symmetric_difference()

names = {'saketh','sai','eswar',30}
age = {32,34,30}
print(names)
print(age)
'''result = names.union(age)
print(result)
result = age | names
print(result)
common = names.intersection(age)
print(common)
common = age & names
print(common)
#we want to update the set with common elements
names.intersection_update(age)
print(names)
print(age)

d = names.difference(age)
print(d)
e = age - names
print(e)

f = names.symmetric_difference(age)
print(f)
g = age ^ names
print(g)

#isdisjoint(),issubset(),issuperset() -->return Boolean value
d = names.isdisjoint(age)
print(d) #checks for null intersection
'''
a = {2,4,6,8}
b = {1,2,4,5,6,8,10}
print(a.issubset(b))
print(b.issuperset(a))






























