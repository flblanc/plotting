#!/usr/bin/env python
#-*-encoding:utf-8-*-




import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Ellipse

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


rmf=runningMeanFast

# Data from unbiased simulations:
ref_data = "/data/flblanc/Unbiased-replica-simulations-analysis"

pr1 = np.genfromtxt("%s/PR-with-waters.colvars.traj" %ref_data)
xpr1 = pr1[:1000,1]
ypr1 = pr1[:1000,2]
zpr1 = pr1[:1000,3]


pts1 = np.genfromtxt("%s/PTS-with-waters.colvars.traj" %ref_data)
xpts1 = pts1[:1000,1]
ypts1 = pts1[:1000,2]
zpts1 = pts1[:1000,3]

# PTS*
xptss = pts1[7000:14000,1]
yptss = pts1[7000:14000,2]
zptss = pts1[7000:14000,3]


ppa1 = np.genfromtxt("%s/PPA-with-waters.colvars.traj" %ref_data)
xppa1 = ppa1[:1000,1]
yppa1 = ppa1[:1000,2]
zppa1 = ppa1[:1000,3]

prw_color = "chartreuse"
ptsw_color= "orangered"
ppaw_color="mediumslateblue"


fig, ax = plt.subplots(figsize=(12,8))
#~ ax.set_facecolor("gainsboro")
CMAP = mpl.cm.get_cmap('Accent')
ii=0.0

k_list = [ 50.0, 100.0, 125.0, 150.0, 200.0 ]

#~ for k in [ 1.0, 5.0, 10.0, 50.0, 200.0 ] : 
for k in k_list : 
    
    data = np.genfromtxt("%s/run1.colvars.traj" %k,skip_header=4)
    
    x = data[:,2]
    y = data[:,3]
    
    #~ ax.plot(rmf(x),rmf(y),linewidth=2.0,label=u"""$k=$ %04.1f kcal/mol/\u00c5^2""" %k)
    ax.scatter(x,y,label=u"""$k=$ %04.1f kcal/mol/\u00c5^2""" %k,color=CMAP(float(len(k_list)-ii)/len(k_list)))
    
    ii+=1.0
    

ax.grid(linestyle='--')
ax.legend(fontsize=16,frameon=False)

# Add ellipses to represent the unbiased simulation data

PR = Ellipse(xy=[np.mean(xpr1),np.mean(ypr1)],width=2.*np.std(xpr1),height=2.*np.std(ypr1),color=prw_color,alpha=0.5)
ax.add_artist(PR)

PTS = Ellipse(xy=[np.mean(xpts1),np.mean(ypts1)],width=2.*np.std(xpts1),height=2.*np.std(ypts1),color=ptsw_color,alpha=0.5)
ax.add_artist(PTS)

PTSstar = Ellipse(xy=[np.mean(xptss),np.mean(yptss)],width=2.*np.std(xptss),height=2.*np.std(yptss),color="red",alpha=0.5)
ax.add_artist(PTSstar)

PPA = Ellipse(xy=[np.mean(xppa1),np.mean(yppa1)],width=2.*np.std(xppa1),height=2.*np.std(yppa1),color=ppaw_color,alpha=0.5)
ax.add_artist(PPA)

ax.set_xlabel(u"""X'""")
ax.set_ylabel(u"""Y'""")

ax.set_xlim(-25.0,+10.0)
ax.set_ylim(-12.0,+5)

#~ fig.savefig("converter.png")
#~ fig.savefig("converter.svg")
fig.savefig("converter.pdf")
    
    
    
fig, axes = plt.subplots(nrows=3,figsize=(12,8),sharex=True)



ii=0.0

k_list = [ 50.0, 100.0, 125.0, 150.0, 200.0 ]

#~ for k in [ 1.0, 5.0, 10.0, 50.0, 200.0 ] : 

for k in k_list : 
    
    data = np.genfromtxt("%s/run1.colvars.traj" %k,skip_header=4)
    
    tt = data[:,0]*2./1e6
    
    x = data[:,2]
    y = data[:,3]
    z = data[:,4]
    
    
    
    ax = axes[0]
    ax.plot(tt,x,label=u"""$k=$ %04.1f kcal/mol/\u00c5^2""" %k,color=CMAP(float(len(k_list)-ii)/len(k_list)))
    
    ax = axes[1]
    ax.plot(tt,y,color=CMAP(float(len(k_list)-ii)/len(k_list)))
    
    ax = axes[2]
    ax.plot(tt,z,color=CMAP(float(len(k_list)-ii)/len(k_list)))
    
    ii+=1.0


ax = axes[0]

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""X', \u00c5""")
ax.grid()

#~ ax.axhline(np.mean(xpr1),color=prw_color,linestyle='--',linewidth=1.5)
#~ ax.axhspan(np.mean(xpr1)-np.std(xpr1),np.mean(xpr1)+np.std(xpr1),color=prw_color,alpha=0.5)

ax.axhline(np.mean(xpts1),color=ptsw_color,linestyle='--',linewidth=1.5)
ax.axhspan(np.mean(xpts1)-np.std(xpts1),np.mean(xpts1)+np.std(xpts1),color=ptsw_color,alpha=0.5)

ax.axhline(np.mean(xppa1),color=ppaw_color,linestyle='--',linewidth=1.5)
ax.axhspan(np.mean(xppa1)-np.std(xppa1),np.mean(xppa1)+np.std(xppa1),color=ppaw_color,alpha=0.5)


ax = axes[1]

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""Y', \u00c5""")
ax.grid()

#~ ax.axhline(np.mean(ypr1),color=prw_color,linestyle='--',linewidth=1.5)
#~ ax.axhspan(np.mean(ypr1)-np.std(ypr1),np.mean(ypr1)+np.std(ypr1),color=prw_color,alpha=0.5)

ax.axhline(np.mean(ypts1),color=ptsw_color,linestyle='--',linewidth=1.5)
ax.axhspan(np.mean(ypts1)-np.std(ypts1),np.mean(ypts1)+np.std(ypts1),color=ptsw_color,alpha=0.5)

ax.axhline(np.mean(yppa1),color=ppaw_color,linestyle='--',linewidth=1.5)
ax.axhspan(np.mean(yppa1)-np.std(yppa1),np.mean(yppa1)+np.std(yppa1),color=ppaw_color,alpha=0.5)

ax = axes[2]

ax.set_xlabel("Time, ns")
ax.set_ylabel(u"""Z', \u00c5""")
ax.grid()

#~ ax.axhline(np.mean(zpr1),color=prw_color,linestyle='--',linewidth=1.5)
#~ ax.axhspan(np.mean(zpr1)-np.std(zpr1),np.mean(zpr1)+np.std(zpr1),color=prw_color,alpha=0.5)

ax.axhline(np.mean(zpts1),color=ptsw_color,linestyle='--',linewidth=1.5)
ax.axhspan(np.mean(zpts1)-np.std(zpts1),np.mean(zpts1)+np.std(zpts1),color=ptsw_color,alpha=0.5)

ax.axhline(np.mean(zppa1),color=ppaw_color,linestyle='--',linewidth=1.5)
ax.axhspan(np.mean(zppa1)-np.std(zppa1),np.mean(zppa1)+np.std(zppa1),color=ppaw_color,alpha=0.5)

plt.tight_layout()

#~ fig.savefig("converter-ts.png")
fig.savefig("converter-ts.pdf")
    

