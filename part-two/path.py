# Path
from pathlib import Path


path = Path("part-two/notes.txt")
path.write_text("What's up boys! \nHow are you?")
# path.write_text("How are you?")
# path.unlink()

try:
    print(path.read_text())
except FileNotFoundError:
    print("Oops! File doesn't exist")


print(path.read_text())
