def createPerYearPlot(years, values, xaxis, yaxis, name, output):

    import numpy as np
    import matplotlib.pyplot as plt

    alphab = years
    frequencies = values

    pos = np.arange(len(alphab))
    width = 1.0     # gives histogram aspect to the bar diagram

    plt.figure(figsize=(20,10))
    plt.title('Trawling density for %s' % name )
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(alphab)

    plt.bar(pos, frequencies, width, color='#aaeeff')    
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.savefig(output)
    plt.close()



#createPerYearPlot(['2001', '2002', '2003', '2004', '2005', '2006','2007','2008','2009','2010','2011','2012','2013','2014'],
#                  [23, 144, 112, 11, 202, 210, 23, 144, 112, 11, 202, 210, 150, 97],
#                  "Year",
#                  "Number of tracks within area",
#                  r"c:\temp\test.png") 

import arcpy
input = r"G:\T&P\ANT\MBM\NKG\Mapdata\Brukere\Aasmund\FISHING_DENSITY\TrawlingDataModel.gdb\FISHING_GRID_STAT2"
fields = ['FDIR_2001', 'FDIR_2002', 'FDIR_2003', 'FDIR_2004', 'FDIR_2005', 'FDIR_2006', 'FDIR_2007', 'FDIR_2008', 'FDIR_2009', 'FDIR_2010', 'FDIR_2011', 'FDIR_2012', 'FDIR_2013', 'FDIR_2014', 'FDIR_2015','FDIR_2016']
cur = arcpy.SearchCursor(input, "FDIR_MEAN_8Y > 50")
for c in cur:
          years=[]
          values=[]
          for f in fields:
            if c.getValue(f) == None:
                values.append(0)                
            else:
                values.append(c.getValue(f))
          
            years.append(f.replace("FDIR_",""))
            createPerYearPlot(years,
                  values,
                  "Year",
                  "Number of tracks within area",
                  c.NAME,        
                  r"c:\temp\%s.png" % c.NAME)  
