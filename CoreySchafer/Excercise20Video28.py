import csv

"""





with open("Excercise20Video28.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)


with open("Excercise20Video28.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line[2])
        print(line[0]) # added by me to play around with it 




with open("Excercise20Video28.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open("new_names_Ex20_Video28.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t",)
        for line in csv_reader:
            csv_writer.writerow(line)


with open('Excercise20Video28.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['email'])

"""
with open('Excercise20Video28.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('Excercise20Video28_New_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
        