### PURPOSE OF SCRIPT IS TO SEND EMAIL BASED IN LAYERS IN AN MXD
###
### MXD (ARCGIS MAP DOCUMENT) WITH LAYERS WITH A DEFINITON QUERY
### 'typically a definiton query asking for recent updated features'
###
### -FOR EACH LAYER IN MXD
### -ADD ATTRIBUTE TABLES TO A MAIL AND A SPREASHEET
### -SEND EMAIL
###



def formatEmail(msg):
    try:
##        
## REMEMBER TO USE DOUBLE %% IN HTML CODE TO AVOID PYTHON ERROR
##        
        msg =  """
<html>
<style>
table {
    width: 100%%;
}

th, td {
    text-align: left;
    padding: 1px;
    border: 1px solid #ddd;
    font-size: 80%%;
}
div.a {
    font-size: 100%%;
}
div.b {
    font-size: 70%%;
    color: #aaaaaa;
}

tr:nth-child(even) {background-color: #f2f2f2;}
</style>

%s
</html>
""" % (msg)
        return msg

    except Exception as e:
       print "Error: unable to format email %s %s %s" % (msg,mailinglist, e)

def MakeHtmlTable(headers, tablearray, maxrows):  
    table = ""
    hx=""
    for h in headers:
        hx += "<th>%s</th>" % h        
    table +=  "<tr>%s</tr>" % hx
    count = 0
    for subarray in tablearray:
        if count >= maxrows:
            break
        count += 1
        row=""
        for value in subarray:
            row += "<td>%s</td>" % value            
        table += "\n<tr>%s</tr>" % row    
    tableHTML = "\n<table>%s</table>" % table
    return tableHTML,count


def mxd2table(mxd):    
    import arcpy
    #mxd=r"G:\T&P\ANT\MBM\NKG\Mapdata\ArcGIS_Common\Scripts\autoQC\AutoQCLayers.mxd"
    layers=arcpy.mapping.ListLayers(arcpy.mapping.MapDocument(mxd), "*", arcpy.mapping.MapDocument(mxd).activeDataFrame)
    allowedfieldtypes =["String","Date"]
    notallowedfieldnames = ["OBJECTID","SHAPE"]
    for l in layers:
            if l.isFeatureLayer and l.supports("DATASOURCE"):

                ## FIND FIELDS THAT ARE TURNED ON IN MXD
                fields=[]
                allfields=[]   ### NEW 2020 -> Add to excel

                if arcpy.Exists("layer"):
                    arcpy.Delete_management("layer")
                arcpy.MakeFeatureLayer_management (l, "layer")                
                

                #find visible fields:
                descfields = arcpy.Describe("layer").fieldInfo
                vfields = [descfields.getFieldName(index) for index in range(0, descfields.count) if descfields.getVisible(index)]


                #find fields with allowed types
                descfields2 = arcpy.Describe("layer").fields
                for field in descfields2:
                    allfields.append(field.name)
                    if field.name in vfields and field.type in allowedfieldtypes and len(field.name) > 0:
                        fields.append(field.name)
                

##                for y in descfields:
##                    if len(y.name) > 0 and y.type in allowedfieldtypes:
##                        #print "%s - %s" % (y.name,y.type)
##                        fields.append(y.name)
                print("%s\n%s\n%s" % (l.name, l.dataSource, l.definitionQuery))
                info = [l.name, l.dataSource, l.definitionQuery, int(arcpy.GetCount_management(l).getOutput(0))]
                print("show fields: %s" % " - ".join(fields))

                ## GET VALUES FROM LAYER IN MXD
                cursor = arcpy.da.SearchCursor(l,fields)
                for q in notallowedfieldnames:
                    try:
                        allfields.remove(q)
                    except:
                        print("failed to remove field%s" % q)
                allcursor = arcpy.da.SearchCursor(l,allfields)
                yield info,fields,cursor, allfields, allcursor

## FUNCTION TO RETURN STYLE TO EXCEL TABLE FOR ODD/EVEN ROWS. 
def tablestyle(number):
    style_odd = xlwt.Style.easyxf("""font: name Arial; pattern: pattern solid, fore_colour ivory; """)
    style_even = xlwt.Style.easyxf("""font: name Arial; pattern: pattern solid, fore_colour white; """)
    if number%2 == 0:
        return style_even
    else:
        return style_odd


import xlwt, datetime
tables = mxd2table(r"F:\TEST\autoQC\AutoQCLayers2.mxd")
content=""
book = xlwt.Workbook()

style1 = xlwt.Style.easyxf("""font: name Arial; borders: left thick, right thick, top thick, bottom thick; pattern: pattern solid, fore_colour light_blue; """)

def tablestyle(color):
    style_odd = xlwt.Style.easyxf("""font: name Arial; pattern: pattern solid, fore_colour ivory; """)
    style_even = xlwt.Style.easyxf("""font: name Arial; pattern: pattern solid, fore_colour white; """)
    if color%2 == 0:
        return style_even
    else:
        return style_odd

    
## SPREADSHEET LOOP ##
tablecount=1
for t in tables:
    info = t[0]
 
    sheet1 = book.add_sheet("T%s_%s" % (tablecount, info[1][info[1].rfind(".")+1:]))
    row1 = sheet1.row(0)
    for index, z in enumerate(t[3]):
        try:            
            row1.write(index, z, style1)
            sheet1.col(index).width = 4000
        except:
            print("failed %s" % z)
    row=1
    for v in t[4]:
        row1 = sheet1.row(row)
        column=0
        for w in v:
            try:
                
                row1.write(column, w, tablestyle(row))
            except:
                print("failed %s" % t[3][column])
            column+=1
        row+=1
## END SPREADSHEET LOOP ##
    
    table = MakeHtmlTable(t[1],t[2],20)
    #print(" || ".join(info))
    if info[3] == 0:
        print("\n\nNO MAIL FOR %s\n\n" % info[1])
        continue
    content += '<br/><div class="a">%s</div><div class="b">%s<br/>%s<br/>total number of features: %s - feature in table: %s</div>' % (info[0],info[1],info[2],info[3],table[1])
    content += table[0]
    #print("%s%s" % (tableheader,htmltable))
    tablecount+=1

from datetime import date
today = datetime.date.today()
xlsSheets = r"F:\TEST\autoQC\AutoQCLayers%s.xls" % today.strftime("%Y%m%d")
book.save(xlsSheets)

from sendMail import sendMail
if len(content) > 0:
    #SendStatoilMail()
    body = formatEmail(content)
    sendMail("New Features in MarinfDB <no-reply@equinor.com>", ["aoek@equinor.com"], "Please check updated features", body,[xlsSheets])

