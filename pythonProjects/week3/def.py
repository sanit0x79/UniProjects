def flipside(s):
    """flipside(s): spiegel s!
    input s: een string
    """

    x=len(s) // 2
    return s [x:] + s [:x]
print (flipside("automaat"))
