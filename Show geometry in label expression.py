def FindLabel ( [OBJECTID] ):
  mxd = arcpy.mapping.MapDocument("CURRENT")
  layers=arcpy.mapping.ListLayers(mxd, "test")
  lr=layers[0]
  with arcpy.da.SearchCursor(lr, 'Shape@','OBJECTID = '+str( [OBJECTID] )) as cursor:
      for row in cursor:
         newSR = arcpy.SpatialReference(32631)
         a=row[0].lastPoint.X
         b=row[0].lastPoint.Y
         return'easting:{:.0f}\nnorthing:{:.0f}'.format(a,b)
