# Replace text in layer names
mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers=arcpy.mapping.ListLayers(mxd, "*", df)
replace = "Ana_EarthByte"

for l in layers:
    print l.name
    if replacetext in l.name:
        print l.name

#---------------------------------
mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers=arcpy.mapping.ListLayers(mxd, "Pipeline Labels", df)

for l in layers:
    for x in l.labelClasses:
        print x.definitonQuery
#---------------

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers=arcpy.mapping.ListLayers(mxd, "Cable Labels", df)

for l in layers:
    for x in l.labelClasses:
        x.SQLQuery = a[count]
        count+=1

#-------------------

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers=arcpy.mapping.ListLayers(mxd, "Installations", df)
for l in layers:
    if l.isFeatureLayer:
        finfo = arcpy.Describe(l).FieldInfo
        for x in range(0, finfo.count):
            if finfo.getFieldName(x) in a:
                finfo.setVisible(x,"VISIBLE") 
                print finfo.getFieldName(x), finfo.getVisible(x)
            else:
                finfo.setVisible(x,"HIDDEN") 
        arcpy.MakeFeatureLayer_management(l,"New_Installations","1=1",r"d:\MarinfWebkart2\MarinInf_1.gdb\MarinInf_1.gdb",finfo)
        
#--------------

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers=arcpy.mapping.ListLayers(mxd, "Installations", df)
a = []
for l in layers:
    if l.isFeatureLayer:
        finfo = arcpy.Describe(l).FieldInfo
        field_list = []
        for x in range(0, finfo.count):
            if finfo.getVisible(x) == "VISIBLE":
                print finfo.getFieldName(x)
                a.append(finfo.getFieldName(x))                
        break

-----------
    
