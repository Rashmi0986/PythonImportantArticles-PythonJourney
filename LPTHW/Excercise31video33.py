"""
making Decisions

"""

print("You enter a dark with two doors will you go through the Door1 or Door2 ")

Door =int(input("Enter your Choice"))

#Door = int(Door)
if int(Door) == 1:
    print("There is a giant bear here eating a cheese cake ")
    print("what do you do ")
    print("1. Take the Cake ")
    print("2. Scream at the bear")

    bear = int(input("> "))
    if bear == 1:
        print("the bear eats your face off , good job ")
    elif bear == 2:
        print("the bear eats your legs off , good job ")
    else:
        print(f"Well the Doing {bear} is probbaly off")
        print("Bear runs away")
    
elif Door == 2:
    print("you stare at the endless abyss at  cthulhu's of retina")
    print("1.Blueberries")
    print("2. Yellow Jacket clothes pin ")
    print("3. Understanding revolvers yelling Melodies")
    insanity = int(input("> "))
    if insanity == 1 or insanity == 2:
        print("Your body survivors powered by the mind of jello ")
        print("Good job")
    else:
        print("the insanity rocks into the eyes into a pool of muck ")
        print("good Job")

else:
    print("You stumble around and fall on a knife and die . Good job")





