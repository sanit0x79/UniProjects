# A
def count_char(zin , let):
   lc = [1 for x in zin if x == let] 
   return sum(lc)


# C
def max_freq_letter(z):
   a = "abcdefghijklmnopqrstuvwxyz"
   max_letter = a[0]
   for x in a:
      if count_char(z, max_letter) < count_char(z, x):
         max_letter = x
   return max_letter