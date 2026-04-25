#Smart Enrollement System -->Students,Courses...
#Raw student data (with duplicates)

students = ['Ram','Sita','Ram','Krishna','Sita']
print(students)
#Remove duplicates using set
unique_students = set(students)
print(unique_students)
#Assign default course using fromkeys
course_map = dict.fromkeys(unique_students,'Python_Programming')
#print(course_map)
#Add a new student manually
course_map['Arjun'] = "Data Science"
#print(course_map)
#Ass multiple students at once using update()
course_map.update({'Meena':'AI',
                   'Raghav':'Java'})
#print(course_map)
#Create another set of students (new batch)
new_batch = {'Kiran','Sita','Arjun'}
#Perform Set Operations
all_students = unique_students.union(new_batch)
print(all_students)
common_students = unique_students & new_batch
print(common_students)
#create mapping for new batch and merge using update
new_course_map = dict.fromkeys(new_batch,"Machine Learning")
print(new_course_map)
course_map.update(new_course_map)
#remove a student using pop
removed_student = course_map.pop("Kiran")
#Copy of dictionary (backup case)
back_up = course_map.copy()
#Final Outputs:
print(f'All Students (Union) : {all_students}')
print(f'Common Students (Intersection):{common_students}')
print(f'\nUpdated Course map: {course_map}')
print(f'\nRemoved Students :{removed_student}')
print(f'\nBackup copy')
print(back_up)















