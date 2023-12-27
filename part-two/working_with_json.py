import json
from pathlib import Path


# movies = [
#     {
#         "title": "Gadar",
#         "year": 1992,
#         "rating": 3.5,
#     },
#     {
#         "title": "DDLJ",
#         "year": 1995,
#         "rating": 4.5,
#     }
# ]

# Write json to file
# data = json.dumps(movies)
# path = Path("movies.json")
# path.write_text(data)
# print(data)


# Read json
path = Path("movies.json")
data = path.read_text()
movies = json.loads(data)
print(movies)
