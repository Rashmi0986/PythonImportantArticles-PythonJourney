# reading and writing files 
from sys import argv 
script , filename = argv

print(f"We are going to erase {filename}")
print("if you dont want that hit ^C ")
print("if you do want that hit return")

input("?")
print("opening the file ")

target = open(filename, "w")

print("Truncating the filename , Goodbye")
target.truncate()

print("Now am going to ask you for three lines")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("am, going to write this to files ")
target.write(f"{line1}\n{line2}\n{line3}")

target.close()

print("printing the written data ")
txt = open(filename)
print(txt.read())
txt.close()