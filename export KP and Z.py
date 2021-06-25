count = 0
with arcpy.da.SearchCursor('profilelines',['SHAPE@','NAME']) as cursor:
    for row in cursor:
        print row[1]	
	count += 1
	f = open(r"c:\temp\linex%s.txt" % row[1], 'w')
	f.writelines("M; Z\n")
	for part in row[0]:
            for pnt in part:
                f.writelines("%s; %s\n" % (pnt.M, pnt.Z))
	f.close
