import ROOT
import numpy

#PDF's
#DESCRIPTION:
#Gaussian-function (gaussian)
# mu   : mean of gaussian function (expected value)
# sigma: standard deviation

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

def gaussian(min_x, max_x, mu, sigma, norm = 1., title = ""):
    mu = ROOT.TFormula("mu", str(mu))
    sigma = ROOT.TFormula("sigma", str(sigma))
    norm = str(norm)
    func = norm + "*ROOT::Math::gaussian_pdf(x, sigma, mu)"
    histogram = ROOT.TF1("fun", func, min_x, max_x)
    histogram.SetParameters(10,4,1,20)
    histogram.SetLineColor(color)
    histogram.SetLineWidth(4)
    histogram.SetTitle(title)
    return histogram

def crystal_ball(min_x, max_x, mu, sigma, alpha, n, norm = 1., title = ""):
    #cb parameters
    mu = ROOT.TFormula("mu", "%s"%mu)
    sigma = ROOT.TFormula("sigma", "%s"%sigma)
    alpha = ROOT.TFormula("alpha","%s"%alpha)
    n = ROOT.TFormula("n", "%s"%n)
    #normalization
    norm = "%s"%norm
    func = norm + "*ROOT::Math::crystalball_function(x, alpha, n, sigma, mu)"
    #tf1
    histogram = ROOT.TF1("fun", func, min_x, max_x)
    histogram.SetParameters(10, 4, 1, 20)
    histogram.SetLineColor(4)
    histogram.SetLineWidth(4)
    histogram.SetTitle(title)
    return histogram

def bw(min_x, max_x, gamma, x0):
    norm = 1.
    gamma = ROOT.TFormula("gamma", "%s"%gamma)
    x0 = ROOT.TFormula("x0", "%s"%x0)
    norm = "%s"%norm
    func = norm + "*ROOT::Math::breitwigner_pdf(x, gamma, x0)"
    histogram = ROOT.TF1("fun", func, min_x, max_x)
    return histogram



