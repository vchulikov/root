#generate hist follow pdf, save result in csv file
import ROOT
import numpy
import math

#create file, hist, array
f = open("output_file.csv", "w")
hist1 = ROOT.TH1F("h1", "h1", 100, 2250, 2320)
array = ([])

#CB
#func = ROOT.TF1("fun","ROOT::Math::crystalball_function(x, 1., 4., 3.5, 2290)",2250,2320)

#GAUSSIAN
mu = ROOT.TFormula("mu",str(2290))
sigma = ROOT.TFormula("sigma",str(3.6))
pi = math.pi
func = ROOT.TF1("fun","[0]*exp((-0.5)*(x-mu)**2/(sigma**2))/(sigma**2*2*pi)**0.5",2250,2320)
func.SetParameters(10,4,1,20)

#fill hist follow distribution
hist1.FillRandom("fun",20000);

hist1.Scale(1./hist1.GetSumOfWeights())

#fill array
for i in range(hist1.GetNbinsX()):
 bin_num = float(i)
 bin_cont = hist1.GetBinContent(i)
 array.append([bin_num, bin_cont])
 f.write("{0},{1}{2}".format(bin_num, bin_cont, "\n"))

#print(array)
hist1.Draw("e1")
