import numpy as np
import matplotlib.pyplot as plt
import os, sys, importlib

def plot_fig1(ifname=None, ofname=None):
  if ifname is None:
    ifname = "agr00_2mode_fig1"
  if ofname is None:
    ofname = "sky_agr00_fig1.png"

  data = importlib.import_module(ifname)

  m2num = data.input.mode2_number_conc
  fn = np.array(data.output.fn)

  fig, ax1 = plt.subplots()
  ax1.plot(m2num, fn[:,0])
  ax1.set_xlabel("mode 2 number conc. [1/cc]")
  ax1.set_ylabel("mode 1 number activation frac.")
  ax1.set_ylim([0,1])
  ax1.set_yticks(np.linspace(0,1,6))
  ax1.grid()
  plt.savefig(ofname)
  plt.close(fig)

def plot_fig2(ifname=None, ofname=None):
  if ifname is None:
    ifname = "agr00_2mode_fig2"
  if ofname is None:
    ofname = "sky_agr00_fig2.png"

  data = importlib.import_module(ifname)
  m2num = data.input.mode2_number_conc
  fn = np.array(data.output.fn)

  fig, (ax1, ax2) = plt.subplots(2,1,sharex=True, sharey=True)
  ax1.plot(m2num, fn[:,0])
  ax1.set_ylabel("mode 1")
  ax1.set_ylim([0,1])
  ax1.set_xlim([0,5000])
  ax1.grid()

  ax2.plot(m2num, fn[:,1])
  ax2.set_ylabel("mode 2")
  ax2.grid()
  ax2.set_xlabel("mode 2 number conc. [1/cc]")

  fig.suptitle("number activation fraction")
  plt.savefig(ofname)
  plt.close(fig)

def plot_fig3(ifname=None, ofname=None):
  if ifname is None:
    ifname = "agr00_2mode_fig3"
  if ofname is None:
    ofname = "sky_agr00_fig3.png"

  data = importlib.import_module(ifname)
  m2sol = np.array(data.input.mode2_solubility)
  fn = np.array(data.output.fn)

  fig, (ax1, ax2) = plt.subplots(2,1,sharex=True, sharey=True)
  ax1.plot(m2sol, fn[:,0])
  ax1.set_ylabel("mode 1")
  ax1.set_ylim([0,1])
  ax1.set_xlim([0,1])
  ax1.grid()

  ax2.plot(m2sol, fn[:,1])
  ax2.set_ylabel("mode 2")
  ax2.grid()
  ax2.set_xlabel("mode 2 solubility fraction")

  fig.suptitle("number activation fraction")
  plt.savefig(ofname)
  plt.close(fig)

def plot_fig4(ifname=None, ofname=None):
  if ifname is None:
    ifname = "agr00_2mode_fig4"
  if ofname is None:
    ofname = "sky_agr00_fig4.png"

  data = importlib.import_module(ifname)
  m2rad = np.array(data.input.mode2_radius)
  fn = np.array(data.output.fn)

  fig, (ax1, ax2) = plt.subplots(2,1,sharex=True, sharey=True)
  ax1.semilogx(m2rad, fn[:,0])
  ax1.set_ylabel("mode 1")
  ax1.set_ylim([0,1])
  ax1.grid()

  ax2.semilogx(m2rad, fn[:,1])
  ax2.set_ylabel("mode 2")
  ax2.grid()
  ax2.set_xlabel("mode 2 radius (micron)")

  fig.suptitle("number activation fraction")
  plt.savefig(ofname)
  plt.close(fig)

def plot_fig5(ifname=None, ofname=None):
  if ifname is None:
    ifname = "agr00_2mode_fig5"
  if ofname is None:
    ofname = "sky_agr00_fig5.png"

  data = importlib.import_module(ifname)
  vvel = np.array(data.input.vertical_velocity)
  fn = np.array(data.output.fn)

  fig, (ax1, ax2) = plt.subplots(2,1,sharex=True, sharey=True)
  ax1.semilogx(vvel, fn[:,0])
  ax1.set_ylabel("mode 1")
  ax1.set_ylim([0,1])
  ax1.grid()

  ax2.semilogx(vvel, fn[:,1])
  ax2.set_ylabel("mode 2")
  ax2.grid()
  ax2.set_xlabel("mode 2 radius (micron)")

  fig.suptitle("updraft velocity (m/s)")
  plt.savefig(ofname)
  plt.close(fig)


if __name__ == "__main__":
  sys.path.append(os.getcwd())

  if os.path.exists("agr00_2mode_fig1.py"):
    plot_fig1()
  else:
    print("figure 1 data not found, skipping...")

  if os.path.exists("agr00_2mode_fig2.py"):
    plot_fig2()
  else:
    print("figure 2 data not found, skipping...")

  if os.path.exists("agr00_2mode_fig3.py"):
    plot_fig3()
  else:
    print("figure 3 data not found, skipping...")


  if os.path.exists("agr00_2mode_fig4.py"):
    plot_fig4()
  else:
    print("figure 4 data not found, skipping...")

  if os.path.exists("agr00_2mode_fig5.py"):
    plot_fig5()
  else:
    print("figure 5 data not found, skipping...")
