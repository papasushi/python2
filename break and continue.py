student_names = ["James","Katrina","Jessica","Mark","Bort","Frank Grimes","Max Power"]

for name in student_names:
    if name =="Mark":
        print("found him! " + name)
        break
    print ("Currently testing " + name)


student_names = ["James","Katrina","Jessica","Mark","Bort","Frank Grimes","Max Power"]

for name in student_names:
    if name =="Bort":
        continue
        print("found him! " + name) #this code is not executed
        break
    print ("Currently testing " + name)