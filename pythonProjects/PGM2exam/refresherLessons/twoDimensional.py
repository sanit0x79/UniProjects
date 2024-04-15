count = 1
l = []

for i in range (0,3):
    row = []
    for i in range (0,3):
        column = []
        row.append(count)
        count += 1
    l.append(row)

print(l)


# Correct solution:

def create_a():
    counter = 1
    table = []

    for x in range (0,3):
        rows = []
        for y in range (0,3):
            column = []
            rows = rows + [counter]
            # or row.append(counter)
            counter += 1
        table = table + [rows]
        # or table.append(rows)
    return table

print(create_a())
