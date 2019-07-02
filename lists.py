student_names = ["Mark","Katrina","Jessica"]
print(student_names[0])
student_names[0]="James"
print(student_names[0])
student_names.append("Homer")
print(student_names)
print("Mark" in student_names)
print(len(student_names)) #how many elements

del student_names[2]
print(student_names)
print(student_names[1:]) #list slicing
