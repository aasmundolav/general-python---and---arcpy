import arcpy

inputgrid =
inputdata =
fieldgrid =

features = arcpy.da.UpdateCursor(inputgrid)
for f in features:
	arcpy.SelectByLocation(f, inputdata, 'intersect')
	f[0] = int(arcpy.GetCount_management(lyrfile).getOutput(0))
	features.update(f)
	
