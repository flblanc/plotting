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




fig, ax = plt.subplots(figsize=(12,8))
#~ ax.set_facecolor("gainsboro")
CMAP = mpl.cm.get_cmap('hsv')
ii=0.0
k_list = [ 50.0, 100.0, 125.0, 150.0, 200.0 ] 
#~ k_list =[ 500.0, 1000.0, 2000.0, 5000.0, 10000.0 ]

nrows = len(k_list)/3 + int(len(k_list)%3!=0)

fig, axes = plt.subplots(figsize=(12,8),nrows=nrows,ncols=3,sharex=True,sharey=True)




for i,k in enumerate(k_list) : 
    
    
    m = i/3
    n = i%3
    
    ax = axes[m,n]
    
    data = np.genfromtxt("%s/run1.colvars.traj" %k,skip_header=4)
    
    s1 = data[:,5]
    s2 = data[:,6]
    
    s1_c = data[:,7]
    s2_c = data[:,8]
    
    #~ ax.plot(rmf(x),rmf(y),linewidth=2.0,label=u"""$k=$ %04.1f kcal/mol/\u00c5^2""" %k)
    
    ax.scatter(s1,s2,label=u"""$k=$ %04.1f kcal/mol/\u00c5$^2$""" %k,color=CMAP(float(len(k_list)-ii)/len(k_list)))
    ax.plot(s1_c,s2_c,linewidth=1.5,color="black",linestyle='--')
    
    ii+=1.0
    ax.grid(linestyle='--')
    ax.legend(fontsize=10,frameon=False)

    ax.set_xlabel(u"""$s_1$, \u00c5""")
    ax.set_ylabel(u"""$s_2$,\u00c5""")

axes[1,2].remove()

plt.tight_layout()

#~ fig.savefig("bias.png")
#~ fig.savefig("bias.svg")
fig.savefig("bias.pdf")
    
