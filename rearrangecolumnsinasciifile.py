import os

iFile = r"D:\HYTAMP_WGSITE\hydrograf-1401_utm32_neptune_block.NED"
oFile = r"D:\HYTAMP_WGSITE\hydrograf-1401_utm32_neptune_block3.xyz"

inFile = open(iFile,'r')
outFile = open(oFile,'w')

for i in inFile:
    data = i.split(" ")
    #print data
    data = [data[1],data[0],data[2]]
    outFile.write(" ".join(data))
