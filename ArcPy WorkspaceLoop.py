import arcpy, os.path

arcpy.env.workspace = r"c:\Users\aoek\AppData\Roaming\Rothwell\PaleoGIS\Scratch"
workspaces = arcpy.ListWorkspaces("*", "FileGDB")

for workspace in workspaces:
    print os.path.split(workspace)[1]
    arcpy.env.workspace = workspace
    featureclasses = arcpy.ListFeatureClasses("World*")
    for featureclass in featureclasses:
        try:
            arcpy.AddField_management(featureclass, "TIME_SLIDER", "TEXT")
        except:
            print "add field failed.."
        arcpy.CalculateField_management(featureclass, "TIME_SLIDER", "'%s'" % os.path.split(workspace)[1][0:10],"PYTHON_9.3") ##
        arcpy.Append_management(featureclass, r"d:\worldBasemap\Paleomap.gdb\World","NO_TEST")
        break
