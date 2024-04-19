""""
Try and except in the video 




try:
    pass
except Exception:
    pass


try:
    f = open("test.txt")
except FileNotFoundError as e:
    #print("file not found error ")
    print(e)
except Exception as e:
    print(e)
else:
    #pass
    print(f.read())
    f.close()
"""
#Interview question 
try:
    f = open("test_1.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    #f.close() #throws --> nameerror:%20name%20'f'%20is%20not%20defined
    print("Executing finally block")

try:
    f = open("test_1.txt")
    raise Exception #manually raising exception 
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error!")
finally:
    print("Executing finally block")







