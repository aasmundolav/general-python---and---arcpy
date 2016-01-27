
##Create list
list =[]

##Open Feature class (FC)
li = arcpy.SearchCursor(r'\\statoil.net\dfs\common\G\ST_GIS_Data_01\RasterData\Bathy_Images\TEST2\SurveyStillPictures.gdb\SurveyStillPictures_Center')

## Iterate FC add to list
for l in li:
  list.append([l.name, 1])

## Create Sort-key by column function (sorts by first colum)
def getkey(item):
  return (item[0])
  
## Sort and count and add to 2nd column

newlist = sorted(list, key=getkey)
count = 0
for n in newlist:
     count +=1
     n[1] = count
     
uli = arcpy.UpdateCursor(r'\\statoil.net\dfs\common\G\ST_GIS_Data_01\RasterData\Bathy_Images\TEST2\SurveyStillPictures.gdb\SurveyStillPictures_Center')
for u in uli:
     for n in newlist:
         if n[0] == u.name:
             u.SEQ = n[1]
             break
    uli.updaterow(u)
