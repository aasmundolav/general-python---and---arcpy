Years = range(2010,2022)
mxd = arcpy.mapping.MapDocument("CURRENT")

for y in Years:
	layers=arcpy.mapping.ListLayers(mxd, "*", df)
	for elm in arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT"):
		if elm.name == "Title":
			elm.text = """<BOL>Sporing Fiskeri Tampen %s</BOL>
Data fra Fiskeridirektoratet 2012-2021""" % y

	for l in layers:
		if "Fiskeri" in l.name:
			l.definitionQuery = "Year = %s" % y
	arcpy.mapping.ExportToPDF(mxd, r"C:\temp\FDIR%s.pdf" % y)
