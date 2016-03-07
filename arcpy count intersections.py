fc = arcpy.UpdateCursor("EuropipeSegments_Update")
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
