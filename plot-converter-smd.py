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



CMAP = mpl.cm.get_cmap('hsv')
ii=0.0

fig2, ax2 = plt.subplots(figsize=(12,8))


k_list =["smd_conv_PR2PTS_1", "smd_conv_PR2PTS_2", "smd_conv_PR2PTS_3", "smd_conv_PTS2PR_1"]
lb_list = ["PR to PTS (1)", "PR to PTS (2)", "PR to PTS (3)", "PTS to PR"]

#~ for k in [ 1.0, 5.0, 10.0, 50.0, 200.0 ] : 
for j,k in enumerate(k_list) : 
    
    data = np.genfromtxt("%s/smd.colvars.traj" %k,skip_header=4)
    data2 = np.genfromtxt("%s/smd2.colvars.traj" %k,skip_header=4,skip_footer=1)
    
    x = np.r_[data[:,2],data2[:,2]]
    x = x[:50000]
    x = x[::5]
    print x[::10].shape
    y = data[:,3]
    
    z = np.genfromtxt("%s/kink-rmsd_pts.dat" %k)[:,1] - np.genfromtxt("%s/kink-rmsd_pr.dat" %k)[:,1]
    z = z[:1000]
    print z.shape
    
    #~ ax.plot(rmf(x),rmf(y),linewidth=2.0,label=u"""$k=$ %04.1f kcal/mol/\u00c5^2""" %k)
    ax2.scatter(x[::10],z,label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)))
    
    ii+=1.0
    


    

ax2.grid(linestyle='--')
ax2.legend(fontsize=16,frameon=False)

ax2.set_xlabel(u"""X'""")
ax2.set_ylabel(u"""Relay Helix kink \u0394RMSD""")

ax2.set_xlim(-25.0,+10.0)
ax2.set_ylim(-1.4,+1.4)


fig2.savefig("converter_kink_smd.pdf")
    




exit()




    
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

fig.savefig("converter-ts.png")
    

