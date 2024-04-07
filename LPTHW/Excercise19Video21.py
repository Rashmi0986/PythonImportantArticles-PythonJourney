def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"you have {cheese_count} cheese")
    print(f"you have {box_of_crackers} boxes of crackers")
    print("Man thats enough for a party")
    print("Get a blanket\n")


print("we can just give the fun. numbers directly")
cheese_and_crackers(20,30)

print("OR we can just use variables fro our scripts")
total_cheese = 10
total_boxes = 20
cheese_and_crackers(total_cheese, total_boxes)

print("we can do even math inside too")
cheese_and_crackers(10+20, 20+50)

print("we can combine the two use variables and do the math")
cheese_and_crackers(total_cheese+20, total_boxes+10)
