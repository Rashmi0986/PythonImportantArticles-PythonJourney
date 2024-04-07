def print_two(*args):
    arg1 , arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def two_args_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")

print_two("Zed", "Shaw")
print_one("zed")
two_args_again("Hello","Test")
print_none()


