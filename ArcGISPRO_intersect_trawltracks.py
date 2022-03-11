p = arcpy.mp.ArcGISProject("CURRENT")
m = p.listMaps()[0]
l = m.listLayers()[0]

for c in cursor:
    count +=1
    print(c.NAME)
    l.definitionQuery = "NAME = '{0}'".format(c.NAME)
    arcpy.management.SelectLayerByAttribute('pipelines', 'NEW_SELECTION',"NAME = '{0}'".format(c.NAME))
    print("pipeline feature selected")
    arcpy.management.SelectLayerByLocation('tracks', 'INTERSECT', 'pipelines')
    print("track features selected")
    arcpy.analysis.Intersect("pipelines #;tracks #", r"D:\Fish_DNVGL\Pipelines.gdb\A{0}".format(count), 'ALL',None, 'POINT')
    print("intersect completed")
