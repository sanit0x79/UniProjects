# Schrijf een functie is_palindrome(s) die gebruik maakt van het bovenstaande recursief algoritme

def is_palindrome(s):
    """
    returnt true als het een palindrome is, anders return false
    """

    if s == "":
        return True
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])