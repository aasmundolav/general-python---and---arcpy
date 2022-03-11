p = arcpy.mp.ArcGISProject("CURRENT")
m = p.listMaps()[0]
l = m.listLayers()[0]

for c in cursor:
    count +=1
    print(count)
    print(c.NAME)
    arcpy.management.SelectLayerByAttribute('pipelines', 'NEW_SELECTION',"NAME = '{0}'".format(c.NAME))
    print("%s pipeline feature selected" % arcpy.GetCount_management('pipelines'))
    arcpy.management.SelectLayerByLocation('tracks', 'INTERSECT', 'pipelines')
    print("%s track features selected" % arcpy.GetCount_management('tracks'))
    arcpy.analysis.Intersect("pipelines #;tracks #", r"D:\Fish_DNVGL\Pipelines.gdb\B{0}".format(count), 'ALL',None, 'POINT')
    print("intersect completed")
