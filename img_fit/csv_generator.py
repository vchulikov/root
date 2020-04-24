import ROOT
import numpy
import math

f = open("all_data.csv", "w")


def fill_arr(item):
 data = numpy.genfromtxt("gen_"+str(item)+".csv", delimiter = ',')
 arr = []
 for i in range(len(data)):
  arr.append(data[i, 1])
 return arr

a = []


a.append(fill_arr(1))
a.append(fill_arr(2))
a.append(fill_arr(3))
a.append(fill_arr(4))
a.append(fill_arr(5))

#print(a[1][1])

for i in range(100):
 print("line")
 for j in range(1, 6):
  print(a[j-1][i])
  f.write(str(a[j-1][i]))
  f.write(",")
 f.write("\n")
