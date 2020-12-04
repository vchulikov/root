import ROOT
import Imports
import numpy as np

npzfile = np.load("learning_info.npz")
train_arr = npzfile['tr']
accur_arr = npzfile['ac']

hist1, hist2 = Imports.plot_results(train_arr, accur_arr)
canv = ROOT.TCanvas("h", "h", 800, 800)
canv.SetTitle("Training Metrics")
canv.Divide(1, 2)
canv.cd(1)
hist1.Draw("hist")
canv.cd(2)
hist2.Draw("hist")

