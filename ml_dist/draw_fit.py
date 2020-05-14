#from ROOT import *
import ROOT
import math
import Imports

#Draw picture
img = ROOT.TImage.Open("./data_infarct.png")
canvas = ROOT.TCanvas("canvas1")
img.Draw("x")

#Create, update and draw pad
p = ROOT.TPad("p","p",0.,0.,1.,1.)
p.SetFillStyle(4000)
p.SetFrameFillStyle(4000)
p.Draw()
p.cd()

#create func for inf
#hist1 = Imports.two_gaussians(0., 250., 86., 33.5, 190., 33.5,"" , 4)
#create func for norm
hist1 = Imports.gaussian(0., 250., 128., 21, "" , 4)

#Set Frame-parameters
p.SetMargin(0.15, 0.06, 0.19, 0.08)

#Draw histogram
hist1.Draw("")
canvas.Update()
