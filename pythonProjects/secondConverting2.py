def amountOfSeconds(seconds):
    minutes, seconds = divmod(seconds,60)
    hours, minutes = divmod(minutes,60)
    days, hours = divmod(hours,24)
    return ("%d Days, %02d Hours, %02d Minutes, %02d seconds" % (days, hours, minutes, seconds))

print(amountOfSeconds(100000))