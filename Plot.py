from numpy import *
import Gnuplot

Algorithm=genfromtxt('plot_algo_eff_loss.dat')
Algorithm2=genfromtxt('plot_algo2_eff_loss.dat')
Random=genfromtxt('plot_random_eff_loss.dat')


Man_Random_nby2=genfromtxt('plot_manipulated_random_eff_loss_nby2.dat')
#Man_Random_nby4=genfromtxt('plot_manipulated_random_eff_loss_nby4.dat')
#Man_Random_nby8=genfromtxt('plot_manipulated_random_eff_loss_nby8.dat')

plot1=Gnuplot.PlotItems.Data(Algorithm, with_="lp lt rgb 'blue'", title="Algorithm from Patient's Side")

plot2=Gnuplot.PlotItems.Data(Random, with_="lp lt rgb 'red'", title="Random")

#plot3=Gnuplot.PlotItems.Data(Man_Random_nby4, with_="lp lt rgb 'green'", title="Man Random n/4")

plot4=Gnuplot.PlotItems.Data(Algorithm2, with_="lp lt rgb 'orange'", title="Algorithm from Doctor's Side")

plot5=Gnuplot.PlotItems.Data(Man_Random_nby2, with_="lp lt rgb 'black'", title="Man Random n/2")

#plot6=Gnuplot.PlotItems.Data(Man_Random_nby8, with_="lp lt rgb 'brown'", title="Man Random n/8")

gp=Gnuplot.Gnuplot(persist = 1)

gp('set xlabel "NO OF PATIENTS" ')
gp('set ylabel "EFFICIENY LOSS" ')
gp('set xrange [0:110]')
gp('set yrange [0:7500]')

gp('set xtics 10')
gp('set ytics 500')

gp.plot(plot2,plot5,plot1,plot4)

epsFilename= 'Efficieny Loss_with_nby2.eps'
gp.hardcopy(epsFilename, terminal= 'postscript',color='rgb')
