# Write new content
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("My first file\n")
    f.write("I study Python\n")

# Append new content
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("This is a new line\n")

# Write a list to a file
fruits = ["Apple", "Banana", "Orange"]

with open("fruits.txt", "w", encoding="utf-8") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

# Read and check the results
with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("fruits.txt", "r", encoding="utf-8") as f:
    print(f.read())