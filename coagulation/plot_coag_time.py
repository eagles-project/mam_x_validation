import os, sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from scipy import stats

sys.path.append(os.getcwd())

def plot_coag_time(prefix):
    """Plot the errors of the time convergence of coagulation as a function of timesteps"""

    fig_name = 'coag_time'
    data = importlib.import_module('%s%s'%(prefix, fig_name))
    selferrornumRK4 = data.output.rel_self_num_RK4
    selferrornumcur = data.output.rel_self_num_cur
    selferrornumFE = data.output.rel_self_num_FE
    selferroraerRK4 = data.output.rel_self_aer_RK4
    selferroraercur = data.output.rel_self_aer_cur
    selferroraerFE = data.output.rel_self_aer_FE
    x=data.input.deltat
    n= len(x)
    list_RK4_qnait = [abs(selferrornumRK4[i][1]) for i in range(1,n)]
    list_RK4_qnpca = [abs(selferrornumRK4[i][3]) for i in range(1,n)]
    list_RK4_qnacc = [abs(selferrornumRK4[i][0]) for i in range(1,n)]
    list_RK4_qaait_so4 = [abs(selferroraerRK4[i][1]) for i in range(1,n)]
    list_RK4_qapca_so4 = [abs(selferroraerRK4[i][3]) for i in range(1,n)]
    list_RK4_qaacc_so4 = [abs(selferroraerRK4[i][0]) for i in range(1,n)]

    list_cur_qnait = [abs(selferrornumcur[i][1]) for i in range(1,n)]
    list_cur_qnpca = [abs(selferrornumcur[i][3]) for i in range(1,n)]
    list_cur_qnacc = [abs(selferrornumcur[i][0]) for i in range(1,n)]
    list_cur_qaait_so4 = [abs(selferroraercur[i][1]) for i in range(1,n)]
    list_cur_qapca_so4 = [abs(selferroraercur[i][3]) for i in range(1,n)]
    list_cur_qaacc_so4 = [abs(selferroraercur[i][0]) for i in range(1,n)]

    list_FE_qnait = [abs(selferrornumFE[i][1]) for i in range(1,n)]
    list_FE_qnpca = [abs(selferrornumFE[i][3]) for i in range(1,n)]
    list_FE_qnacc = [abs(selferrornumFE[i][0]) for i in range(1,n)]
    list_FE_qaait_so4 = [abs(selferroraerFE[i][1]) for i in range(1,n)]
    list_FE_qapca_so4 = [abs(selferroraerFE[i][3]) for i in range(1,n)]
    list_FE_qaacc_so4 = [abs(selferroraerFE[i][0]) for i in range(1,n)]
    print(list_RK4_qaait_so4)
    print(list_RK4_qnait)
    print(list_cur_qaait_so4, list_FE_qaait_so4)
    print(list_cur_qnait, list_FE_qnait)
    f =x[1:]
    # Create figure with 6 axes
    fig, axes = plt.subplots(figsize=(7, 10), nrows=3, ncols=2)
    plt.subplots_adjust(wspace=0.3, hspace=.4)

    # Plot first graph
    axesList = [axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1], axes[2, 0], axes[2, 1]]

    # Create array of titles of each plot
    titles = ['qnRK4', 'qaRK4_so4', 'qnMAM', 'qaMAM_so4','qnFE', 'qaFE_so4']

    # Set standard alpha (transparency) value
    alpha = 1

    slope, intercept, r, p, std_err = stats.linregress(np.log(f), np.log(list_RK4_qnait))
    print('slope of RK4 result is ', slope)
    slope, intercept, r, p, std_err = stats.linregress(np.log(f), np.log(list_cur_qnait))
    print('slope of MAM result is ', slope)
    slope, intercept, r, p, std_err = stats.linregress(np.log(f), np.log(list_FE_qnait))
    print('slope of FE result is ', slope)
    # Plot first graph:
    line1, = axesList[0].plot(f, list_RK4_qnait, color='red')
    line2, = axesList[0].plot(f, list_RK4_qnacc, color='limegreen')
    line3, = axesList[0].plot(f, list_RK4_qnpca, color='blue')
    # 
    line1, = axesList[1].plot(f, list_RK4_qaait_so4, color='red', alpha=alpha)
    line2, = axesList[1].plot(f, list_RK4_qaacc_so4, color='limegreen', alpha=alpha)
    line3, = axesList[1].plot(f, list_RK4_qapca_so4, color='blue', alpha=alpha)
    #cur
    line1, = axesList[2].plot(f, list_cur_qnait, color='red')
    line2, = axesList[2].plot(f, list_cur_qnacc, color='limegreen')
    line3, = axesList[2].plot(f, list_cur_qnpca, color='blue')
     
    line1, = axesList[3].plot(f, list_cur_qaait_so4, color='red', alpha=alpha)
    line2, = axesList[3].plot(f, list_cur_qaacc_so4, color='limegreen', alpha=alpha)
    line3, = axesList[3].plot(f, list_cur_qapca_so4, color='blue', alpha=alpha)
    #FE
    line1, = axesList[4].plot(f, list_FE_qnait, color='red')
    line2, = axesList[4].plot(f, list_FE_qnacc, color='limegreen')
    line3, = axesList[4].plot(f, list_FE_qnpca, color='blue')
     
    line1, = axesList[5].plot(f, list_FE_qaait_so4, color='red', alpha=alpha)
    line2, = axesList[5].plot(f, list_FE_qaacc_so4, color='limegreen', alpha=alpha)
    line3, = axesList[5].plot(f, list_FE_qapca_so4, color='blue', alpha=alpha)

    # Create ticks, axis limits, and title s for each of the 6 plots
    for i in range(6):
        axesList[i].set(ylabel = 'Error [%]', yscale='log',
                       xlabel = 'deltat[s]', xscale ='log',
                       title = titles[i])
        axesList[i].set_ylim(1e-15,1e3)
    fig.legend((line1, line2, line3), ('ait', 'acc', 'pca'), ncol = 3, borderaxespad=0.,
                  bbox_to_anchor=(0.7,0.935))
    plt.savefig(prefix + fig_name + '.png')
    plt.clf()

def usage():
    print('usage: python3 plot_*.py <prefix>')
    print('Here, <prefix> is prepended to each Python module containing data')
    print('computed using a Skywalker-powered driver program. The Python modules')
    print('should be named <prefix>_<figure_name>.py, where <figure_name> is')
    print('the name of a figure as represented by the YAML files in this directory.')
    print('(e.g. haero_vehkamaki2002_contour.py, for vehkamaki2002_contour.yaml)')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        prefix = sys.argv[1] + '_'
    plot_coag_time(prefix);
