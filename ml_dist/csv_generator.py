#create one csv
import ROOT
import numpy
import math

f = open("./files/all_data.csv", "w")
files_num = 200 #i've add 100 more events from desease file


#open file, read data column and return this array
def fill_arr(item):
 data = numpy.genfromtxt("./files/gen_file_"+str(item)+".csv", delimiter = ',')
 arr = []
 for i in range(len(data)):
  arr.append(data[i, 1])
 return arr

#create array to save
a = []

for i in range(1, files_num+1):
 a.append(fill_arr(i))


#write this array to file
for i in range(101): #number of bins in hist
 for j in range(1, files_num+1):
  f.write(str(a[j-1][i]))
  f.write(",")
 f.write("\n")
