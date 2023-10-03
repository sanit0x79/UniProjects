"""
def blaat(s):
    if len(s) == 1: # Stops the program from stackoverflowing
        return
    print(s[0])
    print(s[:1])
    
blaat("test")

def blaat(x, y):
    return x + y

print(blaat("test", "hanze"))
"""

def blaat(x, y):
    if x < y:
        z = x + 10
    else:
        z = y + 10
        return z
    
print(blaat(5,15))