def demo(x):
    y = x/3
    z = g(y)
    return z + y + x

def g(x):
    result = 4*x +2
    return result

print (demo(5))
