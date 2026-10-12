# enumerate example
students = ["Aliya", "Malia", "Dana"]

for index, student in enumerate(students):
    print(index, student)

print("Starting from 1:")

for index, student in enumerate(students, start=1):
    print(index, student)

# zip example
names = ["Aliya", "Malia", "Dana"]
grades = [90, 85, 95]

for name, grade in zip(names, grades):
    print(name, grade)

# Convert zip into a list of pairs
pairs = list(zip(names, grades))
print("Pairs:", pairs)

# Sort numbers in descending order
numbers = [3, 1, 5, 2, 4]
print("Descending:", sorted(numbers, reverse=True))