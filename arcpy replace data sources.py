mxd = arcpy.mapping.MapDocument("CURRENT")
for l in arcpy.mapping.ListLayers(mxd,"*",mxd.activeDataFrame):
	print l.datasetName
	print l.name
	

mxd = arcpy.mapping.MapDocument("CURRENT")
for l in arcpy.mapping.ListLayers(mxd,"*",mxd.activeDataFrame):
	if ".RIG_ANCHOR" in l.datasetName:
		l.replaceDataSource(l.workspacePath, "SDE_WORKSPACE", l.datasetName.replace(".RIG_ANCHOR",".WGS84_RIG_ANCHOR"), False)
		print l.datasetName


mxd = arcpy.mapping.MapDocument("CURRENT")
for l in arcpy.mapping.ListLayers(mxd,"*",mxd.activeDataFrame):
	if "ED50" in l.datasetName:
		l.replaceDataSource(l.workspacePath, "SDE_WORKSPACE", l.datasetName.replace("ED50_","WGS84_"), False)
		print l.datasetName


mxd = arcpy.mapping.MapDocument("CURRENT")
for l in arcpy.mapping.ListLayers(mxd,"*",mxd.activeDataFrame):
        if l.isBroken and ".sde" not in l.dataSource:
            print "%s;%s" % (l.longName, l.dataSource)
            
            
