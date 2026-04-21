#Usecase -->Shopping Cart Update
#Users with their carts (tuple :name,list of items)

Users = [('Saketh',['Laptop','Mouse']),
          ('Rahul',['Phone'])]
print(Users)
print(len(Users))
#Working on Saketh's cart
print(Users[0])
print(Users[0][1])

cart = Users[0][1]
cart.append("Keyboard") #add one item
cart.extend(['USB','Headset']) #adding multiple items
#print(cart)
cart.insert(1,'Tablet')  #insert at specific position
#print(cart)
cart.remove("Mouse") #remove specific item
#print(cart)
removed_item = cart.pop() #remove last item
first_item = cart.pop(0) #remove first item
#print(cart)
cart.sort() #sort items
#print(cart)
cart.reverse() #reverse order
#print(cart)
count_usb = cart.count("USB") #count occurances
index_item = cart.index("Keyboard") #find position

#Fetch all the results
print("Final Cart:",cart)
print("Removed Last:",removed_item)
print("Removed First:",first_item)
print("USB Count:",count_usb)
print("Keyboard Position:",index_item)
print("All Users :",Users)














