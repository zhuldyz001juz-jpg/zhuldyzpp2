import shutil
from pathlib import Path

source = Path("notes.txt")
backup = Path("notes_backup.txt")

# Check if the source file exists
if source.exists():
    # Copy the file
    shutil.copy2(source, backup)
    print("File copied successfully!")

# Check if the backup exists
if backup.exists():
    print("Backup file exists.")

# Count lines in the file
if source.exists():
    with open(source, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("Number of lines:", len(lines))

# Delete the backup file safely
if backup.exists() and backup.is_file():
    backup.unlink()
    print("Backup file deleted.")