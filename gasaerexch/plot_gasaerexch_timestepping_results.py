import os, sys, importlib
import numpy as np
import matplotlib.pyplot as plt

#from matplotlib import colors
#import matplotlib.tri as tri
#from matplotlib.backends.backend_pdf import PdfPages
#import math
#from scipy import stats
#from matplotlib.ticker import ScalarFormatter
#from matplotlib import collections as mc
#import geocat.viz as gv

sys.path.append(os.getcwd())

class generate_plot:

    def __init__(self):

        self.prefix        = 'mam_'
        self.test_name     = sys.argv[1]
        self.file_basename = '%s%s'%(self.prefix, self.test_name)

        # Get test input and output data by importing the python module

        data = importlib.import_module(self.file_basename)
        print('Done importing data module '+self.file_basename)

        # Get the time step sizes and find the shortest one

        self.dt = data.input.dt_mam
        print('Found',np.size(self.dt),'step sizes:',self.dt)

        self.ref_dt_idx = self.dt.index(min(self.dt))
        print('Ref dt:',self.dt[self.ref_dt_idx])
        
        # Get various quantities

        self.time = data.output.model_time
        self.so4g = data.output.so4g_time_series
        self.so4a = data.output.so4a_time_series
        self.soag = data.output.soag_time_series
        self.soaa = data.output.soaa_time_series
        self.soag_amb_qsat = data.output.soag_amb_qsat

    def time_series(self):

        print("Plotting time series")

        title      = ["H2SO4 gas", "Sulfate aerosol", "SOA gas","SOA aerosol"]
        line_color = ["brown",     "red",             "blue",   "green"]
        nsubplot = len(title)

        fig, axs = plt.subplots(nsubplot, 1)
       #fig, axs = plt.subplots(2, 2, figsize=(8, 10))
        #plt.setp(axs, xticks=x, xticklabels=['1','2','6', '18', '180', '1800', '18000'])


       #left  = 0.125  # the left side of the subplots of the figure
       #right = 0.9    # the right side of the subplots of the figure
       #bottom = 0.1   # the bottom of the subplots of the figure 
       #top = 0.9      # the top of the subplots of the figure
       #wspace = 0.3   # the amount of width reserved for blank space between subplots
       #hspace = 0.8   # the amount of height reserved for white space between subplots
       #fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
       #upper = 1e0 
       #lower = 1e-20

        ndt = len(self.dt)

        x  = self.time[self.ref_dt_idx]
        nx = len(x)

        y = [self.so4g[self.ref_dt_idx],
             self.so4a[self.ref_dt_idx],
             self.soag[self.ref_dt_idx],
             self.soaa[self.ref_dt_idx]]


        for j in range(nsubplot):

            axs[j].plot( x, y[j], color='black', marker='o' )
            axs[j].plot( x, y[j], color=line_color[j] )

            axs[j].set(ylabel = '', xlabel = 'Time (s)', title = title[j])
            axs[j].grid()
          # axs[j].set_ylim(lower, upper)

#        fig.legend([lin1, lin2, lin3, lin4],["H2SO4 gas", "Sulfate aerosol", "SOA gas","SOA aerosol"],
#                  ncol=2,  borderaxespad=0.,
#                 bbox_to_anchor=(0.7,0.935))
#        plt.show()

        # Save figure to file
        fig.savefig(self.file_basename+'.png')
        print("Plot file:",self.file_basename+'.png')


aa = generate_plot()
aa.time_series()
