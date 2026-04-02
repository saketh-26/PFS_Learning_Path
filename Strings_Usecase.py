'''
Usecase on Strings : UserName Generator
'''
#Accept inputs from the user
full_name = input("Enter the FullName:").strip()
birth_year = input("Enter the Birth Year:").strip()
#Normalize the name
name_clean = full_name.lower().replace(" ","")
print(name_clean)
#Extract the initials
initials = full_name[0].lower() + full_name.split()[-1][0].lower()
print(initials)
#Create multiple username styles
user_name_1 = name_clean + birth_year
user_name_2 = initials + birth_year
user_name_3 = full_name.title().replace(" ","_")+"_"+ birth_year
#print the results
print(user_name_1)
print(user_name_2)
print(user_name_3)







