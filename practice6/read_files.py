from pathlib import Path

file = Path("example.txt")

file.write_text("Hello Python!\nI am learning file handling.", encoding="utf-8")

# Read the whole file
with open(file, "r", encoding="utf-8") as f:
    print("Read all:")
    print(f.read())

# Read one line
with open(file, "r", encoding="utf-8") as f:
    print("Read one line:")
    print(f.readline())

# Read all lines as a list
with open(file, "r", encoding="utf-8") as f:
    print("Read lines:")
    print(f.readlines())