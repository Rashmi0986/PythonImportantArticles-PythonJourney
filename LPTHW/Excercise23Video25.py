import sys

script , input_encoding , error = sys.argv

def main(language_file, encoding , error):
    line = language_file.readline()
    if line:
        print_line(line , encoding, errors = error)
        main(language_file, encoding, error)
    

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = error)
    cookedStr = raw_bytes.decode(encoding, errors = error)
    print(f"raw_bytes:{raw_bytes}, cookedStr:{cookedStr}")

# was passing the languages.txt  in the Cmdline arguement which was wrong. 
# Need to pay attention to the every line of code i type here 
languages = open("languages.txt")

main(languages, input_encoding, error)

# cmd to run this script >>>>> python Excercise23Video25.py utf-8 test
