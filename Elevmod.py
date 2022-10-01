import arcpy

Elev_cm = arcpy.GetParameterAsText(0)
Hydrodem = arcpy.GetParameterAsText(1)
Output_Folder = arcpy.GetParameterAsText(2)
State_Abbre = arcpy.GetParameterAsText(3)
Separate_Value = arcpy.GetParameterAsText(4)
Log_Value = arcpy.GetParameterAsText(5)
Divide_Value = arcpy.GetParameterAsText(6)

output_raster = arcpy.ia.RasterCalculator([Elev_cm, Hydrodem], ["x", "y"],"x-y")
output_raster.save(Output_Folder+"\\{}_Diff_DTM.tif".format(State_Abbre))

out_raster_2 = arcpy.ia.Con(output_raster, output_raster, None, "VALUE > 0")
out_raster_2.save(Output_Folder+"\\{}_RN.tif".format(State_Abbre))

out_raster_3 = arcpy.ia.Con(out_raster_2, out_raster_2, None, "VALUE > {}".format(Separate_Value))
out_raster_3 = arcpy.ia.RasterCalculator([out_raster_3], ["x"], "Log10(x)/Log10({})".format(Log_Value))
out_raster_3.save(Output_Folder+"\\{}_RN_V2.tif".format(State_Abbre))


out_raster_4 = arcpy.ia.Con(out_raster_2, out_raster_2, None, "VALUE < {}".format(Separate_Value))
output_raster_4 = arcpy.ia.RasterCalculator([out_raster_4], ["x"], "x/{}".format(Divide_Value))
out_raster_4.save(Output_Folder+"\\{}_RN_V3.tif".format(State_Abbre))

arcpy.management.MosaicToNewRaster( "output_raster_3;output_raster_4" , Output_Folder , "{}_RN_V4.tif".format(State_Abbre) ,"","32_BIT_FLOAT", 10,1,"LAST","FIRST")