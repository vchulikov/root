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

#more pdf's here: https://root.cern.ch/doc/v608/group__PdfFunc.html#ga58e74de4844774c4f2b9cdf2df4fb484

def gaussian(min_x, max_x, mu, sigma, title = "", color = 4):
 mu = ROOT.TFormula("mu",str(mu))
 sigma = ROOT.TFormula("sigma",str(sigma))
 pi = math.pi
 histogram = ROOT.TF1("fun","ROOT::Math::gaussian_pdf(x, sigma, mu)",min_x,max_x)#gaussian_pdf
 histogram.SetParameters(10,4,1,20)
 histogram.SetLineColor(color)
 histogram.SetLineWidth(4)
 histogram.SetTitle(title)
 return histogram

def two_gaussians(min_x, max_x, a1, a2, b1, b2, title = "", color = 4):
 a1 = ROOT.TFormula("a1",str(a1))
 a2 = ROOT.TFormula("a2",str(a2))
 b1 = ROOT.TFormula("b1",str(b1))
 b2 = ROOT.TFormula("b2",str(b2))
 pi = math.pi
 histogram = ROOT.TF1("fun","0.65*ROOT::Math::gaussian_pdf(x, a2, a1) + 0.35*ROOT::Math::gaussian_pdf(x, b2, b1)",min_x,max_x)#gaussian_pdf
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

#GENERATE N-files by function "function"
def files_generator(function, files, start_from, type_):
 hist1 = ROOT.TH1F("h1", "h1", 100, 0, 250)
 for i in range(1, files+1):
  f = open("./files/gen_file_" + str(i + start_from-1) + ".csv", "w") #i+100 for second part
  #fill hist follow distribution
  hist1.FillRandom("fun",20000)#20000
  #hist1.Scale(1./hist1.GetSumOfWeights())
  hist1.Scale(1./20000.) #normalization
  #fill array
  for i in range(hist1.GetNbinsX()):
   bin_num = float(i)
   bin_cont = hist1.GetBinContent(i)
   f.write(str(hist1.GetBinCenter(i)) + "," + str(bin_cont) + "\n")
  f.write("type" + "," + str(type_)) #choose a type (norm - 1, inf - 0)
  f.close()
