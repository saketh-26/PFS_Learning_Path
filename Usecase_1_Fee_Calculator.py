'''
Fee Calculator -->Use input() for various inout types and also print()
'''
#Get Student details
name = input("Enter the Student Name:")
place = input("Enter the place")
age = int(input("Enter the age:"))
course = input("Enter the Department")
#accept the fee details
admission_fees = float(input("Enter the Admission Fees:"))
tuition_fees = float(input("Enter the Tuition Fees:"))
hostel_fees = int(input("Enter the Hostel Fees:"))
#Calculate the Fees
total_fees = admission_fees + tuition_fees + hostel_fees
#print() -->output engine
print("---------------------->")
print("Student Details are :",name,place,age,course,sep='\t')
print(f"Admission Fees is {admission_fees}")
print("Tuition Fees is {}".format(tuition_fees))
print(f'Hostel Fees is {hostel_fees}')
print('------------------')
print(f'Total Fees is {total_fees}')









