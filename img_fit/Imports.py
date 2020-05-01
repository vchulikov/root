import ROOT
import math
import numpy

#PDF's
#DESCRIPTION:
#Gaussian-function (gaussian)
# mu   : mean of gaussian function (expected value)
# sigma: standard deviation

#Linear-function (linear)
# slope    : slope
# intercept: intercept

#Crystal-ball-function (crystal_ball)
#https://en.wikipedia.org/wiki/Crystal_Ball_function
#mu   : mean value 
#sigma: sigma (link)
#alpha: alpha (link)
#n    : n (link)

#Other options (in any function)
# min_x: minimum of x-axis
# max_x: maximun of x-axis
# title: (optional) title of the histogram
# color: (optional) line color

def gaussian(min_x, max_x, mu, sigma, title = "", color = 4):
 mu = ROOT.TFormula("mu",str(mu))
 sigma = ROOT.TFormula("sigma",str(sigma))
 pi = math.pi
 histogram = ROOT.TF1("fun","[0]*exp((-0.5)*(x-mu)**2/(sigma**2))/(sigma**2*2*pi)**0.5",min_x,max_x)
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

def crystal_ball(min_x, max_x, mu, sigma, alpha, n, title = "", color = 4):
 mu = ROOT.TFormula("mu",str(mu))
 sigma = ROOT.TFormula("sigma",str(sigma))
 alpha = ROOT.TFormula("alpha",str(alpha))
 n = ROOT.TFormula("n",str(n))
 pi = math.pi
 histogram = ROOT.TF1("fun","ROOT::Math::crystalball_function(x, alpha, n, sigma, mu)",min_x,max_x)
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

def exponent(min_x, max_x, lambd, x0, title = "", color = 4):
 lambd = ROOT.TFormula("lambd",str(lambd))
 x0 = ROOT.TFormula("x0",str(x0))
 histogram = ROOT.TF1("fun","ROOT::Math::exponential_pdf(x, lambd, x0)", min_x, max_x)
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

def linear(min_x, max_x, slope, intercept, title = "", color = 4):
 slope = ROOT.TFormula("slope",str(slope))
 intercept = ROOT.TFormula("intercept",str(intercept))
 histogram = ROOT.TF1("fun","intercept+x*slope", min_x,max_x)
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

#GENERATE

def generator_pdf(distr_f):
 pdf = distr_f
 f = open("output_file.csv", "w")
 hist1 = ROOT.TH1F("h1", "h1", 100, 2250, 2320)
 array = ([])

 #fill hist follow distribution
 hist1.FillRandom("fun", 20000);
 hist1.Scale(1./hist1.GetSumOfWeights())

 #fill array and write it to csv file
 for i in range(hist1.GetNbinsX()):
  bin_cont = hist1.GetBinContent(i)
  bin_cent = hist1.GetBinCenter(i)
  array.append([bin_cent, bin_cont])
  f.write(str(bin_cent) + "," + str(bin_cont) + "\n") 

 hist1.Draw("hist e")
