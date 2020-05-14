#generate hist by pdf, save result in csv file
import ROOT
import numpy
import math
import Imports

#Seed
ROOT.gRandom.SetSeed(0)

#disease func
#func = Imports.two_gaussians(0., 250., 86., 33.5, 190., 33.5,"" , 4)
#norm func
func = Imports.gaussian(0., 250., 128., 21, "" , 4)

#how many files need to create
files_number = 100
start_from   = 101 #1 - disease, 101 - norm
event_type   = 1   #0 - disease, 1   - norm, 

#generate datasets by pdf (func)
Imports.files_generator(func, files_number, start_from, event_type)
