#ksi2815-> ksi2645 + Pi; 
#Ksi2645-> ksi2470 + Pi

from ROOT import *
import array, random

c1 = TCanvas("c1","", 600, 600)
h1 = TH2F("h1", "", 100, 0., 3., 100, 0. , .5 ) 

E = 2.815; px = 0.; py = 0.; pz = 0.

Ksi2815 = TLorentzVector(px, py, pz, E)

mass_array_1 = array.array('d', [2.645, 0.139])
mass_array_2 = array.array('d', [2.470, 0.139])

gen_ksi2645_pi = TGenPhaseSpace()
gen_ksi2470_pi = TGenPhaseSpace()

gen_ksi2645_pi.SetDecay(Ksi2815, 2, mass_array_1)

gen_events = 0

while(gen_events < 100000):
 weight_ksi2645_pi = gen_ksi2645_pi.Generate()
 vKsi2645 = gen_ksi2645_pi.GetDecay(0)
 vPi1 = gen_ksi2645_pi.GetDecay(1)

 gen_ksi2470_pi.SetDecay(vKsi2645, 2, mass_array_2)
 weight_ksi2470_pi = gen_ksi2470_pi.Generate()
 vKsi2470 = gen_ksi2470_pi.GetDecay(0)
 vPi2 = gen_ksi2470_pi.GetDecay(1)

 rnd = random.random()
 #if(gen_events%10000 ==0): print(str(weight_ksi2645_pi*weight_ksi2470_pi))
 if ( rnd < weight_ksi2645_pi*weight_ksi2470_pi):
  h1.Fill((vKsi2470+vPi2).Mag(), (vPi1+vPi2).Mag())
  gen_events+=1 


c1.cd(1) 
h1.Draw("zcol")
c1.Update()
