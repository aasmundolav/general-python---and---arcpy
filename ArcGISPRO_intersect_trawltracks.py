p = arcpy.mp.ArcGISProject("CURRENT")
m = p.listMaps()[0]
l = m.listLayers()[0]

for c in cursor:
    count +=1
    print(c.NAME)
    l.definitionQuery = "NAME = '{0}'".format(c.NAME)
    arcpy.management.SelectLayerByLocation('mergeWGS84', 'INTERSECT', 'TNPipelines_ClipNCS')
    arcpy.analysis.Intersect("TNPipelines_ClipNCS #;mergeWGS84 #", r"D:\Fish_DNVGL\Pipelines.gdb\F{0}".format(count), 'ALL',None, 'POINT')
