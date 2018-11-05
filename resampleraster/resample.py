__author__ = 'ecpease'

from osgeo import gdal, gdalconst
import os

class Resample():
	def __init__(self,inputfile, referencefile, outputfile):
		self.inputfile = inputfile
		self.referencefile = referencefile
		self.outputfile = outputfile

	def resample(self):
		in_file = self.inputfile
		input_file = gdal.Open(in_file, gdalconst.GA_ReadOnly)
		inputProj = input_file.GetProjection()
		inputTrans = input_file.GetGeoTransform()

		ref_file = self.referencefile
		reference = gdal.Open(ref_file, gdalconst.GA_ReadOnly)
		referenceProj = reference.GetProjection()
		referenceTrans = reference.GetGeoTransform()
		bandreference = reference.GetRasterBand(1)    
		x = reference.RasterXSize 
		y = reference.RasterYSize

		out_file = self.outputfile
		driver= gdal.GetDriverByName('GTiff')
		output = driver.Create(out_file,x,y,1,bandreference.DataType)
		output.SetGeoTransform(referenceTrans)
		output.SetProjection(referenceProj)

		gdal.ReprojectImage(input_file,output,inputProj,referenceProj,gdalconst.GRA_Bilinear)

		del output

