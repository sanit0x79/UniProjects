numbers = [7, 8, 7, 6, 5, 3]

passingGrade = [grade for grade in numbers if grade >= 6] # problem a
average = sum(passingGrade) / len(passingGrade) # problem b

print(average)