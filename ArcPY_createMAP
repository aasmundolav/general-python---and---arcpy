#!/usr/bin/python
# -*- coding: utf-8 -*-
#--------------------------------
#
# Name: Create Maps for Geotechical Scope of work / work pacakge
# Purpose:  Create Maps for Geotechical Scope of work / work pacakge
# Author: AOEK
# Created: 10.10.2017
# Script Version:  1
# ArcGIS Version:  10.2
# Python Version:  2.7.5
#--------------------------------
import os
import sys
import arcpy

Keysheets = arcpy.GetParameter(0)
GeotechnicalPnt = arcpy.GetParameter(1)
MxdTemplate = arcpy.GetParameterAsText(2)
Scale = arcpy.GetParameterAsText(3)
Layers = arcpy.GetParameter(4)
OutputFolder = arcpy.GetParameterAsText(5)
   

def do_analysis(*argv):
    """TODO: Add documentation about this function here"""
    try:
        ## OPEN Mxd Template
        mxd = arcpy.mapping.MapDocument(MxdTemplate)
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        df.spatialReference = arcpy.Describe(GeotechnicalPnt).spatialReference
        arcpy.AddMessage("Changing map template projection to %s" % arcpy.Describe(GeotechnicalPnt).spatialReference.name)
        
        ## Add Geotech Layers
        addLayer = arcpy.mapping.AddLayer(df,GeotechnicalPnt,"TOP")
        arcpy.AddMessage("Adding %s to map template data frame" % GeotechnicalPnt)
        addLayer = arcpy.mapping.AddLayer(df,Keysheets,"BOTTOM")
        arcpy.AddMessage("Adding %s to map template data frame" % Keysheets)

        ## Add Other Layers (on bottom)
        for l in Layers:            
            arcpy.mapping.AddLayer(df, l, "BOTTOM")
            arcpy.AddMessage("Aux layer %s added to map template data frame" % l)

        ## Set Scale
        arcpy.AddMessage("Changing map scale to 1:%s" % Scale) 
        df.scale = int(Scale)

        ## Fix Legend
        legenditems = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "*")
        if len(legenditems) > 0:              
            legend = legenditems[0]
            legend.autoAdd = True
        LegendStyle = "G:\T&P\ANT\MBM\NKG\Mapdata\ArcGIS_Common\Scripts\ReplaceLayersInMxds\LegendStyle.style"
        style=arcpy.mapping.ListStyleItems(LegendStyle,"Legend Items","*")[0]
        arcpy.AddMessage("Updating %s items using %s" % (legend.name,style.itemName))
        [legend.updateItem(lyr, style, True, True) for lyr in legend.listLegendItemLayers()]
        
        ## Find number of locations
        numberofmaps = arcpy.GetCount_management(GeotechnicalPnt)

        ## Export maps using Cursor
        rows = arcpy.SearchCursor(GeotechnicalPnt)        
        countmaps = 0
        for row in rows:
            countmaps +=1
            df.panToExtent (row.getValue('SHAPE').extent)

            mxd.title = "Survey ID:%s  Location Name: %s  Map #%s of %s" % (row.getValue('SURVEY_ID_REF'), row.getValue('SAMPLE_NAME'),countmaps, numberofmaps ) 

            exportfilename = os.path.join(OutputFolder, "%s_%sof%s.pdf" % (row.getValue('SAMPLE_NAME'),countmaps, numberofmaps))
            arcpy.AddMessage("Creating map %s.pdf" % exportfilename)
            arcpy.mapping.ExportToPDF(mxd, exportfilename)
            

  
        pass
    except arcpy.ExecuteError:
        print arcpy.GetMessages(2)
        arcpy.AddError(arcpy.GetMessages(2))
    except Exception as e:
        print e.args[0]
        arcpy.AddError(e.args[0])
# End do_analysis function

 
# This test allows the script to be used from the operating
# system command prompt (stand-alone), in a Python IDE, 
# as a geoprocessing script tool, or as a module imported in
# another script


if __name__ == '__main__':
    # Arguments are optional
    argv = tuple(arcpy.GetParameterAsText(i)
        for i in range(arcpy.GetArgumentCount()))
    do_analysis(*argv)
