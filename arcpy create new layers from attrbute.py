field = "NAME"
mxd = arcpy.mapping.MapDocument("Current")
df = arcpy.mapping.ListDataFrames(mxd)[0]
layer = 'Source Rocks, SOMA'
LC = arcpy.mapping.ListLayers(mxd,layer,df)
cursor = arcpy.SearchCursor(layer)
att= []
 
for c in cursor:
 	if not c.getValue(field) in att:
 		att.append(c.getValue(field))
 		CL = LC[0]
 		CL.name = "%s - %s" % (c.getValue(field),layer)
 		CL.definitionQuery = "%s = '%s'" % (field,c.getValue(field))
 		arcpy.mapping.AddLayer(df,CL,"TOP")
