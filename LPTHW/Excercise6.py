types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"

y = f"Those who knows {binary} those who {do_not}"

print(x)
print(y)

#Solution suggested to avoid the mistake of skipping f in print - Re-read the code 
print(f"I said {x} ")
print(f"I said {y} ")

hilarious = False
joke_evaluation = "Isn't that joke too funny !!!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with the right side ..."

print(w+e)

