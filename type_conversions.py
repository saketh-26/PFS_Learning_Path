'''
TypeConversion (Typecasting) :It is process of converting one datatype to another
int(),float(),bool(),str(),list(),tuple(),set(),dict()
'''
#Converting -->int()
'''
a = 5
print(a)
print(type(a))
b = float(a) #Valid
print(b)
print(type(b))
c = bool(a)
print(c)
print(type(c))
d = str(a)
print(d)
print(type(d))

#e = list(a)
#print(e) #int object is not iterable
#f = tuple(a)
#print(f)
#g = set(a)
#print(g)
h = dict(a)
#print(h)

#Converting from float()

a = 5.2
print(a)
print(type(a))
b = int(a)
print(b) #truncating the decimal value
print(type(b))
c = bool(a)
print(c)
print(type(c))
d = str(a)
print(d)
print(type(d))
e = list(a)
print(e) #float object is not iterable
print(type(e))
#same for tuple(),set(),dict()

#Converting from bool() -->True,False
boolean = False
print(boolean)
print(type(boolean))
b = int(boolean)
c = int(True)
print(b,c)
d = float(boolean)
e = float(True)
print(d,e)
f = str(boolean)
g = str(True)
print(f,g)
print(f+g)
h = list(boolean)
print(h) #bool object is not iterable
#same for tuple(),set(),dict()
'''
#Converting from str()
name = "Codegnan"
#a = int(name)
#print(a) #ValueError
'''a = '10' #Numeric string
b = int(a)
print(type(b))
c = '10.2'
d = int(c)  #use float() instead
print(d)

#b = float(name)
#print(b) #ValueError
c = float('10')
print(c)
d = float('10.2')
print(d)
#both are converted to float values

d = bool(name)
print(d)

print(name)
print(type(name))
d = list(name)
print(d) #it splits into characters
e = tuple(name)
print(e)# Valid
f = set(name)
print(f) #removes duplicates
#g = dict(name)
#print(g) #needs key-value pair like structure
g = dict.fromkeys(name)
print(g)
'''

#Converting from list()
data = [1,5,8,9,23]
#a = int(data)#TypeError
#print(a) 
#b = float(data)#TypeError
#print(b)
#c = bool(data)
#print(c)
'''print(data)
d = str(data)#Allowed
print(d)
print(type(d))
print(len(d))
e = tuple(data)
print(e)
f = set(data)
print(f)
#g = dict(data)
#print(g)
g = dict.fromkeys(data)
print(g)
print(len(g))

#Converting from tuple()
place = ('Vijaywada','codegnan',25)
#a = int(place) #TypeError
#print(a)
#b = float(place)
#print(b)
c = bool(place)
print(c)
d = str(place) #tuple is converted to string
print(d)
e = list(place)
print(e)
f = set(place)
print(f)
#g = dict(place) #ValueError
#print(g)
g = dict.fromkeys(place)
print(g)

#Converting from set()
a = {1,5,8,1,2,6}
print(a)
#b = int(a) #TypeError
#print(b)
#c = float(a)#TypeError
#print(c)
d = bool(a) #Allowed returns True/False depending on input
print(d) 
e = list(a)
print(e)
f = tuple(a)
print(f)
#g = dict(a) #TypeError
#print(g)
g = dict.fromkeys(a)
print(g)
'''
#Converting from dict()

a = {1:1,2:4,3:9,4:16,5:25}
print(a)
print(len(a))
#b = int(a) #TypeError
#print(b)
#c = float(a)#TypeError
#print(c)
'''d = bool(a)
print(d)
e = str(a)
print(e)
print(len(e))'''
f = list(a) #returns keys as output
print(f)
g = tuple(a)
print(g)
h = set(a)
print(h)
g = dict.fromkeys(a)
print(g)


















