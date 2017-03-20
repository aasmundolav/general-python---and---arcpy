with arcpy.da.UpdateCursor('TEST', ['PERIOD', 'YEAR'],where_clause="YEAR = 2016 AND PERIOD IS NULL") as cursor:    
    for row in cursor:
        cursor.deleteRow() 
