#!/usr/bin/env python
#-*-encoding:utf-8-*-


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 20.0


def runningMeanFast(x, N=100):
    """Updated version with modification by Prof. Hugues Talbot."""
    x1 = np.pad(x,N,mode='reflect')
    output =np.convolve(x1, np.ones((N,))/N)[(N-1):]
    return output[N:-N]
    
rmf=runningMeanFast

pr1 = np.genfromtxt("PR-with-waters/kink-rmsd_pts.dat")
pr1[:,1] = pr1[:,1] - np.genfromtxt("PR-with-waters/kink-rmsd_pr.dat")[:,1]





pr2 = np.genfromtxt("PR-with-waters-2/kink-rmsd_pts.dat")
pr2[:,1] = pr2[:,1] - np.genfromtxt("PR-with-waters-2/kink-rmsd_pr.dat")[:,1]

pts1 = np.genfromtxt("PTS-with-waters/kink-rmsd_pts.dat")
pts1[:,1] = pts1[:,1] - np.genfromtxt("PTS-with-waters/kink-rmsd_pr.dat")[:,1]


pts2 = np.genfromtxt("PTS-with-waters-2/kink-rmsd_pts.dat")
pts2[:,1] = pts2[:,1] - np.genfromtxt("PTS-with-waters-2/kink-rmsd_pr.dat")[:,1]

ppa1 = np.genfromtxt("PPA-with-waters/kink-rmsd_pts.dat")
ppa1[:,1] = ppa1[:,1] - np.genfromtxt("PPA-with-waters/kink-rmsd_pr.dat")[:,1]


ppa2 = np.genfromtxt("PPA-with-waters-2/kink-rmsd_pts.dat")
ppa2[:,1] = ppa2[:,1] - np.genfromtxt("PPA-with-waters-2/kink-rmsd_pr.dat")[:,1]


fig, axes = plt.subplots(ncols=3,sharey=True)
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(3*width, 1*height)

lw = 2.5

# PR
ax = axes[0]


ax.plot(pr1[:,0]/100.0,rmf(pr1[:,1]),color='darkgreen',label="PR aMD (1)",linewidth=lw)
ax.plot(pr2[:,0]/100.0,rmf(pr2[:,1]),color='lightgreen',label="PR aMD (2)",linewidth=lw)
ax.grid()
ax.set_ylim(-1.4,+1.4)

ax.legend(loc='lower right',frameon=False)

ax.set_ylabel(u"""Relay Helix kink \u0394RMSD, \u00c5""")

# PTS 
ax = axes[1]
ax.plot(pts1[:,0]/100.0,rmf(pts1[:,1]),color='darkred',label="PTS aMD (1)",linewidth=lw)
ax.plot(pts2[:,0]/100.0,rmf(pts2[:,1]),color='red',label="PTS aMD (2)",linewidth=lw)
ax.grid()
ax.set_xlabel("Time, ns")

ax.legend(loc='upper right',frameon=False)

# PPS 
ax = axes[2]
ax.plot(ppa1[:,0]/100.0,rmf(ppa1[:,1]),color='darkblue',label="PPS aMD (1)",linewidth=lw)
ax.plot(ppa2[:,0]/100.0,rmf(ppa2[:,1]),color='lightblue',label="PPS aMD (2)",linewidth=lw)
ax.grid()

ax.legend(loc='upper left',frameon=False)

plt.tight_layout()
fig.savefig("kink-drmsd.png")
fig.savefig("kink-drmsd.pdf")
