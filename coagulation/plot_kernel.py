import os, sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

sys.path.append(os.getcwd())

def plot_kernel_contour(prefix):
    """Plot the contours of the kernel of coagulation as a function of different Diameter pairs"""

    fig_name = 'coag_kernel'
    data = importlib.import_module('%s%s'%(prefix, fig_name))
    D1, D2, RERR = data.input.dpwet1, \
               data.input.dpwet2, \
               data.output.relative_error

    # Convert relative humidity to percent.
    RERR = [100*abs(er) for er in RERR]
    nx, ny = 100, 100
    d1 = np.linspace(min(D1), max(D1), nx)
    d2 = np.linspace(min(D2), max(D2), ny)
    triang = tri.Triangulation(D1, D2)
    interpolator = tri.LinearTriInterpolator(triang, RERR)
    Xi, Yi = np.meshgrid(d1, d2)
    Ji = interpolator(Xi, Yi)

    plt.contourf(d1, d2, Ji, cmap='jet')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('D1 [m]')
    plt.ylabel('D2 [m]')
#    plt.title('relerror abs(W-F)/F between Fuchs and Whitby kernel @T=293.15K, P=101325Pa')
    cbar = plt.colorbar()
    cbar.set_label('%')
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
    plot_kernel_contour(prefix);
