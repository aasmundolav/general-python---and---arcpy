import arcpy, os.path

arcpy.env.workspace = r"c:\Users\aoek\AppData\Roaming\Rothwell\PaleoGIS\Scratch"
workspaces = arcpy.ListWorkspaces("*", "FileGDB")

for workspace in workspaces:
  arcpy.env.workspace = workspace
  featureclasses = arcpy.ListFeatureClasses("World*")
  for featureclass in featureclasses:
    arcpy.AddField_management(featureclass, "TIME_SLIDER", "TEXT")
    arcpy.CalculateField_management(featureclass, "TIME_SLIDER", os.path.split(workspace)[1])
    arcpy.Merge_management(featureclass, r"d:\worldBasemap\Paleomap.gdb\World")
