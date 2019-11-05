#!/usr/bin/env python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 

#plt.style.use('Solarize_Light2')

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 15.0
mpl.rcParams['lines.markersize'] = 8.0
mpl.rcParams['lines.linewidth'] = 2.0
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['legend.frameon'] = False

string1 = np.genfromtxt("optimization_4CV_unnormalized/string.average.dat")
string2 = np.genfromtxt("replica-optimization_4CV_unnormalized/string.average.dat")

guess = np.genfromtxt("replica-optimization_4CV_unnormalized/string.initial.reparam.dat")

nimages = np.shape(string1)[0]

progress_parameter = np.linspace(0,1,nimages)

fig, axes = plt.subplots(ncols=2)
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 1*height)

ax = axes[0]

ax.plot(progress_parameter, string1[:,3],marker='o', color="lawngreen",markeredgecolor='green',zorder=2,label="String optimization 1")
ax.plot(progress_parameter, string2[:,3],marker='v', color="deepskyblue",markeredgecolor='blue',zorder=2,label="String optimization 2")
ax.plot(progress_parameter, guess[:,3],marker='s', color="lightgray",markeredgecolor='darkgray',zorder=2,alpha=0.5,label="Guess path")

ax.set_xlabel("Progress parameter $\\alpha$")
ax.set_ylabel("Ring-to-ring distance $l$, \u00c5")

ax.legend()

ax = axes[1]

ax.plot(progress_parameter, string1[:,4],marker='o', color="lawngreen",markeredgecolor='green',zorder=2)
ax.plot(progress_parameter, string2[:,4],marker='v', color="deepskyblue",markeredgecolor='blue',zorder=2)
ax.plot(progress_parameter, guess[:,4],marker='s', color="lightgray",markeredgecolor='darkgray',zorder=2,alpha=0.5)

ax.set_xlabel("Progress parameter $\\alpha$")
ax.set_ylabel("End-to-end distance $L$, \u00c5")

fig.tight_layout()
fig.savefig("tails_CVs.png")




fig, axes = plt.subplots(ncols=2,sharey=True)
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 1*height)

ax = axes[0]

ax.plot(progress_parameter, string1[:,1],marker='o', color="lawngreen",markeredgecolor='green',zorder=2,label="String optimization 1")
ax.plot(progress_parameter, string2[:,1],marker='v', color="deepskyblue",markeredgecolor='blue',zorder=2,label="String optimization 2")
ax.plot(progress_parameter, guess[:,1],marker='s', color="lightgray",markeredgecolor='darkgray',zorder=2,alpha=0.5,label="Guess path")

ax.set_xlabel("Progress parameter $\\alpha$")
ax.set_ylabel("$P_1$, \u00c5")

ax.legend()

ax = axes[1]

ax.plot(progress_parameter, string1[:,2],marker='o', color="lawngreen",markeredgecolor='green',zorder=2)
ax.plot(progress_parameter, string2[:,2],marker='v', color="deepskyblue",markeredgecolor='blue',zorder=2)
ax.plot(progress_parameter, guess[:,2],marker='s', color="lightgray",markeredgecolor='darkgray',zorder=2,alpha=0.5)

ax.set_xlabel("Progress parameter $\\alpha$")
ax.set_ylabel("$P_2$, \u00c5")

fig.tight_layout()
fig.savefig("projections_CVs.png")



















plt.close('all')
