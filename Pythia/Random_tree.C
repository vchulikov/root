#include "TROOT.h"
#include "TFile.h"
#include "TTree.h"
#include "TRandom.h"

void Random_tree()
{
   TFile f("random_tree.root","recreate");
   TTree tree("tree","tree description");

   Float_t Mass;
   Double_t Random;
   Int_t Event;

   tree.Branch("Random",&Random,"Random/D");
   tree.Branch("Event",&Event,"Event/I");
   tree.Branch("Mass",&Mass,"Mass/F");
   
   //fill the tree
   for (Int_t i = 0; i < 10000; i++) 
   {
     Mass = gRandom->Gaus(0,1);
     Random = gRandom->Rndm();
     Event = i;
     tree.Fill();
   }   
   tree.Write();
}




