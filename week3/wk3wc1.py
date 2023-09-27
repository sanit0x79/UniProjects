# Defineer interp, geeft low + high - low terug en vermenigvuldigt hem met fraction
def interp(low, hi, fraction):
    return low + (hi - low) * fraction
    
def test_interp():
    # Test met een lage waarde voor fraction (0)
    assert interp(10, 20, 0) == 10

    # Test met een hoge waarde voor fraction (1)
    assert interp(10, 10, 1) == 10

    # Test met een negatieve waarde voor fraction
    assert interp(-10, 10, 0.25) == -5

    print("Alle testen zijn geslaagd!")

test_interp()