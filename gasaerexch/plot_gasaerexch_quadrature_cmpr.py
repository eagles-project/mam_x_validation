import os, sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from matplotlib.ticker import ScalarFormatter
from matplotlib import collections as mc
#import geocat.viz as gv

'''
Postprocess script for the test of quadrature in MAM's gas-aerosol exchange parameterization.

Author: Qiyang Yan, PNNL, 2022
'''

sys.path.append(os.getcwd())

class generate_plot:
    def __init__(self, Dp_opt):
        self.prefix = sys.argv[1] + '_'
        self.input_data_name = sys.argv[2] 
        data = importlib.import_module('%s%s'%(self.prefix, self.input_data_name))

        uptk_beta, uptk_direct, uptk_rect, self.ghqp = data.output.uptkaer_beta,\
                                                  data.output.uptkaer_direct,\
                                                  data.output.uptkaer_rect, \
                                                  data.input.nghq

        self.beta = data.output.beta

        if Dp_opt == 'Dpg':
            uptk_mean  = data.output.uptkaer_mean
        elif Dp_opt == 'Dpn':
            uptk_mean  = data.output.uptkaer_meandn
        elif Dp_opt == 'Dps':
            uptk_mean  = data.output.uptkaer_meands
        elif Dp_opt == 'Dpv':
            uptk_mean  = data.output.uptkaer_meandv

        uptk_meandg  = data.output.uptkaer_mean
        uptk_meandn  = data.output.uptkaer_meandn
        uptk_meands  = data.output.uptkaer_meands
        uptk_meandv  = data.output.uptkaer_meandv

        self.pmid, self.temp = data.input.pmid, data.input.temp
        self.pmidlen, self.templen = 3, 4
        self.nghqlen = 4

        self.uptk_beta_1 = [uptk_beta[i][0] for i in range(len(uptk_beta))]
        self.uptk_beta_2 = [uptk_beta[i][1] for i in range(len(uptk_beta))]
        self.uptk_beta_3 = [uptk_beta[i][2] for i in range(len(uptk_beta))]
        self.uptk_beta_4 = [uptk_beta[i][3] for i in range(len(uptk_beta))]

        self.b_error, self.d_error = data.output.uptkaer_beta_relerror, data.output.uptkaer_direct_relerror
        #self.b_error_1 = [b_error[i][0] for i in range(len(b_error))]
        #self.b_error_2 = [b_error[i][1] for i in range(len(b_error))]
        #self.b_error_3 = [b_error[i][2] for i in range(len(b_error))]
        #self.b_error_4 = [b_error[i][3] for i in range(len(b_error))]

#        self.d_error_1 = [d_error[i][0] for i in range(len(d_error))]
#        self.d_error_2 = [d_error[i][1] for i in range(len(d_error))]
#        self.d_error_3 = [d_error[i][2] for i in range(len(d_error))]
#        self.d_error_4 = [d_error[i][3] for i in range(len(d_error))]

        self.uptk_direct_1 = [uptk_direct[i][0] for i in range(len(uptk_direct))]
        self.uptk_direct_2 = [uptk_direct[i][1] for i in range(len(uptk_direct))]
        self.uptk_direct_3 = [uptk_direct[i][2] for i in range(len(uptk_direct))]
        self.uptk_direct_4 = [uptk_direct[i][3] for i in range(len(uptk_direct))]

        self.uptk_rect_1 = [uptk_rect[i][0] for i in range(len(uptk_rect))]
        self.uptk_rect_2 = [uptk_rect[i][1] for i in range(len(uptk_rect))]
        self.uptk_rect_3 = [uptk_rect[i][2] for i in range(len(uptk_rect))]
        self.uptk_rect_4 = [uptk_rect[i][3] for i in range(len(uptk_rect))]
        
        self.uptk_mean_1 = [uptk_mean[i][0] for i in range(len(uptk_mean))]
        self.uptk_mean_2 = [uptk_mean[i][1] for i in range(len(uptk_mean))]
        self.uptk_mean_3 = [uptk_mean[i][2] for i in range(len(uptk_mean))]
        self.uptk_mean_4 = [uptk_mean[i][3] for i in range(len(uptk_mean))]

        self.uptk_meandg_1 = [uptk_meandg[i][0] for i in range(len(uptk_meandg))]
        self.uptk_meandg_2 = [uptk_meandg[i][1] for i in range(len(uptk_meandg))]
        self.uptk_meandg_3 = [uptk_meandg[i][2] for i in range(len(uptk_meandg))]
        self.uptk_meandg_4 = [uptk_meandg[i][3] for i in range(len(uptk_meandg))]

        self.uptk_meandn_1 = [uptk_meandn[i][0] for i in range(len(uptk_meandn))]
        self.uptk_meandn_2 = [uptk_meandn[i][1] for i in range(len(uptk_meandn))]
        self.uptk_meandn_3 = [uptk_meandn[i][2] for i in range(len(uptk_meandn))]
        self.uptk_meandn_4 = [uptk_meandn[i][3] for i in range(len(uptk_meandn))]

        self.uptk_meands_1 = [uptk_meands[i][0] for i in range(len(uptk_meands))]
        self.uptk_meands_2 = [uptk_meands[i][1] for i in range(len(uptk_meands))]
        self.uptk_meands_3 = [uptk_meands[i][2] for i in range(len(uptk_meands))]
        self.uptk_meands_4 = [uptk_meands[i][3] for i in range(len(uptk_meands))]

        self.uptk_meandv_1 = [uptk_meandv[i][0] for i in range(len(uptk_meandv))]
        self.uptk_meandv_2 = [uptk_meandv[i][1] for i in range(len(uptk_meandv))]
        self.uptk_meandv_3 = [uptk_meandv[i][2] for i in range(len(uptk_meandv))]
        self.uptk_meandv_4 = [uptk_meandv[i][3] for i in range(len(uptk_meandv))]

      # self.pp = PdfPages(self.prefix + self.input_data_name + Dp_opt + '.pdf')

    def ghq_beta(self):
        n= self.pmidlen
        m= self.templen
        temp_range = [180, 233, 273, 298]
        pmid_range = [1000, 10000, 100000]
        beta_ait = np.zeros((n,m))
        beta_acc = np.zeros((n,m))
        beta_pca = np.zeros((n,m))
        beta_coa = np.zeros((n,m))
        for i in range(m):
            for j in range(n):
                for k in range(len(self.beta)):
                    if self.temp[k] == temp_range[i] and self.pmid[k]==pmid_range[j] and self.ghqp[k] == 2:
                        beta_ait[j,i]= self.beta[k][1]
                        beta_acc[j,i]= self.beta[k][0]
                        beta_pca[j,i]= self.beta[k][3]
                        beta_coa[j,i]= self.beta[k][2]
        levels = np.arange(1.0,2.055555,0.05)
        fig, ax = plt.subplots(2,2,figsize=(14, 10)) 

        ax[0,0].contour(temp_range, pmid_range, beta_ait, levels, colors='k')
        fills1=ax[0,0].contourf(temp_range, pmid_range, beta_ait, levels, cmap='jet')
        fig.colorbar(fills1, ax= ax[0,0])

        ax[0,1].contour(temp_range, pmid_range, beta_acc, levels, colors='k')
        fills2= ax[0,1].contourf(temp_range, pmid_range, beta_acc, levels, cmap='jet')
        fig.colorbar(fills2, ax= ax[0,1])

        ax[1,0].contour(temp_range, pmid_range, beta_pca, levels, colors='k')
        fills3=ax[1,0].contourf(temp_range, pmid_range, beta_pca, levels, cmap='jet')
        fig.colorbar(fills3, ax= ax[1,0])

        ax[1,1].contour(temp_range, pmid_range, beta_coa, levels, colors='k')
        fills4=ax[1,1].contourf(temp_range, pmid_range, beta_coa, levels, cmap='jet')
        fig.colorbar(fills4, ax= ax[1,1])
        mode = ['Aitken','Accumulation','Primary Carbon','Coarse']
        n= 0
        for i in range(2):
            for j in range(2):
                ax[i,j].set_xlabel('Temperature [K]')
                ax[i,j].set_ylabel('Pressure [Pa]')
                ax[i,j].set_title('beta of '+mode[n]+' mode')
                ax[i,j].set(yscale='log',ylim=(1e3, 1e5))
                n+=1
        fig.savefig('beta_contour.pdf')

    def ghq_convergence_dot(self):
        n= self.nghqlen
        m= (self.pmidlen) * (self.templen)
        y1 = np.zeros((m,n))
        y2 = np.zeros((m,n))
        y3 = np.zeros((m,n))
        y4 = np.zeros((m,n))
        y5 = np.zeros((m,n))
        y6 = np.zeros((m,n))
        
        for i in range(m):
#            y1[i] = [abs(self.uptk_beta_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
#            y2[i] = [abs(self.uptk_direct_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y1[i] = [abs(self.b_error[j][1]) for j in range(0+n*i,n+n*i)]
            y2[i] = [abs(self.d_error[j][1]) for j in range(0+n*i,n+n*i)]
            y3[i] = [abs(self.uptk_meandg_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y4[i] = [abs(self.uptk_meandn_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y5[i] = [abs(self.uptk_meands_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y6[i] = [abs(self.uptk_meandv_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
        x = self.ghqp[:n]
        w = 0.25
        fig, ax = plt.subplots(figsize=(10, 7))
        colors = [ 'blue', 'lightskyblue', 'green', 'sandybrown', 'violet', 'red']

# set the log scale error bar
        nn = 1
        yy1 = np.zeros(n)
        e1 = np.zeros(n)
        yy2 = np.zeros(n)
        e2 = np.zeros(n)
        yy3 = np.zeros(nn)
        e3 = np.zeros(nn)
        yy4 = np.zeros(nn)
        e4 = np.zeros(nn)
        yy5 = np.zeros(nn)
        e5 = np.zeros(nn)
        yy6 = np.zeros(nn)
        e6 = np.zeros(nn)
        for j in range(n):
            yy1[j] = sum(y1[:, j])/m
            e1[j] = np.std(y1[:, j])/yy1[j]*0.432
            yy2[j] = sum(y2[:, j])/m
            e2[j] = np.std(y2[:, j])/yy2[j]*0.432

        for j in range(1):
            yy3[j] = sum(y3[:, j])/m
            e3[j] = np.std(y3[:, j])/yy3[j]*0.432
            yy4[j] = sum(y4[:, j])/m
            e4[j] = np.std(y4[:, j])/yy4[j]*0.432
            yy5[j] = sum(y5[:, j])/m
            e5[j] = np.std(y5[:, j])/yy5[j]*0.432
            yy6[j] = sum(y6[:, j])/m
            e6[j] = np.std(y6[:, j])/yy6[j]*0.432

        err_b1 = tuple(zip(x, 10**(np.log10(yy1)-e1)))
        err_a1 = tuple(zip(x, 10**(np.log10(yy1)+e1)))
        err_b2 = tuple(zip(x, 10**(np.log10(yy2)-e2)))
        err_a2 = tuple(zip(x, 10**(np.log10(yy2)+e2)))
        xx=[1]
        err_b3 = tuple(zip(xx, 10**(np.log10(yy3)-e3)))
        err_a3 = tuple(zip(xx, 10**(np.log10(yy3)+e3)))
        err_b4 = tuple(zip(xx, 10**(np.log10(yy4)-e4)))
        err_a4 = tuple(zip(xx, 10**(np.log10(yy4)+e4)))
        err_b5 = tuple(zip(xx, 10**(np.log10(yy5)-e5)))
        err_a5 = tuple(zip(xx, 10**(np.log10(yy5)+e5)))
        err_b6 = tuple(zip(xx, 10**(np.log10(yy6)-e6)))
        err_a6 = tuple(zip(xx, 10**(np.log10(yy6)+e6)))

# Make a tuple containing those points to describe the line segment
        segments1 = tuple(zip(err_b1, err_a1))
        segments2 = tuple(zip(err_b2, err_a2))

        segments3 = tuple(zip(err_b3, err_a3))
        segments4 = tuple(zip(err_b4, err_a4))
        segments5 = tuple(zip(err_b5, err_a5))
        segments6 = tuple(zip(err_b6, err_a6))

# Create a line collection so we can plot all of the segments with one call
        bars1 = mc.LineCollection(segments1, colors=colors[0], linewidths=2.0)
        bars2 = mc.LineCollection(segments2, colors=colors[1], linewidths=2.0)
        bars3 = mc.LineCollection(segments3, colors=colors[2], linewidths=2.0, alpha=0.5)
        bars4 = mc.LineCollection(segments4, colors=colors[3], linewidths=2.0, alpha=0.5)
        bars5 = mc.LineCollection(segments5, colors=colors[4], linewidths=2.0, alpha=0.5)
        bars6 = mc.LineCollection(segments6, colors=colors[5], linewidths=2.0, alpha=0.5)

        plt.setp(ax, xticks=[1, 2, 4, 10, 20], xticklabels=['1','2', '4', '10', '20'])
        line1,=plt.plot(x, yy1, color= colors[0], linewidth=1.0, marker='.', markersize=10)
        line2,=plt.plot(x, yy2, color=colors[1], linewidth=1.0, marker='.', markersize=10)

        line3,=plt.plot(xx, yy3, color=colors[2], linewidth=1.0, marker='.', markersize=12, alpha=0.5)
        line4,=plt.plot(xx, yy4, color=colors[3], linewidth=1.0, marker='.', markersize=12, alpha=0.5)
        line5,=plt.plot(xx, yy5, color=colors[4], linewidth=1.0, marker='.', markersize=12, alpha=0.5)
        line6,=plt.plot(xx, yy6, color=colors[5], linewidth=1.0, marker='.', markersize=12, alpha=0.5)
        print(yy1)
        print(yy2)
        ax.add_collection(bars1)
        ax.add_collection(bars2)
        ax.add_collection(bars3)
        ax.add_collection(bars4)
        ax.add_collection(bars5)
        ax.add_collection(bars6)

# Remove axis lines on top and right sides
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

# Use geocat.viz.util convenience function to set axes tick values
        plt.yscale('log')
#        plt.xscale('log')
        plt.xlabel('# of Guass-Hermite quadrature points', fontsize=15)
        plt.ylabel('abs(relative error)', fontsize=15)
        fig.legend([line1, line2, line3, line4, line5, line6],["MAM method", "Gauss-Hermite method", "Using geometric mean diamater",
                   "Using number mean diamater", "Using surface mean diamater","Using volume mean diamater"],
                  ncol=2,  borderaxespad=0.,
                 bbox_to_anchor=(0.80,0.27),frameon=False, prop={'size': 12})
       #gv.set_axes_limits_and_ticks(ax, ylim=(1e-17, 1e0))

# Use geocat.viz.util convenience function to add minor and major tick lines
       #gv.add_major_minor_ticks(ax,
       #                 y_minor_per_major=5,
       #                 x_minor_per_major=1,
       #                 labelsize=14)

# Use geocat.viz.util convenience function to add title to the plot axis.
       #gv.set_titles_and_labels(ax, maintitle='Relative error of uptake rates in accumulation mode \n compared to Riemann sum using 6000 points',maintitlefontsize=18)

# Make both major and minor ticks point inwards towards the plot
        ax.tick_params(direction="in", which='both')

# Set ticks only at left and bottom sides of plot
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')

# Display Plot
        fig.savefig('gasaerexchage_quadrauture_rel_error.pdf')

    def ghq_convergence_box(self):
        """ Plot # of ghq points vs relative error parameter direct ghq, beta ghq and 4-mean using
        explicit method as the truth """
        n= self.nghqlen
        m= (self.pmidlen) * (self.templen)
        y1 = np.zeros((m,n))
        y2 = np.zeros((m,n))
        y3 = np.zeros((m,n))
        y4 = np.zeros((m,n))
        y5 = np.zeros((m,n))
        y6 = np.zeros((m,n))
        for i in range(m):
            y1[i] = [abs(self.uptk_beta_2[j]-self.uptk_rect_2[j])/self.uptk_rect_2[j] for j in range(0+n*i,n+n*i)]
            y2[i] = [abs(self.uptk_direct_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y3[i] = [abs(self.uptk_meandg_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y4[i] = [abs(self.uptk_meandn_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y5[i] = [abs(self.uptk_meands_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y6[i] = [abs(self.uptk_meandv_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
        print(y6)
        x = self.ghqp[:n]
        w = 0.25
        fig, ax = plt.subplots(figsize=(12, 6))
        boxplots = ax.boxplot(y1,
                       labels=x,
                       widths=w,
                      showfliers=False)
        boxplots1= ax.boxplot(y2, 
                       labels=x,
                       widths=w,
                      showfliers=False) 
        boxplots2= ax.boxplot(y3,
                       labels=x,
                       widths=w,
                      showfliers=False)
        boxplots3= ax.boxplot(y4,
                       labels=x,
                       widths=w,
                      showfliers=False)
        boxplots4= ax.boxplot(y5,
                       labels=x,
                       widths=w,
                      showfliers=False)
        boxplots5= ax.boxplot(y6,
                       labels=x,
                       widths=w,
                      showfliers=False)
        colors = ['orangered', 'deepskyblue', 'greenyellow', 'sandybrown', 'violet', 'aqua']
        aa=0
        for bplot in (boxplots, boxplots1, boxplots2, boxplots3, boxplots4, boxplots5):
            for elements in ['boxes', 'medians', 'whiskers', 'caps']:
                for box in bplot[elements]:
                    box.set(color=colors[aa] )
                    if elements == 'whiskers':
                        box.set(linestyle='--')
                    if elements == 'boxes':
                        box.set(linewidth=2) 
            aa+=1

# Remove axis lines on top and right sides
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

# Use geocat.viz.util convenience function to set axes tick values
        plt.yscale('log')
       # plt.xscale('log')
        plt.xlabel('# of Guass-Hermite quadrature points', fontsize=15)
        plt.ylabel('abs(relative error)', fontsize=15)

        fig.legend([boxplots["boxes"][0],boxplots1["boxes"][0],boxplots2["boxes"][0],boxplots3["boxes"][0],boxplots4["boxes"][0],boxplots5["boxes"][0]],["MAM method", "Gauss-Hermite method", "Using geometric mean diamater",
                   "Using number mean diamater", "Using surface mean diamater","Using volume mean diamater"],
                  ncol=2,  borderaxespad=0.,
                 bbox_to_anchor=(0.7,0.17),frameon=False, prop={'size': 12})
       #gv.set_axes_limits_and_ticks(ax, ylim=(1e-12, 1e2))

# Use geocat.viz.util convenience function to add minor and major tick lines
       #gv.add_major_minor_ticks(ax,
       #                 y_minor_per_major=5,
       #                 x_minor_per_major=1,
       #                 labelsize=14)

# Use geocat.viz.util convenience function to add title to the plot axis.
       #gv.set_titles_and_labels(ax, maintitle='Relative error of uptake rates compared to rectangular method using 6000 points')

# Make both major and minor ticks point inwards towards the plot
        ax.tick_params(direction="in", which='both')

# Set ticks only at left and bottom sides of plot
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')

# Display Plot
        #plt.show()
        fig.savefig('gasaerexchage_quadrauture_rel_error.pdf')

    def ghq_convergence_n1(self):
        """ Plot # of ghq points vs uptk rate parameter using direct ghq and beta ghq
        explicit method as the truth """
        n= self.nghqlen
        m= (self.pmidlen) * (self.templen)
        x = self.ghqp[:n]
        fig, axs = plt.subplots(m, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(m):
            y1 = self.uptk_beta_1[0+n*i:n+n*i]
            y2 = self.uptk_direct_1[0+n*i:n+n*i]
            y3 = self.uptk_rect_1[0+n*i:n+n*i]
            y4 = self.uptk_mean_1[0+n*i:n+n*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'go', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'yo', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y3)*1.3)
            
            
            y1 = [abs(self.uptk_beta_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y2 = [abs(self.uptk_direct_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            y3 = [abs(self.uptk_mean_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+n*i,n+n*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='log',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(1e-12, 1e2)
        fig.legend([lin1, lin2, lin3, lin4],["beta", "direct", "explicit","mean"], 
                  ncol=4,  borderaxespad=0.,
                 bbox_to_anchor=(0.7,0.935)) 
#         fig.legend([lin1, lin2, lin3],["beta", "direct", "explicit"], 
#                    ncol=3,  borderaxespad=0.,
#                   bbox_to_anchor=(0.7,0.935)) 
        fig.suptitle('Accumulation mode')
        self.pp.savefig(fig)


    def ghq_convergence_n2(self):
        """ Plot # of ghq points vs uptk rate parameter using direct ghq and beta ghq
        explicit method as the truth """
        n= self.nghqlen
        m= (self.pmidlen) * (self.templen)

        x = self.ghqp[:n]
        fig, axs = plt.subplots(m, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(m):
            y1 = self.uptk_beta_2[0+n*i:n+n*i]
            y2 = self.uptk_direct_2[0+n*i:n+n*i]
            y3 = self.uptk_rect_2[0+n*i:n+n*i]
            y4 = self.uptk_mean_2[0+n*i:n+n*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'g-', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'y-', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y1)*1.3)
            
            
            y1 = [abs(self.uptk_beta_2[j]-self.uptk_rect_2[j])/self.uptk_rect_2[j] for j in range(0+n*i,n+n*i)]
            y2 = [abs(self.uptk_direct_2[j]-self.uptk_rect_2[j])/self.uptk_rect_2[j] for j in range(0+n*i,n+n*i)]
            y3 = [abs(self.uptk_mean_2[j]-self.uptk_rect_2[j])/self.uptk_rect_2[j] for j in range(0+n*i,n+n*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='log',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(1e-12, 1e2)
        fig.legend([lin1, lin2, lin3, lin4],["MAM method", "Gauss-Hermite method", "Rectangular method with 6000 points","Using geometric mean diamater"], 
                  ncol=4,  borderaxespad=0.,
                 bbox_to_anchor=(0.7,0.935)) 
#         fig.legend([lin1, lin2, lin3],["beta", "direct", "explicit"], 
#                    ncol=3,  borderaxespad=0.,
#                   bbox_to_anchor=(0.7,0.935)) 
        
        fig.suptitle('Aitken mode')
        self.pp.savefig(fig)
        
    def ghq_convergence_n3(self):
        """ Plot # of ghq points vs uptk rate parameter using direct ghq and beta ghq
        explicit method as the truth """

        n= self.nghqlen
        m= (self.pmidlen) * (self.templen)

        x = self.ghqp[:n]
        fig, axs = plt.subplots(m, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(m):
            y1 = self.uptk_beta_3[0+n*i:n+n*i]
            y2 = self.uptk_direct_3[0+n*i:n+n*i]
            y3 = self.uptk_rect_3[0+n*i:n+n*i]
            y4 = self.uptk_mean_3[0+n*i:n+n*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'g-', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'y-', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y1)*1.3)
            
            
            y1 = [abs(self.uptk_beta_3[j]-self.uptk_rect_3[j])/self.uptk_rect_3[j] for j in range(0+n*i,n+n*i)]
            y2 = [abs(self.uptk_direct_3[j]-self.uptk_rect_3[j])/self.uptk_rect_3[j] for j in range(0+n*i,n+n*i)]
            y3 = [abs(self.uptk_mean_3[j]-self.uptk_rect_3[j])/self.uptk_rect_3[j] for j in range(0+n*i,n+n*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='log',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(1e-12, 1e2)
        fig.legend([lin1, lin2, lin3, lin4],["beta", "direct", "explicit","mean"], 
                  ncol=4,  borderaxespad=0.,
                 bbox_to_anchor=(0.7,0.935)) 
#         fig.legend([lin1, lin2, lin3],["beta", "direct", "explicit"], 
#                    ncol=3,  borderaxespad=0.,
#                   bbox_to_anchor=(0.7,0.935))
        fig.suptitle('Coarse mode')
        self.pp.savefig(fig)

    def ghq_convergence_n4(self):
        """ Plot # of ghq points vs uptk rate parameter using direct ghq and beta ghq
        explicit method as the truth """
        n= self.nghqlen
        m= (self.pmidlen) * (self.templen)

        x = self.ghqp[:n]
        fig, axs = plt.subplots(m, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(m):
            y1 = self.uptk_beta_4[0+n*i:n+n*i]
            y2 = self.uptk_direct_4[0+n*i:n+n*i]
            y3 = self.uptk_rect_4[0+n*i:n+n*i]
            y4 = self.uptk_mean_4[0+n*i:n+n*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'g-', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'y-', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y1)*1.3)
            
            
            y1 = [abs(self.uptk_beta_4[j]-self.uptk_rect_4[j])/self.uptk_rect_4[j] for j in range(0+n*i,n+n*i)]
            y2 = [abs(self.uptk_direct_4[j]-self.uptk_rect_4[j])/self.uptk_rect_4[j] for j in range(0+n*i,n+n*i)]
            y3 = [abs(self.uptk_mean_4[j]-self.uptk_rect_4[j])/self.uptk_rect_4[j] for j in range(0+n*i,n+n*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='log',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[n*i], self.pmid[n*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(1e-12, 1e2)
        fig.legend([lin1, lin2, lin3, lin4],["beta", "direct", "explicit","mean"], 
                   ncol=4,  borderaxespad=0.,
                  bbox_to_anchor=(0.7,0.935)) 
        #fig.legend([lin1, lin2, lin3],["beta", "direct", "explicit"], 
        #           ncol=3,  borderaxespad=0.,
        #          bbox_to_anchor=(0.7,0.935))
        fig.suptitle('Primary carbon mode')
        self.pp.savefig(fig)
        self.pp.close()


dp=['Dpg','Dpn','Dps','Dpv']
for i in dp:       
    plot = generate_plot(i)

#    plot.ghq_convergence_n1()
#    plot.ghq_convergence_n2()
#    plot.ghq_convergence_n3()
#    plot.ghq_convergence_n4()        

plot.ghq_convergence_dot()
plot.ghq_beta()
