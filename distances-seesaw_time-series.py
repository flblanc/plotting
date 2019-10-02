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
N=200
def runningMeanFast(x, N=N):
    """Updated version with modification by Prof. Hugues Talbot."""
    x1 = np.pad(x,N,mode='reflect')
    output =np.convolve(x1, np.ones((N,))/N)[(N-1):]
    return output[N:-N]


rmf=runningMeanFast

prw_color = "chartreuse"
prwr_color = "#4B8F8C"
prwr2_color = "#9CC5A1"



ptsw_color= "orangered"
ptswr_color="yellow"
ptswr2_color="brown"

ppaw_color="mediumslateblue"# pps atp
ppawr_color= "#3943B7"
ppawr2_color= "#5F758E"

ppiw_color="aquamarine"      # pih pps
ppiwr_color="darkturquoise"  





name = "seesaw_cv"
suffix = "seesaw_cv-19apr18"

data_rep="."


obs_prw  = np.genfromtxt("%s/PR-with-waters_seesaw-distances.dat" %data_rep)
obs_prwr = np.genfromtxt("%s/PR-with-waters-replica_seesaw-distances.dat" %data_rep)
obs_prwr2 = np.genfromtxt("%s/PR-with-waters-replica2_seesaw-distances.dat" %data_rep)

obs_ptsw = np.genfromtxt("%s/PTS-with-waters_seesaw-distances.dat" %data_rep)
obs_ptswr = np.genfromtxt("%s/PTS-with-waters-replica_seesaw-distances.dat" %data_rep)
obs_ptswr2 = np.genfromtxt("%s/PTS-with-waters-replica2_seesaw-distances.dat" %data_rep)

obs_ppaw = np.genfromtxt("%s/PPA-with-waters_seesaw-distances.dat" %data_rep)
obs_ppawr = np.genfromtxt("%s/PPA-with-waters-replica_seesaw-distances.dat" %data_rep)
obs_ppawr2 = np.genfromtxt("%s/PPA-with-waters-replica2_seesaw-distances.dat" %data_rep)

obs_ppiw = np.genfromtxt("%s/PPI-with-waters_seesaw-distances.dat" %data_rep)
obs_ppiwr = np.genfromtxt("%s/PPI-with-waters-replica_seesaw-distances.dat" %data_rep)


#~ obs_xray = np.genfromtxt("%s/XRAY_seesaw-distances.dat" %data_rep)
    
# Time

tt_prw = obs_prw[:,0]/100.0
tt_prwr = obs_prwr[:,0]/100.0
tt_prwr2 = obs_prwr2[:,0]/100.0


tt_ptsw = obs_ptsw[:,0]/100.0
tt_ptswr = obs_ptswr[:,0]/100.0
tt_ptswr2 = obs_ptswr2[:,0]/100.0

tt_ppaw = obs_ppaw[:,0]/100.0
tt_ppawr = obs_ppawr[:,0]/100.0
tt_ppawr2 = obs_ppawr2[:,0]/100.0


tt_ppiw = obs_ppiw[:,0]/100.0
tt_ppiwr = obs_ppiwr[:,0]/100.0

# s2
y_prw = obs_prw[:,1]
y_prwr = obs_prwr[:,1]
y_prwr2 = obs_prwr2[:,1]




y_ppaw = obs_ppaw[:,1]
y_ppawr = obs_ppawr[:,1]
y_ppawr2 = obs_ppawr2[:,1]

y_ppiw = obs_ppiw[:,1]
y_ppiwr = obs_ppiwr[:,1]

y_ptsw = obs_ptsw[:,1]
y_ptswr = obs_ptswr[:,1]
y_ptswr2 = obs_ptswr2[:,1]


# s1
x_prw = obs_prw[:,2]
x_prwr = obs_prwr[:,2]
x_prwr2 = obs_prwr2[:,2]




x_ppaw = obs_ppaw[:,2]
x_ppawr = obs_ppawr[:,2]
x_ppawr2 = obs_ppawr2[:,2]

x_ppiw = obs_ppiw[:,2]
x_ppiwr = obs_ppiwr[:,2]

x_ptsw = obs_ptsw[:,2]
x_ptswr = obs_ptswr[:,2]
x_ptswr2 = obs_ptswr2[:,2]


fig, axes = plt.subplots(ncols=2,nrows=3,sharey='col')

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 3*height)

# s1

# PR
fs=15
lw = 2.5
ax = axes[0,0]

ax.plot(tt_prw,rmf(x_prw),color=prw_color,label="PR+ATP (1)",linewidth=lw)
ax.plot(tt_prwr,rmf(x_prwr),color=prwr_color,label="PR+ATP (2)",linewidth=lw)
ax.plot(tt_prwr2,rmf(x_prwr2),color=prwr2_color,label="PR+ATP (3)",linewidth=lw)
ax.grid()
ax.legend(loc='best',fontsize=fs,frameon=False,markerscale=10.0)

ax.set_xlim(0.0,200.0)
ax.set_ylim(11.0,15.0)

ax.set_ylabel(u"""$s_1$, \u00c5""",fontsize=fs)


# PTS 

ax = axes[1,0]

ax.plot(tt_ptsw,rmf(x_ptsw), color=ptsw_color,label="PTS+ATP (1)",linewidth=lw)
ax.plot(tt_ptswr,rmf(x_ptswr), color=ptswr_color,label="PTS+ATP (2)",linewidth=lw)
ax.plot(tt_ptswr2,rmf(x_ptswr2), color=ptswr2_color,label="PTS+ATP (3)",linewidth=lw)

ax.axhline(np.mean(x_prw),linewidth=1.5*lw, linestyle='--',color='green')

ax.grid()
ax.legend(loc='best',fontsize=fs,frameon=False,markerscale=10.0)

ax.set_xlim(0.0,306.0)
ax.set_ylim(11.0,15.0)
# PPS 

ax = axes[2,0]

ax.plot(tt_ppaw,rmf(x_ppaw), color=ppaw_color,label="PPS+ATP (1)",linewidth=lw)
ax.plot(tt_ppawr,rmf(x_ppawr), color=ppawr_color,label="PPS+ATP (2)",linewidth=lw)
ax.plot(tt_ppawr2,rmf(x_ppawr2), color=ppawr2_color,label="PPS+ATP (3)",linewidth=lw)

ax.plot(tt_ppiw,rmf(x_ppiw), color=ppiw_color,linewidth=lw)
ax.plot(tt_ppiwr,rmf(x_ppiwr), color=ppiwr_color,linewidth=lw)
ax.grid()
ax.legend(loc='best',fontsize=fs,frameon=False,markerscale=10.0)
ax.set_xlabel("Time, ns")
ax.axhline(np.mean(x_prw),linewidth=1.5*lw, linestyle='--',color='green')

ax.set_xlim(0.0,101.0)
ax.set_ylim(11.0,15.0)
#### s2

# PR

ax = axes[0,1]

ax.plot(tt_prw,rmf(y_prw),color=prw_color,label="PR+ATP (1)",linewidth=lw)
ax.plot(tt_prwr,rmf(y_prwr),color=prwr_color,label="PR+ATP (2)",linewidth=lw)
ax.plot(tt_prwr2,rmf(y_prwr2),color=prwr2_color,label="PR+ATP (3)",linewidth=lw)
ax.set_ylim(15.0,22.0)
ax.set_xlim(0.0,200.0)
ax.grid()

ax.set_ylabel(u"""$s_2$, \u00c5""",fontsize=fs)

# PTS 

ax = axes[1,1]

ax.plot(tt_ptsw,rmf(y_ptsw), color=ptsw_color,label="PTS+ATP (1)",linewidth=lw)
ax.plot(tt_ptswr,rmf(y_ptswr), color=ptswr_color,label="PTS+ATP (2)",linewidth=lw)
ax.plot(tt_ptswr2,rmf(y_ptswr2), color=ptswr2_color,label="PTS+ATP (3)",linewidth=lw)
ax.grid()
ax.set_ylim(15.0,22.0)
ax.set_xlim(0.0,306.0)
ax.axhline(np.mean(y_prw),linewidth=1.5*lw, linestyle='--',color='green')



# PPS 

ax = axes[2,1]

ax.plot(tt_ppaw,rmf(y_ppaw), color=ppaw_color,linewidth=lw)
ax.plot(tt_ppawr,rmf(y_ppawr), color=ppawr_color,linewidth=lw)
ax.plot(tt_ppawr2,rmf(y_ppawr2), color=ppawr2_color,linewidth=lw)

ax.plot(tt_ppiw,rmf(y_ppiw), color=ppiw_color,label="PPS+ADP.Pi (1)",linewidth=lw)
ax.plot(tt_ppiwr,rmf(y_ppiwr), color=ppiwr_color,label="PPS+ADP.Pi (2)",linewidth=lw)
ax.grid()
ax.set_ylim(15.0,22.0)
ax.set_xlim(0.0,101.0)
ax.set_xlabel("Time, ns")
ax.legend(loc='best',fontsize=fs,frameon=False,markerscale=10.0)
ax.axhline(np.mean(y_prw),linewidth=1.5*lw, linestyle='--',color='green')

#~ plt.tight_layout()
#~ fig.savefig("time-series.png")
#~ fig.savefig("time-series.svg")
fig.savefig("time-series.pdf")





