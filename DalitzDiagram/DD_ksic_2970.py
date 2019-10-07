#ksi_2970 -> ksi_2470 + Pi + Pi

from ROOT import *
import array, random

c1 = TCanvas("c1","", 600, 600)
h1 = TH2F("h1", "", 100, 2.5, 3., 100, 0. , .7 ) 

E = 2.970
px = 0.
py = 0.
pz = 0.

P = TLorentzVector(px, py, pz, E)

mass_array = array.array('d', [2.470, 0.139, 0.139])

gen = TGenPhaseSpace()
gen.SetDecay(P, 3, mass_array);
gen_events = 0

while(gen_events < 100000):
 weight = gen.Generate()
 vKp = gen.GetDecay(0)
 vKm = gen.GetDecay(1)
 vPi = gen.GetDecay(2)
 rnd = random.random()
 if(gen_events%10000 ==0): 
  print(str(weight))
  print(str(rnd))
 if ( rnd < weight):
  h1.Fill((vKp+vKm).Mag(), (vKm+vPi).Mag())
  gen_events+=1 


c1.cd(1) 
h1.Draw("zcol")
c1.Update()
