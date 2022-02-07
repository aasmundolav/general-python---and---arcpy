Years = range(2010,2022)
mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame

for y in Years:
	print y
	layers=arcpy.mapping.ListLayers(mxd, "*", df)
	print y
	aa=arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[0]
	
	aa.text = """<BOL>Sporing Fiskeri Tampen %s</BOL>
	Data fra Fiskeridirektoratet 2010-2020""" % y
	
	for l in layers:
		if "Fiskeri" in l.name:
			l.definitionQuery = "Year = %s" % y
	arcpy.mapping.ExportToPNG(mxd, r"C:\temp\FDIR%s.png" % y)
