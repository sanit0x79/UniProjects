# A
def count_char(zin , let):
   lc = [1 for x in zin if x == let] 
   return sum(lc)

print(count_char("ASHJDKJHASDJLKAuEAHWJCJNACuASEJKndasdj", "N"))

# C
def max_freq_letter(z):
   a = "abcdefghijklmnopqrstuvwxyz"
   max_letter = a[0]
   for x in a:
      if count_char(z, max_letter) < count_char(z, x):
         max_letter = x
   return max_letter

# B
# Je gebruikt een for loop om door elke letter van het alfabet te itereren, je start met de string a="alfabet hier"
# dan maak je een variabele aan voor de max voorkomende letter, in dit geval is dit a[0], aan het einde van de loop return je de max letter
# als het aantal voorkomens van x groter is dan dat van max_letter, dan wordt max_letter bijgewerkt naar x 
#
#
