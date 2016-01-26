import subprocess

def createGDALraster(inputfile, outputfile): ## eg. c:\temp\output.tif, c:\temp\input.tif ##:
    fwToolsTranslate = "\"c:\\Program Files (x86)\\FWTools2.4.7\\bin\\gdal_translate.exe\""
    fwToolsOverviews = "\"c:\\Program Files (x86)\\FWTools2.4.7\\bin\\gdaladdo.exe\""
    
    fullCmd = '%s -co "TILED=YES" -co "BIGTIFF=IF_NEEDED" -co "COMPRESS=LZW" \"%s" "%s"' % (fwToolsTranslate, inputfile, outputfile)

    print str(fullCmd)
    process = subprocess.Popen(str(fullCmd))
    returncode = process.wait()
    if returncode<>0:
        print "Error when creating GeoTiff file. returncode: %s" % returncode
        return "Error when creating GeoTiff file. returncode: %s" % returncode
    
    fullCmd = "%s -r average --config TILED YES %s 2 4 8 16 32 64 128" % (fwToolsOverviews , outputfile)
    print str(fullCmd)
    process = subprocess.Popen(str(fullCmd))
    returncode = process.wait()
    if returncode<>0:
        print "Error when adding overviews. returncode: %s" % returncode
        return "Error when creating GeoTiff file. returncode: %s" % returncode


### EXAMPLE call. Should work with any supporter GDAL raster.   
createGDALraster(r"C:/temp/Bathymetry_DTM_Statoil4.tif", r"C:/temp/Bathymetry_DTM_Statoil4_output12.tif")
###  
