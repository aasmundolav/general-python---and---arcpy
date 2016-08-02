count = 0
with arcpy.da.UpdateCursor(fc, ['SHAPE@']) as cursor:
	 for row in cursor:
		 newGeom = arcpy.Array()
		 for part in row[0]:
			 newPart = arcpy.Array()
			 for pnt in part:
				 newPnt = arcpy.Point(pnt.X +100, pnt.Y+100)
				 count +=1
				 newPart.add(newPnt)
                         newGeom.add(newPart)
                 new = arcpy.Polyline(newGeom)
                 row[0] = new
                 cursor.updateRow(row)     
