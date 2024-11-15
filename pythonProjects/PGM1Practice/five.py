i = 0

def number_stairs(i):
    for y in range(1, i+1):
        for x in range(1, y+1):
            print(x,end="")
        print()
number_stairs(5)
