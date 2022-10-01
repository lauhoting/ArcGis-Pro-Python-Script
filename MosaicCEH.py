import arcpy

#Catseed/Elev_cm/Hydrodem Folder Directory
CEH_File = arcpy.GetParameterAsText(0)

#Output Folder Directory
Output_Folder = arcpy.GetParameterAsText(1)

#State Abbreviation
State = arcpy.GetParameterAsText(2)

#State Shapefile Directory
StateShape = arcpy.GetParameterAsText(3)

#Desired Output File Name
OutputName = arcpy.GetParameterAsText(4)

#Type of Data(Catseed, Elev_cm/Hydrodem)
CEH_Type = arcpy.GetParameterAsText(5)

arcpy.env.workspace = CEH_File

rlist = arcpy.ListRasters()

arcpy.management.MosaicToNewRaster( rlist , Output_Folder , OutputName ,"","32_BIT_FLOAT", 10,1,"LAST","FIRST")

v1_dir = Output_Folder+"\\"+OutputName

out_raster = arcpy.sa.ExtractByMask(v1_dir, StateShape)
out_raster.save(Output_Folder+"\\{}_{}_v2.tif".format(State,CEH_Type))