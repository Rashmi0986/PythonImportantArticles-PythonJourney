from sys import argv 
script , input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

cur_file = open(input_file)

print("first lets print the whole file content ")
print_all(cur_file)

print("now Lets rewind a file kind of tape")
rewind(cur_file)

print("Now lets print the content line by line")
cur_line = 1
#print("cur_line : 1 ")
print_a_line(cur_line,cur_file)
cur_line+=1
print_a_line(cur_line,cur_file)

cur_line+=1
print_a_line(cur_line,cur_file)

#google python +=


    