import csv

# Write
with open("data.csv", "w") as f:
    writer = csv.writer(f)

    writer.writerow(["Name", "Age", "Education"])
    writer.writerow(["John", "23", "Graduate"])
    writer.writerow(["Jake", "26", "PG"])

# Read
with open("data.csv") as file:
    reader = csv.reader(file)
    rows = list(reader)[1:]

    total_age = 0
    for row in rows:
        print(row)
        total_age += int(row[1])

    print(total_age//len(rows))
