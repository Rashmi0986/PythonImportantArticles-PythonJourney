# reading files 
from sys import argv 

# collect the variables provided in the command line 
script , filename = argv 

# open the file name using open()
txt = open(filename)

# print the filename 
print(f"here is your {filename}")

# read file name here
print(txt.read())
#close the reader here 
txt.close()
# Try reading any other filename here
print("type the filename again ")
prompt = "> "
file_again = input(prompt)
txt_again = open(file_again)


print(txt_again.read())

#close the file here 
txt_again.close()

