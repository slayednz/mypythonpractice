import csv

name = input("what's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

students = []

with open("students.csv") as file:
    read = csv.DictReader(file)
    for row in read:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

