from sys import argv
script , username = argv
prompt = '> '

print(f"Hi {username}, I'm the {script}")
print("I would like to ask you few questions")

print(f"Do you like me {username} ?")
likes = input(prompt)
print(f"where do you live {username}")
location = input(prompt)

print("What kind of computer you have ")
computer= input(prompt)

print(f"""
Alright so you said {likes} likes about me,
and you are located at {location},
you have {computer}
      """)




