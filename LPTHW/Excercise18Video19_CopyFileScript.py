#more files 

from sys import argv 
from os.path import exists

script , from_file , to_file = argv

print(f"copying {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()

print(f"the input file is len(in_data) long")
print(f"Does the output file exist {exists(to_file)}")
print("Ready Hit return or abort")

input()

out_file = open(to_file, 'w')
out_file.write(in_data)
out_file.close()

print("Alright All done!! below is the Contents written \n ")
outObj = open(to_file)
out_data = outObj.read()
print(out_data)

out_file.close()
in_file.close()
