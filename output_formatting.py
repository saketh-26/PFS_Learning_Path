'''
print() function -->It is basically used to display the output such as numbers,
text or any other datatype to the console

#Printing text
print("Hello Codegnan!")
print("Hello Codegnan,this is Saketh")

#printing multiple items
name = "Codegnan"
place = "Hyderabad"
print(name,place)
print("Name:",name,"Place:",place)

#using sep to change the separator

print("2026","03","08") #default space
print("2026","03","08",sep='-')
print("2026","03","08",sep='/')

#Using end to control line endings
print("Hello Codegnan")
print("This is Saketh from Hyderabad")

print("Hello Codegnan",end='')
print("This is Saketh from Hyderabad")
print("Hello Codegnan",end=' ')
print("This is Saketh from Hyderabad")
print("Hello Codegnan",end='\t')
print("This is Saketh from Hyderabad")

#Output Formatting
#Using commas (simple print method)
name="Codegnan"
place = "Hyderabad"
age = 7
print("Name:",name,"Place:",place,"Age:",age)
print("---",name,"****",place,"###",age)

#Using Modulus (%) Operator (%formatting)
#%d -->integer,%s-->string,%f --->float
name = "Sunny"
age = 32
score = 95.35
#Using Modulus operator
print("%s %d %f"%(name,age,score))
print("%s %d %.f"%(name,age,score))
print("Name : %s | Age : %d | Score : %.2f"%(name,age,score))


#Using str.format() method -->we use {} as placeholders,.format() to store the
#variables

name = "Codegnan"
place = "Vijaywada"
age = 7
marks = 89.456
print("{}".format(name))
print("Name : {} | Age : {} |Place : {}".format(name,age,place))
print("{}".format(marks))
print("{:.1f}".format(marks)) #{:.1f} -->formats the marks with 1 decimal place
'''

#using f-strings (Most recommended)
name = "Codegnan"
place = "Vijaywada"
print(f'{name} is in {place}')
print(f'{name} is in {place} and also in Hyderabad & Vizag')

















