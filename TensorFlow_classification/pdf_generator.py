#generate hist by pdf, save result in csv file
import ROOT
import numpy
import math
import Imports

#Seed
ROOT.gRandom.SetSeed(0)

#generate datasets by pdf (func)
Imports.files_generator(Imports.gaussian(-4, 4., 0.3, 0.34, "" , 4) , 50, 1,  0)
Imports.files_generator(Imports.gaussian(-4, 4., -0.3, 0.34, "" , 4) , 25, 51,  0)
Imports.files_generator(Imports.gaussian(-4, 4., 0.6, 0.34, "" , 4) , 25, 76,  0)


Imports.files_generator(Imports.gaussian(-4, 4., 1.5, 0.8,  "" , 5) , 50, 101, 1)
Imports.files_generator(Imports.gaussian(-4, 4., 1.7, 0.8,  "" , 5) , 25, 151, 1)
Imports.files_generator(Imports.gaussian(-4, 4., 1.3, 0.8,  "" , 5) , 25, 176, 1)

#Imports.files_generator(func, files_number, start_from, event_type)
