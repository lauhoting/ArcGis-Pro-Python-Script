import arcpy

#Directory of the US State Shapefile
USStateMap = arcpy.GetParameterAsText(0)

#State Full Name
StateName = arcpy.GetParameterAsText(1)

#Directory of Output Folder
OutputFolder = arcpy.GetParameterAsText(2)

#State Abbreviation
StateAbbre = arcpy.GetParameterAsText(3)

#Create Temporary Layer to Select State of Interest
TemLay = arcpy.MakeFeatureLayer_management(USStateMap, StateAbbre, """ "NAME" = '{}' """.format(StateName))

#Export the State of Interest as Shapefile
arcpy.management.CopyFeatures(TemLay, OutputFolder+"\\{}.shp".format(StateAbbre))
