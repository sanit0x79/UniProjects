def flipside(s):
    x = len(s) // 2
    return s[x:] + s[:x]

def flipside(s):
    return s[len(s) // 2: + s[:len(s) // 2]


def convert_from_seconds(s):
             """ een getal naar dagen, uren, minuten en seconden
             Zet een getal om naar een lijst van
             [days, hours, minutes, seconds]
             input s: een int
             """
             
             days = s // (24 * 60 * 60)
             s = s  % (24 * 60 * 60)

             hours = s // (60 * 60)
             s = s % (60 * 60)

             minutes = s // 60
             s = s % 60

             return [days, hours, minutes, s]

# Return vs print

def dbl(x):
    return 2 * x
a_dbl = dbl(20) + 20

def dbl_pr(x):
    print(2 * x)
