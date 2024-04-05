formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one" , "two", "three", "four"))
print(formatter.format(True, False, False, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your own text here ",
    "May be a Poem",
    "or a song",
    "which excites you"
))
