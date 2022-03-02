import os, sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

sys.path.append(os.getcwd())

class generate_plot:
    def __init__(self, Dp_opt):
        self.prefix = sys.argv[1] + '_'
        self.input_data_name = 'uptkrates_1box1gas_4sub'
        data = importlib.import_module('%s%s'%(self.prefix, self.input_data_name))

        uptk_beta, uptk_direct, uptk_rect, self.ghqp = data.output.uptkaer_beta,\
                                                  data.output.uptkaer_direct,\
                                                  data.output.uptkaer_rect, \
                                                  data.input.nghq
        if Dp_opt == 'Dpg':
            uptk_mean  = data.output.uptkaer_mean
        elif Dp_opt == 'Dpn':
            uptk_mean  = data.output.uptkaer_meandn
        elif Dp_opt == 'Dps':
            uptk_mean  = data.output.uptkaer_meands
        elif Dp_opt == 'Dpv':
            uptk_mean  = data.output.uptkaer_meandv

        self.pmid, self.temp = data.input.pmid, data.input.temp

        self.uptk_beta_1 = [uptk_beta[i][0] for i in range(len(uptk_beta))]
        self.uptk_beta_2 = [uptk_beta[i][1] for i in range(len(uptk_beta))]
        self.uptk_beta_3 = [uptk_beta[i][2] for i in range(len(uptk_beta))]
        self.uptk_beta_4 = [uptk_beta[i][3] for i in range(len(uptk_beta))]


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
        self.pp = PdfPages(self.prefix + self.input_data_name + Dp_opt + '.pdf')

    def ghq_convergence_n1(self):
        """ Plot # of ghq points vs uptk rate parameter using direct ghq and beta ghq
        explicit method as the truth """
        x = self.ghqp[:4]
        fig, axs = plt.subplots(8, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(8):
            y1 = self.uptk_beta_1[0+4*i:4+4*i]
            y2 = self.uptk_direct_1[0+4*i:4+4*i]
            y3 = self.uptk_rect_1[0+4*i:4+4*i]
            y4 = self.uptk_mean_1[0+4*i:4+4*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'g-', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'y-', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y3)*1.3)
            
            
            y1 = [abs(self.uptk_beta_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+4*i,4+4*i)]
            y2 = [abs(self.uptk_direct_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+4*i,4+4*i)]
            y3 = [abs(self.uptk_mean_1[j]-self.uptk_rect_1[j])/self.uptk_rect_1[j] for j in range(0+4*i,4+4*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(0.0, 1.0)
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
        x = self.ghqp[:4]
        fig, axs = plt.subplots(8, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(8):
            y1 = self.uptk_beta_2[0+4*i:4+4*i]
            y2 = self.uptk_direct_2[0+4*i:4+4*i]
            y3 = self.uptk_rect_2[0+4*i:4+4*i]
            y4 = self.uptk_mean_2[0+4*i:4+4*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'g-', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'y-', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y1)*1.3)
            
            
            y1 = [abs(self.uptk_beta_2[j]-self.uptk_rect_2[j])/self.uptk_rect_2[j] for j in range(0+4*i,4+4*i)]
            y2 = [abs(self.uptk_direct_2[j]-self.uptk_rect_2[j])/self.uptk_rect_2[j] for j in range(0+4*i,4+4*i)]
            y3 = [abs(self.uptk_mean_2[j]-self.uptk_rect_2[j])/self.uptk_rect_2[j] for j in range(0+4*i,4+4*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(0.0, 1.0)
        fig.legend([lin1, lin2, lin3, lin4],["beta", "direct", "explicit","mean"], 
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
        x = self.ghqp[:4]
        fig, axs = plt.subplots(8, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(8):
            y1 = self.uptk_beta_3[0+4*i:4+4*i]
            y2 = self.uptk_direct_3[0+4*i:4+4*i]
            y3 = self.uptk_rect_3[0+4*i:4+4*i]
            y4 = self.uptk_mean_3[0+4*i:4+4*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'g-', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'y-', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y1)*1.3)
            
            
            y1 = [abs(self.uptk_beta_3[j]-self.uptk_rect_3[j])/self.uptk_rect_3[j] for j in range(0+4*i,4+4*i)]
            y2 = [abs(self.uptk_direct_3[j]-self.uptk_rect_3[j])/self.uptk_rect_3[j] for j in range(0+4*i,4+4*i)]
            y3 = [abs(self.uptk_mean_3[j]-self.uptk_rect_3[j])/self.uptk_rect_3[j] for j in range(0+4*i,4+4*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(0.0, 1.0)
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
        x = self.ghqp[:4]
        fig, axs = plt.subplots(8, 2,figsize=(8, 16))
        plt.setp(axs, xticks=x, xticklabels=['2','4','10','20'])
        

        left  = 0.125  # the left side of the subplots of the figure
        right = 0.9    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure 
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.3   # the amount of width reserved for blank space between subplots
        hspace = 0.8   # the amount of height reserved for white space between subplots
        fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
        
        for i in range(8):
            y1 = self.uptk_beta_4[0+4*i:4+4*i]
            y2 = self.uptk_direct_4[0+4*i:4+4*i]
            y3 = self.uptk_rect_4[0+4*i:4+4*i]
            y4 = self.uptk_mean_4[0+4*i:4+4*i]
            lin1, = axs[i, 0].plot(x, y1, 'ro')
            lin2, = axs[i, 0].plot(x, y2, 'bo')
            lin3, = axs[i, 0].plot(x, y3, 'g-', alpha = 0.5)
            lin4, = axs[i, 0].plot(x, y4, 'y-', alpha = 0.7)
            axs[i, 0].set(ylabel = 'uptakerate [1/s]', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 0].grid()
            axs[i, 0].set_ylim(min(y4)*0.01, max(y1)*1.3)
            
            
            y1 = [abs(self.uptk_beta_4[j]-self.uptk_rect_4[j])/self.uptk_rect_4[j] for j in range(0+4*i,4+4*i)]
            y2 = [abs(self.uptk_direct_4[j]-self.uptk_rect_4[j])/self.uptk_rect_4[j] for j in range(0+4*i,4+4*i)]
            y3 = [abs(self.uptk_mean_4[j]-self.uptk_rect_4[j])/self.uptk_rect_4[j] for j in range(0+4*i,4+4*i)]
            axs[i, 1].plot(x, y1, 'ro')
            axs[i, 1].plot(x, y2, 'bo')
            axs[i, 1].plot(x, y3, 'yo')
            #axs[0, 0].plot(x, self.uptk_rect_1[:4], '.')
            axs[i, 1].set(ylabel = 'abs(relerror)', yscale='linear',
                       xlabel = 'nghq [#]', 
                       title = 'T=%s K,P=%s Pa'%(self.temp[4*i], self.pmid[4*i] ))
            axs[i, 1].grid()
            axs[i, 1].set_ylim(0.0, 1.0)
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

    plot.ghq_convergence_n1()
    plot.ghq_convergence_n2()
    plot.ghq_convergence_n3()
    plot.ghq_convergence_n4()        
