def calibrate():
    total = 0
    with open('inputday1.txt', 'r') as file:
        for line in file.readlines(): # reads through the entire file
            digits = [character for character in line.strip() if character.isdigit()] # create a list of digits using list comprehension
            calibration = int(digits[0] + digits[-1]) # convert the first and last digit to an integer and add them together
            total += calibration # add the calibration to the total
    return total

print(calibrate())
