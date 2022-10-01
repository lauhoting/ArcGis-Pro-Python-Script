import arcpy
import os

CEH_File = arcpy.GetParameterAsText(0) #r"E:\Previsico\WY\Catseed"

Output_Folder = arcpy.GetParameterAsText(1) #r"E:\Previsico\WY\Combined_CEH\New_Catseed"

State = arcpy.GetParameterAsText(2) #WY

StateShape = arcpy.GetParameterAsText(3) #r"E:\Previsico\WY\WY_Boundary\WY.shp"

OutputName = arcpy.GetParameterAsText(4) #"WY_Catseed.tif"

CEH_Type = arcpy.GetParameterAsText(5) #Catseed/Elev_cm/Hydrodem

arcpy.env.workspace = CEH_File

rlist = arcpy.ListRasters()

arcpy.management.MosaicToNewRaster( rlist , Output_Folder , OutputName ,"","32_BIT_FLOAT", 10,1,"LAST","FIRST")

v1_dir = Output_Folder+"\\"+OutputName

out_raster = arcpy.sa.ExtractByMask(v1_dir, StateShape)
out_raster.save(Output_Folder+"\\{}_{}_v2.tif".format(State,CEH_Type))