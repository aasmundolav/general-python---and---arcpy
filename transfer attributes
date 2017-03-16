with arcpy.da.UpdateCursor('TEST', ['SHAPE@', 'SURVEY_ID_REF']) as cursor:
    for row in cursor:
        iGeometry = arcpy.da.SearchCursor('All Surveys', ['SHAPE@','SURVEY_ID'],) SURVEY_ID = row[1]
        for g in iGeometry:
            if g[1] == row[1]:
                print "match %s" % g[1]
                row[0] == g[0]
                break
        cursor.updateRow(row)
