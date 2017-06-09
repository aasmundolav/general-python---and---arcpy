def getmean(xs):
    mean = 0
    for x in xs:
        if x > 0:
            mean += x
        else:
            mean += 0
    return mean/len(xs)
    
    getmean([!attribute!, !attribute!,!attribute!,!attribute!])
