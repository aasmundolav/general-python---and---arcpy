import arcpy

inputShapefile = arcpy.GetParameterAsText(0)
shiftX = arcpy.GetParameter(1)
shiftY = arcpy.GetParameter(2)
heading = arcpy.GetParameter(3)
outputShapefile = arcpy.GetParameterAsText(4)

arcpy.env.overwriteOutput = True
arcpy.CopyFeatures_management(inputShapefile,outputShapefile)

def RotateXYandShift(x, y, dx, dy, angle):  
    """Rotate an xy cooordinate about a specified origin  
  
    x,y      xy coordinates
    dx, dy   shift coodinates
    xc,yc   center of rotation  = 0
    angle   angle  
    units    "DEGREES" (default) or "RADIANS"  
    """  
    import math  
    x = x - 0 # xc  
    y = y - 0 # yc  
    angle = math.radians(angle)  
    xr = (x * math.cos(angle)) - (y * math.sin(angle)) + 0 #xc  
    yr = (x * math.sin(angle)) + (y * math.cos(angle)) + 0 #yc  
    return xr + dx, yr + dy

count = 0
with arcpy.da.UpdateCursor(outputShapefile, ['SHAPE@']) as cursor:
    for row in cursor:
        newGeom = arcpy.Array()
        for part in row[0]:
            newPart = arcpy.Array()
            for pnt in part:
                newcoord = RotateXYandShift(pnt.X, pnt.Y, shiftX , shiftY, -heading)
                if count == 100:
                    arcpy.AddMessage(newcoord)
                newPnt = arcpy.Point(newcoord[0], newcoord[1])
                count +=1
                newPart.add(newPnt)
            newGeom.add(newPart)
            new = arcpy.Polyline(newGeom)
            row[0] = new
            cursor.updateRow(row)
        
arcpy.AddMessage("Tranformed %s points" % count)
