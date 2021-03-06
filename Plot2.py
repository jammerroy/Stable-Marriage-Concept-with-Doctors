from __future__ import division
from decimal import *
import numpy as np
import Gnuplot
import math

g=Gnuplot.Gnuplot(persist=1)

f1=open("plot_random_best.dat",'a')
f2=open("plot_algo_best.dat",'a')
f3=open("plot_algo2_best.dat",'a')

f4=open("plot_manipulated_random_best_nby2.dat",'a')

r1=[]
r2=[]
r3=[]
r4=[]
r5=[]
r6=[]

print 'RANDOM'

with open('plot_random_best.dat') as ab:
    for line in ab:
        r1.append(float(line))
print r1

print 'ALGORITHM 1'

with open('plot_algo_best.dat') as ab:
    for line in ab:
        r2.append(float(line))
print r2

print '\n'

print 'ALGORITHM 2'

with open('plot_algo2_best.dat') as ab:
    for line in ab:
        r3.append(float(line))
print r3

print '\n'

with open('plot_manipulated_random_best_nby2.dat') as ab:
    for line in ab:
        r4.append(int(line))
print r4

#x=[50,100,150,200,250,300,350,400,450,500]
g('set xtics ("10" 0, "20" 1, "30" 2, "40" 3, "50" 4,"60" 5,"70" 6,"80" 7,"90" 8,"100" 9) ')
#g('set title "House Allocation"')

g('set xlabel "Number of Agents"')
g('set ylabel "Number of Best Allocations(Patients) "')

g('set xrange [-1:10]')
g('set yrange [0:40]')
g('set style data histograms')
g('set style fill solid 1.0 border -1')

#g('set style line 1 lc rgb "red" lt 1 lw 2')

d1 = Gnuplot.PlotItems.Data(r1,title='Random')
d2 = Gnuplot.PlotItems.Data(r2,title='Patient Proposing')
d3 = Gnuplot.PlotItems.Data(r3,title="Doctor Proposing")
d4 = Gnuplot.PlotItems.Data(r4,title='Man Random n/2')

#g.hardcopy("aaa.png")
g.plot(d1,d2,d3,d4)

epsFilename= 'best_allocation_with_nby2.eps'
g.hardcopy(epsFilename, terminal= 'postscript',color='rgb')
