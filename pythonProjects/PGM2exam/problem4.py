def half_m_table(size):
    for rij in range(1, size + 1):
        for kolom in range(1, rij + 1):
            print(str(kolom * rij) + " ", end="")
        print()

half_m_table(5)