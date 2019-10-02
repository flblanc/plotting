#!/usr/bin/env python
#-*-encoding:utf-8-*-

##############################################
## VERSION OF 9 august for thesis - AMD ##
##############################################



import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.lines import Line2D
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

prw_color = "darkgreen"
prwr_color = "lightgreen"




ptsw_color= "darkred"
ptswr_color="red"


ppaw_color="darkblue"# pps atp
ppawr_color= "lightblue"





name = "myo6"
suffix = "conv-17sep18"




obs_prw  = np.genfromtxt("PR-with-waters.colvars.traj")
obs_prwr = np.genfromtxt("PR-with-waters-2.colvars.traj")


obs_ptsw = np.genfromtxt("PTS-with-waters.colvars.traj")
obs_ptswr = np.genfromtxt("PTS-with-waters-2.colvars.traj")


obs_ppaw = np.genfromtxt("PPA-with-waters.colvars.traj")
obs_ppawr = np.genfromtxt("PPA-with-waters-2.colvars.traj")

obs_xray = np.genfromtxt("XRAY.colvars.traj")

# Time

tt_prw = obs_prw[:,0]/100.0
tt_prwr = obs_prwr[:,0]/100.0



tt_ptsw = obs_ptsw[:,0]/100.0
tt_ptswr = obs_ptswr[:,0]/100.0


tt_ppaw = obs_ppaw[:,0]/100.0
tt_ppawr = obs_ppawr[:,0]/100.0




# X'
x_prw = obs_prw[:,1]
x_prwr = obs_prwr[:,1]





x_ppaw = obs_ppaw[:,1]
x_ppawr = obs_ppawr[:,1]



x_ptsw = obs_ptsw[:,1]
x_ptswr = obs_ptswr[:,1]



# Y'
y_prw = obs_prw[:,2]
y_prwr = obs_prwr[:,2]




#~ x_ppiw = obs_ppiw[:,2]
y_ppaw = obs_ppaw[:,2]
y_ppawr = obs_ppawr[:,2]


y_ptsw = obs_ptsw[:,2]
y_ptswr = obs_ptswr[:,2]



### SCATTER/DENSITY LINES ### 

fig, ax = plt.subplots(ncols=1,nrows=1)
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 2*height)

xmin=-25.
xmax=+10.

ymin=-27.
ymax=+8.


rast=True
s=5.0
sx = 150.0
cx="yellow"
a=1
eps = 5.0






X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])

pdf_pr1 = np.reshape(kde(np.vstack([x_prw, y_prw]))(positions).T, X.shape)
pdf_pr2 = np.reshape(kde(np.vstack([x_prwr, y_prwr]))(positions).T, X.shape)



pdf_pts1 = np.reshape(kde(np.vstack([x_ptsw, y_ptsw]))(positions).T, X.shape)
pdf_pts2 = np.reshape(kde(np.vstack([x_ptswr, y_ptswr]))(positions).T, X.shape)


pdf_ppa1 = np.reshape(kde(np.vstack([x_ppaw, y_ppaw]))(positions).T, X.shape)
pdf_ppa2 = np.reshape(kde(np.vstack([x_ppawr, y_ppawr]))(positions).T, X.shape)





ax.contour(X,Y,pdf_pr1, colors=prw_color)
ax.contour(X,Y,pdf_pr2, colors=prwr_color)


ax.contour(X,Y,pdf_pts1, colors=ptsw_color)
ax.contour(X,Y,pdf_pts2, colors=ptswr_color)


ax.contour(X,Y,pdf_ppa1, colors=ppaw_color)
ax.contour(X,Y,pdf_ppa2, colors=ppawr_color)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)



ax.scatter(obs_xray[0,1], obs_xray[0,2],s=sx, marker="^",color=cx,edgecolors="black",zorder=7)
ax.scatter(obs_xray[1,1], obs_xray[1,2],s=sx, marker="^",color=cx,edgecolors="black",zorder=7)
ax.scatter(obs_xray[2,1], obs_xray[2,2],s=sx, marker="^",color=cx,edgecolors="black",zorder=7)

ax.annotate(s="PR (X-ray)",xy = (obs_xray[0,1], obs_xray[0,2]), xytext = (obs_xray[0,1], obs_xray[0,2]+ 2*eps),arrowprops=dict(facecolor='black',width=2.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center")
ax.annotate(s="PTS (X-ray)",xy = (obs_xray[1,1], obs_xray[1,2]), xytext = (obs_xray[1,1], obs_xray[1,2]+ 2*eps),arrowprops=dict(facecolor='black',width=2.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center")
ax.annotate(s="PPS (X-ray)",xy = (obs_xray[2,1], obs_xray[2,2]), xytext = (obs_xray[2,1]- 1*eps, obs_xray[2,2]- 1*eps),arrowprops=dict(facecolor='black',width=2.0,linewidth=1.0,shrink=0.15),verticalalignment="center",horizontalalignment="center")



custom_lines = [Line2D([0], [0], color=prw_color, lw=4,label="PR aMD (1)"),
                Line2D([0], [0], color=prwr_color, lw=4,label="PR aMD (2)"),
                Line2D([0], [0], color=ptsw_color, lw=4,label="PTS aMD (1)"),
                Line2D([0], [0], color=ptswr_color, lw=4,label="PTS aMD (2)"),
                Line2D([0], [0], color=ppaw_color, lw=4,label="PPS aMD (1)"),
                Line2D([0], [0], color=ppawr_color, lw=4,label="PPS aMD (2)")]



ax.legend(handles=custom_lines,loc='lower left',ncol=1,fontsize=25,frameon=False,markerscale=10.0)

ax.set_xlabel(u"""$X', \ \AA$""")
ax.set_ylabel(u"""$Y', \ \AA$""")


ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

fig.savefig("%s-density-%s.pdf" %(name,suffix), dpi=300)
fig.savefig("%s-density-%s.svg" %(name,suffix), dpi=300)








