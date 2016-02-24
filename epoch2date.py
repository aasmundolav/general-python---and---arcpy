import time
def date2epoch(i):
    if i > 12:
        e = time.strptime(input, "%d.%m%.%Y %H.%M.%S")
    if i < 12:
        e = time.strptime(input, "%d.%m.%Y")
    return time.mktime(e)

def epoch2date(i):
    e = time.strftime("%d.%m%.%Y %H.%M.%S",time.gmtime(i))
    return e
        
