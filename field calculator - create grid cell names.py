import arcpy

#use python parser
createGridName(!Shape!.extent)

def createGridName(inp):
	N=(inp.YMax+inp.YMin)/2
	E=(inp.XMax+inp.XMin)/2
	B=((int((E-int(E))*6)+1) + 6 * (11-(int((N-int(N))*12))))
	return "%s-%s-%s" % (int(N),int(E),'{:02.0f}'.format(B))
