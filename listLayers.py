import OS

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers=arcpy.mapping.ListLayers(mxd, "*", df)

for l in layers:
    l.name = name
    l.maxScale
    l.minScale
    l.definitionQuery
    l.labelClasses[0].expression
