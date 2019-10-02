#!/usr/bin/env python
#-*-encoding:utf-8-*-




import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Ellipse
import analysis_tools as at

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 20.0

CMAP = mpl.cm.get_cmap('hsv')
ii=0.0

fig, ax = plt.subplots(figsize=(12,8))


k_list =["SMD-RSH1-PR2PTS-100ns", "SMD-RSH1-PR2PTS-100ns_2"]
lb_list = ["Quaternions + distances (1)", "Quaternions + distances (2)"]

 
for j,k in enumerate(k_list) : 
    
    data = np.genfromtxt("%s/run_full-subsampled.colvars.traj" %k) 
    
    tt = data[:,0]/500000

    ncv = 10

    a = 0.8  # transparency
    lw = 2.0 # linewidth



    W = data[:,-1]
    
    
    
    
    ax.plot(tt,W,label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)),linewidth=2.5)
    ii+=1.0

ax.set_xlim(0.0,100.0)
ax.grid()
ax.set_xlabel("Time, ns")
ax.set_ylabel("Non-equilibrium work, kcal/mol")


ax.legend()
fig.savefig("work-long.pdf")
