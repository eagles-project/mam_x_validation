import os, sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from scipy import stats
from matplotlib.ticker import ScalarFormatter
from matplotlib import collections as mc
import geocat.viz as gv

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
        
        self.uptkait = data.output.uptk_ait
        self.uptkacc = data.output.uptk_acc
        self.uptkcoa = data.output.uptk_coarse
        self.uptkpca = data.output.uptk_pca
        self.so4g = data.output.so4g_time
        self.so4a = data.output.so4a_time
        self.soag = data.output.soag_time
        self.soaa = data.output.soaa_time

        temp_range = [180, 200, 233, 273, 298]
        pmid_range = [10000, 100000]
        self.testnum = len(pmid_range)*len(temp_range)
        #dt_range = [0.1, 0.316, 1, 3.163, 10, 31.579, 100, 300, 900, 1800]
        self.dt_range = [0.1, 1, 2, 4, 10, 50, 100, 300, 900, 1800]
        self.nstep = [1800/n for n in self.dt_range]
        self.pp = PdfPages(self.prefix + self.input_data_name + '.pdf')


    def contour_uptk(self):
        print("contour plot")
        temp_range = [180, 200, 233, 273, 298]
        pmid_range = [10000, 100000]
        rate_ait = np.zeros((len(pmid_range),len(temp_range)))
        rate_acc = np.zeros((len(pmid_range),len(temp_range)))
        rate_pca = np.zeros((len(pmid_range),len(temp_range)))
        rate_coa = np.zeros((len(pmid_range),len(temp_range)))
        for i in range(len(temp_range)):
            for j in range(len(pmid_range)):
                for k in range(len(self.uptkait)):
                    if self.temp[k] == temp_range[i] and self.pmid[k]==pmid_range[j] and self.dtsubstep[k] == 0.1:
                        rate_ait[j,i]= 1.0/self.uptkait[k]
                        rate_acc[j,i]= 1.0/self.uptkacc[k]
                        rate_pca[j,i]= 1.0/self.uptkpca[k]
                        rate_coa[j,i]= 1.0/self.uptkcoa[k]
        fig, ax = plt.subplots(2,2,figsize=(14, 10))
        levels_ait = np.arange(np.amin(rate_ait)*0.1, np.amax(rate_ait)*1.5, (np.amax(rate_ait)*1.5-np.amin(rate_ait)*0.1)/20.0)
        levels_acc = np.arange(np.amin(rate_acc)*0.1, np.amax(rate_acc)*1.5, (np.amax(rate_acc)*1.5-np.amin(rate_acc)*0.1)/20.0)
        levels_pca = np.arange(np.amin(rate_pca)*0.1, np.amax(rate_pca)*1.5, (np.amax(rate_pca)*1.5-np.amin(rate_pca)*0.1)/20.0)
        levels_coa = np.arange(np.amin(rate_coa)*0.1, np.amax(rate_coa)*1.5, (np.amax(rate_coa)*1.5-np.amin(rate_coa)*0.1)/20.0)
        #levels = np.power(10., lev_exp)

        ax[0,0].contour(temp_range, pmid_range, rate_ait, levels_ait, colors='k')
        fills1=ax[0,0].contourf(temp_range, pmid_range, rate_ait, levels_ait, cmap='jet')
        fig.colorbar(fills1, ax= ax[0,0])

        ax[0,1].contour(temp_range, pmid_range, rate_acc, levels_acc, colors='k')
        fills2= ax[0,1].contourf(temp_range, pmid_range, rate_acc, levels_acc, cmap='jet')
        fig.colorbar(fills2, ax= ax[0,1])

        ax[1,0].contour(temp_range, pmid_range, rate_pca, levels_pca, colors='k')
        fills3=ax[1,0].contourf(temp_range, pmid_range, rate_pca, levels_pca, cmap='jet')
        fig.colorbar(fills3, ax= ax[1,0])

        ax[1,1].contour(temp_range, pmid_range, rate_coa, levels_coa, colors='k')
        fills4=ax[1,1].contourf(temp_range, pmid_range, rate_coa, levels_coa, cmap='jet')
        fig.colorbar(fills4, ax= ax[1,1])

        mode = ['Aitken','Accumulation','Primary Carbon','Coarse']
        n= 0
        for i in range(2):
            for j in range(2):
                ax[i,j].set_xlabel('Temperature [K]')
                ax[i,j].set_ylabel('Pressure [Pa]')
                ax[i,j].set_title('e-folding time of uptake rate[s] of '+mode[n]+' mode')
                n+=1
#    ax.set_title('(H2SO4 conc = 5e8/cc)')
        fig.savefig('e-folding_time_uptk.png')

    def time_series(self):
        print("time series plot.")
        n=len(self.dt_range)
        nref = -n      # T=298K,P=1000hPa dt=0.1s
        x = np.arange(0, 1800, self.dt_range[nref])
        fig, axs = plt.subplots(4, 1,figsize=(8, 10))
        #plt.setp(axs, xticks=x, xticklabels=['1','2','6', '18', '180', '1800', '18000'])

        colors = ['coral', 'deepskyblue', 'red', 'blue']
        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        upper = 1e0
        lower = 1e-20
        y1 = self.so4g[nref]
        y2 = self.so4a[nref] 
        y3 = self.soag[nref]
        y4 = self.soaa[nref]

        lin1, = axs[0].plot(x, y1, color= colors[3])
        lin2, = axs[1].plot(x, y2, color= colors[1])
        lin3, = axs[2].plot(x, y3, color= colors[2])
        lin4, = axs[3].plot(x, y4, color= colors[0])
        spec = ["H2SO4 gas", "Sulfate aerosol", "SOA gas","SOA aerosol"]
        for j in range(4):
            axs[j].set(ylabel = 'mixing ratio', yscale='linear',
                          xlabel = 'time [s]', xscale ='linear',
                           title = spec[j]+' T=298K,P=1000hPa dt=0.1s')
            axs[j].grid()
            #axs[j].set_ylim(lower, upper)

#        fig.legend([lin1, lin2, lin3, lin4],["H2SO4 gas", "Sulfate aerosol", "SOA gas","SOA aerosol"],
#                  ncol=2,  borderaxespad=0.,
#                 bbox_to_anchor=(0.7,0.935))
#        plt.show()
        fig.savefig('time_series.png')

        
    def convergence_sum(self):
        n=len(self.dt_range)
        y1 = np.zeros((self.testnum,n-1))
        y2 = np.zeros((self.testnum,n-1))
        y3 = np.zeros((self.testnum,n-1))
        y4 = np.zeros((self.testnum,n-1))
        for i in range(self.testnum):
            y1[i] = [abs(a) if a!=-1 else 0. for a in self.qsoa_aer[1+n*i:n+n*i]]
            y2[i] = [abs(a) if a!=-1 else 0. for a in self.qso4_aer[1+n*i:n+n*i]]
            y3[i] = [abs(a) if a!=-1 else 0. for a in self.qsoa_gas[1+n*i:n+n*i]]
            y4[i] = [abs(a) if a!=-1 else 0. for a in self.qso4_gas[1+n*i:n+n*i]]

        #err_below = tuple(zip(x, err_below))
        #err_above = tuple(zip(x, err_above))
        yy1 = np.zeros(n-1)
        e1 = np.zeros(n-1)
        yy2 = np.zeros(n-1)
        e2 = np.zeros(n-1)
        yy3 = np.zeros(n-1)
        e3 = np.zeros(n-1)
        yy4 = np.zeros(n-1)
        e4 = np.zeros(n-1)
        for j in range(n-1):
            yy1[j] = sum(y1[:, j])/self.testnum
            e1[j] = np.std(y1[:, j])/yy1[j]*0.432
            yy2[j] = sum(y2[:, j])/self.testnum
            e2[j] = np.std(y2[:, j])/yy2[j]*0.432
            yy3[j] = sum(y3[:, j])/self.testnum
            e3[j] = np.std(y3[:, j])/yy3[j]*0.432
            yy4[j] = sum(y4[:, j])/self.testnum
            e4[j] = np.std(y4[:, j])/yy4[j]*0.432
        #x = self.nstep[:-1]
        x = self.dt_range[1:]
        w = 0.5

        colors = ['coral', 'deepskyblue', 'red', 'blue']
        err_b1 = tuple(zip(x, 10**(np.log10(yy1)-e1)))
        err_a1 = tuple(zip(x, 10**(np.log10(yy1)+e1)))
        err_b2 = tuple(zip(x, 10**(np.log10(yy2)-e2)))
        err_a2 = tuple(zip(x, 10**(np.log10(yy2)+e2)))
        err_b3 = tuple(zip(x, 10**(np.log10(yy3)-e3)))
        err_a3 = tuple(zip(x, 10**(np.log10(yy3)+e3)))
        err_b4 = tuple(zip(x, 10**(np.log10(yy4)-e4)))
        err_a4 = tuple(zip(x, 10**(np.log10(yy4)+e4)))
# Make a tuple containing those points to describe the line segment
        segments1 = tuple(zip(err_b1, err_a1))
        segments2 = tuple(zip(err_b2, err_a2))
        segments3 = tuple(zip(err_b3, err_a3))
        segments4 = tuple(zip(err_b4, err_a4))
# Create a line collection so we can plot all of the segments with one call
        bars1 = mc.LineCollection(segments1, colors=colors[0], linewidths=2.0)
        bars2 = mc.LineCollection(segments2, colors=colors[1], linewidths=2.0)
        bars3 = mc.LineCollection(segments3, colors=colors[2], linewidths=2.0)
        bars4 = mc.LineCollection(segments4, colors=colors[3], linewidths=2.0)

# regress dt = 1, 2, 4, 10
        e = 4
        s = 0
        slope, intercept, r, p, std_err = stats.linregress(np.log(x[s:e]), np.log(yy1[s:e]))
        print('slope of soa aerosol result is ', slope)

        slope, intercept, r, p, std_err = stats.linregress(np.log(x[s:e]), np.log(yy2[s:e]))
        print('slope of sulfate aerosol result is ', slope)

        slope, intercept, r, p, std_err = stats.linregress(np.log(x[s:e]), np.log(yy3[s:e]))
        print('slope of soa gas result is ', slope)

        slope, intercept, r, p, std_err = stats.linregress(np.log(x[s:e]), np.log(yy4[s:e]))
        print('slope of h2so4 gas result is ', slope)

        x0=[1, 10, 100, 1000]
        y0=[1e-8, 1e-7, 1e-6, 1e-5]
# plot
        fig, ax = plt.subplots(figsize=(8, 6))
        line0,=plt.plot(x0, y0, color = 'black',linestyle='dashed', dashes=[10, 5],linewidth=1.0)
        line1,=plt.plot(x, yy1, color= colors[0], linewidth=1.0, marker='.', markersize=10)
        line2,=plt.plot(x, yy2, color=colors[1], linewidth=1.0, marker='.', markersize=10)
        line3,=plt.plot(x, yy3, color=colors[2], linewidth=1.0, marker='.', markersize=10)
        line4,=plt.plot(x, yy4, color=colors[3], linewidth=1.0, marker='.', markersize=10)
        ax.add_collection(bars1)
        ax.add_collection(bars2)
        ax.add_collection(bars3)
        ax.add_collection(bars4)

# Remove axis lines on top and right sides
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

# Use geocat.viz.util convenience function to set axes tick values
        plt.yscale('log')
        plt.xscale('log')
        plt.autoscale(True)
        plt.xlabel('timestep(s) in 30 min', fontsize=15)
        plt.ylabel('abs(relative error)', fontsize=15)

#        fig.legend([line2, line4,line0],["sulfate aerosol", "sulfuric acid gas", "$O(\Delta t)$"],
#                  ncol=2,  borderaxespad=0.,
#                 bbox_to_anchor=(0.75,0.22),frameon=False, prop={'size': 12})
#        fig.legend([line1, line3, line0],["SOA aerosol", "SOA gas precursor", "$O(\Delta t)$"],
#                  ncol=2,  borderaxespad=0.,
#                 bbox_to_anchor=(0.75,0.22),frameon=False, prop={'size': 12})
        fig.legend([line1, line2, line3, line4, line0],["SOA aerosol", "sulfate aerosol", "soa gas","sulfuric acid gas", "$O(\Delta t)$"],
                  ncol=3,  borderaxespad=0.,
                 bbox_to_anchor=(0.85,0.22),frameon=False, prop={'size': 12})
        gv.set_axes_limits_and_ticks(ax, ylim=(1e-18, 1e4))

# Use geocat.viz.util convenience function to add minor and major tick lines
        gv.add_major_minor_ticks(ax,
                         y_minor_per_major=5,
                         x_minor_per_major=1,
                         labelsize=14)

# Use geocat.viz.util convenience function to add title to the plot axis.
        gv.set_titles_and_labels(ax, maintitle='Relative error of the time convergence test compared to 0.1s timestep',  maintitlefontsize=15)

# Make both major and minor ticks point inwards towards the plot
        ax.tick_params(direction="in", which='both')

# Set ticks only at left and bottom sides of plot
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')

# Display Plot
#        plt.show()
        fig.savefig('gasexch_time_nodg_update.png')   
 
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
                axs[i,j].set(ylabel = 'relative error', yscale='log',
                           xlabel = 'nstep [#]', xscale ='log',
                           title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
                axs[i,j].grid()
            axs[i,0].set_ylim(1e-14, 1e1)
            axs[i,1].set_ylim(1e-14, 1e1)
            axs[i,2].set_ylim(1e-14, 1e1)
            axs[i,3].set_ylim(1e-14, 1e1)
        
        fig.legend([lin1, lin2, lin3, lin4],["asoa", "aso4", "gsoa","gso4"], 
                  ncol=4,  borderaxespad=0.,
                 bbox_to_anchor=(0.7,0.935)) 
 
        self.pp.savefig(fig)
        self.pp.close()

aa= generate_plot()
aa.contour_uptk()
aa.time_series()
aa.convergence_sum()
