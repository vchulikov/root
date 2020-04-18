Image was taken from: "Search for the doubly charmed baryon Ksi_cc+": https://arxiv.org/pdf/1909.12273.pdf

# How to run:
1. run use command ***python -i draw_fit.py***\
for changing draw-parameters use ***execfile("draw_fit.py")*** command in the interactive mode (after first run)
2. to generate random sampled distribution use ***python -i pdf_generate.py***\

# Description:

Gaussian-function (gaussian)\
**mu**   : mean of gaussian function (expected value)\
**sigma**: standard deviation

Linear-function (linear)\
**slope**    : slope\
**intercept**: intercept

Crystal-ball-function (crystal_ball)\
**The parameters' description in this link (https://en.wikipedia.org/wiki/Crystal_Ball_function)**

Other options (in any function)\
**min_x**: minimum of x-axis\
**max_x**: maximun of x-axis\
**title**: (optional) title of the histogram\
**color**: (optional) line color
