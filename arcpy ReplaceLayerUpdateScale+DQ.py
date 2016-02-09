array = [[r"D:\MarinfWebkart2\CableTemplate.lyr","Cables"], [r"D:\MarinfWebkart2\CableTemplate.lyr","Pipelines"], [r"D:\MarinfWebkart2\InstallationTemplate.lyr","Installations"]]

for a in array:
    DQandSCALEarray = []
    updatewithlayer = a[0]
    wildcard = a[1]

    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = mxd.activeDataFrame
    layers=arcpy.mapping.ListLayers(mxd, wildcard, df)



    for l in layers:
        print l.name
        if l.isFeatureLayer:
            DQandSCALEarray.append({"DQ":l.definitionQuery, "MAX":l.maxScale, "MIN":l.minScale})
            name,dq,mx,mn = l.name, l.definitionQuery,l.maxScale, l.minScale
            arcpy.mapping.UpdateLayer(df,l,arcpy.mapping.Layer(updatewithlayer), False)        
            l.name, l.definitionQuery,l.maxScale, l.minScale = name,dq,mx,mn
