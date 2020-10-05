#create one csv by list of pdfs
import ROOT
import numpy
import math

f = open( "./files/all_data.csv", "w")
files_num = 200

#####################################################################
f.write("20.")
f.write(",")
f.write("100.")
f.write(",")

for i in range(100):
    f.write("bin_" + str(i+1))
    f.write(",")

f.write("\n")

#####################################################################

def write_file(item):
    bins_num = 100
    data = numpy.genfromtxt("./files/gen_file_"+ str(item) + ".csv", delimiter = ',')

    for i in range(len(data)):
        if i == bins_num:
            f.write(str( int(data[i][1]) ))
            f.write("\n")
        else:
            f.write(str(data[i][1]))
            f.write(",")

#####################################################################

for i in range(files_num):
    write_file(i+1)
