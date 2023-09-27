def amountOfSeconds(seconds):
    minutes = seconds // 60
    hours = seconds // 3600
    days = seconds // 86400
    seconds = seconds % (24 * 3600) # 24*3600 since one hour has 3600 seconds and one day has 24 hours.
    seconds %= 60
    minutes %= 60
    hours %= 24
    #return("%d Days : %02d Hours : %02d Minutes : %02d Seconds " % (days, hours, minutes, seconds))
    return[days, hours, minutes, seconds]
print(amountOfSeconds(60))

"""  
seconds = 60
minutes = seconds // 60
hours = seconds // 3600
days = seconds // 86400
seconds = seconds % (24 * 3600)
seconds %= 60
minutes %= 60
hours %= 24
print("%d Days : %02d Hours : %02d Minutes : %02d Seconds " % (days, hours, minutes, seconds))
print(type(days))
"""
"""
import datetime

def amountOfSeconds(seconds):
    return str(datetime.timedelta(seconds = seconds))
"""