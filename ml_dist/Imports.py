import ROOT
import math
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

#Other options (any function)
# min_x: minimum of x-axis
# max_x: maximun of x-axis
# title: (optional) title of the histogram
# color: (optional) line color
#chairman в сессии, протон час (45 минут говорение)
#more pdfs here: https://root.cern.ch/doc/v608/group__PdfFunc.html#ga58e74de4844774c4f2b9cdf2df4fb484

def gaussian(min_x, max_x, mu, sigma, title = "", color = 4):
    mu = ROOT.TFormula("mu", str(mu))
    sigma = ROOT.TFormula("sigma", str(sigma))
    pi = math.pi
    histogram = ROOT.TF1("fun","ROOT::Math::gaussian_pdf(x, sigma, mu)", min_x, max_x)
    histogram.SetParameters(10, 4, 1, 20)
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
    histogram = ROOT.TF1("fun","0.65*ROOT::Math::gaussian_pdf(x, a2, a1) + 0.35*ROOT::Math::gaussian_pdf(x, b2, b1)", min_x, max_x)
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


#GENERATION

#GENERATE N-files by function "function"
def files_generator(function, files, start_from, type_):
    hist1 = ROOT.TH1F("h1", "h1", 100, -4., 4.) 
    for i in range(1, files+1):
        f = open("./files/gen_file_" + str(i + start_from-1) + ".csv", "w")
        hist1.FillRandom("fun",10000) #10000/100
        print(hist1.GetSumOfWeights())
        hist1.Scale(1./10000) #Normalization
        for i in range(hist1.GetNbinsX()):
            bin_num = float(i)
            bin_cont = hist1.GetBinContent(i)
            f.write(str(hist1.GetBinCenter(i)) + "," + str(bin_cont) + "\n")
        f.write("type" + "," + str(type_))
        f.close()

#DRAW PLOT IN MODEL
def plot_results(a, b):

    hist1 = ROOT.TH1F("h1", "", len(a), 0., len(a)) #LOSS
    hist2 = ROOT.TH1F("h2", "", len(b), 0., len(b)) #ACCURACY
    hist1.SetStats(False)
    hist2.SetStats(False)
    for i in range(len(a)):
        hist1.SetBinContent(i+1, a[i])
        hist2.SetBinContent(i+1, b[i])
    hist1.SetYTitle("LOSS")
    hist2.SetYTitle("ACCURACY")
    hist2.SetXTitle("EPOCH")
    return hist1, hist2
