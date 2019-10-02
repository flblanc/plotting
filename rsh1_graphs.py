#!/usr/bin/env python
#-*-encoding:utf-8-*-

##############################################
## VERSION OF 9 august for thesis - AMD ##
##############################################



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

prw_color = "darkgreen"
prwr_color = "lightgreen"




ptsw_color= "darkred"
ptswr_color="red"


ppaw_color="darkblue"# pps atp
ppawr_color= "lightblue"





name = "myo6"
suffix = "rsh1-9aug18"




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




# T_RH
x_prw = obs_prw[:,4]
x_prwr = obs_prwr[:,4]





x_ppaw = obs_ppaw[:,4]
x_ppawr = obs_ppawr[:,4]



x_ptsw = obs_ptsw[:,4]
x_ptswr = obs_ptswr[:,4]



# T_SH1
y_prw = obs_prw[:,5]
y_prwr = obs_prwr[:,5]





y_ppaw = obs_ppaw[:,5]
y_ppawr = obs_ppawr[:,5]


y_ptsw = obs_ptsw[:,5]
y_ptswr = obs_ptswr[:,5]



#~ 
fig, ax = plt.subplots()
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 2*height)

xmin=0.0
xmax=+100.0

ymin=0.0
ymax=+100.0


rast=True
s=5.0
sx = 150.0
cx="yellow"
a=1
eps = 10.0

ax.scatter(x_prw, y_prw, color=prw_color, label="PR aMD (1)",s=s, alpha=a,rasterized=rast)
ax.scatter(x_prwr, y_prwr, color=prwr_color, label="PR aMD (2)",s=s, alpha=a,rasterized=rast)




ax.scatter(x_ptsw, y_ptsw, color=ptsw_color, label="PTS aMD (1)",s=s, alpha=a,rasterized=rast)
ax.scatter(x_ptswr, y_ptswr, color=ptswr_color, label="PTS aMD (2)",s=s, alpha=a,rasterized=rast)



ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


ax.scatter(x_ppaw, y_ppaw, color=ppaw_color, label="PPS aMD (1)",s=s, alpha=a,rasterized=rast)
ax.scatter(x_ppawr, y_ppawr, color=ppawr_color, label="PPS aMD (2)",s=s, alpha=a,rasterized=rast)


# 
square_box = dict(boxstyle="round",fc="white",lw=0.5,edgecolor="black")


ax.scatter(obs_xray[0,4], obs_xray[0,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[1,4], obs_xray[1,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[2,4], obs_xray[2,5],s=sx, marker="^",color=cx,edgecolors="black")



ax.annotate(s="PR (X-ray)",xy = (obs_xray[0,4], obs_xray[0,5]), xytext = (obs_xray[0,4]+2*eps, obs_xray[0,5]+ 2*eps),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0, width=6.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center",bbox=square_box)
ax.annotate(s="PTS (X-ray)",xy = (obs_xray[1,4], obs_xray[1,5]), xytext = (obs_xray[1,4]-2*eps, obs_xray[1,5]+ 2*eps),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0,width=6.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center")
ax.annotate(s="PPS (X-ray)",xy = (obs_xray[2,4], obs_xray[2,5]), xytext = (obs_xray[2,4]+ 3*eps, obs_xray[2,5]),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0,width=6.0,linewidth=1.0,shrink=0.15),verticalalignment="center",horizontalalignment="center")

ax.text(s="PR (X-ray)",x = obs_xray[0,4]+2*eps, y = obs_xray[0,5]+ 2*eps,bbox=square_box,ha='center', va = 'center')
ax.text(s="PTS (X-ray)",x = obs_xray[1,4]-2*eps,y= obs_xray[1,5]+ 2*eps, bbox=square_box,ha='center', va = 'center')
ax.text(s="PPS (X-ray)",x = obs_xray[2,4]+ 3*eps,y= obs_xray[2,5], bbox = square_box,ha='center', va = 'center')

leg = ax.legend(loc='best', frameon=True,markerscale=5.0,ncol=1,framealpha=1.0)
frame = leg.get_frame()
frame.set_linewidth(1.5)
frame.set_edgecolor("black")
frame.set_alpha = 1
ax.set_xlabel(u"""$\Theta_{RH}$, deg""")
ax.set_ylabel(u"""$\Theta_{SH1}$, deg""")

#~ ax.grid()
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

fig.savefig("%s-scatter-%s.pdf" %(name,suffix), dpi=300)



### SCATTER/DENSITY LINES ### 

fig, axes = plt.subplots(ncols=1,nrows=2)
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 4*height)
#~ xmin=0.0
#~ xmax=+70.0

#~ ymin=0.0
#~ ymax=+70.0


rast=True
s=5.0
sx = 150.0
cx="yellow"
a=1
eps = 5.0

ax = axes[0]

ax.scatter(x_prw, y_prw, color=prw_color, label="PR aMD (1)",s=s, alpha=a,rasterized=rast)
ax.scatter(x_prwr, y_prwr, color=prwr_color, label="PR aMD (2)",s=s, alpha=a,rasterized=rast)




ax.scatter(x_ptsw, y_ptsw, color=ptsw_color, label="PTS aMD (1)",s=s, alpha=a,rasterized=rast)
ax.scatter(x_ptswr, y_ptswr, color=ptswr_color, label="PTS aMD (2)",s=s, alpha=a,rasterized=rast)



ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


ax.scatter(x_ppaw, y_ppaw, color=ppaw_color, label="PPS aMD (1)",s=s, alpha=a,rasterized=rast)
ax.scatter(x_ppawr, y_ppawr, color=ppawr_color, label="PPS aMD (2)",s=s, alpha=a,rasterized=rast)


# 
square_box = dict(boxstyle="round",fc="white",lw=0.5,edgecolor="black")


ax.scatter(obs_xray[0,4], obs_xray[0,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[1,4], obs_xray[1,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[2,4], obs_xray[2,5],s=sx, marker="^",color=cx,edgecolors="black")



ax.annotate(s="PR (X-ray)",xy = (obs_xray[0,4], obs_xray[0,5]), xytext = (obs_xray[0,4]+3*eps, obs_xray[0,5]+ 1.0*eps),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0, width=6.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center",bbox=square_box)
ax.annotate(s="PTS (X-ray)",xy = (obs_xray[1,4], obs_xray[1,5]), xytext = (obs_xray[1,4]-2*eps, obs_xray[1,5]+ 3*eps),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0,width=6.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center")
ax.annotate(s="PPS (X-ray)",xy = (obs_xray[2,4], obs_xray[2,5]), xytext = (obs_xray[2,4]+ 5*eps, obs_xray[2,5]),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0,width=6.0,linewidth=1.0,shrink=0.15),verticalalignment="center",horizontalalignment="center")

ax.text(s="PR (X-ray)",x = obs_xray[0,4]+3*eps, y = obs_xray[0,5]+ 1.0*eps,bbox=square_box,ha='center', va = 'center')
ax.text(s="PTS (X-ray)",x = obs_xray[1,4]-2*eps,y= obs_xray[1,5]+ 3*eps, bbox=square_box,ha='center', va = 'center')
ax.text(s="PPS (X-ray)",x = obs_xray[2,4]+ 5*eps,y= obs_xray[2,5], bbox = square_box,ha='center', va = 'center')

leg = ax.legend(loc='best', frameon=True,markerscale=5.0,ncol=1,framealpha=1.0)
frame = leg.get_frame()
frame.set_linewidth(1.5)
frame.set_edgecolor("black")
frame.set_alpha = 1
ax.set_xlabel(u"""$\Theta_{RH}$, deg""")
ax.set_ylabel(u"""$\Theta_{SH1}$, deg""")

#~ ax.grid()
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
#~ xmin=-25.
#~ xmax=+10.

#~ ymin=-27.
#~ ymax=+8.


X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])

pdf_pr1 = np.reshape(kde(np.vstack([x_prw, y_prw]))(positions).T, X.shape)
pdf_pr2 = np.reshape(kde(np.vstack([x_prwr, y_prwr]))(positions).T, X.shape)



pdf_pts1 = np.reshape(kde(np.vstack([x_ptsw, y_ptsw]))(positions).T, X.shape)
pdf_pts2 = np.reshape(kde(np.vstack([x_ptswr, y_ptswr]))(positions).T, X.shape)


pdf_ppa1 = np.reshape(kde(np.vstack([x_ppaw, y_ppaw]))(positions).T, X.shape)
pdf_ppa2 = np.reshape(kde(np.vstack([x_ppawr, y_ppawr]))(positions).T, X.shape)


ax = axes[1]

lw2 = 3.5
ax.contour(X,Y,pdf_pr1, colors=prw_color)
ax.contour(X,Y,pdf_pr2, colors=prwr_color,linewidths=lw2)


ax.contour(X,Y,pdf_pts1, colors=ptsw_color)
ax.contour(X,Y,pdf_pts2, colors=ptswr_color)


ax.contour(X,Y,pdf_ppa1, colors=ppaw_color)
ax.contour(X,Y,pdf_ppa2, colors=ppawr_color,linewidths=lw2)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)



ax.scatter(obs_xray[0,4], obs_xray[0,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[1,4], obs_xray[1,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[2,4], obs_xray[2,5],s=sx, marker="^",color=cx,edgecolors="black")

# 
square_box = dict(boxstyle="round",fc="white",lw=0.5,edgecolor="black")


ax.scatter(obs_xray[0,4], obs_xray[0,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[1,4], obs_xray[1,5],s=sx, marker="^",color=cx,edgecolors="black")
ax.scatter(obs_xray[2,4], obs_xray[2,5],s=sx, marker="^",color=cx,edgecolors="black")



ax.annotate(s="PR (X-ray)",xy = (obs_xray[0,4], obs_xray[0,5]), xytext = (obs_xray[0,4]+3*eps, obs_xray[0,5]+ 1.0*eps),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0, width=6.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center",bbox=square_box)
ax.annotate(s="PTS (X-ray)",xy = (obs_xray[1,4], obs_xray[1,5]), xytext = (obs_xray[1,4]-2*eps, obs_xray[1,5]+ 7*eps),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0,width=6.0,linewidth=1.0,shrink=0.1),verticalalignment="center",horizontalalignment="center")
ax.annotate(s="PPS (X-ray)",xy = (obs_xray[2,4], obs_xray[2,5]), xytext = (obs_xray[2,4]+ 5*eps, obs_xray[2,5]),arrowprops=dict(facecolor='lightgrey',headwidth=15.0,headlength=10.0,width=6.0,linewidth=1.0,shrink=0.15),verticalalignment="center",horizontalalignment="center")

ax.text(s="PR (X-ray)",x = obs_xray[0,4]+3*eps, y = obs_xray[0,5]+ 1.0*eps,bbox=square_box,ha='center', va = 'center')
ax.text(s="PTS (X-ray)",x = obs_xray[1,4]-2*eps,y= obs_xray[1,5]+ 7*eps, bbox=square_box,ha='center', va = 'center')
ax.text(s="PPS (X-ray)",x = obs_xray[2,4]+ 5*eps,y= obs_xray[2,5], bbox = square_box,ha='center', va = 'center')


frame = leg.get_frame()
frame.set_linewidth(1.5)
frame.set_edgecolor("black")
frame.set_alpha = 1
ax.set_xlabel(u"""$\Theta_{RH}$, deg""")
ax.set_ylabel(u"""$\Theta_{SH1}$, deg""")

#~ ax.grid()
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

fig.savefig("%s-density-%s.pdf" %(name,suffix), dpi=300)






### PANEL TS ####

fig, axes = plt.subplots(ncols=3,nrows=2,sharey='row',sharex='col')

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(3*width, 2*height)

lw = 2.5


ax = axes[0,0] 



ax.plot(tt_prw, rmf(x_prw), label="PR aMD (1)", color=prw_color, linewidth=lw)
ax.plot(tt_prwr, rmf(x_prwr), label="PR aMD (2)", color=prwr_color, linewidth=lw)
ax.legend(loc='best',ncol=1,fontsize=16,frameon=True)

ax.set_xlim(0,200.0)
ax.set_ylim(xmin,xmax-20.0)

ax.set_ylabel(u"""$\Theta_{RH}$, deg""")

ax = axes[0,2]

ax.plot(tt_ppaw, rmf(x_ppaw), label="PPS aMD (1)", color=ppaw_color, linewidth=lw)


ax.plot(tt_ppawr, rmf(x_ppawr), label="PPS aMD (2)", color=ppawr_color, linewidth=lw)
ax.legend(loc='best',ncol=1,fontsize=16,frameon=True)

ax.set_xlim(0,100.0)



ax = axes[0,1]
ax.plot(tt_ptsw, rmf(x_ptsw), label="PTS aMD (1)", color=ptsw_color, linewidth=lw)

ax.plot(tt_ptswr, rmf(x_ptswr), label="PTS aMD (2)", color=ptswr_color, linewidth=lw)
ax.legend(loc='best',ncol=1,fontsize=16,frameon=True)


ax.set_xlim(0,100.0)


#Y'

ax = axes[1,0] 

ax.plot(tt_prw, rmf(y_prw), label="PR aMD (1)", color=prw_color, linewidth=lw)
ax.plot(tt_prwr, rmf(y_prwr), label="PR aMD (2)", color=prwr_color, linewidth=lw)

ax.set_ylim(ymin,ymax)
ax.set_xlim(0,200)
ax.set_ylabel(u"""$\Theta_{SH1}$, deg""")


ax = axes[1,1]

ax.plot(tt_ptsw, rmf(y_ptsw), label="PR aMD (1)", color=ptsw_color, linewidth=lw)


ax.plot(tt_ptswr, rmf(y_ptswr), label="PTS aMD (2)", color=ptswr_color, linewidth=lw)


ax.set_xlim(0,100)
ax.set_xlabel(u"""Time, ns""")


# z'



ax =axes[1,2]
ax.plot(tt_ppaw, rmf(y_ppaw), label="PPS aMD (1)", color=ppaw_color, linewidth=lw)


ax.plot(tt_ppawr, rmf(y_ppawr), label="PPS aMD (2)", color=ppawr_color, linewidth=lw)




# 


for i in axes.flatten():
    
    i.grid()
    

plt.tight_layout()
fig.savefig("panel-%s-%s.pdf" %(name,suffix))












