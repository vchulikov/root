import ROOT
import math
import Imports

#Link:
#https://arxiv.org/pdf/1909.12273.pdf ; figure 3

#Draw picture
img = ROOT.TImage.Open("./data.jpg")
canvas = ROOT.TCanvas("canvas1")
img.Draw("x")

#Create, update and draw pad
p = ROOT.TPad("p","p",0.,0.,1.,1.)
p.SetFillStyle(4000)
p.SetFrameFillStyle(4000)
p.Draw()
p.cd()

#Set function
#hist1 = Imports.gaussian(2250., 2300., 2290., 3.6, "" , 4)
#hist1 = Imports.crystal_ball(2250., 2300., 2290., 3.8, 10., 1.,"" , 4)
hist1 = Imports.exponent(2250., 2300., 0.3, 2290., title = "", color = 4)

#Set Frame-parameters
p.SetMargin(0.15, 0.06, 0.19, 0.08)

#Draw histogram
hist1.Draw("")
canvas.Update()
