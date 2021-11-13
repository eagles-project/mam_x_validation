# This script generates plots for cross-validating the parameterization of 
# cluster growth after nucleation. 
# Before this script is executed, it is expected that a Skywalker-powered 
# test driver program has been run with multiple .yaml files as input,
# and that the output data has been written into python modules.

import os, sys, importlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.tri as tri
import numpy as np

# Look for data in whatever directory we're running in.
sys.path.append(os.getcwd())

# This function returns true if x and y are "equal" for plotting purposes,
# false if not
def equal(x, y):
    return abs(x - y) < 1e-6

# Plot results 
def plot_nucgrowth_case1_qso4a_del(prefix):
    fig_name = 'nucgrowth_case1_qso4a_del'
    data = importlib.import_module('%s%s'%(prefix, fig_name[:15]))

    dnclusterdt, qso4a_del  = data.input.dnclusterdt, data.output.qso4a_del
    qh2so4_cur = data.input.qh2so4_cur
    tmp_uptkrate = data.input.tmp_uptkrate
    cnum_h2so4 = data.input.cnum_h2so4
    radius_cluster = data.input.radius_cluster
    so4vol = data.input.so4vol

    fig, axs = plt.subplots(3, 2,figsize=(12, 8))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.3   # the amount of width reserved for blank space between subplots
    hspace = 0.8   # the amount of height reserved for white space between subplots
    fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
    
    axs[0, 0].plot(dnclusterdt, qso4a_del, '.')
    axs[0, 0].set(xlabel = 'dnclusterdt [#/cm3/s]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[0, 0].set_xlim(min(dnclusterdt)*0.7, max(dnclusterdt)*1.5)
    axs[0, 0].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[0, 0].grid()

    axs[0, 1].plot(qh2so4_cur, qso4a_del, '.')
    axs[0, 1].set(xlabel = 'qh2so4_cur [mol/mol-air]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[0, 1].set_xlim(min(qh2so4_cur)*0.7, max(qh2so4_cur)*1.5)
    axs[0, 1].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[0, 1].grid()

    axs[1, 0].plot(tmp_uptkrate, qso4a_del, '.')
    axs[1, 0].set(xlabel = 'tmp_uptkrate [1/s]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[1, 0].set_xlim(min(tmp_uptkrate)*0.7, max(tmp_uptkrate)*1.5)
    axs[1, 0].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[1, 0].grid()

    axs[1, 1].plot(cnum_h2so4, qso4a_del, '.')
    axs[1, 1].set(xlabel = 'cnum_h2so4 [#]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[1, 1].set_xlim(min(cnum_h2so4)*0.7, max(cnum_h2so4)*1.5)
    axs[1, 1].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[1, 1].grid()

    axs[2, 0].plot(radius_cluster, qso4a_del, '.')
    axs[2, 0].set(xlabel = 'radius_cluster [nm]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[2, 0].set_xlim(min(radius_cluster)*0.7, max(radius_cluster)*1.5)
    axs[2, 0].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[2, 0].grid()

    axs[2, 1].plot(so4vol, qso4a_del, '.')
    axs[2, 1].set(xlabel = 'so4vol [#/cm3]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[2, 1].set_xlim(min(so4vol)*0.7, max(so4vol)*1.5)
    axs[2, 1].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[2, 1].grid()
    
#    fig.tight_layout() 

    plt.savefig(prefix + fig_name + '.png')
    plt.clf()

def plot_nucgrowth_case1_qnuma_del(prefix):
    fig_name = 'nucgrowth_case1_qnuma_del'
    data = importlib.import_module('%s%s'%(prefix, fig_name[:15]))

    dnclusterdt, qnuma_del = data.input.dnclusterdt, data.output.qnuma_del
    qh2so4_cur = data.input.qh2so4_cur
    tmp_uptkrate = data.input.tmp_uptkrate
    cnum_h2so4 = data.input.cnum_h2so4
    radius_cluster = data.input.radius_cluster
    so4vol = data.input.so4vol

    fig, axs = plt.subplots(3, 2,figsize=(12, 8))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.3   # the amount of width reserved for blank space between subplots
    hspace = 0.8   # the amount of height reserved for white space between subplots
    fig.subplots_adjust(left, bottom, right, top, wspace, hspace)

    axs[0, 0].plot(dnclusterdt, qnuma_del, '.')
    axs[0, 0].set(xlabel = 'dnclusterdt [#/cm3/s]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[0, 0].set_xlim(min(dnclusterdt)*0.7, max(dnclusterdt)*1.5)
    axs[0, 0].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[0, 0].grid()

    axs[0, 1].plot(qh2so4_cur, qnuma_del, '.')
    axs[0, 1].set(xlabel = 'qh2so4_cur [mol/mol-air]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[0, 1].set_xlim(min(qh2so4_cur)*0.7, max(qh2so4_cur)*1.5)
    axs[0, 1].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[0, 1].grid()

    axs[1, 0].plot(tmp_uptkrate, qnuma_del, '.')
    axs[1, 0].set(xlabel = 'tmp_uptkrate [1/s]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[1, 0].set_xlim(min(tmp_uptkrate)*0.7, max(tmp_uptkrate)*1.5)
    axs[1, 0].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[1, 0].grid()

    axs[1, 1].plot(cnum_h2so4, qnuma_del, '.')
    axs[1, 1].set(xlabel = 'cnum_h2so4 [#]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[1, 1].set_xlim(min(cnum_h2so4)*0.7, max(cnum_h2so4)*1.5)
    axs[1, 1].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[1, 1].grid()

    axs[2, 0].plot(radius_cluster, qnuma_del, '.')
    axs[2, 0].set(xlabel = 'radius_cluster [nm]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[2, 0].set_xlim(min(radius_cluster)*0.7, max(radius_cluster)*1.5)
    axs[2, 0].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[2, 0].grid()

    axs[2, 1].plot(so4vol, qnuma_del, '.')
    axs[2, 1].set(xlabel = 'so4vol [#/cm3]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=1, RH=50%')
    axs[2, 1].set_xlim(min(so4vol)*0.7, max(so4vol)*1.5)
    axs[2, 1].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[2, 1].grid()

    plt.savefig(prefix + fig_name + '.png')
    plt.clf()


def plot_nucgrowth_case2_qso4a_del(prefix):
    fig_name = 'nucgrowth_case2_qso4a_del'
    data = importlib.import_module('%s%s'%(prefix, fig_name[:15]))

    dnclusterdt, qso4a_del  = data.input.dnclusterdt, data.output.qso4a_del
    qh2so4_cur = data.input.qh2so4_cur
    tmp_uptkrate = data.input.tmp_uptkrate
    cnum_h2so4 = data.input.cnum_h2so4
    radius_cluster = data.input.radius_cluster
    so4vol = data.input.so4vol  

    fig, axs = plt.subplots(3, 2,figsize=(12, 8))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.3   # the amount of width reserved for blank space between subplots
    hspace = 0.8   # the amount of height reserved for white space between subplots
    fig.subplots_adjust(left, bottom, right, top, wspace, hspace)

    axs[0, 0].plot(dnclusterdt, qso4a_del, '.')
    axs[0, 0].set(xlabel = 'dnclusterdt [#/cm3/s]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[0, 0].set_xlim(min(dnclusterdt)*0.7, max(dnclusterdt)*1.5)
    axs[0, 0].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[0, 0].grid()

    axs[0, 1].plot(qh2so4_cur, qso4a_del, '.')
    axs[0, 1].set(xlabel = 'qh2so4_cur [mol/mol-air]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[0, 1].set_xlim(min(qh2so4_cur)*0.7, max(qh2so4_cur)*1.5)
    axs[0, 1].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[0, 1].grid()

    axs[1, 0].plot(tmp_uptkrate, qso4a_del, '.')
    axs[1, 0].set(xlabel = 'tmp_uptkrate [1/s]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[1, 0].set_xlim(min(tmp_uptkrate)*0.7, max(tmp_uptkrate)*1.5)
    axs[1, 0].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[1, 0].grid()

    axs[1, 1].plot(cnum_h2so4, qso4a_del, '.')
    axs[1, 1].set(xlabel = 'cnum_h2so4 [#]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[1, 1].set_xlim(min(cnum_h2so4)*0.7, max(cnum_h2so4)*1.5)
    axs[1, 1].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[1, 1].grid()

    axs[2, 0].plot(radius_cluster, qso4a_del, '.')
    axs[2, 0].set(xlabel = 'radius_cluster [nm]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[2, 0].set_xlim(min(radius_cluster)*0.7, max(radius_cluster)*1.5)
    axs[2, 0].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[2, 0].grid()

    axs[2, 1].plot(so4vol, qso4a_del, '.')
    axs[2, 1].set(xlabel = 'so4vol [#/cm3]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[2, 1].set_xlim(min(so4vol)*0.7, max(so4vol)*1.5)
    axs[2, 1].set_ylim(min(qso4a_del)*0.7, max(qso4a_del)*1.5)
    axs[2, 1].grid()
 
    plt.savefig(prefix + fig_name + '.png')
    plt.clf()

def plot_nucgrowth_case2_qnuma_del(prefix):
    fig_name = 'nucgrowth_case2_qnuma_del'
    data = importlib.import_module('%s%s'%(prefix, fig_name[:15]))

    dnclusterdt, qnuma_del = data.input.dnclusterdt, data.output.qnuma_del
    qh2so4_cur = data.input.qh2so4_cur
    tmp_uptkrate = data.input.tmp_uptkrate
    cnum_h2so4 = data.input.cnum_h2so4
    radius_cluster = data.input.radius_cluster
    so4vol = data.input.so4vol  

    fig, axs = plt.subplots(3, 2,figsize=(12, 8))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.3   # the amount of width reserved for blank space between subplots
    hspace = 0.8   # the amount of height reserved for white space between subplots
    fig.subplots_adjust(left, bottom, right, top, wspace, hspace)

    axs[0, 0].plot(dnclusterdt, qnuma_del, '.')
    axs[0, 0].set(xlabel = 'dnclusterdt [#/cm3/s]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[0, 0].set_xlim(min(dnclusterdt)*0.7, max(dnclusterdt)*1.5)
    axs[0, 0].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[0, 0].grid()

    axs[0, 1].plot(qh2so4_cur, qnuma_del, '.')
    axs[0, 1].set(xlabel = 'qh2so4_cur [mol/mol-air]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[0, 1].set_xlim(min(qh2so4_cur)*0.7, max(qh2so4_cur)*1.5)
    axs[0, 1].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[0, 1].grid()

    axs[1, 0].plot(tmp_uptkrate, qnuma_del, '.')
    axs[1, 0].set(xlabel = 'tmp_uptkrate [1/s]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[1, 0].set_xlim(min(tmp_uptkrate)*0.7, max(tmp_uptkrate)*1.5)
    axs[1, 0].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[1, 0].grid()

    axs[1, 1].plot(cnum_h2so4, qnuma_del, '.')
    axs[1, 1].set(xlabel = 'cnum_h2so4 [#]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[1, 1].set_xlim(min(cnum_h2so4)*0.7, max(cnum_h2so4)*1.5)
    axs[1, 1].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[1, 1].grid()

    axs[2, 0].plot(radius_cluster, qnuma_del, '.')
    axs[2, 0].set(xlabel = 'radius_cluster [nm]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[2, 0].set_xlim(min(radius_cluster)*0.7, max(radius_cluster)*1.5)
    axs[2, 0].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[2, 0].grid()

    axs[2, 1].plot(so4vol, qnuma_del, '.')
    axs[2, 1].set(xlabel = 'so4vol [#/cm3]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=273K,PBL=0, RH=50%')
    axs[2, 1].set_xlim(min(so4vol)*0.7, max(so4vol)*1.5)
    axs[2, 1].set_ylim(min(qnuma_del)*0.7, max(qnuma_del)*1.5)
    axs[2, 1].grid()

    plt.savefig(prefix + fig_name + '.png')
    plt.clf()


def plot_nucgrowth_case3_qso4a_del(prefix):
    fig_name = 'nucgrowth_case3_qso4a_del'
    data = importlib.import_module('%s%s'%(prefix, fig_name[:15]))

    dnclusterdt, qso4a_del  = data.input.dnclusterdt[50:], data.output.qso4a_del[50:]
    qh2so4_cur = data.input.qh2so4_cur[50:]
    tmp_uptkrate = data.input.tmp_uptkrate[50:]
    cnum_h2so4 = data.input.cnum_h2so4[50:]
    radius_cluster = data.input.radius_cluster[50:]
    so4vol = data.input.so4vol[50:]

    fig, axs = plt.subplots(3, 2,figsize=(12, 8))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.3   # the amount of width reserved for blank space between subplots
    hspace = 0.8   # the amount of height reserved for white space between subplots
    fig.subplots_adjust(left, bottom, right, top, wspace, hspace)

    axs[0, 0].plot(dnclusterdt, qso4a_del, '.')
    axs[0, 0].set(xlabel = 'dnclusterdt [#/cm3/s]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[0, 0].set_xlim(min(dnclusterdt), max(dnclusterdt))
    axs[0, 0].set_ylim(min(qso4a_del), max(qso4a_del))
    axs[0, 0].grid()

    axs[0, 1].plot(qh2so4_cur, qso4a_del, '.')
    axs[0, 1].set(xlabel = 'qh2so4_cur [mol/mol-air]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[0, 1].set_xlim(min(qh2so4_cur), max(qh2so4_cur))
    axs[0, 1].set_ylim(min(qso4a_del), max(qso4a_del))
    axs[0, 1].grid()

    axs[1, 0].plot(tmp_uptkrate, qso4a_del, '.')
    axs[1, 0].set(xlabel = 'tmp_uptkrate [1/s]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[1, 0].set_xlim(min(tmp_uptkrate), max(tmp_uptkrate))
    axs[1, 0].set_ylim(min(qso4a_del), max(qso4a_del))
    axs[1, 0].grid()

    axs[1, 1].plot(cnum_h2so4, qso4a_del, '.')
    axs[1, 1].set(xlabel = 'cnum_h2so4 [#]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[1, 1].set_xlim(min(cnum_h2so4), max(cnum_h2so4))
    axs[1, 1].set_ylim(min(qso4a_del), max(qso4a_del))
    axs[1, 1].grid()

    axs[2, 0].plot(radius_cluster, qso4a_del, '.')
    axs[2, 0].set(xlabel = 'radius_cluster [nm]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[2, 0].set_xlim(min(radius_cluster), max(radius_cluster))
    axs[2, 0].set_ylim(min(qso4a_del), max(qso4a_del))
    axs[2, 0].grid()

    axs[2, 1].plot(so4vol, qso4a_del, '.')
    axs[2, 1].set(xlabel = 'so4vol [#/cm3]', xscale='linear',
               ylabel = 'qso4a_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[2, 1].set_xlim(min(so4vol), max(so4vol))
    axs[2, 1].set_ylim(min(qso4a_del), max(qso4a_del))
    axs[2, 1].grid()
 
    plt.savefig(prefix + fig_name + '.png')
    plt.clf()

def plot_nucgrowth_case3_qnuma_del(prefix):
    fig_name = 'nucgrowth_case3_qnuma_del'
    data = importlib.import_module('%s%s'%(prefix, fig_name[:15]))

    dnclusterdt, qnuma_del = data.input.dnclusterdt[50:], data.output.qnuma_del[50:]
    qh2so4_cur = data.input.qh2so4_cur[50:]
    tmp_uptkrate = data.input.tmp_uptkrate[50:]
    cnum_h2so4 = data.input.cnum_h2so4[50:]
    radius_cluster = data.input.radius_cluster[50:]
    so4vol = data.input.so4vol[50:]

    fig, axs = plt.subplots(3, 2,figsize=(12, 8))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.3   # the amount of width reserved for blank space between subplots
    hspace = 0.8   # the amount of height reserved for white space between subplots
    fig.subplots_adjust(left, bottom, right, top, wspace, hspace)

    axs[0, 0].plot(dnclusterdt, qnuma_del, '.')
    axs[0, 0].set(xlabel = 'dnclusterdt [#/cm3/s]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[0, 0].set_xlim(min(dnclusterdt), max(dnclusterdt))
    axs[0, 0].set_ylim(min(qnuma_del), max(qnuma_del))
    axs[0, 0].grid()

    axs[0, 1].plot(qh2so4_cur, qnuma_del, '.')
    axs[0, 1].set(xlabel = 'qh2so4_cur [mol/mol-air]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[0, 1].set_xlim(min(qh2so4_cur), max(qh2so4_cur))
    axs[0, 1].set_ylim(min(qnuma_del), max(qnuma_del))
    axs[0, 1].grid()

    axs[1, 0].plot(tmp_uptkrate, qnuma_del, '.')
    axs[1, 0].set(xlabel = 'tmp_uptkrate [1/s]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[1, 0].set_xlim(min(tmp_uptkrate), max(tmp_uptkrate))
    axs[1, 0].set_ylim(min(qnuma_del), max(qnuma_del))
    axs[1, 0].grid()

    axs[1, 1].plot(cnum_h2so4, qnuma_del, '.')
    axs[1, 1].set(xlabel = 'cnum_h2so4 [#]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[1, 1].set_xlim(min(cnum_h2so4), max(cnum_h2so4))
    axs[1, 1].set_ylim(min(qnuma_del), max(qnuma_del))
    axs[1, 1].grid()

    axs[2, 0].plot(radius_cluster, qnuma_del, '.')
    axs[2, 0].set(xlabel = 'radius_cluster [nm]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[2, 0].set_xlim(min(radius_cluster), max(radius_cluster))
    axs[2, 0].set_ylim(min(qnuma_del), max(qnuma_del))
    axs[2, 0].grid()

    axs[2, 1].plot(so4vol, qnuma_del, '.')
    axs[2, 1].set(xlabel = 'so4vol [#/cm3]', xscale='linear',
               ylabel = 'qnuma_del [mol/mol-air]', yscale='linear',
               title = 'T=233K,PBL=1, RH=50%')
    axs[2, 1].set_xlim(min(so4vol), max(so4vol))
    axs[2, 1].set_ylim(min(qnuma_del), max(qnuma_del))
    axs[2, 1].grid()

    plt.savefig(prefix + fig_name + '.png')
    plt.clf()

def usage():
    print('nucgrowth_plots.py: generates plots for MAM nucleation growth parameterizations.')
    print('usage: python3 nucgrowth_plots.py <prefix>')
    print('Here, <prefix> is prepended to each Python module containing data')
    print('computed using a Skywalker-powered driver program. The Python modules')
    print('should be named <prefix>_<figure_name>.py, where <figure_name> is')
    print('the name of a figure as represented by the YAML files in this directory.')
    print('(e.g. mam_nucgrowth_case1.py, for nucgrowth_case1.yaml)')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        prefix = sys.argv[1] + '_'
    plot_nucgrowth_case1_qso4a_del(prefix)
    plot_nucgrowth_case1_qnuma_del(prefix)
    plot_nucgrowth_case2_qso4a_del(prefix)
    plot_nucgrowth_case2_qnuma_del(prefix)
    plot_nucgrowth_case3_qso4a_del(prefix)
    plot_nucgrowth_case3_qnuma_del(prefix)

