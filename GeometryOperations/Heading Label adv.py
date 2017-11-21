def FindLabel([OID]):
  import math
  mxd = arcpy.mapping.MapDocument("CURRENT")
  layers=arcpy.mapping.ListLayers(mxd, "Export_Output_8")
  lr=layers[0]
  with arcpy.da.SearchCursor(lr, 'Shape@','OID = '+str( [OID] )) as cursor:
    for row in cursor:
        shape = row[0].getPart(0)
        #return'<BOL>X1: {:.0f} Y1:{:.0f} X2:{:.0f} Y2:{:.0f}</BOL>'.format(shape[0].X,shape[1].X,shape[0].Y,shape[1].Y)
        count = row[0].pointCount
        radian1 = math.atan((shape[0].X - shape[1].X)/(shape[0].Y - shape[1].Y))
        radian2 = math.atan((shape[count-2].X - shape[count-1].X)/(shape[count-2].Y - shape[count-1].Y))
        degrees1 = radian1 * 180 / math.pi
        degrees2 = radian2 * 180 / math.pi
        if (shape[0].Y < shape[1].Y):
                degrees1 = degrees1 + 180
        if (degrees1 < 0):
                degrees1 = degrees1 + 360
        if (shape[count-2].Y < shape[count-1].Y):
                degrees2 = degrees2 + 180
        if (degrees2 < 0):
                degrees2 = degrees2 + 360
        return'<BOL>Heading1: {:.0f}- Heading2:  {:.0f} Deflection: {:.0f}</BOL> '.format(degrees1, degrees2, abs(degrees1 - degrees2 -180))
