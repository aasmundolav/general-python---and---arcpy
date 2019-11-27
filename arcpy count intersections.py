## TRIAL TEST THAT WORKED IN PYTHON INSIDE ARCMAP:

t='tracks'
c='fishnet'

fc = arcpy.UpdateCursor(c)
count = 0
for f in fc:
    arcpy.SelectLayerByAttribute_management(c,"NEW_SELECTION", '"OID" = %s' % f.OID)
    arcpy.SelectLayerByLocation_management(t, "INTERSECT", c,"","NEW_SELECTION")
    result = arcpy.GetCount_management(t).getOutput(0)
    count+=1
    print "%s number of intersections: %s" % (count, result)
    f.CountAll_2018 = result
    fc.updateRow(f)
    
    


## please use a copy of grid ##

polygonGrid = '"c:\\"
arcpy.descibe(polygonGrid)
## Print number of selected features.

layers=

## Print number of layers. Print layer names.
for l in layers:
    if 


fc = arcpy.UpdateCursor(c)
count = 0
for f in fc:
    if f.OBJECTID < 370:
        continue
    arcpy.SelectLayerByAttribute_management("EuropipeSegments","NEW_SELECTION", '"OBJECTID" = %s' % f.OBJECTID)
    arcpy.SelectLayerByLocation_management("AISLines", "INTERSECT", "EuropipeSegments","","NEW_SELECTION")
    result = arcpy.GetCount_management("AISLines").getOutput(0)
    count+=1
    print "%s number of intersections: %s" % (f.OBJECTID, result)
    f.CROSSINGNU = result
    fc.updateRow(f)
