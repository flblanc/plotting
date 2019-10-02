#!/usr/bin/env python
#-*-encoding: utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#~ import analysis_tools as at 
from scipy.stats import gaussian_kde as kde
from matplotlib.patches import Ellipse


mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 18.0



def runningMeanFast(x, N=1000):
    """Updated version with modification by Prof. Hugues Talbot."""
    x1 = np.pad(x,N,mode='reflect')
    output =np.convolve(x1, np.ones((N,))/N)[(N-1):]
    return output[N:-N]
rmf = runningMeanFast

CMAP = mpl.cm.get_cmap('hsv')






a = 0.8  # transparency
lw = 2.0 # linewidth

def gather_data(rep):
	
	data = np.genfromtxt("%s/analyze-tmd1.colvars.traj" %rep)
	x = data[:,1]
	y = data[:,2]
	
	gg = np.genfromtxt("%s/tmd1.colvars.traj" %rep)
	dr = gg[:,1]
	drc = gg[:,-2]
	w  = gg[:,-1]
	tt = gg[:,0]/5
	tt /=1e5
	
	dr = dr[::50]
	drc = drc[::50]
	w = w[::50]
	tt = tt[::50]
	
	return x,y,dr,drc,w,tt
	
	
	
	
rep1 = "dTMD_RHSH1_PR2PTS_1"
x1,y1,dr1,drc1,w1,tt1 = gather_data(rep1)

rep2 = "dTMD_RHSH1_PTS2PR_1"
x2,y2,dr2,drc2,w2,tt2 = gather_data(rep2)

#~ exit()

#### REFERENCE DATA FROM UNBIASED SIMULATIONS ####

ref_repertory="/media/florian/FBLANC_PRO/Data_for_thesis/Unbiased-replica-simulations-analysis"
prw_data = np.genfromtxt("%s/PR-with-waters.colvars.traj" %ref_repertory)
ptsw_data = np.genfromtxt("%s/PTS-with-waters.colvars.traj" %ref_repertory)




prw_color = "chartreuse"
ptsw_color= "orangered"

# PR REFERENCE DATA #

prw_compX = prw_data[:,1]
prw_compY = prw_data[:,2]
prw_compZ = prw_data[:,3]

# PTS REFERENCE DATA # 

ptsw_compX = ptsw_data[:,1]
ptsw_compY = ptsw_data[:,2]
ptsw_compZ = ptsw_data[:,3]


 # Projection of the converter components # 
 
xmin=-20.
xmax=+10.

ymin=-16.
ymax=0.

X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])

pr = np.vstack([prw_compX[:4000], prw_compY[:4000]])
pdf_2d_pr = kde(pr)
Z_pr = np.reshape(pdf_2d_pr(positions).T, X.shape)



pts = np.vstack([ptsw_compX[:4000], ptsw_compY[:4000]])
pdf_2d_pts = kde(pts)
Z_pts = np.reshape(pdf_2d_pts(positions).T, X.shape)

pts_other = np.vstack([ptsw_compX[15000:21000], ptsw_compY[15000:21000]])
pdf_2d_pts_other = kde(pts_other)
Z_pts_other = np.reshape(pdf_2d_pts_other(positions).T, X.shape)

nlevels = 5

levels_pr = np.linspace(0.0, Z_pr.max(), nlevels+1)[1:]
levels_pts = np.linspace(0.00, Z_pts.max(), nlevels+1)[1:]
levels_pts_other = np.linspace(0.00, Z_pts_other.max(), nlevels+1)[1:]

#~ lws = np.linspace(0.7, 1.5, nlevels)
lws =2.5


fig, axes = plt.subplots(nrows=2,ncols=2,sharex="col",sharey="col") 

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 2*height)



ax = axes[0,0]

ax.plot(tt1,dr1,color=CMAP(0.2),label="Forward")
ax.plot(tt1,drc1,color='black',linestyle='--')
ax.legend()
ax.grid()
ax.set_ylabel(u"""$\Delta RMSD_{R/SH1}$, \u00c5""")
ax.set_xlabel(u"""Time, ns""")
ax.set_xlim(0.0,15.0)

ax = axes[0,1]
ax.contour(X,Y,Z_pr, colors=prw_color, linewidths = lws, levels=levels_pr)
ax.contour(X,Y,Z_pts, colors=ptsw_color, linewidths = lws, levels=levels_pts)
ax.contour(X,Y,Z_pts_other, colors="brown", linewidths = lws, levels=levels_pts)

square_box_pr = dict(boxstyle="round",fc="white",lw=1.5,edgecolor=prw_color)
square_box_pts = dict(boxstyle="round",fc="white",lw=1.5,edgecolor=ptsw_color)
square_box_pts_other = dict(boxstyle="round",fc="white",lw=1.5,edgecolor="brown")
ax.text(s="PR", x = 7.5, y = -6.5, color='black',fontsize=15,bbox=square_box_pr)
ax.text(s="PTS (initial)", x = -13.0, y = -2.5, color='black',fontsize=15,bbox=square_box_pts)
ax.text(s="PTS (other basin)", x = -15.0, y = -14, color='black',fontsize=15,bbox=square_box_pts_other)


# Projection of TMD data
ax.scatter(x1,y1,color=CMAP(0.2),rasterized=True)
ax.grid()
ax.set_xlabel(u"""X', \u00c5""")
ax.set_ylabel(u"""Y', \u00c5""")


ax = axes[1,0]
ax.plot(tt2,dr2,color=CMAP(0.8),label="Backward")
ax.plot(tt2,drc2,color='black',linestyle='--')
ax.legend()
ax.grid()
ax.set_ylabel(u"""$\Delta RMSD_{R/SH1}$, \u00c5""")
ax.set_xlabel(u"""Time, ns""")
ax.set_xlim(0.0,15.0)


ax = axes[1,1]
ax.contour(X,Y,Z_pr, colors=prw_color, linewidths = lws, levels=levels_pr)
ax.contour(X,Y,Z_pts, colors=ptsw_color, linewidths = lws, levels=levels_pts)
ax.contour(X,Y,Z_pts_other, colors="brown", linewidths = lws, levels=levels_pts)

#~ square_box_pr = dict(boxstyle="round",fc="white",lw=1.5,edgecolor=prw_color)
#~ square_box_pts = dict(boxstyle="round",fc="white",lw=1.5,edgecolor=ptsw_color)
#~ ax.text(s="PR", x = 7.5, y = -6.5, color='black',fontsize=10,bbox=square_box_pr)
#~ ax.text(s="PTS", x = -13.0, y = 0, color='black',fontsize=10,bbox=square_box_pts)


# Projection of TMD data
ax.scatter(x2,y2,color=CMAP(0.8),rasterized=True)
ax.grid()
ax.set_xlabel(u"""X', \u00c5""")
ax.set_ylabel(u"""Y', \u00c5""")

plt.tight_layout()


fig.savefig("dtmd.pdf")

