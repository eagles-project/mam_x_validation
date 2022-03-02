import os, sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

sys.path.append(os.getcwd())

class generate_plot:
    def __init__(self):
        self.prefix = sys.argv[1] + '_'
        self.input_data_name = 'gasaerexch_timeconvergence'
        data = importlib.import_module('%s%s'%(self.prefix, self.input_data_name))

        self.qsoa_aer, self.qso4_aer, self.qso4_gas, self.qsoa_gas = data.output.qsoa_aer_rel,\
                                                  data.output.qso4_aer_rel,\
                                                  data.output.qso4_gas_rel, \
                                                  data.output.qsoa_gas_rel
        self.pmid, self.temp, self.dtsubstep = data.input.pmid, data.input.temp,  data.input.dtsubstep
        temp_range = [ 180, 200, 233, 273, 298]
        pmid_range = [1000, 100000]
        self.testnum = len(pmid_range)*len(temp_range)
        #dt_range = [0.1, 0.316, 1, 3.163, 10, 31.579, 100, 300, 900, 1800]
        self.dt_range = [0.1,1,10, 100, 300, 900, 1800]
        self.nstep = [1800/n for n in self.dt_range]
        self.pp = PdfPages(self.prefix + self.input_data_name + '.pdf')
        
    
    def convergence(self):
        x = self.nstep[:]
        fig, axs = plt.subplots(self.testnum, 4,figsize=(2*self.testnum, 16))
        plt.setp(axs, xticks=x, xticklabels=['1','2','6', '18', '180', '1800', '18000'])
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        n=len(self.dt_range)
        
        for i in range(self.testnum):
            y1 = [abs(a) if a!=-1 else 0. for a in self.qsoa_aer[0+n*i:n+n*i]]
            y2 = [abs(a) if a!=-1 else 0. for a in self.qso4_aer[0+n*i:n+n*i]]
            y3 = [abs(a) if a!=-1 else 0. for a in self.qsoa_gas[0+n*i:n+n*i]]
            y4 = [abs(a) if a!=-1 else 0. for a in self.qso4_gas[0+n*i:n+n*i]]
            lin1, = axs[i,0].plot(x, y1, 'r-')
            lin2, = axs[i,1].plot(x, y2, 'b-')
            lin3, = axs[i,2].plot(x, y3, 'g-')
            lin4, = axs[i,3].plot(x, y4, 'y-')
            for j in range(4):
                axs[i,j].set(ylabel = 'relative error', yscale='linear',
                           xlabel = 'nstep [#]', xscale ='log',
                           title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
                axs[i,j].grid()
            axs[i,0].set_ylim(0, max(y1)*2)
            axs[i,1].set_ylim(0, max(y2)*2)
            axs[i,2].set_ylim(0, max(y3)*2)
            axs[i,3].set_ylim(0, max(y4)*2)
            
        
        fig.legend([lin1, lin2, lin3, lin4],["asoa", "aso4", "gsoa","gso4"], 
                  ncol=4,  borderaxespad=0.,
                 bbox_to_anchor=(0.7,0.935)) 
 
        self.pp.savefig(fig)
        self.pp.close()

aa= generate_plot()
aa.convergence()
