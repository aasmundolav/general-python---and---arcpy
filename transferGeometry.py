import arcpy

table=
locations=
commonfield=
output=

geometries=[]

inputcursor = arcpy.da.InsertCursor(output, ['SHAPE@',commonfield])

with arcpy.da.SearchCursor(table, [commonfield]) as cursor:
    for row in cursor:    
        inputcursor.insertRow(row)
        del inputcursor
        
def getLocationGeometry(ID, field, iLocations):
  with arcpy.da.SearchCursor(iLocations, ['SHAPE@',field]) as iCursor:
    for row in cursor:
      if row[1] == ID:
        return row[0]
      
  
