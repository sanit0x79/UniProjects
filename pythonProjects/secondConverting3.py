import datetime

def secondsToTime(seconds):
    return str(datetime.timedelta(seconds=seconds))

print(secondsToTime(100000))