import os, sys, importlib
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.getcwd())

''' 
 Postprocessing for time integration tests on MAM's aerosol-gas mass exchange parameterizations.
 The following functions are defined and executed:

  - __init__: load data from a python module written by the test driver

  - solution_error_and_convergence: calculate solution error w.r.t. the referece solution 
    (i.e., the one obtained with the smallest step size), then create self-convergence plots

  - plot_time_series: plot time series of some of the unknowns and other QoIs, e.g., 
    tendencies and coefficients in the equation, to show what happened in the test.

History: 

  - Initial version by Hui Wan, PNNL, Sept. 2022, with input from Jeff Johnson and Qiyang Yan.

'''

class process_time_integration_results:

    #===================================================================================
    # The __init__ function load data from the python module written by the test driver
    #===================================================================================
    def __init__(self):

        self.prefix        = 'mam_'
        self.test_name     = sys.argv[1]
        self.plot_format   = sys.argv[2]   # .pdf, .png, etc.
        self.file_basename = '%s%s'%(self.prefix, self.test_name)

        # Get test input-output data by importing the python module

        data = importlib.import_module(self.file_basename)
        print('Done importing data module '+self.file_basename+'.py')

        # Get the time step sizes

        self.dt = data.input.dt_mam
        print('Found',np.size(self.dt),'step sizes:',self.dt)

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

        print('__init__ done')

    #================================================================================================
    # Function solution_error_and_convergence calculates the absolute and relative solution errors
    # w.r.t. the referece solution (i.e., the one obtained with the smallest step size),
    # then create self-convergence plots
    #================================================================================================
    def solution_error_and_convergence(self):

        #--------------------------------------------------------------------------------------------
        # First, identify the reference solution - the one obtained with the shortest step size
        #--------------------------------------------------------------------------------------------
        # Find the shortest time step used in test 

        idt_ref = self.dt.index(min(self.dt))
        print('dt ref:',self.dt[idt_ref])

        # Find the last step in the time series (i.e., the end of the simulation)

        itime_ref = len(self.time[idt_ref]) - 1
        print('itime ref:',itime_ref)

        # Save the solution 

        so4g_ref = self.so4g[idt_ref][itime_ref]
        soag_ref = self.soag[idt_ref][itime_ref]

        #--------------------------------------------------------------------------------------------
        # Now, calculate errors w.r.t. the reference solution
        #--------------------------------------------------------------------------------------------
        # Create arrays for saving the errors and dt's for plotting

        ndt = len(self.dt)

        abs_err_so4g = np.zeros(ndt)
        abs_err_soag = np.zeros(ndt)
        rel_err_so4g = np.zeros(ndt)
        rel_err_soag = np.zeros(ndt)

        # Calculate solution error for H2SO4 gas and SOA gas at the end of each simulation

        for idt in range(ndt):

            # Find the index of the last step in the time series

            itime = len(self.so4g[idt]) - 1  # print('idt =',idt,'dt = ',self.dt[idt],'itime = ',itime)

            # Calculate absolute error

            abs_err_so4g[idt] = abs( self.so4g[idt][itime] - so4g_ref )
            abs_err_soag[idt] = abs( self.soag[idt][itime] - soag_ref )

            # Calculate relative error

            rel_err_so4g[idt] = np.where( so4g_ref !=0, abs(abs_err_so4g[idt]/so4g_ref), 0.)
            rel_err_soag[idt] = np.where( soag_ref !=0, abs(abs_err_soag[idt]/soag_ref), 0.)

        # Print results to stdout for a quick check

        debug = True
        debug = False
        if debug:
           print('abs. solution error in so4 gas mixing ratio:',abs_err_so4g)
           print('abs. solution error in soa gas mixing ratio:',abs_err_soag)
           print('rel. solution error in so4 gas mixing ratio:',rel_err_so4g)
           print('rel. solution error in soa gas mixing ratio:',rel_err_soag)

        #--------------------------------------------------------------------------------------------
        # Plot self-convergence
        #--------------------------------------------------------------------------------------------
        # Collect dt's and relative errors into tmp arrays xx and yy for plotting, skipping the 
        # reference solution

        xx = np.zeros(ndt-1)
        yy = np.zeros((2,ndt-1))   # First dimension has size 2: H2SO4 and SOAG

        ii = 0
        for idt in range(ndt):
            if idt != idt_ref:
               xx[ii]    = self.dt[idt]
               yy[0][ii] = rel_err_so4g[idt]
               yy[1][ii] = rel_err_soag[idt]
               ii += 1
            
        if debug:
           print(xx) 
           print(yy) 

        # Plot solution error against dt: panel for H2SO4 gas; one for SOA gas

        color   = ['darkorange','teal']
        title   = ['H2SO4 gas','SOA gas']
        nsubplt = len(title)

        fig,axs = plt.subplots(1,nsubplt)  # 1 row, multiple columns
        fig.subplots_adjust(left=0.15, bottom=0.15, right=0.9, top=0.75, wspace=0.4) # adjust margins

        for isubplt in range(nsubplt):

            # Error vs dt
 
            axs[isubplt].plot(xx,yy[isubplt], color=color[isubplt], marker='.')

            # An additional line to show the 1st-order slope

            if not all(yy[isubplt]==0.):
               yy_1st_order = 1.2 * xx * yy[isubplt][0]/ xx[0]
               axs[isubplt].plot(xx, yy_1st_order, color='black', linestyle='dashed')

            # Add axis labels, panel titles, grid, etc.

            if any(yy[isubplt]==0.):
               yscale='linear'
            else:
               yscale='log'
     
            axs[isubplt].set(ylabel = 'Relative error', yscale=yscale,
                             xlabel = 'Time step length (s)',  xscale ='log', title = title[isubplt]  )
            axs[isubplt].grid(axis='both',which='both') # both axes; major and minor ticks

        # Done. Save plot to file

        plt_file_fullname = self.file_basename+'_self_convergence'+self.plot_format
        fig.savefig( plt_file_fullname )
        print("Plot file:",plt_file_fullname)

    #==============================================================================================
    # The plot_time_series function plots time series of some unknowns and other QoIs, e.g., 
    # tendencies and coefficients in the equation, to show what happened in the test.
    #==============================================================================================
    def plot_time_series(self):

        print("Plotting time series")

        title = [["H2SO4 gas mixing ratio", "SOA gas mixing ratio"], 
                 ["SO4 mixing ratio",       "SOA mixing ratio"],
                 ["H2SO4 gas cond/evap rate", "SOA gas tend. due to cond/evap"],
                 ["SOAG gas amb. qsat",       "SOA # of sub-cycles"]] 
        ncol  = 2
        nrow  = 4

        it0_arr = [[0,0],[0,0],[1,1],[1,1]]  # First time slice to plot. 0 = including IC; 1 = no IC. 

        #---------------------------------------------------------------------------------------
        # Multi-panel figure. Set margins to allow for enough space for titles, tickmarks, etc.
        #---------------------------------------------------------------------------------------
        fig,axs = plt.subplots(nrow, ncol, figsize=(8,10))
        fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=0.55)

        #--------------------------------------------------------------------------------------------
        # Loop through different runs that used different step sizes
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
        plt_file_fullname = self.file_basename+'_time_series'+self.plot_format
        fig.savefig( plt_file_fullname )
        print("Plot file:",plt_file_fullname)



#===================================================================================
# Execute the functions to process test results
#===================================================================================
aa = process_time_integration_results()
aa.solution_error_and_convergence()
aa.plot_time_series()
