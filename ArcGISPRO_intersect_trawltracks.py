#'pipeline' is name of layer with pipeline with KP values
#'tracks' is name of layer with all line tracks that crosses (KP value not required)

outputFGB=r"D:\Fish_DNVGL\Pipelines.gdb"


p = arcpy.mp.ArcGISProject("CURRENT")
m = p.listMaps()[0]
l = m.listLayers()[0]

cursor = arcpy.SearchCursor('pipelines')
count=0
for c in cursor:
    count +=1
    print(count)
    print(c.NAME)
    arcpy.management.SelectLayerByAttribute('pipelines', 'NEW_SELECTION',"OBJECTID_1 = '{0}'".format(c.OBJECTID_1))
    print("%s pipeline feature selected" % arcpy.GetCount_management('pipelines'))
    arcpy.management.SelectLayerByLocation('tracks', 'INTERSECT', 'pipelines')
    print("%s track features selected" % arcpy.GetCount_management('tracks'))
    arcpy.analysis.Intersect("pipelines #;tracks #", r"D:\Fish_DNVGL\Pipelines.gdb\B{0}".format(count), 'ALL',None, 'POINT')
    print("intersect completed")
