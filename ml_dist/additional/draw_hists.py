import ROOT
import numpy
#import math

data = numpy.genfromtxt("./files/gen_file_1.csv", delimiter = ',')
data2 = numpy.genfromtxt("./files/gen_file_2.csv", delimiter = ',')
data3 = numpy.genfromtxt("./files/gen_file_101.csv", delimiter = ',')
data4 = numpy.genfromtxt("./files/gen_file_102.csv", delimiter = ',')


hist1 = ROOT.TH1F("h1", "h1", 100, 0, 250)
hist2 = ROOT.TH1F("h2", "h2", 100, 0, 250)
hist3 = ROOT.TH1F("h3", "h3", 100, 0, 250)
hist4 = ROOT.TH1F("h4", "h4", 100, 0, 250)



print(len(data))

for i in range(len(data)): 
 print(data[i, 0])
 hist1.Fill(data[i, 0], data[i, 1])
 hist2.Fill(data2[i, 0], data2[i, 1])
 hist3.Fill(data3[i, 0], data3[i, 1])
 hist4.Fill(data4[i, 0], data4[i, 1])

hist4.Draw("hist")
hist4.SetLineColor(1)
hist3.Draw("hist same")
hist3.SetLineColor(2)
hist2.Draw("hist same")
hist2.SetLineColor(3)
hist1.Draw("hist same")
hist1.SetLineColor(4)
