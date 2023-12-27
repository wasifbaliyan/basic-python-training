person = {
    "name": "John",
    "age": 24,
    "country": "UK"
}

point = dict(x="a", y="b")

point["z"] = "c"
del point["x"]
print(point)

for key in person:
    print(key, person[key])


if "work" in person:
    print(person["work"])

print(person.get("work", 0))

for key, value in person.items():
    print(key, value)
