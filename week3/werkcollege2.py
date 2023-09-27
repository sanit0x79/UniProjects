def main():
    print(dbl(21))
    print(dbl("wauw!"))
    
def testing():
    assert dbl(21) == 42
    
def dbl (x):
    return 2 * x

main()
testing()
