import arcpy

USStateMap = arcpy.GetParameterAsText(0) #r"E:\Previsico\WY\US_state\cb_2018_us_state_20m.shp"
StateName = arcpy.GetParameterAsText(1) #"Wyoming"
OutputFolder = arcpy.GetParameterAsText(2) #r"E:\Previsico\WY\WY_Boundary"
StateAbbre = arcpy.GetParameterAsText(3) #"WY"

TemLay = arcpy.MakeFeatureLayer_management(USStateMap, StateAbbre, """ "NAME" = '{}' """.format(StateName))

arcpy.management.CopyFeatures(TemLay, OutputFolder+"\\{}.shp".format(StateAbbre))
