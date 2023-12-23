def EvenNums(num):
    print(num)
    if num % 2 != 0:
        print("Please enter an even number")
    elif num == 2:
        return num
    else:
        return EvenNums(num-2)

EvenNums(8)