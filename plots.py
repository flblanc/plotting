#!/usr/bin/env python
#-*-encoding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 20.0
N=200
def runningMeanFast(x, N=N):
    """Updated version with modification by Prof. Hugues Talbot."""
    x1 = np.pad(x,N,mode='reflect')
    output =np.convolve(x1, np.ones((N,))/N)[(N-1):]
    return output[N:-N]
rmf = runningMeanFast
lw = 3.5


dists = np.genfromtxt("as-dist.dat")


tt = dists[:,0]/100.

d1 = dists[:,1]
dg = dists[:,2]
rh = dists[:,3]

fig, axes = plt.subplots(ncols=1,nrows=3,sharex=True)
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 3*height)


ax = axes[0]

ax.plot(tt,dg)

#~ ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""$d_{\\gamma}$, \u00c5""")
ax.annotate(s="Hydrogen bond formation", xy = (58.0, 3.5), xytext=(80,6.0),arrowprops=dict(facecolor='black',width=2.0,linewidth=1.0,shrink=0.1))



ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_xlim(0.0,tt[-1])

ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")


ax = axes[1]

ax.plot(tt,d1)

#~ ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""$d_1$, \u00c5""")
ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)



ax = axes[2]

ax.plot(tt,rh)

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""A458O : N477ND2 distance, \u00c5""")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)



ax.set_xlim(0.0,tt[-1])

ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")

#~ fig.savefig("rh.pdf")
plt.tight_layout()
fig.savefig("distances_during_smd_then_static_along_distances.pdf")




dists = np.genfromtxt("coupling_distances.dat")


b1 = dists[:,1]
b2 = dists[:,2]
b3 = dists[:,3]
b4 = dists[:,4]
b5 = dists[:,5]

def rampe(xi,xf):
    a = xi + (tt[:1500]/tt[1500])*(xf-xi)
    b = xf*np.ones(tt[1500:].shape)
    return np.r_[a,b]


fig, axes = plt.subplots(ncols=3,nrows=2,sharex='col')
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(3*width, 2*height)


# 

#~ colvars:   The force constant for colvar "dist1" will be rescaled to 49.3827 according to the specified width.
#~ colvars:   The force constant for colvar "dist2" will be rescaled to 640 according to the specified width.
#~ colvars:   The force constant for colvar "dist3" will be rescaled to 6.77404 according to the specified width.
#~ colvars:   The force constant for colvar "dist4" will be rescaled to 1777.78 according to the specified width.
#~ colvars:   The force constant for colvar "dist5" will be rescaled to 5.91716 according to the specified width.

ax =axes[0,0]

ax.plot(tt,b1)
ax.plot(tt,rampe(3.01,3.91),linestyle='--')
ax.set_ylabel(u"""$b_1$, \u00c5""")
ax.set_xlabel("Time, ns")
ax.set_xlim(0.0,120.0)



ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[0,1]

ax.plot(tt,b2)
ax.plot(tt,rampe(3.51,3.26),linestyle='--')
ax.set_ylabel(u"""$b_2$, \u00c5""")
ax.set_xlabel("Time, ns")
ax.set_xlim(0.0,120.0)


ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[0,2]

ax.plot(tt,b3)
ax.plot(tt,rampe(4.52,6.95),linestyle='--')
ax.set_ylabel(u"""$b_3$, \u00c5""")
ax.set_xlabel("Time, ns")
ax.set_xlim(0.0,120.0)


ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[1,0]

ax.plot(tt,b4)
ax.plot(tt,rampe(2.97,2.82),linestyle='--')
ax.set_ylabel(u"""$b_4$, \u00c5""")
ax.set_xlabel("Time, ns")
ax.set_xlim(0.0,120.0)


ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[1,1]

ax.plot(tt,b5)
ax.plot(tt,rampe(6.59,3.99),linestyle='--')
ax.set_ylabel(u"""$b_5$, \u00c5""")
ax.set_xlabel("Time, ns")
ax.set_xlim(0.0,120.0)


ax.axvline(x=15.0,linewidth=lw,linestyle='--',color="gray")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax = axes[1,2]
ax.remove()

plt.tight_layout()
fig.savefig("drivers_during_smd_then_static_along_distances.pdf")









