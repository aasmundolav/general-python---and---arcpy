def setZvalues(fc, field):
	with arcpy.da.UpdateCursor(fc, ['SHAPE@', field]) as cursor:
		 count = 0
		 for row in cursor:
			 newGeom = arcpy.Array()
			 for part in row[0]:
				 newPart = arcpy.Array()
				 for pnt in part:
					 pnt.Z = row[1]
					 newPart.add(pnt)
					 newGeom.add(newPart)
					 new = arcpy.Polyline(newGeom, None ,True)
					 row[0] = new
					 cursor.updateRow(row)   
