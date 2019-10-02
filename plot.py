#!/usr/bin/env python
#-*-encoding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 20.0

def runningMeanFast(x, N=1000):
    """Updated version with modification by Prof. Hugues Talbot."""
    x1 = np.pad(x,N,mode='reflect')
    output =np.convolve(x1, np.ones((N,))/N)[(N-1):]
    return output[N:-N]

lw = 3.5
rmf = runningMeanFast
rmsd=np.genfromtxt("active-site-rmsd.dat")
tr = rmsd[:,0]/10. # in ns
rmsd = rmsd[:,1]

tr = tr[2:]
rmsd = rmsd[2:]

fig, axes = plt.subplots(nrows=2, ncols=2,sharex='col')
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 2*height)

ax = axes[0,0]
ax.plot(tr, rmsd, color="mediumslateblue")

ax.set_ylabel(u"""Active site RMSD, \u00c5""")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


ax.set_xlim(xmin=0.0, xmax=40.0)
ax.set_ylim(ymin=0.0, ymax=1.6)
ax.set_xlabel("Time, ns")
ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')



#~ fig.savefig("rmsd-active-site.png")


#################################################################
ax = axes[0,1]
dd = np.genfromtxt("active-site-distances-ppa.dat")
tt = dd[:,0]/100.

dg = dd[:,2]

N=100


ax.plot(tt[:4000], dg[:4000], color="mediumslateblue", alpha=0.5)
ax.plot(tt[:4000], runningMeanFast(dg[:4000],N=N), color="mediumslateblue", linewidth=2.0)


ax.set_ylabel(u"""Distance $d_{\\gamma}$, \u00c5""")

ax.set_xlim(xmin=0.0, xmax=40.0)
ax.set_ylim(ymin=0.0, ymax=7.0)
ax.set_xlabel("Time, ns")
ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax = axes[1,0]
dg = np.genfromtxt("sw2_rh.dat")[:,1]

ax.plot(tt[:4000], dg[:4000], color="mediumslateblue", alpha=0.5)
ax.plot(tt[:4000], runningMeanFast(dg[:4000],N=N), color="mediumslateblue", linewidth=2.0)

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""Distance between A458O and N477ND2, \u00c5""")

ax.set_xlim(xmin=0.0, xmax=40.0)
ax.set_ylim(ymin=0.0, ymax=10.0)

ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


# critical salt bridge
ax = axes[1,1]
dd = np.genfromtxt("active-site-distances-ppa.dat")
tt = dd[:,0]/100.

dg = dd[:,1]

N=100


ax.plot(tt[:4000], dg[:4000], color="mediumslateblue", alpha=0.5)
ax.plot(tt[:4000], runningMeanFast(dg[:4000],N=N), color="mediumslateblue", linewidth=2.0)


ax.set_ylabel(u"""Distance $d_{1}$, \u00c5""")
ax.set_xlabel("Time, ns")
ax.set_xlim(xmin=0.0, xmax=40.0)
ax.set_ylim(ymin=0.0, ymax=8.0)

ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)





plt.tight_layout()

fig.savefig("as_rmsd_atp-h-bond.pdf")



###############################

dists = np.genfromtxt("coupling-distances-ppa.dat")

N = 100
b1 = rmf(dists[:,1],N)
b2 = rmf(dists[:,2],N)
b3 = rmf(dists[:,3],N)
b4 = rmf(dists[:,4],N)
b5 = rmf(dists[:,5],N)


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

ax.plot(tt,b1, color="mediumslateblue",linewidth=lw)
ax.set_ylabel(u"""$b_1$ (V149N : L455O), \u00c5""")
ax.set_xlabel("Time, ns")

ax.set_xlim(xmin=0.0, xmax=40.0)


ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[0,1]

ax.plot(tt,b2, color="mediumslateblue",linewidth=lw)
ax.set_ylabel(u"""$b_2$ (T158OG1 : D456CG), \u00c5""")
ax.set_xlabel("Time, ns")

ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[0,2]

ax.plot(tt,b3, color="mediumslateblue",linewidth=lw)
ax.set_ylabel(u"""$b_3$ (G151N : I457O), \u00c5""")
ax.set_xlabel("Time, ns")

ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[1,0]

ax.plot(tt,b4, color="mediumslateblue",linewidth=lw)
ax.set_ylabel(u"""$b_4$ (K208N : D456O), \u00c5""")
ax.set_xlabel("Time, ns")

ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax =axes[1,1]

ax.plot(tt,b5, color="mediumslateblue",linewidth=lw)
ax.set_ylabel(u"""$b_5$ (F206O : A458N), \u00c5""")
ax.set_xlabel("Time, ns")


ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax = axes[1,2]
ax.remove()

plt.tight_layout()
fig.savefig("behaviour_of_b_observables_in_MD-PPA.pdf")







exit()
#####################################################################
### Correlation with converter dynamics


conv = np.genfromtxt("/data/flblanc/angular-decomposition-NAMD/analyze-ppa.colvars.traj")
z = conv[:,3]

fig, ax = plt.subplots()
ax.plot(tt[:4000],z[0:4000],color="mediumslateblue", alpha=0.5)
ax.plot(tt[:4000], runningMeanFast(z[:4000],N=N), color="mediumslateblue", linewidth=2.0)
ax.set_xlim(xmin=0.0, xmax=40.0)


ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""Converter Z' component, \u00c5""")

fig.savefig("conv-z.png")


x = conv[:,1]

fig, ax = plt.subplots()
ax.plot(tt[:4000],x[0:4000],color="mediumslateblue", alpha=0.5)
ax.plot(tt[:4000], runningMeanFast(x[:4000],N=N), color="mediumslateblue", linewidth=2.0)
ax.set_xlim(xmin=0.0, xmax=40.0)


ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""Converter X' component, \u00c5""")

fig.savefig("conv-x.png")


y = conv[:,2]

fig, ax = plt.subplots()
ax.plot(tt[:4000],y[0:4000],color="mediumslateblue", alpha=0.5)
ax.plot(tt[:4000], runningMeanFast(y[:4000],N=N), color="mediumslateblue", linewidth=2.0)
ax.set_xlim(xmin=0.0, xmax=40.0)


ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""Converter Y' component, \u00c5""")

fig.savefig("conv-y.png")


# Distance of the converter COM from its position at the beginning of the simulation

ddc= np.sqrt(x**2 + y**2 + z**2)

ddc -= ddc[0]

fig, ax = plt.subplots()
ax.plot(tt[:4000],ddc[0:4000],color="mediumslateblue", alpha=0.5)
ax.plot(tt[:4000], runningMeanFast(ddc[:4000],N=N), color="mediumslateblue", linewidth=2.0)
ax.set_xlim(xmin=0.0, xmax=40.0)


ax.axvline(x=5.9, linestyle='--',linewidth=lw,color='red')
ax.axvline(x=29.6, linestyle='--',linewidth=lw,color='red')

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""Converter distance from t=0, \u00c5""")

fig.savefig("conv-ddc.png")
