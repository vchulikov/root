import ROOT
import Imports
import numpy as np

#Link:
#https://arxiv.org/pdf/1909.12273.pdf ; figure 3

def save():
    global p
    arr = np.array([p.GetLeftMargin(), 
                    p.GetRightMargin(), 
                    p.GetBottomMargin(),
                    p.GetTopMargin()])
    np.savez("pad", arr = arr)

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

#Set Frame-parameters
try:
    npzfile = np.load("pad.npz")['arr']
    p.SetMargin(npzfile[0], npzfile[1], npzfile[2], npzfile[3])
except:
    p.SetMargin(0.15, 0.06, 0.19, 0.08)


#Set function
#hist1 = Imports.gaussian(2250., 2300., 2290., 3.6, "" , 18000)
#hist1 = Imports.crystal_ball(2230., 2330., 2287., 6., 10., 10., norm=18000)
hist1 = Imports.bw(2230., 2330., 12., 2288.)

#Draw histogram
hist1.Draw("")
canvas.Update()
