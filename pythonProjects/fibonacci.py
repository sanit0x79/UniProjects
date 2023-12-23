def Fibonacci(index):
    if index <= 1:
        return index
    else:
        return Fibonacci(index - 1) + Fibonacci(index - 2)
    
print(Fibonacci(8))