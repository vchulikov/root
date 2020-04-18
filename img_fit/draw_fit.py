from ROOT import *
import math

#Links
#https://arxiv.org/pdf/1909.12273.pdf ; figure 3

#Running
#run use command python -i draw_fit_v003.py
#for changing draw-parameters use execfile("draw_fit.py") command in the interactive mode (after first run)

#Description:
#Gaussian-function (gaussian)
# mu   : mean of gaussian function (expected value)
# sigma: standard deviation

#Linear-function (linear)
# slope    : slope
# intercept: intercept

#Other options (in any function)
# min_x: minimum of x-axis
# max_x: maximun of x-axis
# title: (optional) title of the histogram
# color: (optional) line color

def gaussian(min_x, max_x, mu, sigma, title = "", color = 4):
 mu = TFormula("mu",str(mu))
 sigma = TFormula("sigma",str(sigma))
 pi = math.pi
 histogram = TF1("gaussian","[0]*exp((-0.5)*(x-mu)**2/(sigma**2))/(sigma**2*2*pi)**0.5",min_x,max_x)
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

def linear(min_x, max_x, slope, intercept, title = "", color = 4):
 slope = TFormula("slope",str(slope))
 intercept = TFormula("intercept",str(intercept))
 histogram = TF1("linear","intercept+x*slope", min_x,max_x)
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

def crystal_ball(min_x, max_x, mu, sigma, alpha, n, title = "", color = 4):
 mu = TFormula("mu",str(mu))
 sigma = TFormula("sigma",str(sigma))
 alpha = TFormula("alpha",str(alpha))
 n = TFormula("n",str(n))
 pi = math.pi
 histogram = TF1("cb","ROOT::Math::crystalball_function(x, alpha, n, sigma, mu)",min_x,max_x)
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

#path to picture
img = TImage.Open("./data.jpg")
canvas = TCanvas("canvas1")
img.Draw("x")

#create, update and draw pad
p = TPad("p","p",0.,0.,1.,1.)
p.SetFillStyle(4000)
p.SetFrameFillStyle(4000)
p.Draw()
#set a position in canvas
p.cd()

#create fucntion
hist1 = gaussian(2250., 2300., 2290., 2., "" , 4)

#frame-parameters
p.SetMargin(0.15, 0.06, 0.19, 0.08)

#draw histogram
hist1.Draw("")
#update canvas
canvas.Update()
