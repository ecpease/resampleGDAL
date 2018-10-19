from osgeo import gdal, gdalconst
import os

inputfile = os.path.join('PRISM', 'PRISM_ppt_stable_4kmM3_201701_bil.bil')
input = gdal.Open(inputfile, gdalconst.GA_ReadOnly)
inputProj = input.GetProjection()
inputTrans = input.GetGeoTransform()

referencefile = os.path.join('na_dem_15s_bil', 'na_dem_15s.bil')
reference = gdal.Open(referencefile, gdalconst.GAReadOnly)
referenceProj = reference.GetProjection()
referenceTrans = reference.GetGeoTransform()
bandreference = reference.GetRasterBand(1)    
x = reference.RasterXSize 
y = reference.RasterYSize


outputfile = os.path.join('output', 'PRISM_resample.tif')
driver= gdal.GetDriverByName('GTiff')
output = driver.Create(outputfile,x,y,1,bandreference.DataType)
output.SetGeoTransform(referenceTrans)
output.SetProjection(referenceProj)

gdal.ReprojectImage(input,output,inputProj,referenceProj,gdalconst.GRA_Bilinear)

del output