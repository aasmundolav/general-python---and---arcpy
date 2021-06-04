
def getDMS(shape):
    x = 48.123456
    d = int(x)
    m = int((x - int(x))*60)
    s = int((((x - int(x))*60) - int((x - int(x))*60))*60)
    return "%s %s %s " % (d,m,s)
