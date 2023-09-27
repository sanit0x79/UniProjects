seconds = int(input("How many seconds do you want to convert: "))
              
def secondsToTime(seconds):
    minutes, seconds = divmod(seconds,60)
    hours, minutes = divmod(minutes,60)
    days, hours = divmod(hours,24)
    return ("%d Days, %02d Hours, %02d Minutes, %02d seconds" % (days, hours, minutes, seconds))

print(secondsToTime(seconds))
