S = "time to think this is over! "
result = "" 

for i in range(len(S)):
		if S[i - 1] == " ":
				result += S[i]
print(result) # "t t t t i o! "

