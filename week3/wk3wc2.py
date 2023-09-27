def sayHello():
    print("Hello")
    
def bedragIncBtw(bedrag):
    return bedrag * 1.21


teBetalen = bedragIncBtw(100)
print(teBetalen)


def main():
    totaalFactuur = 0
    totaalFactuur = totaalFactuur + bedragIncBtw(100)
    totaalFactuur = totaalFactuur + bedragIncBtw(250)
    print(totaalFactuur)
    
    sayHello()

main()
