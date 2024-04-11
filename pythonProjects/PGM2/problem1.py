L = [
    ["0308230", 7.6, True],
    ["8273927", 5.1, False],
    ["8234987", 6.4, False],
    ["2368612", 5.9, True],
    ["9731827", 3.2, False]
]

#HW = [[x[0], x[1]+ 0.5] for x in L if x[2] == True]

#print(HW)
HW = []
for x in L:
    if x[2] == True:
        HW += [x[0], x[1]+0.5]
