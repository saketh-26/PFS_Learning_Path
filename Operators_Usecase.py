#Operators usecase -->Student Evaluation Scenario
#Accepting Inputs from the user
name = input("Enter the Student name:")
marks = int(input("Enter the marks:"))
attendance = int(input("Enter the Attendance:"))
subject = input("Enter the Subject:")
#Arithmetic Operators ->Add Bonus
total = marks + 5
#Comparision Operators
passed = total >= 50
#Logical Operators
eligible = passed and (attendance > 75)
#Assignment Opertors
total += 2 #grace marks
#Membership Operators
subjects = ['Maths','Science','English','Telugu']
is_valid = subject in subjects
#Unary Operator
attendance_check = not(attendance < 75)
#Check all the output results
print("Total is :",total)
print(f'Passed : {passed}')
print("Eligible :",eligible)
print("Valid Subject",is_valid)
print(f'Attendance OK,{attendance_check}')





