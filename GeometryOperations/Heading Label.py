def FindLabel([OBJECTID]):
  import math
  mxd = arcpy.mapping.MapDocument("CURRENT")
  layers=arcpy.mapping.ListLayers(mxd, "Export_Output_3")
  lr=layers[0]
  degreeses={}
  with arcpy.da.SearchCursor(lr, 'Shape@','OBJECTID = '+str( [OBJECTID] )) as cursor:
    for row in cursor:
        shape = row[0]
        radian = math.atan((shape.lastPoint.X - shape.firstPoint.X)/(shape.lastPoint.Y - shape.firstPoint.Y))
        degrees = radian * 180 / math.pi
        if (shape.lastPoint.Y < shape.firstPoint.Y):
                degrees = degrees + 180
        if (degrees < 0):
                degrees = degrees + 360
        return'<BOL>Heading: {:.0f}</BOL>'.format(degrees)
