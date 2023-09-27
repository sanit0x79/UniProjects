price = int(input("What is the price of the product: "))

if price >= 300:
    output = (price - (price * 0.3))
elif price in range (199, 300):
    output = (price - (price * 0.2))
elif price in range (99, 200):
    output = (price - (price * 0.1))
else:
    output = price

print(output)
