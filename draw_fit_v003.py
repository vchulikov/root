from ROOT import *

img = TImage.Open("data.jpg")
c1 = TCanvas("c1")#,"The FillRandom example",200,10,700,900)
img.Draw("x")

p = TPad("p","p",0.,0.,1.,1.)
p.SetFillStyle(4000)
p.SetFrameFillStyle(4000)
p.Draw()
p.cd()

##2225, 2345
x_min = 2250.
x_max = 2300.

mu = TFormula("mu","2290")
sigma = TFormula("sigma","5")

hist1 = TF1("sqroot","[0]*exp((-0.5)*(x-mu)**2/(sigma**2))/(sigma**2*2*3.14)**0.5",x_min,x_max)


p.SetMargin(0.15, 0.06, 0.19, 0.08)
hist1.SetParameters(10,4,1,20)

hist1.SetLineColor(4)
hist1.SetLineWidth(4)
hist1.Draw("")

c1.Update()



