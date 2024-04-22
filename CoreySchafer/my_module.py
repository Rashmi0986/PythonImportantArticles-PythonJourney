print("Imported Module")
test = "test_string"

def find_index(to_search, target):
    # find the index of a value in a sequence 
    for i , val in enumerate(to_search):
        if val == target:
            return i 
    return -1

    
