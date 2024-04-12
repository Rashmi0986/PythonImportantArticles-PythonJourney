def break_words(stuff):
    """This function will break words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words here """
    return sorted(words)


def print_first_word(words):
    """prints the first word here"""
    word = words[0]
    print(word)
    word = words.pop()
    print(word)

def print_last_word(words):
    """prints the last word here """
    print(words.pop(-1))

def sort_sentence(sentence):
    """Takes in a full Sentence and returns the sorted words """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Takes in a full Sentence and returns the first and last words """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_last_sorted(sentence):
    """Takes in a full Sentence and returns the first and last words in the sorted order """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


#To cehck the doc strings try the below steps from the terminal 
"""
Excercise25Video27.py
1.Type python from the teminal 
2. help('Excercise25Video27')

also we can check this 
2. help('Excercise25Video27.break_words')

quit()
to get out of python terminal 

"""
