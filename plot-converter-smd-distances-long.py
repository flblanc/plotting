#!/usr/bin/env python
#-*-encoding:utf-8-*-




import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Ellipse
import analysis_tools as at
from scipy.stats import gaussian_kde as kde

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

CMAP = mpl.cm.get_cmap('hsv')
ii=0.0


fig, axes = plt.subplots(nrows=4,ncols=1,sharex='col')#,figsize=(12,8))
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 4*height)

ax1 = axes[0]
ax2 = axes[1]
ax3 = axes[2]
ax4 = axes[3]

ax1.set_xlim(0.0,100.0)

#~ BEGIN distance
#~ --TITLE n1
#~ --SELE /A/65/CA : /A/707/CA
#~ --TITLE n2
#~ --SELE /A/66/CA : /A/763/CA
#~ --TITLE n3
#~ --SELE /A/492/CD : /A/708/CZ
#~ --TITLE n4
#~ --SELE /A/499/CA : /A/753/CA
#~ END

ax1.set_ylabel(u"""Distance L65CA : S707CA, \u00c5""")
ax2.set_ylabel(u"""Distance M66CA : F763CA, \u00c5""")
ax3.set_ylabel(u"""Distance E492CD : R708CZ, \u00c5""")
ax4.set_ylabel(u"""Distance E499CA : L753CA, \u00c5""")


ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

ax4.set_xlabel("Time, ns")

k_list =["SMD-RSH1-PR2PTS-100ns", "SMD-RSH1-PR2PTS-100ns_2"] #, "SMD-RSH1-quaternions-PR2PTS-100ns"]
lb_list = ["Quaternions + distances (1)", "Quaternions + distances (2)"] #, "Quaternions only"]


for j,k in enumerate(k_list) : 
    
    data = np.genfromtxt("%s/nter-distances.dat" %k) 
    
    tt = data[:,0]/100

    n1 = rmf(data[:,1])
    n2 = rmf(data[:,2])
    n3 = rmf(data[:,3])
    n4 = rmf(data[:,4])
    
    
    ax1.plot(tt,n1,label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)),linewidth=lw)
    ax2.plot(tt,n2,label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)),linewidth=lw)
    ax3.plot(tt,n3,label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)),linewidth=lw)
    ax4.plot(tt,n4,label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)),linewidth=lw)


    
    ii+=1.0

ax1.legend()

plt.tight_layout()
fig.savefig("distances-nter-smd-long.pdf")

    

