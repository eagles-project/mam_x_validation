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

def plot_vehkamaki2002_fig7(prefix, plot_file):
    # Fetch scatter data from skywalker.
    data = importlib.import_module('%svehkamaki2002_fig7'%prefix)
    RH, T, c_h2so4 = data.input.user.relative_humidity, \
                     data.input.user.temperature, \
                     data.output.metrics.nucleation_threshold

    # We are going to plot a whole bunch of concentrations at different
    # temperatures!
    xs = []
    ys = []
    Ts = [190.15 + 5.0*i for i in range(20)]
    for Ti in Ts:
        x, y = [RH[i], c_h2so4[i] for i in range(len(RH)) if abs(T[i]-Ti)<1e-6]
        plt.plot(x, y, label = 'T [K] = %g'%Ti)
    plt.legend()
    plt.xlabel('Relative humidity [-]')
    plt.ylabel('Threshold concentration of H2SO4 [1/cc]')
    plt.savefig(prefix + plot_file)

def plot_vehkamaki2002_fig9(prefix, plot_file):
    # Fetch scatter data from skywalker.
    data = importlib.import_module('%svehkamaki2002_fig9'%prefix)
    RH, c_h2so4, T, J = data.input.user.relative_humidity, \
                        data.input.user.c_h2so4, \
                        data.input.user.temperature, \
                        data.output.metrics.nucleation_rate

    # Convert relative humidity to percent.
    RH = [100*rh for rh in RH]

    fig, axs = plt.subplots(2, 1)

    # Fig 9a
    c_h2so4a, Ja = [c_h2so4[i], J[i] for i in range(len(J)) if abs(RH[i]-38.2)<1e-6]
    axs[0].plot(c_h2so4a, Ja)
    axs[0].set(xlabel = 'H2SO4 concentration [#/cc]', xscale='linear',
               ylabel = 'Nucleation rate [#/cc/s]', yscale='log',
               title = '298K, RH=38.2%')
    axs[0].set_xlim(0, 4e+10)
    axs[0].set_ylim(0.001, 1e+06)
    axs[0].grid()

    # Fig 9b
    c_h2so4b, Jb = [c_h2so4[i], J[i] for i in range(len(J)) if abs(RH[i]-52.3)<1e-6]
    axs[1].plot(c_h2so4b, Jb)
    axs[1].set(xlabel = 'H2SO4 concentration [#/cc]', xscale='linear',
               ylabel = 'Nucleation rate [#/cc/s]', yscale='log',
               title = '298K, RH=52.3%')
    axs[1].set_xlim(0, 4e+10)
    axs[1].set_ylim(0.001, 1e+06)
    axs[1].grid()

    plt.savefig(prefix + plot_file)

def plot_vehkamaki2002_fig10(prefix, plot_file):
    # Fetch scatter data from skywalker.
    data = importlib.import_module('%svehkamaki2002_fig10'%prefix)
    RH, c_h2so4, T, J = data.input.user.relative_humidity, \
                        data.input.user.c_h2so4, \
                        data.input.user.temperature, \
                        data.output.metrics.nucleation_rate

    fig, axs = plt.subplots(2, 1)

    # Fig 10a
    c_h2so4a, Ja = [c_h2so4[i], J[i] for i in range(len(J)) if abs(RH[i]-0.075)<1e-6]
    axs[0].plot(c_h2so4a, Ja)
    axs[0].set(xlabel = 'H2SO4 concentration [#/cc]', xscale='linear',
               ylabel = 'Nucleation rate [#/cc/s]', yscale='log',
               title = 'T=298K, RH=7.5%')
    axs[0].set_xlim(1e+10, 1e+12)
    axs[0].set_ylim(0.001, 1e+05)
    axs[0].grid()

    # Fig 10b
    c_h2so4b, Jb = [c_h2so4[i], J[i] for i in range(len(J)) if abs(RH[i]-15.3)<1e-6]
    axs[1].plot(c_h2so4b, Jb)
    axs[1].set(xlabel = 'H2SO4 concentration [#/cc]', xscale='linear',
               ylabel = 'Nucleation rate [#/cc/s]', yscale='log',
               title='298K, RH=15.3%')
    axs[1].set_xlim(1e+10, 1e+12)
    axs[1].set_ylim(0.001, 1e+05)
    axs[1].grid()

    plt.savefig(prefix + plot_file)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        prefix = ''
    else:
        prefix = sys.argv[1] + '_'
    plot_vehkamaki2002_contour(prefix, 'vehkamaki2002_contour.png')
    plot_vehkamaki2002_contour(prefix, 'vehkamaki2002_fig7.png')
    plot_vehkamaki2002_contour(prefix, 'vehkamaki2002_fig9.png')
    plot_vehkamaki2002_contour(prefix, 'vehkamaki2002_fig10.png')

