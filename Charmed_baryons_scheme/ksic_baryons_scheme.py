from ROOT import *

c1 = TCanvas('c1','Ksi-c baryons',200,10,1000,800)
c1.Range(0,-0.1,1,1.15)

def reson(m):
 ma = "_c (" + str(m) + ")"
 return ma

def eq(m):
 pos = 4*(m-2450)/2450
 return pos

def add_part(mass, mass_unc, width, width_unc, nam, isospin, spin, p):
 y_pos = eq(mass)
 l = TLatex()
 l.SetTextSize(0.018)
 l.DrawLatex(.8, y_pos +0.0075, nam  + '; '+ "I(J^p) = " + isospin + '(' + spin + '^' + p + ')')
 l.DrawLatex(.4, y_pos + 0.01, "M = " + str(mass) + "\pm"+ str(mass_unc) + ' MeV')
 if width != None:
  l.DrawLatex(.4, y_pos - 0.01, "\Gamma = " + str(width) + "\pm" + str(width_unc) + "MeV")
 line_n = TLine(.55, y_pos+0.015,.75,y_pos+0.015)
 line_n.SetLineWidth(2)
 return line_n

def add_decay(state1, state2, dec_part, mode_num):
 y_pos_1 = eq(state1)
 y_pos_2 = eq(state2)
 x_pos_1 = 0.65-mode_num
 x_pos_2 = 0.65-mode_num
 ar = TArrow()
 ar.DrawArrow(x_pos_1,y_pos_1+0.015, x_pos_2, y_pos_2+0.015,0.015,'|>')
 l = TLatex()
 l.SetTextSize(0.018)
 l.DrawLatex(x_pos_1, 0.5*(y_pos_1+y_pos_2), dec_part)

gBenchmark.Start('tree')

title = TLatex()
title.SetTextSize(0.05)
title.DrawLatex(0.4, 1.05, "\Xi_c - baryons")

#part. lines

name = '\Xi'
#mass, mass unc, width, width unc, name, qn
line_2970 = add_part(float(2969.4), 0.8, 20., 2.4, name + reson(2970), "1/2", "?", "?")
line_2970.Draw()

line_2930 = add_part(float(2942.),  0.8, 15., 9., name + reson(2930), "?", "?", "?")
line_2930.Draw()

line_2815 = add_part(float(2816.73), 0.8, 2.43, 0.26,  name + reson(2815), "1/2", "3/2", "-")
line_2815.Draw()

line_2790 = add_part(float(2790.4),  0.8, 8.9, 1.0, name + reson(2790), "1/2", "1/2", "-")
line_2790.Draw()

line_2645 = add_part(float(2645.57), 0.8, 2.14, 0.19,  name + reson(2645), "1/2", "3/2", "+")
line_2645.Draw()

line_2578 = add_part(float(2578.4), 0.8, None, None,  name + reson(2578), "1/2", "1/2", "+")
line_2578.Draw()

line_2470 = add_part(float(2467.93), 0.18, None, None,  name, "1/2", "1/2", "+")
line_2470.Draw()

#decay lines

dec1_2970 = add_decay(float(2969.4), float(2578.4), '\pi', -0.08)
dec2_2970 = add_decay(float(2969.4), float(2645.57), '\pi', -0.07)
dec3_2970 = add_decay(float(2969.4), float(2467.93), '2 \pi', -0.09)

dec1_2815 = add_decay(float(2816.73), float(2578.4), '\pi', -0.05)
dec2_2815 = add_decay(float(2816.73), float(2645.57), '\pi', -0.04)

dec1_2790 = add_decay(float(2790.4), float(2578.4), '\pi', -0.02)

dec1_2645 = add_decay(float(2645.57), float(2467.93), '\pi', -0.0)

dec1_2578 = add_decay(float(2578.4), float(2467.93), '\gamma', 0.02)

#axis

line_ = TLine(.1,0.01,.1,0.99)
line_.Draw()

obj_list = []
obj_text_list = []
mass_list = [2500., 2600., 2700., 2800., 2900., 3000.]
for ln in range(len(mass_list)):
 y_pos = eq(mass_list[ln])
 txt = TText(.2, y_pos+0.015, str(int(mass_list[ln])))
 txt.SetTextSize(0.02)
 ln = TLine(.1,y_pos ,.2, y_pos)
 obj_list.append(ln)
 obj_text_list.append(txt)

for i in range(len(obj_list)):
 obj_list[i].Draw()
 obj_text_list[i].Draw()

#text

axis_title = TText(0.07, 0.4, "Mass")
axis_title.SetTextAngle(90)
axis_title.SetTextSize(0.02)
axis_title.Draw()

#MeV/c2
title = TLatex()
title.SetTextSize(0.03)
title.DrawLatex(0.16, 1.05, "\[MeV/c^{2}")


c1.Update()

gBenchmark.Show('tree')
