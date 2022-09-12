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
        self.soag_niter    = data.output.soag_niter
        self.so4g_ddt_exch = data.output.so4g_ddt_exch
        self.soag_ddt_exch = data.output.soag_ddt_exch


    def time_series(self):

        print("Plotting time series")

        title = [["H2SO4 gas mixing ratio", "SOA gas mixing ratio"], 
                 ["SO4 mixing ratio",       "SOA mixing ratio"],
                 ["H2SO4 gas cond/evap rate", "SOA gas cond/evap rate"],
                 ["SOAG gas amb. qsat",       "SOA # of sub-cycles"]] 
        ncol  = 2
        nrow  = 4

        it0_arr = [[0,0],[0,0],[1,1],[1,1]]

        fig, axs = plt.subplots(nrow, ncol, figsize=(8,10))
        fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=0.55)

        #--------------------------------------------------------------------------------------------
        # Loop through different runs using different time steps
        #--------------------------------------------------------------------------------------------
        dt_color = ['gold','mediumseagreen','aqua','cornflowerblue','blueviolet','magenta','crimson']
        ndt = len(self.dt)

        for idt in range(ndt):

            # Time series plot. X axis is model time

            x  = self.time[idt]
            nx = len(x)

            # Different panels show different quantities

            y = [ [ self.so4g[idt], self.soag[idt] ],
                  [ self.so4a[idt], self.soaa[idt] ], 
                  [ self.so4g_ddt_exch[idt], self.soag_ddt_exch[idt] ], 
                  [ self.soag_amb_qsat[idt], self.soag_niter[idt] ]     ]

            for j in range(ncol):
                for i in range(nrow):

                    it0 = it0_arr[i][j]

                    yy = y[i][j] 
                    axs[i,j].plot( x[it0:], yy[it0:], color=dt_color[idt], marker='.', label='dt = '+str(self.dt[idt]) )
                    axs[i,j].plot( x[it0:], yy[it0:], color=dt_color[idt] )

                    axs[i,j].set(ylabel = '', xlabel = 'Time (s)', title = title[i][j] )
                    axs[i,j].grid()
                  # axs[i,j].set_ylim(lower, upper)

                    plt.legend(loc='best',fontsize='x-small')

        #-------------------------------------
        # Done plotting. Save figure to file
        #-------------------------------------
        fig.savefig(self.file_basename+'.png')
        print("Plot file:",self.file_basename+'.png')

#------------------------------------------------------------
aa = generate_plot()
aa.time_series()
