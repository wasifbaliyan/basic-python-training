# Path
from pathlib import Path


path = Path("my_notes.txt")
path.write_text("What's up boys! \nHow are you?")
# path.write_text("How are you?")
# path.unlink()
# print(path.stat())
# path.rename("my_notes.txt")


try:
    print(path.read_text())
except FileNotFoundError:
    print("Oops! File doesn't exist")


print(path.read_text())
print(Path.home())


# Directories

# path = Path("part-one")
# print(path.exists())
# print(path.is_dir())
# python_files = [p for p in path.glob("*.py")]
# print(python_files)
