""" top4talen = ["PHP", "C", "Python", "Java"]

for i in range (len(top4talen)):
	if top4talen[i] =="C":
		top4talen[i] = "C++"
"""
""" 
for i in range (1,101,5):
    print(i) """

""" 
for letter in "Hanze":
    print(letter) """
""" 
list = [5, 20, 32, 2]

for i in range(len(list)):
    list[i] *= 2
print(list) """

list = [5, 20, 30, 2]
sums = []

for i in range(len(list) - 1):
	sums.append(list[i] + list[i+1])

print(sums)