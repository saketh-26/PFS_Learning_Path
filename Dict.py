'''
Dictionary -->A Dictionary is an Ordered,Mutable Collection that stores the
data in key,value pairs.Unlike Lists,tuples,which were indexed by position,
dictionaries are indexed by unique keys

we use {} curly braces where each key is followed by a colon : and the key-value
pairs are separated bu commas

Syntax: a = {key1:value1,key2:value2,........keyn:valuen}

Key Features :
->Keys must be Unique
-->Keys must be Immutable
-->Values can be of any datatype

#Creation of Dictionaries

data = {'rollnos':[45,35,65,75],
        'names':['Steve','Roger','Matt','Spidey'],
        'marks':(65,85,46,86)}
print(data)
print(type(data))
print(len(data))
#print(data[0]) #KeyError -->only values to be accessed by keys
print(data.keys()) #returns keys

print(data['rollnos'])
print(data['names'])
print(type(data['names']))
print(data['names'][1])

print(data['names'][1:])
print(data['marks'][1:])
print(data['names'][::2])

print(data['marks'][::3])
#print(data['Saketh']) #raises Keyerror as key is not present
print(data.get('Saketh')) #get() will return value if key is present,else default\
print(data.get('marks'))

#Add new details into the above dictionary
print(data.values()) #returns values from the dictionary

print(data['rollnos'])
data['rollnos'].append(95)
print(data['rollnos'])
data['names'].extend(['Sunny','Sony','Sai'])
print(type(data['marks']))

data['marks']=list(data['marks'])
print(data)
data['marks'].insert(1,95)
print(data)
#Update the dictionary
data['address'] = {'Hyd','Vjwda','Vzg','Knr'}
print(data)
data['address'].add('Bnglre')
print(data)
data['names'].remove('Sai')
print(data)
data['marks'].clear()
print(data)

#Accessing data from dictionary ->keys(),values(),items()
print(data.items()) #returns key-value pairs

#Adding and Updating data from the dictionary

data['address'] = {'Hyd','Knr','Vjwda','Vzg'}
print(data)

data.update({'age':[25,26,21,23],'gender':['male','female']})
print(data)
#setdefault() -->return value for existing key else update the dictionary       
print(data.setdefault('age')) #existing key we are able to get the value
print(data.setdefault('Country'))
print(data)

#fromkeys() -->Dictionary method used to create a new dictionary with a
#set of keys and a common default value

#syntax -->dict.fromkeys(iterable,value)
#iterable -->list,tuple,string
#value -->optional (default-->None)

data=['Codegnan','Python','Java','GENAI']
d  = dict.fromkeys(data)
print(d)
e = dict.fromkeys(data,'Hyd')
print(e)
e['Python'] = 'Vjwda'
print(e)
d['Codegnan'] = ['Hyd','Vjwda','Vzg']
print(d)


#Removing elements from the dictionary -->pop(),popitem(),clear()
data = {'Names':['Codegnan','Python','GENAI','Java'],
        'address':'Hyd','age':7}
print(data)
data.pop('age') #needs key
print(data)
#data.pop() #raises TypeError
data.popitem() #remove and return a key,value pair as a tuple 
print(data)
data.update({'Gender':['Male','Female'],
             'age':(7,8,9),
             'marks':[75,85,65]})
print(data)
data.popitem()
print(data)
#we can use del keyword also
del data['age']
print(data)
#clear() -->clears all the values from the dictionary and returns {}
data.clear()
print(data)

#built-in methods over dictionaries
data = {'rollnos':[45,35,65,75],
        'names':['Steve','Roger','Matt','Spidey'],
        'marks':(65,85,46,86)}
print(data)
print(type(data)) #returns the type of the object
print(len(data))
#max(),min()
print(max(data)) #fetches the key
print(min(data))
print(max(data['marks']))
'''
#Nested Dictionaries -->A Dictionary can contain another dictionary as its value
students = {'Alice':{'age':21,'address':'Hyd'},
             'Bob':{'age':20,'address':'Vjwda'},
             'Steve':{'age':21,'address':'Vzg'}}

print(students)
print(students['Alice'])
print(students['Alice']['age'])















