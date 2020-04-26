#generate hist follow pdf, save result in csv file
import ROOT
import numpy
import math

#GENERATE N-files by function "function"
def files_generator(function, files):
 hist1 = ROOT.TH1F("h1", "h1", 100, 0, 250)
 for i in range(1, files+1):
  f = open("./files/gen_file_" + str(i) + ".csv", "w")
  #fill hist follow distribution
  hist1.FillRandom("fun",20000)
  hist1.Scale(1./hist1.GetSumOfWeights())
  #fill array
  for i in range(hist1.GetNbinsX()):
   bin_num = float(i)
   bin_cont = hist1.GetBinContent(i)
   f.write(str(hist1.GetBinCenter(i)) + "," + str(bin_cont) + "\n")
  f.close()

#GAUSSIAN
mu = ROOT.TFormula("mu",str(130)) #peak's center
sigma = ROOT.TFormula("sigma",str(20)) #rmsd
pi = math.pi
func = ROOT.TF1("fun","[0]*exp((-0.5)*(x-mu)**2/(sigma**2))/(sigma**2*2*pi)**0.5",2250,2320)
func.SetParameters(10,4,1,20)

#SEED
ROOT.gRandom.SetSeed(0)

#how many files need to create
files_number = 100
#generate by func
files_generator(func, files_number)
