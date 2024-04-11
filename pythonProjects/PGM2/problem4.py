def number_stairs(size):
    for rij in range(size + 1):
        for kolom in range(1, rij+1):
            print(str(kolom), end = " ")
        print()
    print()

number_stairs(5)
number_stairs(3)