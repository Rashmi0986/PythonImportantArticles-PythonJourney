# file objects 
"""
f = open("test.txt",'r')
print(f.readline())
print(f.name)
print(f.mode)
f.close()
"""
# context manager example 
#Noted : mode shpuld be closed in the single quotes - made mistake twice
"""
with open("test.txt", 'r') as f:
    print(f.readlines())

print(f.closed)

with open("test.txt", 'r') as f:
    fcont = f.readline()
    print(fcont)
    fcont = f.readline()
    print(fcont)


with open("test.txt", 'r') as f:
    for line in f:
        print(line)

        
with open("test.txt") as f:
    fcont = f.read(10) # reads just first 10 charecters
    print(fcont, end="")



with open("test.txt", 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end="")
        f_contents = f.read(size_to_read)

# Suppose if you want to add any charecter post reading certain length of the charecter 
# then use the end = "*"
# check the example below 
with open("test.txt", 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end="**")
        f_contents = f.read(size_to_read)

#output looks like this 

1.hello fi**le object **example in** CS folder** 
2.file w**ith a mult**iple lines** of data 


with open("test.txt") as f:
    fcont = f.read(10) # reads just first 10 charecters
    print(fcont, end="***")
    
    f.seek(0)

    fcont = f.read(10) # reads just first 10 charecters
    print(fcont, end="***")


#with open("test_with_write.txt",'w') as f:
    #f.write("Writing this line here ")

with open("test_with_write.txt",'r') as f:
    fcont = f.readline()
    print(fcont)



with open("test.txt", 'r') as rf:
    with open("test_copy.txt", 'w') as wf:
        for line in rf:
            wf.write(line)
        #fcont = rf.readline()
        #wf.write(fcont)

with open("test_copy.txt",'r') as f:
    fcont = f.readline()
    print(fcont)

    """

# Copying a JPG file - Just test that - havent tested the below code 
with open("dog.jpg", 'rb') as rf:
    with open("dog_copy.jpg", 'wb') as wf:
        chunkSize = 4096
        rf_chunk = rf.read(chunkSize)
        while len(rf_chunk) > 0 :
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunkSize)








    



