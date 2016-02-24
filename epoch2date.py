import time
def date2epoch(i):
    if len(i) > 12:
        e = time.strptime(i, "%d.%m.%Y %H.%M.%S")
    if len(i) < 12:
        e = time.strptime(i, "%d.%m.%Y")
    return time.mktime(e)

def epoch2date(i):
    e = time.strftime("%d.%m%.%Y %H.%M.%S",time.gmtime(i))
    return e
        
