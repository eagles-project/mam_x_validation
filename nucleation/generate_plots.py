# This script generates plots for cross-validating the particle nucleation
# process. To generate the data needed by the script, run skywalker in the
# current directory, using nucleation.yaml as input. This writes a file called
# haero_skywalker.py to the directory, which is then imported as a module.

import sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
import numpy as np

def plot_vehkamaki2002_contour(prefix, plot_file):
    """Plot the contours of the rate of nucleation as a function of temperature
and relative humidity."""

    # Fetch scatter data from skywalker.
    data = importlib.import_module('%svehkamaki2002_contour'%prefix)
    RH, T, J = data.input.user.relative_humidity, \
               data.input.user.temperature, \
               data.output.metrics.nucleation_rate

    # Convert relative humidity to percent.
    RH = [100*rh for rh in RH]

    # Interpolate the data onto a triangulated grid.
    nx, ny = 100, 100
    RHi = np.linspace(min(RH), max(RH), nx)
    Ti = np.linspace(min(T), max(T), ny)
    triang = tri.Triangulation(RH, T)
    interpolator = tri.LinearTriInterpolator(triang, J)
#    interpolator = tri.CubicTriInterpolator(triang, J)
    Xi, Yi = np.meshgrid(RHi, Ti)
    Ji = interpolator(Xi, Yi)

    # Plot contours. We get a little fancy in order to explicitly set log levels
    # because the ticker.LogLocator doesn't "get it."
#    plt.suptitle('Nucleation rate [#/cc/sec]')
    fig, ax = plt.subplots()
    lev_exp = np.arange(-3, 11)
    levels = np.power(10., lev_exp)
    contours = ax.contour(RHi, Ti, Ji, levels, colors='k')
    fills = ax.contourf(RHi, Ti, Ji, levels, cmap='jet',
                        norm=colors.LogNorm(), extend='min')

    ax.set_xlabel('Relative humidity [%]')
    ax.set_ylabel('Temperature [K]')
    ax.set_title('Nucleation rate [#/cc/sec]')
#    ax.set_title('(H2SO4 conc = 5e8/cc)')
    fig.colorbar(fills)
#    plt.show()
    plt.savefig(prefix + plot_file)

def plot_vehkamaki2002_fig9(prefix, plot_file):
    # Fetch scatter data from skywalker.
    data = importlib.import_module('%svehkamaki2002_fig9'%prefix)
    RH, T, J = data.input.user.relative_humidity, \
               data.input.user.temperature, \
               data.output.metrics.nucleation_rate

    # Convert relative humidity to percent.
    RH = [100*rh for rh in RH]

    ax.set_xlabel('Relative humidity [%]')
    ax.set_ylabel('Temperature [K]')
    ax.set_title('Temperature [K]')
    plt.savefig(prefix + plot_file)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        prefix = ''
    else:
        prefix = sys.argv[1] + '_'
    plot_vehkamaki2002_contour(prefix, 'vehkamaki2002_contour.png')

