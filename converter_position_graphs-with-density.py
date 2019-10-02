#!/usr/bin/env python
#-*-encoding:utf-8-*-

###############################################
## VERSION OF 22 AUGUST FOR THESIS ##
###############################################



import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
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





name = "myo6"
suffix = "thesis"

data_rep="/media/florian/FBLANC_PRO/Data_for_thesis/Unbiased-replica-simulations-analysis"


obs_prw  = np.genfromtxt("%s/PR-with-waters.colvars.traj" %data_rep)
obs_prwr = np.genfromtxt("%s/PR-with-waters-replica.colvars.traj" %data_rep)
obs_prwr2 = np.genfromtxt("%s/PR-with-waters-replica2.colvars.traj" %data_rep)

obs_ptsw = np.genfromtxt("%s/PTS-with-waters.colvars.traj" %data_rep)
obs_ptswr = np.genfromtxt("%s/PTS-with-waters-replica.colvars.traj" %data_rep)
obs_ptswr2 = np.genfromtxt("%s/PTS-with-waters-replica2.colvars.traj" %data_rep)

obs_ppaw = np.genfromtxt("%s/PPA-with-waters.colvars.traj" %data_rep)
obs_ppawr = np.genfromtxt("%s/PPA-with-waters-replica.colvars.traj" %data_rep)
obs_ppawr2 = np.genfromtxt("%s/PPA-with-waters-replica2.colvars.traj" %data_rep)

obs_ppiw = np.genfromtxt("%s/PPI-with-waters.colvars.traj" %data_rep)
obs_ppiwr = np.genfromtxt("%s/PPI-with-waters-replica.colvars.traj" %data_rep)


obs_xray = np.genfromtxt("%s/XRAY.colvars.traj" %data_rep)

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

# X'
x_prw = obs_prw[:,1]
x_prwr = obs_prwr[:,1]
x_prwr2 = obs_prwr2[:,1]



#~ x_ppiw = obs_ppiw[:,1]
x_ppaw = obs_ppaw[:,1]
x_ppawr = obs_ppawr[:,1]
x_ppawr2 = obs_ppawr2[:,1]

x_ppiw = obs_ppiw[:,1]
x_ppiwr = obs_ppiwr[:,1]

x_ptsw = obs_ptsw[:,1]
x_ptswr = obs_ptswr[:,1]
x_ptswr2 = obs_ptswr2[:,1]


# Y'
y_prw = obs_prw[:,2]
y_prwr = obs_prwr[:,2]
y_prwr2 = obs_prwr2[:,2]



#~ x_ppiw = obs_ppiw[:,2]
y_ppaw = obs_ppaw[:,2]
y_ppawr = obs_ppawr[:,2]
y_ppawr2 = obs_ppawr2[:,2]

y_ppiw = obs_ppiw[:,2]
y_ppiwr = obs_ppiwr[:,2]

y_ptsw = obs_ptsw[:,2]
y_ptswr = obs_ptswr[:,2]
y_ptswr2 = obs_ptswr2[:,2]


#~ 
#~ fig, ax = plt.subplots()
    

#~ xmin=-25.
#~ xmax=+10.
#~ 
#~ ymin=-12.
#~ ymax=+5.



#~ ax.scatter(x_prw, y_prw, color=prw_color, label="PR+ATP",s=0.2, alpha=0.8)
#~ ax.scatter(x_prwr, y_prwr, color=prwr_color, label="PR+ATP (2)",s=0.2, alpha=0.8)
#~ ax.scatter(x_prwr2, y_prwr2, color=prwr2_color, label="PR+ATP (3)",s=0.2, alpha=0.8)
#~ 
#~ 
#~ 
#~ ax.scatter(x_ptsw, y_ptsw, color=ptsw_color, label="PTS+ATP",s=0.2, alpha=0.8)
#~ ax.scatter(x_ptswr, y_ptswr, color=ptswr_color, label="PTS+ATP (2)",s=0.2, alpha=0.8)
#~ ax.scatter(x_ptswr2, y_ptswr2, color=ptswr2_color, label="PTS+ATP (3)",s=0.2, alpha=0.8)
#~ 
#~ 
#~ 
#~ ax.scatter(x_ppaw, y_ppaw, color=ppaw_color, label="PPS+ATP",s=0.2, alpha=0.8)
#~ ax.scatter(x_ppawr, y_ppawr, color=ppawr_color, label="PPS+ATP (2)",s=0.2, alpha=0.8)
#~ ax.scatter(x_ppawr2, y_ppawr2, color=ppawr2_color, label="PPS+ATP (3)",s=0.2, alpha=0.8)
#~ ax.scatter(x_ppiw, y_ppiw, color=ppiw_color, label="PPS+ADP.Pi",marker='o',s=0.1)
#~ ax.scatter(x_ppiwr, y_ppiwr, color=ppiwr_color, label="PPS+ADP.Pi (2)",marker='o',s=0.1)
#~ 
#~ 
#~ ax.scatter(obs_xray[0,1], obs_xray[0,2], color="green",s=30.0, marker="x")
#~ ax.scatter(obs_xray[1,1], obs_xray[1,2], color="red",s=30.0, marker="x")
#~ ax.scatter(obs_xray[2,1], obs_xray[2,2], color="blue",s=30.0, marker="x")
#~ 
#~ 
#~ leg = ax.legend(loc='lower left', frameon=False,markerscale=10.0)
#~ frame = leg.get_frame()
#~ frame.set_linewidth(0.0)
#~ ax.set_xlabel(u"""$X', \ \AA$""")
#~ ax.set_ylabel(u"""$Y', \ \AA$""")


#~ ax.set_xlim(xmin,xmax)
#~ ax.set_ylim(ymin,ymax)

#~ ax.grid(linewidth=0.2, color='black',linestyle='--')
#~ 
#~ 
#~ fig.savefig("%s-scatter-%s.png" %(name,suffix), dpi=300)
#~ fig.savefig("%s-scatter-%s.svg" %(name, suffix))
#~ fig.savefig("%s-scatter-%s.pdf" %(name,suffix), dpi=300)


# Z' = f(t)

z_prw =  obs_prw[:,3]
z_prwr =  obs_prwr[:,3]
z_prwr2 =  obs_prwr2[:,3]

z_ptsw = obs_ptsw[:,3]
z_ptswr = obs_ptswr[:,3]
z_ptswr2 = obs_ptswr2[:,3]


z_ppaw = obs_ppaw[:,3]
z_ppawr = obs_ppawr[:,3]
z_ppawr2 = obs_ppawr2[:,3]

z_ppiw = obs_ppiw[:,3]
z_ppiwr = obs_ppiwr[:,3]

#~ z_prw = runningMeanFast(z_prw_full, N=200)
#~ z_prwr = runningMeanFast(z_prwr_full, N=200)
#~ z_prwr2 = runningMeanFast(z_prwr2_full, N=200)
#~ 
#~ z_ptsw = runningMeanFast(z_ptsw_full, N=200)
#~ z_ptswr = runningMeanFast(z_ptswr_full, N=200)
#~ z_ptswr2 = runningMeanFast(z_ptswr2_full, N=200)
#~ 
#~ z_ppaw = runningMeanFast(z_ppaw_full, N=200)
#~ z_ppawr = runningMeanFast(z_ppawr_full, N=200)
#~ z_ppawr2 = runningMeanFast(z_ppawr2_full, N=200)
#~ 
#~ z_ppiw = runningMeanFast(z_ppiw_full, N=200)
#~ z_ppiwr = runningMeanFast(z_ppiwr_full, N=200)

#~ fig, ax = plt.subplots()
#~ 
#~ ax.plot(tt_prw, rmf(z_prw), label="PR+ATP", color=prw_color, linewidth=2.0)
#~ ax.plot(tt_prwr, rmf(z_prwr), label="PR+ATP (2)", color=prwr_color, linewidth=2.0)
#~ ax.plot(tt_prwr2, rmf(z_prwr2), label="PR+ATP (3)", color=prwr2_color, linewidth=2.0)
#~ 
#~ 
#~ 
#~ ax.plot(tt_ptsw, rmf(z_ptsw), label="PTS+ATP", color=ptsw_color, linewidth=2.0)
#~ ax.plot(tt_ptswr, rmf(z_ptswr), label="PTS+ATP (2)", color=ptswr_color, linewidth=2.0)
#~ ax.plot(tt_ptswr2, rmf(z_ptswr2), label="PTS+ATP (3)", color=ptswr2_color, linewidth=2.0)
#~ 
#~ 
#~ ax.plot(tt_ppaw, rmf(z_ppaw), label="PPS+ATP", color=ppaw_color, linewidth=2.0)
#~ ax.plot(tt_ppawr, rmf(z_ppawr), label="PPS+ATP (2)", color=ppawr_color, linewidth=2.0)
#~ ax.plot(tt_ppawr2, rmf(z_ppawr2), label="PPS+ATP (3)", color=ppawr2_color, linewidth=2.0)
#~ 
#~ ax.plot(tt_ppiw, rmf(z_ppiw), label="PPS+ADP.Pi", color=ppiw_color, linewidth=2.0)
#~ ax.plot(tt_ppiwr, rmf(z_ppiwr), label="PPS+ADP.Pi (2)", color=ppiwr_color, linewidth=2.0)
#~ 
#~ ax.grid(linewidth=0.2, color='black',linestyle='--')
#~ 
#~ 
#~ ax.set_xlabel(u"""Time, ns""")
#~ ax.set_ylabel(u"""$Z',\ \AA$""")
#~ 
#~ ax.set_xlim(xmin=0.0, xmax=126.)
#~ 
#~ 
#~ fig.savefig("%s-Z-smoothed-%s.svg" %(name,suffix))
#~ fig.savefig("%s-Z-smoothed-%s.png" %(name,suffix), dpi=300)
#~ fig.savefig("%s-Z-smoothed-%s.pdf" %(name,suffix), dpi=300)


### PANEL ####

fig, axes = plt.subplots(ncols=1,nrows=3,sharex=True,sharey=True)

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(1*width, 3*height)

xmin=-25.0
xmax=+10.0

ymin=-25.0
ymax=+5.0

X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])



pdf_pr1 = np.reshape(kde(np.vstack([x_prw, y_prw]))(positions).T, X.shape)
pdf_pr2 = np.reshape(kde(np.vstack([x_prwr, y_prwr]))(positions).T, X.shape)
pdf_pr3 = np.reshape(kde(np.vstack([x_prwr2, y_prwr2]))(positions).T, X.shape)


pdf_pts1 = np.reshape(kde(np.vstack([x_ptsw, y_ptsw]))(positions).T, X.shape)
pdf_pts2 = np.reshape(kde(np.vstack([x_ptswr, y_ptswr]))(positions).T, X.shape)
pdf_pts3 = np.reshape(kde(np.vstack([x_ptswr2, y_ptswr2]))(positions).T, X.shape)

pdf_ppa1 = np.reshape(kde(np.vstack([x_ppaw, y_ppaw]))(positions).T, X.shape)
pdf_ppa2 = np.reshape(kde(np.vstack([x_ppawr, y_ppawr]))(positions).T, X.shape)
pdf_ppa3 = np.reshape(kde(np.vstack([x_ppawr2, y_ppawr2]))(positions).T, X.shape)

pdf_ppi1 = np.reshape(kde(np.vstack([x_ppiw, y_ppiw]))(positions).T, X.shape)
pdf_ppi2 = np.reshape(kde(np.vstack([x_ppiwr, y_ppiwr]))(positions).T, X.shape)

cx = "black"
# PR 


# Scatter

ax = axes[0]
ax.set_xlabel(u"""$X'$, \u00c5""")
ax.set_ylabel(u"""$Y'$, \u00c5""")

ax.contour(X,Y,pdf_pts1, colors=ptsw_color)
ax.contour(X,Y,pdf_pts2, colors=ptswr_color)
ax.contour(X,Y,pdf_pts3, colors=ptswr2_color)

ax.contour(X,Y,pdf_ppa1, colors=ppaw_color)
ax.contour(X,Y,pdf_ppa2, colors=ppawr_color)
ax.contour(X,Y,pdf_ppa3, colors=ppawr2_color)

ax.contour(X,Y,pdf_ppi1, colors=ppiw_color)
ax.contour(X,Y,pdf_ppi2, colors=ppiwr_color)


ax.scatter(x_prw, y_prw, color=prw_color, label="PR+ATP",s=0.2, alpha=0.8,rasterized=True)
ax.scatter(x_prwr, y_prwr, color=prwr_color, label="PR+ATP (2)",s=0.2, alpha=0.8,rasterized=True)
ax.scatter(x_prwr2, y_prwr2, color=prwr2_color, label="PR+ATP (3)",s=0.2, alpha=0.8,rasterized=True)
ax.grid(linewidth=0.2, color='black',linestyle='--')
ax.legend(loc='lower center',ncol=3,fontsize=10,frameon=False,markerscale=10.0)

#~ ax.scatter(obs_xray[0,1], obs_xray[0,2], color="green",s=120.0, marker="x")
ax.scatter(obs_xray[0,1], obs_xray[0,2], marker="^",color=cx,edgecolors="black",s=140.0)



# PTS
# scatter



ax = axes[1]

ax.set_xlabel(u"""$X'$, \u00c5""")
ax.set_ylabel(u"""$Y'$, \u00c5""")

ax.contour(X,Y,pdf_pr1, colors=prw_color)
ax.contour(X,Y,pdf_pr2, colors=prwr_color)
ax.contour(X,Y,pdf_pr3, colors=prwr2_color)

ax.contour(X,Y,pdf_ppa1, colors=ppaw_color)
ax.contour(X,Y,pdf_ppa2, colors=ppawr_color)
ax.contour(X,Y,pdf_ppa3, colors=ppawr2_color)

ax.contour(X,Y,pdf_ppi1, colors=ppiw_color)
ax.contour(X,Y,pdf_ppi2, colors=ppiwr_color)

ax.scatter(x_ptsw, y_ptsw, color=ptsw_color, label="PTS+ATP",s=0.2, alpha=0.8,rasterized=True)
ax.scatter(x_ptswr, y_ptswr, color=ptswr_color, label="PTS+ATP (2)",s=0.2, alpha=0.8,rasterized=True)
ax.scatter(x_ptswr2, y_ptswr2, color=ptswr2_color, label="PTS+ATP (3)",s=0.2, alpha=0.8,rasterized=True)
ax.grid(linewidth=0.2, color='black',linestyle='--')
ax.legend(loc='best',ncol=3,fontsize=10,frameon=False,markerscale=10.0)

#~ ax.scatter(obs_xray[1,1], obs_xray[1,2], color="red",s=120.0, marker="x")
ax.scatter(obs_xray[1,1], obs_xray[1,2], marker="^",color=cx,edgecolors="black",s=140.0)





# PPS 
# scatter



ax = axes[2]
ax.set_xlabel(u"""$X'$, \u00c5""")
ax.set_ylabel(u"""$Y'$, \u00c5""")

ax.contour(X,Y,pdf_pr1, colors=prw_color)
ax.contour(X,Y,pdf_pr2, colors=prwr_color)
ax.contour(X,Y,pdf_pr3, colors=prwr2_color)

ax.contour(X,Y,pdf_pts1, colors=ptsw_color)
ax.contour(X,Y,pdf_pts2, colors=ptswr_color)
ax.contour(X,Y,pdf_pts3, colors=ptswr2_color)

ax.scatter(x_ppaw, y_ppaw, color=ppaw_color, label="PPS+ATP",s=0.2, alpha=0.8,rasterized=True)
ax.scatter(x_ppawr, y_ppawr, color=ppawr_color, label="PPS+ATP (2)",s=0.2, alpha=0.8,rasterized=True)
ax.scatter(x_ppawr2, y_ppawr2, color=ppawr2_color, label="PPS+ATP (3)",s=0.2, alpha=0.8,rasterized=True)

ax.scatter(x_ppiw, y_ppiw,color=ppiw_color,label="PPS+ADP.Pi",s=0.2, alpha=0.8,rasterized=True)
ax.scatter(x_ppiwr, y_ppiwr,color=ppiwr_color,label="PPS+ADP.Pi (2)",s=0.2, alpha=0.8,rasterized=True)

ax.grid(linewidth=0.2, color='black',linestyle='--')
ax.legend(loc='lower center',ncol=2,fontsize=10,frameon=True,markerscale=10.0)

#~ ax.scatter(obs_xray[2,1], obs_xray[2,2], color="blue",s=120.0, marker="x")
ax.scatter(obs_xray[2,1], obs_xray[2,2], marker="^",color=cx,edgecolors="black",s=140.0)

plt.tight_layout()
fig.savefig("converter-density-unbiased.pdf")
exit()

#############################################################################


fig, axes = plt.subplots(ncols=3,nrows=1)

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(4*width, 4*height)

ax = axes[1,0] 

# X'(t)
ax.plot(tt_prw, rmf(x_prw), label="PR+ATP", color=prw_color, linewidth=2.0)
ax.plot(tt_prw, x_prw, color=prw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_prwr, rmf(x_prwr), label="PR+ATP (2)", color=prwr_color, linewidth=2.0)
ax.plot(tt_prwr, x_prwr, color=prwr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_prwr2, rmf(x_prwr2), label="PR+ATP (3)", color=prwr2_color, linewidth=2.0)
ax.plot(tt_prwr2, x_prwr2, color=prwr2_color, linewidth=0.5, alpha=0.5)

# Y'(t)

ax = axes[2,0]
ax.plot(tt_prw, rmf(y_prw), label="PR+ATP", color=prw_color, linewidth=2.0)
ax.plot(tt_prw, y_prw, color=prw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_prwr, rmf(y_prwr), label="PR+ATP (2)", color=prwr_color, linewidth=2.0)
ax.plot(tt_prwr, y_prwr, color=prwr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_prwr2, rmf(y_prwr2), label="PR+ATP (3)", color=prwr2_color, linewidth=2.0)
ax.plot(tt_prwr2, y_prwr2, color=prwr2_color, linewidth=0.5, alpha=0.5)

# Z

ax=axes[3,0]
ax.plot(tt_prw, rmf(z_prw), label="PR+ATP", color=prw_color, linewidth=2.0)
ax.plot(tt_prw, z_prw, color=prw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_prwr, rmf(z_prwr), label="PR+ATP (2)", color=prwr_color, linewidth=2.0)
ax.plot(tt_prwr, z_prwr, color=prwr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_prwr2, rmf(z_prwr2), label="PR+ATP (3)", color=prwr2_color, linewidth=2.0)
ax.plot(tt_prwr2, z_prwr2, color=prwr2_color, linewidth=0.5, alpha=0.5)

# X 
ax=axes[1,1]
ax.plot(tt_ptsw, rmf(x_ptsw), label="PTS+ATP", color=ptsw_color, linewidth=2.0)
ax.plot(tt_ptsw, x_ptsw, color=ptsw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ptswr, rmf(x_ptswr), label="PTS+ATP (2)", color=ptswr_color, linewidth=2.0)
ax.plot(tt_ptswr, x_ptswr, color=ptswr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ptswr2, rmf(x_ptswr2), label="PTS+ATP (3)", color=ptswr2_color, linewidth=2.0)
ax.plot(tt_ptswr2, x_ptswr2, color=ptswr2_color, linewidth=0.5, alpha=0.5)
# Y
ax=axes[2,1]
ax.plot(tt_ptsw, rmf(y_ptsw), label="PTS+ATP", color=ptsw_color, linewidth=2.0)
ax.plot(tt_ptsw, y_ptsw, color=ptsw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ptswr, rmf(y_ptswr), label="PTS+ATP (2)", color=ptswr_color, linewidth=2.0)
ax.plot(tt_ptswr, y_ptswr, color=ptswr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ptswr2, rmf(y_ptswr2), label="PTS+ATP (3)", color=ptswr2_color, linewidth=2.0)
ax.plot(tt_ptswr2, y_ptswr2, color=ptswr2_color, linewidth=0.5, alpha=0.5)
# Z 
ax = axes[3,1]
ax.plot(tt_ptsw, rmf(z_ptsw), label="PTS+ATP", color=ptsw_color, linewidth=2.0)
ax.plot(tt_ptsw, z_ptsw, color=ptsw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ptswr, rmf(z_ptswr), label="PTS+ATP (2)", color=ptswr_color, linewidth=2.0)
ax.plot(tt_ptswr, z_ptswr, color=ptswr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ptswr2, rmf(z_ptswr2), label="PTS+ATP (3)", color=ptswr2_color, linewidth=2.0)
ax.plot(tt_ptswr2, z_ptswr2, color=ptswr2_color, linewidth=0.5, alpha=0.5)




# X'
ax = axes[1,2]
ax.plot(tt_ppaw, rmf(x_ppaw), label="PPS+ATP", color=ppaw_color, linewidth=2.0)
ax.plot(tt_ppaw, x_ppaw, color=ppaw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppawr, rmf(x_ppawr), label="PPS+ATP (2)", color=ppawr_color, linewidth=2.0)
ax.plot(tt_ppawr, x_ppawr, color=ppawr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppawr2, rmf(x_ppawr2), label="PPS+ATP (3)", color=ppawr2_color, linewidth=2.0)
ax.plot(tt_ppawr2, x_ppawr2, color=ppawr2_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppiw, rmf(x_ppiw), label="PPS+ADP.Pi", color=ppiw_color, linewidth=2.0)
ax.plot(tt_ppiw, x_ppiw, color=ppiw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppiwr, rmf(x_ppiwr), label="PPS+ADP.Pi (2)", color=ppiwr_color, linewidth=2.0)
ax.plot(tt_ppiwr, x_ppiwr,  color=ppiwr_color, linewidth=0.5, alpha=0.5)
#~ ax.set_ylabel(u"""$X'$, \u00c5""")

# Y'
ax =axes[2,2]
ax.plot(tt_ppaw, rmf(y_ppaw), label="PPS+ATP", color=ppaw_color, linewidth=2.0)
ax.plot(tt_ppaw, y_ppaw, color=ppaw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppawr, rmf(y_ppawr), label="PPS+ATP (2)", color=ppawr_color, linewidth=2.0)
ax.plot(tt_ppawr, y_ppawr, color=ppawr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppawr2, rmf(y_ppawr2), label="PPS+ATP (3)", color=ppawr2_color, linewidth=2.0)
ax.plot(tt_ppawr2, y_ppawr2, color=ppawr2_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppiw, rmf(y_ppiw), label="PPS+ADP.Pi", color=ppiw_color, linewidth=2.0)
ax.plot(tt_ppiw, y_ppiw, color=ppiw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppiwr, rmf(y_ppiwr), label="PPS+ADP.Pi (2)", color=ppiwr_color, linewidth=2.0)
ax.plot(tt_ppiwr, y_ppiwr,  color=ppiwr_color, linewidth=0.5, alpha=0.5)
# Z'
ax = axes[3,2]
ax.plot(tt_ppaw, rmf(z_ppaw), label="PPS+ATP", color=ppaw_color, linewidth=2.0)
ax.plot(tt_ppaw, z_ppaw, color=ppaw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppawr, rmf(z_ppawr), label="PPS+ATP (2)", color=ppawr_color, linewidth=2.0)
ax.plot(tt_ppawr, z_ppawr, color=ppawr_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppawr2, rmf(z_ppawr2), label="PPS+ATP (3)", color=ppawr2_color, linewidth=2.0)
ax.plot(tt_ppawr2, z_ppawr2, color=ppawr2_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppiw, rmf(z_ppiw), label="PPS+ADP.Pi", color=ppiw_color, linewidth=2.0)
ax.plot(tt_ppiw, z_ppiw, color=ppiw_color, linewidth=0.5, alpha=0.5)

ax.plot(tt_ppiwr, rmf(z_ppiwr), label="PPS+ADP.Pi (2)", color=ppiwr_color, linewidth=2.0)
ax.plot(tt_ppiwr, z_ppiwr,  color=ppiwr_color, linewidth=0.5, alpha=0.5)

#~ ax.grid(linewidth=0.2, color='black',linestyle='--')


#~ ax.grid(linewidth=0.2, color='black',linestyle='--')







#~ ax.legend(loc='best',ncol=3,fontsize=16,frameon=False)
#~ ax.set_ylabel(u"""$Y'$, \u00c5""")
#~ ax.grid(linewidth=0.2, color='black',linestyle='--')


#~ 
#~ 
#~ 
#~ ax.legend(loc='best',ncol=3,fontsize=16,frameon=False)
#~ 
#~ ax.set_ylabel(u"""$Y'$, \u00c5""")
#~ ax.grid(linewidth=0.2, color='black',linestyle='--')

#~ ax.set_xlabel("Time, ns")
#~ 
#~ # 





#~ ax.set_ylabel(u"""$Z'$, \u00c5""")
#~ ax.grid(linewidth=0.2, color='black',linestyle='--')
#~ 
#~ 
#~ 
#~ 
#~ 
#~ ax.set_ylabel(u"""$Z'$, \u00c5""")
#~ 
#~ 
for j in xrange(1,4): # loop over CVs
        
        
    
        
    axes[j,0].set_xlim(0.0,200.)
    axes[j,1].set_xlim(0.0,306.0)
    axes[j,2].set_xlim(0.0,100.0)
    
    axes[j,0].set_xticks(np.arange(0.0,220.,20))
    axes[j,1].set_xticks(np.arange(0.0,350.,50))
    axes[j,2].set_xticks(np.arange(0.0,120.,20))
   
   

    axes[j,0].grid(linewidth=0.2, color='black',linestyle='--')
    axes[j,1].grid(linewidth=0.2, color='black',linestyle='--')
    axes[j,2].grid(linewidth=0.2, color='black',linestyle='--')
    


for j in xrange(3): # loop over states
    
    
    axes[0,j].set_xlim(-25,10)
    axes[0,j].set_ylim(-25,4.0)
    
    axes[1,j].set_ylim(-25,10)
    axes[1,j].set_ylabel(u"""$X'$, \u00c5""")
    
    axes[2,j].set_ylim(-25,4.0)
    axes[2,j].set_ylabel(u"""$Y'$, \u00c5""")
    
    axes[3,j].set_ylim(40,58)
    axes[3,j].set_ylabel(u"""$Z'$, \u00c5""")
    axes[3,j].set_xlabel(u"""Time, ns""")

    


plt.tight_layout()
#~ fig.savefig("new_panel_density-%s-%s.svg" %(name,suffix))
#~ fig.savefig("new_panel_density-%s-%s.png" %(name,suffix),dpi=600)
fig.savefig("new_panel_density-%s-%s.pdf" %(name,suffix))











