#generate hist follow pdf, save result in csv file
import ROOT
import numpy
import math
import Imports

#choose function

#pdf = Imports.gaussian(2250., 2300., 2260., 3.6)
#pdf = Imports.crystal_ball(2250., 2300., 2290., 3.8, 1., 1.)
#pdf = Imports.linear(2250., 2300., 0.3, 1000.)
pdf = Imports.exponent(2250., 2300., 0.3, 2290.)

#generate
Imports.generator_pdf(pdf)
