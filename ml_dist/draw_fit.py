import ROOT
import math
import Imports

#Draw picture
img = ROOT.TImage.Open("./data.png")
canvas = ROOT.TCanvas("canvas1")
img.Draw("x")

#Create, update and draw pad
p = ROOT.TPad("p","p",0.,0.,1.,1.)
p.SetFillStyle(4000)
p.SetFrameFillStyle(4000)
p.Draw()
p.cd()

#Signal
#hist1 = Imports.gaussian(-4, 4., 0.3, 0.34, "" , 4)
#Background
hist1 = Imports.gaussian(-4, 4., 1.5, 0.8, "" , 5)

#Set Frame-parameters
p.SetMargin(0.15, 0.06, 0.19, 0.08)

#Draw histogram
hist1.Draw("")
canvas.Update()
