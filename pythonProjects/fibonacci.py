def Fibonacci(i):
    if i <= 1:
        return i
    else:
        return Fibonacci(i - 1) + Fibonacci(i - 2)
    
print(Fibonacci(8))
