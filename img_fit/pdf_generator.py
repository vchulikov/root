#generate hist follow pdf, save result in csv file
import ROOT
import numpy

#create file, hist, array
f = open("output_file.csv", "w")
hist1 = ROOT.TH1F("h1", "h1", 30, 2250, 2320)
array = ([])

#fill hist follow distribution
for i in range(100000):
 val = ROOT.gRandom.Gaus(2290., 3.6)
 hist1.Fill(val)

#normalisation
hist1.Scale(1./hist1.GetSumOfWeights())

#fill array
for i in range(hist1.GetNbinsX()):
 bin_num = float(i)
 bin_cont = hist1.GetBinContent(i)
 array.append([bin_num, bin_cont])
 f.write("{0},{1}{2}".format(bin_num, bin_cont, "\n"))

#print(array)
hist1.Draw("e1")
