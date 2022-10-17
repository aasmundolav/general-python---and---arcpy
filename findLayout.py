import arcpy, time
start_time=time.time()


cx = [[100,100,-20]]#,[300,300,40]]

def RotateXYandShift(x, y, dx, dy, angle):
    xc =525526.846
    yc =6707525.391
    """Rotate an xy cooordinate about a specified origin  
  
    x,y      xy coordinates
    dx, dy   shift coodinates
    xc,yc   center of rotation  = 0
    
    angle   angle  
    units    "DEGREES" (default) or "RADIANS"  
    """  
    import math  
    x = x - xc # xc  
    y = y - yc # yc  
    angle = math.radians(angle)  
    xr = (x * math.cos(angle)) - (y * math.sin(angle)) + xc #xc  
    yr = (x * math.sin(angle)) + (y * math.cos(angle)) + yc #yc  
    return xr + dx, yr + dy



def RotateXYandShiftPolygon(geometry, dx, dy, angle):  
    """Rotate a polygon geometry""" 

    newGeom = arcpy.Array()
    for part in geometry:
        newPart = arcpy.Array()
        for pnt in part:
                        newcoord = RotateXYandShift(pnt.X, pnt.Y, dx, dy, angle)
                        newPnt = arcpy.Point(newcoord[0], newcoord[1])
                        newPart.add(newPnt)

        newGeom.add(newPart)
    new = arcpy.Polygon(newGeom)
    new = arcpy.Geometry('Polygon',newGeom,arcpy.SpatialReference(32631))
#    row[0] = new
#    cursor.updateRow(row)
    return new



GeoOrg = r"D:\TrollVind3D\TrollVindLayout\BufferGrid_WTG_generalized.shp"
GeoSR= ""
polygons = r"D:\TrollVind3D\TrollVindLayout\Polygons_v1710.shp"
logg = r"D:\TrollVind3D\TrollVindLayout\Logg.txt"

count = 0

##for c in cx:
##    count+=1
##    output = r"D:\TrollVind3D\TrollVindLayout\Test666778899%s.shp" % count
##    arcpy.CopyFeatures_management(GeoOrg,output)
##    with arcpy.da.UpdateCursor(output, ['SHAPE@']) as cursor:
##        for row in cursor:
##            newGeom = arcpy.Array()
##            for part in row[0]:
##                newPart = arcpy.Array()
##                for pnt in part:
##                                newcoord = RotateXYandShift(pnt.X, pnt.Y, c[0],c[1],c[2])
##                                newPnt = arcpy.Point(newcoord[0], newcoord[1])
##                                newPart.add(newPnt)
##                newGeom.add(newPart)
##            new = arcpy.Polygon(newGeom)
##            row[0] = new
##            cursor.updateRow(row)
##    print("sec: %s" % str(round(time.time() - start_time,0)))

mooringGeos = []
polygonGeos = []
c=cx[0]
with arcpy.da.SearchCursor(GeoOrg, ['SHAPE@']) as cursor2:
    for row2 in cursor2:
        mooringGeos.append(row2[0])

with arcpy.da.SearchCursor(polygons, ['SHAPE@','NAME']) as cursor3:
    for row3 in cursor3:
        polygonGeos.append(row3)

countWithin = 0

for p in polygonGeos:
    for m in mooringGeos:
        if m.within(p[0]):
                    countWithin += 1
    print("test: counted %s intersection in %s" % (countWithin,p[1]))
                                                

for h in range(0,59):    
    rotatedGeos=[]
    for m in mooringGeos:
        countWithin = 0
        count +=1
        #if count == 1:
        #    print(m.JSON)
        rotatedGeos.append(RotateXYandShiftPolygon(m,0,0,-h))
        #if count == 1:
        #    print(RotateXYandShiftPolygon(m,0,0,-h).JSON)
        
    for p in polygonGeos:
        countWithin = 0
        for r in rotatedGeos:
            if r.within(p[0]):
                countWithin+=1
        print("%s\t%s\t%s" % (h,p[1],countWithin))

#geometries.append(RotateXYandShiftPolygon(row2[0],c[0],c[1],c[2]))

print(len(mooringGeos))
print(len(polygonGeos))
