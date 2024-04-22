Student = {'name': 'John',
           'age': 25,
           'Courses': ["math", "compSc"]
           }
"""
print(Student['name'])
print(Student['Courses'])
print(Student['age'])
"""
print(Student.get("name"))

print(Student.get("Phone")) # just returns None 

print(Student.get("Phone", "Not Found")) # can be written this way as well 

#print(Student["Phone"]) returns Error ====> Keyerror: 'Phone'

#update oepration - update can be add , remove or overwrite existing values 
Student.update({"Phone": '5555-555'})

print(Student.items())

print(len(Student))

print(Student.keys())
print(Student.values())

for k , v in Student.items():
    print(f"{k} : {v}")






