def f(x):
    if x == 0:
        return 12
    else:
        return f(x-1) + 10*x
    
print (f(2))
