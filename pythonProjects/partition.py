def partitions(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return partitions(n - m, m) + partitions(n, m - 1)


print(partitions(7, 4))
