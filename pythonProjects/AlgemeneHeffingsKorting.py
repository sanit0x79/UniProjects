inkomen = int(input("Voer belastbaar inkomen in: "))

if inkomen < 22661:
    ahk = (3070)
elif inkomen in range(22661, 73031):
    ahk = (3070 - 0.06095 * (inkomen - 22660))
elif inkomen >= 73031:
    ahik = (0)
print ("Uw algemene heffingskorting is: %.2f " % float(ahk))
