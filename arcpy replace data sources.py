mxd = arcpy.mapping.MapDocument("CURRENT")
for l in arcpy.mapping.ListLayers(mxd,"*",mxd.activeDataFrame):
	l.findAndReplaceWorkspacePath("",r"\\ws630\Projects\_databaseconnections\GIS_GIT.sde")




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
	if l.isFeatureLayer:
		l.replaceDataSource(r"\\ws630\Projects\PROJECT_SERVICES\TrollWind\data\layout\LayoutJan2023.gdb", "FILEGDB_WORKSPACE")
		print l.datasetName


mxd = arcpy.mapping.MapDocument("CURRENT")
for l in arcpy.mapping.ListLayers(mxd,"*",mxd.activeDataFrame):
        if l.isBroken and ".sde" not in l.dataSource:
            print "%s;%s" % (l.longName, l.dataSource)
            
            
