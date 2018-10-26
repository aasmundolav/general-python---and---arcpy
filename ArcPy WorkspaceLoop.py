import arcpy, os.path

## FIND GDBs IN FOLDER:
## findfolders( r"G:\T&P\ANT\MBM\NKG\Mapdata\GIS_data\GeotechincalPoints\gt_ssdm_delivery_2018",".gdb")
def findFolders(folder,ending)
    workspaces = []
    for path, dirs, files in os.walk(folder):
        for d in dirs:
            if d.endswith(ending):
                workspaces.append(os.path.join(path,d))
                print d
    return workspaces



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
