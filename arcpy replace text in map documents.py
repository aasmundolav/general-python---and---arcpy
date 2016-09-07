import arcpy,os
arcpy.env.workspace = r"G:\T&P\ANT\MBM\NKG\Mapdata\ArcGIS_Common\Map_templates\TEMPLATE_RIGMOVE"
mxds = arcpy.ListFiles("*.mxd")
for m in mxds:
    print m
    mmxd = arcpy.mapping.MapDocument(os.path.join(arcpy.env.workspace,m))
    arcpy.AddMessage("Getting text elements from mxd: %s" % m)
    legenditems = arcpy.mapping.ListLayoutElements(mmxd, "TEXT_ELEMENT", "*")
    for l in legenditems:
        if "This can cause discrepancies in the" in l.text:
            print l.text
            #l.text = l.text.replace("This can cause discrepancies in the relevant locations of features shown on detailed maps","This can cause discrepancies in the relative locations of features shown on detailed maps")

    #mmxd.save()
