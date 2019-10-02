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



CMAP = mpl.cm.get_cmap('hsv')
ii=0.0


fig, axes = plt.subplots(nrows=2,ncols=1,sharex='row',figsize=(12,8))
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(1*width, 2*height)



ax = axes[1]
ax2 = axes[0]
#~ ax3 = axes[0,1]

#~ fig2, ax2 = plt.subplots(figsize=(12,8))
#~ fig, ax = plt.subplots(figsize=(12,8))


k_list =["SMD-RSH1-PR2PTS-100ns", "SMD-RSH1-PR2PTS-100ns_2"] #, "SMD-RSH1-quaternions-PR2PTS-100ns"]
lb_list = ["Quaternions + distances (1)", "Quaternions + distances (2)"] #, "Quaternions only"]

#~ for k in [ 1.0, 5.0, 10.0, 50.0, 200.0 ] : 
for j,k in enumerate(k_list) : 
    
    data = np.genfromtxt("%s/run_full-subsampled.colvars.traj" %k) 
    
    tt = data[:,0]/500000


    #~ N = len(tt)/20
    #~ print N
    ncv = 10

    a = 0.8  # transparency
    lw = 2.0 # linewidth

    # Quaternions are turned into their orientation angles #
    sh1_quaternion = data[:,(15,17,19,21)]
    sh1_angle = np.zeros((len(tt)))

    rh_quaternion = data[:,(6,8,10,12)]
    rh_angle = np.zeros((len(tt)))

    #~ sh1_quaternion_center = data[:,(41,43,45,47)]
    #~ sh1_angle_center = np.zeros((len(tt)))

    #~ rh_quaternion_center = data[:,(32,34,36,38)]
    #~ rh_angle_center = np.zeros((len(tt)))

    for i in xrange(len(tt)):
        rh_angle[i] =  at.ComputeAxis(rh_quaternion[i,:],tolerance=1e-6)[-1]
        sh1_angle[i] = at.ComputeAxis(sh1_quaternion[i,:],tolerance=1e-6)[-1]
        
        #~ rh_angle_center[i] =  at.ComputeAxis(rh_quaternion_center[i,:],tolerance=1e-6)[-1]
        #~ sh1_angle_center[i] = at.ComputeAxis(sh1_quaternion_center[i,:],tolerance=1e-6)[-1]


    d1 = data[:,1]
    d2 = data[:,2]
    d3 = data[:,3]
    d4 = data[:,4]

    #~ d1_center = data[:,27]
    #~ d2_center = data[:,28]
    #~ d3_center = data[:,29]
    #~ d4_center = data[:,30]

    rh_sh1_d = data[:,23]
    #~ rh_sh1_d_center = data[:,49]

    xp = data[:,24]
    yp = data[:,25]
    zp = data[:,26]

    #~ xp_center = data[:,50]
    #~ yp_center = data[:,51]
    #~ zp_center = data[:,52]

    W = data[:,-1]
    
    
    
    
    dr = np.genfromtxt("%s/kink-rmsd_pts.dat" %k)[:,1] - np.genfromtxt("%s/kink-rmsd_pr.dat" %k)[:,1]

    print dr.shape
    
    #~ ax.plot(rmf(x),rmf(y),linewidth=2.0,label=u"""$k=$ %04.1f kcal/mol/\u00c5^2""" %k)
    ax2.scatter(xp[::10],dr[::10],label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)))
    ax.scatter(xp[::10],yp[::10],label=lb_list[j],color=CMAP(float(len(k_list)-ii)/len(k_list)))
    
    ii+=1.0


#### REFERENCE DATA FROM UNBIASED SIMULATIONS ####

ref_repertory="/data/flblanc/Unbiased-replica-simulations-analysis"
prw_data = np.genfromtxt("%s/PR-with-waters.colvars.traj" %ref_repertory)
ptsw_data = np.genfromtxt("%s/PTS-with-waters.colvars.traj" %ref_repertory)

prw_dr = np.genfromtxt("%s/Seesaw-vs-kink/PRw1.colvars.traj" %ref_repertory)[:,5]
ptsw_dr = np.genfromtxt("%s/Seesaw-vs-kink/PTSw1.colvars.traj" %ref_repertory)[:,5]


prw_color = "chartreuse"
ptsw_color= "orangered"

# PR REFERENCE DATA #

prw_compX = prw_data[:,1]
prw_compY = prw_data[:,2]
prw_compZ = prw_data[:,3]


prw_rh_orientAngle  = prw_data[:,4]
prw_sh1_orientAngle = prw_data[:,5]




# PTS REFERENCE DATA # 

ptsw_compX = ptsw_data[:,1]
ptsw_compY = ptsw_data[:,2]
ptsw_compZ = ptsw_data[:,3]


ptsw_rh_orientAngle  = ptsw_data[:,4]
ptsw_sh1_orientAngle = ptsw_data[:,5]






 # Projection of the converter components # 
 
xmin=-15.
xmax=+10.

ymin=-14.
ymax=0.

X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])

pr = np.vstack([prw_compX[:4000], prw_compY[:4000]])
pdf_2d_pr = kde(pr)
Z_pr = np.reshape(pdf_2d_pr(positions).T, X.shape)



pts = np.vstack([ptsw_compX[:4000], ptsw_compY[:4000]])
pdf_2d_pts = kde(pts)
Z_pts = np.reshape(pdf_2d_pts(positions).T, X.shape)

nlevels = 5

levels_pr = np.linspace(0.0, Z_pr.max(), nlevels+1)[1:]
levels_pts = np.linspace(0.00, Z_pts.max(), nlevels+1)[1:]

#~ lws = np.linspace(0.7, 1.5, nlevels)
lws =2.5


ax.contour(X,Y,Z_pr, colors=prw_color, linewidths = lws, levels=levels_pr)
ax.contour(X,Y,Z_pts, colors=ptsw_color, linewidths = lws, levels=levels_pts)

square_box_pr = dict(boxstyle="round",fc="white",lw=1.5,edgecolor=prw_color)
square_box_pts = dict(boxstyle="round",fc="white",lw=1.5,edgecolor=ptsw_color)
ax2.text(s="PR", x = 7.5, y = 1.2, color='black',fontsize=30,bbox=square_box_pr)
ax2.text(s="PTS", x = -13.0, y = -0.5, color='black',fontsize=30,bbox=square_box_pts)


# Projection of converter vs kink


xmin=-15.
xmax=+10.

ymin=-1.4
ymax=+1.4

X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])

pr = np.vstack([prw_compX[:4000], prw_dr[:4000]])
pdf_2d_pr = kde(pr)
Z_pr = np.reshape(pdf_2d_pr(positions).T, X.shape)



pts = np.vstack([ptsw_compX[:4000], ptsw_dr[:4000]])
pdf_2d_pts = kde(pts)
Z_pts = np.reshape(pdf_2d_pts(positions).T, X.shape)

nlevels = 5

levels_pr = np.linspace(0.0, Z_pr.max(), nlevels+1)[1:]
levels_pts = np.linspace(0.00, Z_pts.max(), nlevels+1)[1:]

#~ lws = np.linspace(0.7, 1.5, nlevels)
lws = 2.5


ax2.contour(X,Y,Z_pr, colors=prw_color, linewidths = lws, levels=levels_pr)
ax2.contour(X,Y,Z_pts, colors=ptsw_color, linewidths = lws, levels=levels_pts)



ax2.grid(linestyle='--')
ax.grid(linestyle='--')
ax2.legend(fontsize=16,frameon=True)

ax2.set_xlabel(u"""X', \u00c5""")
ax.set_xlabel(u"""X', \u00c5""")
ax.set_ylabel(u"""Y', \u00c5""")
ax2.set_ylabel(u"""Relay Helix kink \u0394RMSD, \u00c5""")

ax2.set_xlim(-15.0,+10.0)
ax2.set_ylim(-1.4,+1.4)




### NON EQUILIBRIUM WORK ### 




plt.tight_layout()

fig.savefig("converter_smd-long.pdf")
#~ fig2.savefig("converter_kink_smd-long.pdf")
    




exit()




    

