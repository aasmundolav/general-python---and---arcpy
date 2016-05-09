import arcpy, os.path

arcpy.env.workspace = "c:/data"
workspaces = arcpy.ListWorkspaces("*", "FileGDB")

for workspace in workspaces:
  arcpy.env.workspace = workspace
  featureclasses = arcpy.ListFeatureClasses("*")
  for featureclass in featureclasses:
    arcpy.AddField_management(featureclass, "TIME_SLIDER", "TEXT")
    arcpy.CalculateField_management(featureclass, "TIME_SLIDER", os.path.split(workspace)[1])
