#SECOND PART
#ASCII TO ROOT
#REQUIREMENTS: ASCII-FILE (dataset.txt)

import re, array, os
import ROOT
from ROOT import TFile, TTree, gROOT, addressof

arr = ["pt","y","ct","ch","id","ipc","p_p","eta_p","phi_p","p_k","eta_k","p_3","eta_3","ntrk","NNp","im","m12","m13","m23","NNk","NN3","lgi"]


gROOT.ProcessLine(
"struct staff_t {\
   Float_t pt;\
   Float_t y;\
   Float_t im;\
   Float_t ntrk;\
   Float_t lgi;\
};");

staff = ROOT.staff_t()

f = TFile( 'dataset.root', 'RECREATE' )
tree = TTree( 'ds_k', 'staff data from ascii file' )
tree.Branch( 'pt', ROOT.AddressOf( staff, 'pt' ), 'pt/F' )
tree.Branch( 'y', ROOT.AddressOf( staff, 'y' ), 'y/F' )
tree.Branch( 'im', ROOT.AddressOf( staff, 'im' ), 'im/F' )
tree.Branch( 'ntrk', ROOT.AddressOf( staff, 'ntrk' ), 'ntrk/F' )
tree.Branch( 'lgi', ROOT.AddressOf( staff, 'lgi' ), 'lgi/F' )

for line in open("PATH-TO-DIR/dataset.txt").readlines():
 t = list(filter( lambda x: x, re.split( '\s+', line ) ) )
 staff.pt  = float(t[0])
 staff.y  = float(t[1])
 staff.im  = float(t[15])
 staff.ntrk  = float(t[13])
 staff.lgi  = float(t[21])
 tree.Fill()

tree.Print()
tree.Write()
