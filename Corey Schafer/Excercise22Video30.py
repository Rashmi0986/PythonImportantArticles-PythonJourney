"""
Regular expressions
"""
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
"""
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)


sentence = 'Start a sentence and then bring it to an end'

#print('\rtab')
pattern = re.compile("abc")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

sentence = 'Start a sentence and then bring it to an end'

#print('\rtab')
pattern = re.compile(r"\.")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


pattern = re.compile(r"\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


pattern = re.compile(r"\D")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern = re.compile(r"\w")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)



pattern = re.compile(r"\W")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


pattern = re.compile(r"\s")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

 
pattern = re.compile(r"\S")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


pattern = re.compile(r"\S")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)


pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
matches = pattern.finditer(text_to_search)
with open("Excercise22Video30.txt", 'r') as f:
    contents = f.read()
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)


"""
#import re
#sentence = "Start a sentence and bring it to the end "
sentence = '''
cat 
mat
sat
'''
pattern = re.compile(r'[^b]at')

matches = pattern.finditer(sentence)
for match in matches:
    print(match)
