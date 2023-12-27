import csv


# Read from one file and write other file
with open("sample_data.csv") as source, open("target.csv", "w") as target:
    reader = csv.reader(source)
    writer = csv.writer(target)

    data_list = list(reader)[1:]
    target_list = []
    target_list.append(['Data_value', 'STATUS', 'UNITS', 'Magnitude', 'Subject',
                        'Group'])
    for row in data_list:
        a, b, C, d, E, F, G, H, I, *other = row
        target_row = [C, E, F, G, H, I]
        target_list.append(target_row)

    writer.writerows(target_list)
