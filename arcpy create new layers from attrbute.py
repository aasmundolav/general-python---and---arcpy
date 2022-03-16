field = "NAME"
mxd = arcpy.mapping.MapDocument("Current")
df = arcpy.mapping.ListDataFrames(mxd)[0]
layer = 'ThisOne'
LC = arcpy.mapping.ListLayers(mxd,layer,df)
cursor = arcpy.SearchCursor(layer)
att= []
 
for c in cursor:
 	if not c.getValue(field) in att:
 		att.append(c.getValue(field))
 		CL = LC[0]
 		CL.name = "%s" % c.getValue(field)
 		CL.definitionQuery = "%s = '%s'" % (field,c.getValue(field))
 		arcpy.mapping.AddLayer(df,CL,"TOP")
   arcpy.CopyFeatures_management(CL, r"\\ws630\Projects\PROJECT_SERVICES\UtsiraNord\Data\singleshapes2\%s.shp" % c.getValue(field))
