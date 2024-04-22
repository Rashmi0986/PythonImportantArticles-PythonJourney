from sys import exit


def gold_room():
    print("this room is full of gold how much you take ")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("!! man learn to type number")
    
    if how_much < 50:
        print("nice you are not greedy !! you win!")
        exit(0)
    else:
        dead("You greedy ")

def bear_room():
    print("There is a bear here ")
    print("the bear has bunch of hoeny ")
    print("The fat bear is in front of door")
    print("how are you going to move to the bear")
    bear_moved = False
    # added this fix to make it clear to the user

    print("Select from the below Choices\n1.take honey\n2.taunt bear\n3.open door\n")
    while True:
        choice = int(input("> "))
        #if choice == "take honey":
        if choice == 1:
            print("the bear looks at you and slaps at you on face")
        #elif choice == "taunt bear" and not bear_moved:
        elif choice == 2 and not bear_moved:
            print("bear has moved from the door")
            print("you can go through it now ")
            bear_moved = True
        elif choice == 2 and bear_moved:
            dead("the bear gets pissed off and chews your leg off")
        elif choice == 3 and bear_moved:
            gold_room()
        else:
            print("I've got no idea what that means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
start()       





