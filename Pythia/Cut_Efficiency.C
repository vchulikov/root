#include "TF1.h"
#include "TH1D.h"
#include "TRandom.h"
#include "TLorentzVector.h"
#include "TCanvas.h"
double pi = 3.14159;

void my_gen(){
  TF1* fY = new TF1("fY","gaus",-10,10);

  fY->SetParameter(0,1.); // normalization
  fY->SetParameter(1,0.); // mean
  fY->SetParameter(2,2.); // width
  
  TF1* fPt = new TF1("fPt","[0]*x*exp(-x/[1])",0,5);
  fPt->SetParameter(0,1.);
  fPt->SetParameter(1,0.6); // GeV

  TH1D* hM = new TH1D("hM","",100,0.,5.);

  TH1D* hPtGen = new TH1D("hPtGen","",100,0,5);
  TH1D* hPtAcc = new TH1D("hPtAcc","",100,0,5);

  double mMu = 0.105658; // GeV
  for (int ev=0;ev<10000;ev++){
    double m = 3.096; // GeV
    double y = fY->GetRandom();
    double pt = fPt->GetRandom();
    double phi = gRandom->Uniform(0,2*pi);
    TLorentzVector p;
    double mt = sqrt(m*m+pt*pt);   // transverse mass
    double E  = mt*TMath::CosH(y);
    double pz = mt*TMath::SinH(y);
    double px = pt*cos(phi);
    double py = pt*sin(phi);
    p.SetPxPyPzE(px,py,pz,E);

    // rest frame
    double phiMu = gRandom->Uniform(0,2*pi);  // phi'
    double costMu = gRandom->Uniform(-1,1);   // cos(theta')
    double thetaMu = acos(costMu);
    double pMu = sqrt(m*m/4-mMu*mMu);
    double pzMu = pMu*costMu;
    double ptMu = pMu*sqrt(1-costMu*costMu);
    double pxMu = ptMu*cos(phiMu);
    double pyMu = ptMu*sin(phiMu);

    TLorentzVector p4Mu1,p4Mu2;
    p4Mu1.SetXYZM(-pxMu,-pyMu,-pzMu,mMu);
    p4Mu2.SetXYZM(+pxMu,+pyMu,+pzMu,mMu);

    TVector3 zaxis = p.Vect().Unit();
    p4Mu1.RotateUz(zaxis);
    p4Mu2.RotateUz(zaxis);

    TVector3 boost = p.BoostVector();
    p4Mu1.Boost(boost);
    p4Mu2.Boost(boost);

    TLorentzVector pSum = p4Mu1 + p4Mu2;
    double mSum = pSum.M();
    hM->Fill(mSum);
    double ptSum = pSum.Pt();
    double ySum = pSum.Rapidity();
    hPtGen->Fill(ptSum);
    if (p4Mu1.Pt()>0.1 && p4Mu2.Pt()>0.1) {
      hPtAcc->Fill(ptSum);
    }
  }
  hM->Draw();

  new TCanvas;
  hPtAcc->SetLineColor(kRed);
  hPtGen->Draw();
  hPtAcc->Draw("same");
}
