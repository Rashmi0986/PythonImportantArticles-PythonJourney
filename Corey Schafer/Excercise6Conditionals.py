"""
Temp = False
if Temp:
    print("Conditionals was True")
else:
    print("Conditionals is False")



Language = "Java"
if Language == "Java":
    print("Language is Java")
elif Language == "Python":
    print("Language is Python")
else:
    print("No match Found")

user = "Admin"
#logged_in = False
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
"""
temp = [1,2,3]
b = temp 
listid = id(temp)
print(listid)
print(id(temp) == id(b))
