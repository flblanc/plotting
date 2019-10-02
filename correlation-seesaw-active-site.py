#!/usr/bin/env python
#-*-encoding:utf-8-*-




import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#~ from scipy.stats import gaussian_kde as kde



mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 20.0

# Simulation PPS ATP 1 only
ppaw_color="mediumslateblue"# pps atp
# active site data:

as_data = np.genfromtxt("active-site-distances-ppa.dat")
ss_data = np.genfromtxt("PPA-with-waters_seesaw-distances.dat")

print as_data.shape
print ss_data.shape

d1 = as_data[:,1]
dg = as_data[:,2]

s1 = ss_data[:,2]
s2 = ss_data[:,1]

fig, axes = plt.subplots(ncols=2,nrows=2)

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 2*height)

# d1 s1

ax = axes[0,0]
ax.scatter(s1,d1,color=ppaw_color)
ax.grid()
ax.set_xlabel(u"""$s_1$, \u00c5""")
ax.set_ylabel(u"""$d_1$, \u00c5""")

# dg s1

ax = axes[0,1]
ax.scatter(s1,dg,color=ppaw_color)
ax.grid()
ax.set_xlabel(u"""$s_1$, \u00c5""")
ax.set_ylabel(u"""$d_{\\gamma}$, \u00c5""")

# d1 s2

ax = axes[1,0]
ax.scatter(s2,d1,color=ppaw_color)
ax.grid()
ax.set_xlabel(u"""$s_2$, \u00c5""")
ax.set_ylabel(u"""$d_1$, \u00c5""")

# dg s2

ax = axes[1,1]
ax.scatter(s2,dg,color=ppaw_color)
ax.grid()
ax.set_xlabel(u"""$s_2$, \u00c5""")
ax.set_ylabel(u"""$d_{\\gamma}$, \u00c5""")




plt.tight_layout()
fig.savefig("corr-as-ss.pdf")

