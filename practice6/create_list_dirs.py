import os
from pathlib import Path

# Create nested directories
Path("data/documents").mkdir(parents=True, exist_ok=True)
print("Directories created.")

# Show the current directory
print("Current directory:", os.getcwd())

# List all files and folders
print("All items:", os.listdir("."))

# List only directories and files
for item in Path(".").iterdir():
    if item.is_dir():
        print("Directory:", item.name)
    elif item.is_file():
        print("File:", item.name)

# Find text files
print("Text files:")
for file in Path(".").glob("*.txt"):
    print(file.name)

# Check path permissions
path = Path("example.txt")

print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

# Find filename and directory portion
if path.exists():
    print("Filename:", path.name)
    print("Directory:", path.parent)

# Generate 26 files: A.txt to Z.txt
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    Path(letter + ".txt").touch()

print("26 files created.")