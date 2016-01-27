## Attributes: FIELDNAME, CURRENTLIC
## CURRENTLIC has a list of items seperated by comma.

## SCRIPT COPIES GEOMETRY FOR EACH ITEM IN CURRENTLIC.

##Before:
##[NAME], [PL1, PL2, PL3],[GEOMETRY]

##After:
##[NAME], [PL1], [GEOMETRY]
##[NAME], [PL2], [GEOMETRY]
##[NAME], [PL3], [GEOMETRY]

## SCRIPT SAMPLE CREATED USING ARCGIS 10.2


searchC =  arcpy.da.SearchCursor("DECC_OFF_Hydrocarbon_Fields", ("FIELDNAME","CURRENTLIC","SHAPE@")) #plus other attribute if you need
insertC = arcpy.da.InsertCursor("NewFeatureClass", ("FIELDNAME","CURRENTLIC","SHAPE@")) 
for row in searchC:
    A = row[1].split(",")
    print A
    for i in range(0,len(A)):
        newRow = [row[0] , A[i], row[2]]
        insertC.insertRow(newRow)
