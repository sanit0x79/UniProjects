L = []
for x in range(10):
    row = []
    for y in range(10):
        row = row + [x*y]
    print(row)


l = ""
count = 0
for x in range(5):
    row = " "
    for y in range(5):
        row = row + " " + str(x * y)
        count += x * y
    print(row)
print("Total sum:", count)