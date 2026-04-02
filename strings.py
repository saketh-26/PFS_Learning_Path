'''
Strings --> A String is sequence of characters used to represent text,it can be
enclosed in single,double or triple quotes
Strings are Immutable (cannot be changed)
Indexed (each character has a position)

name = "Codegnan"
print(name)
print(type(name))
#checking for type conversion
#b = float(name) #ValueError same for float also
#print(b)
roll_no = '2512' #Numeric String
print(roll_no)
print(type(roll_no))
b = int(roll_no)
print(type(b))
c = float(roll_no)
print(c)
print(type(c))
d = bool(roll_no)
print(d)
print(type(d))

#Operations on Strings:
#Repetition
#Concatenation
#Indexing
#Slicing

#Repetition * -->Repeating string multiple times
name = 'Codegnan'
print(name*5)
print('Python !' * 4)
print('*' * 12)
#print(name * '*') #TypeError

#Concatenation -->Joining/Combining multiple strings +
name = 'Python'
place = 'Codegnan'
print(f'{name} in {place} is interesting')
print(name + place,"is interesting")
print(name +" "+place,"is interesting")
print(name+"\t"+place,"is interesting")

#String Indexing -->It means accessing individual characters in a string
#using their position
#Every character has a position (it can be space also)
#Indexing starts at 0 not 1 -->Positive indexing
#len() will return the number of items in a collection
text = "Python"
print(type(text))
print(len(text))

#Postive Indexing starts from 0 to len(obj) - 1
#Negative Indexing it allows access from the end -1 to first position

print(text[0]) #it takes first position
print(text[5])
print(text[-1]) #it returns last character
print(text[-5])

#String Slicing -->Extracting a part of strings using index ranges
#Syntax --> string[start:end] #start is included,end is excluded
#len(obj)

#Simple Slicing
text = "Programming"
print(len(text))
print(text[0:4])

#Middle Slicing
print(text[3:7])
#if we omit end
print(text[3:])

#Omitting Start or end Index
#Start Omitted
print(text[:6])
#End Omitted
print(text[6:])

#Negative indexing slicing
#Slice from end
text = "PythonProgramming"
print(len(text))
print(text[-11:])
#Slice using negative range
#print(text[-11:-18]) #it results empty space
print(text[-18:-11])
print(text[-10:-2])

#full string slicing ->slice with step value
#syntax is string[start:step:end]
print(text[1:10:1])
print(text[1:10:2]) #one character will be skipped after slicing within start:end
#skip characters without mentioning start ,end
print(text[::2]) #takes every 2nd character

#Reverse string
print(text[::-1]) #step -1 reverses traversal
print(text[::-2])

#String Methods
#Case Conversion Methods
#upper(),lower(),title(),capitalize(),swapcase()
a = "Codegnan"
print(a.upper())
b = a.upper()
print(a,b)
c = a.lower()
print(a,b,c)
#capitalize() -->capitalizes the first character
text = "hello codegnan"
print(text.capitalize())
#title() -->capitalizes the first letter of each word
print(text.title())
#swapcase() -->converts upper -->lower & viceversa
print('CoDeGnan'.swapcase())

#Search & Find Methods
#index(),find(),count()
a = "Codegnan"
print(len(a))
#count() -->counts how many times sub string appears
print(a.count('n'))
print(a.count('n',1,6)) #it checks start and end index
#index() -->give index positin of a character,if not found,it raises an error
print(a.index('d'))
#print(a.index('S')) #ValueError
print(a.index('n')) #it retrns the first occurance of the substring
print(a.index('n',6,8))
#find() returns the index of first occurance,-1 if not found
print(a.find('n'))
print(a.find('S')) #it shouldn't raise Error,returns -1
print(a.find('n',6,8))

#String testing Methods -->boolean result
a = "Python"
#startswith(),endswith()
print(a.startswith('P')) #checks the substring
print(a.startswith('y',0,3)) #False
print(a.startswith('y',1)) #specify index position
#endswith() checks how the string ends with sub
print(a.endswith('n'))
#isalpha(),isdigit(),isalnum()
print('hello'.isalpha()) #returns True if all characters are alphabets
print('hello12'.isalnum()) #returns True if all characters are alphanumeric
print('8106429771'.isdigit()) #returns True for digit string
#isupper(),islower(),istitle()
print('CODEGNAN'.isupper()) #returns True only if all characters are uppercase
print('codegnan'.islower())
print('Hello codegnan'.istitle())#returns True if the string is in title case
#isidentifier() #returns True for a valid identifier
print('Saketh2612'.isidentifier())
print('2612Saketh'.isidentifier()) #returns False as it is not a valid Identifier

#Replace method
#replace() -->replaces occurances of old with new
a = "Codegnan"
b = "Saketh"
print(a.replace('n','r'))
print('apple'.replace('p','b'))'''
#Splitting and Joining Methods
#split(sep) -->splits the string into a list by sep
'''a = "Codegnan"
b = a.split(':')
print(a,b)
b = "Codegnan,Python,Saketh"
c = b.split()
print(b,c)
d = b.split(',') #now we split with , list with 3 objects
print(b,d)

#join(iterable)-->join elements with a separator
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print(":".join("Saketh"))
print('-->'.join("Python"))'''

#WhiteSpace & Trimming Methods
#strip() -->removes leading and trailing characters(default:spaces)
a = "  hello "
print(len(a))
b = a.strip()
print(b)
print(len(b))
#lstrip() -->remove leading characters
print('--->codegnan'.lstrip('--->'))
a = "--->codegnan"
b = a.lstrip('--->')
print(a,b)
#rstrip() -->removes trailing characters
print('codegnan--->'.rstrip('--->'))



















