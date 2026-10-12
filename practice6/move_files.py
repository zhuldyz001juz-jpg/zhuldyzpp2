import shutil
from pathlib import Path

# Create source and destination directories
source_dir = Path("source")
destination_dir = Path("destination")

source_dir.mkdir(exist_ok=True)
destination_dir.mkdir(exist_ok=True)

# Create a sample file
source_file = source_dir / "hello.txt"
source_file.write_text("Hello from Python!", encoding="utf-8")

# Copy file to another directory
copied_file = destination_dir / "hello_copy.txt"
shutil.copy2(source_file, copied_file)
print("File copied.")

# Move file to another directory
moved_file = destination_dir / "hello_moved.txt"
shutil.move(str(source_file), str(moved_file))
print("File moved.")

# Remove an empty directory
empty_dir = Path("empty_folder")
empty_dir.mkdir(exist_ok=True)

if empty_dir.is_dir() and not any(empty_dir.iterdir()):
    empty_dir.rmdir()
    print("Empty directory removed.")