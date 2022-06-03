
c = [0,1],[2,3]

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

for x in c:
	count+=1
	output = r"D:\test\HT2%s.shp" % count
	arcpy.CopyFeatures_management('A',output)
	with arcpy.da.UpdateCursor(output, ['SHAPE@']) as cursor:
	 for row in cursor:
		 newGeom = arcpy.Array()
		 for part in row[0]:
			 newPart = arcpy.Array()
			 for pnt in part:
                                 newcoord = RotateXYandShift(pnt.X, pnt.Y, c[0],c[1],29)
				 newPnt = arcpy.Point(newcoord[0], newcoord[1])
				 count +=1
				 newPart.add(newPnt)
                         newGeom.add(newPart)
                 new = arcpy.Polyline(newGeom)
                 row[0] = new
                 cursor.updateRow(row)


