def createPerYearPlot(years, values, xaxis, yaxis, output):

    import numpy as np
    import matplotlib.pyplot as plt

    alphab = years
    frequencies = values

    pos = np.arange(len(alphab))
    width = 1.0     # gives histogram aspect to the bar diagram

    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(alphab)

    plt.bar(pos, frequencies, width, color='#aaeeff')
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.savefig(output)



createPerYearPlot(['2001', '2002', '2003', '2004', '2005', '2006','2007','2008','2009','2010','2011','2012','2013','2014'],
                  [23, 144, 112, 11, 202, 210, 23, 144, 112, 11, 202, 210, 150, 97],
                  "Year",
                  "Number of tracks within area",
                  r"c:\temp\test.png") 
