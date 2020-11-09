def setZvalues(fc, field):
	with arcpy.da.UpdateCursor(fc, ['SHAPE@', field]) as cursor:
		 count = 0
		 for row in cursor:
			 for pnt in row[0]:
				x = row[1]*1000
			 	pnt.M = x
			 	new = arcpy.PointGeometry(pnt, None ,True, True)
			 	row[0] = new
			 	cursor.updateRow(row)   
