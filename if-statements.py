number=5
if number:
    print("number is defined and truthy")

text = "Python"
if text:
    print("test is defined and truthy")

python_course = True
if python_course:
    print("this will execute")

aliens_found = None
if aliens_found:
    print("this will NOT execute")

number=5
if number != 5:
    print("this will not execute")

python_course = True
if not python_course:
    print("this will also not execute")

number = 3
python_course=True
if number == 3 and python_course:
    print("this will execute")
if number == 17 or python_course:
    print ("this will also execute")

a=1
b=2
print ("bigger" if a > b else "smallers")
