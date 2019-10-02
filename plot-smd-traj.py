#!/usr/bin/env python
#-*-encoding: utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import analysis_tools as at 


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


data = np.genfromtxt("run_full-subsampled.colvars.traj") 


tt = data[:,0]/500000


N = len(tt)/20
print N
ncv = 10

a = 0.8  # transparency
lw = 2.0 # linewidth

# Quaternions are turned into their orientation angles #
sh1_quaternion = data[:,(15,17,19,21)]
sh1_angle = np.zeros((len(tt)))

rh_quaternion = data[:,(6,8,10,12)]
rh_angle = np.zeros((len(tt)))

sh1_quaternion_center = data[:,(41,43,45,47)]
sh1_angle_center = np.zeros((len(tt)))

rh_quaternion_center = data[:,(32,34,36,38)]
rh_angle_center = np.zeros((len(tt)))

for i in xrange(len(tt)):
    rh_angle[i] =  at.ComputeAxis(rh_quaternion[i,:],tolerance=1e-6)[-1]
    sh1_angle[i] = at.ComputeAxis(sh1_quaternion[i,:],tolerance=1e-6)[-1]
    
    rh_angle_center[i] =  at.ComputeAxis(rh_quaternion_center[i,:],tolerance=1e-6)[-1]
    sh1_angle_center[i] = at.ComputeAxis(sh1_quaternion_center[i,:],tolerance=1e-6)[-1]


d1 = data[:,1]
d2 = data[:,2]
d3 = data[:,3]
d4 = data[:,4]

d1_center = data[:,27]
d2_center = data[:,28]
d3_center = data[:,29]
d4_center = data[:,30]

rh_sh1_d = data[:,23]
rh_sh1_d_center = data[:,49]

xp = data[:,24]
yp = data[:,25]
zp = data[:,26]

xp_center = data[:,50]
yp_center = data[:,51]
zp_center = data[:,52]

W = data[:,-1]

#~ fig, axes = plt.subplots(nrows = ncv+1,sharex=True ) 

#~ bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
#~ width, height = bbox.width, bbox.height
#~ fig.set_size_inches(2*width, (1+ncv)*height)

fig, axes = plt.subplots(nrows = 4,sharex=True ) 

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 4*height)
# d1
ax = axes[0]

ax.plot(tt,d1,alpha=a)
ax.plot(tt,rmf(d1,N),linewidth=lw)
ax.plot(tt,d1_center,color='black',linestyle='--',linewidth=lw)
ax.grid()
ax.set_ylabel(u"""Distance 486O 490N, \u00c5""")

# d2
ax = axes[1]

ax.plot(tt,d2,alpha=a)
ax.plot(tt,rmf(d2,N),linewidth=lw)
ax.plot(tt,d2_center,color='black',linestyle='--',linewidth=lw)
ax.grid()
ax.set_ylabel(u"""Distance 485O 489N, \u00c5""")

# d3
ax = axes[2]

ax.plot(tt,d3,alpha=a)
ax.plot(tt,rmf(d3,N),linewidth=lw)
ax.plot(tt,d3_center,color='black',linestyle='--',linewidth=lw)
ax.grid()
ax.set_ylabel(u"""Distance 485O 490N, \u00c5""")

# d4
ax = axes[3]

ax.plot(tt,d4,alpha=a)
ax.plot(tt,rmf(d4,N),linewidth=lw)
ax.plot(tt,d4_center,color='black',linestyle='--',linewidth=lw)
ax.grid()
ax.set_ylabel(u"""Distance 486O 491N, \u00c5""")
fig.savefig("kink_distances.pdf")

# RH angle
ax = axes[4] 
ax.grid()
ax.plot(tt,rh_angle,alpha=a)
ax.plot(tt,rmf(rh_angle,N=N),linewidth=lw)
ax.plot(tt,rh_angle_center,color='black',linestyle='--',linewidth=lw)
#~ ax.plot(tt,rh_angle_center)


ax.set_ylabel(u"""Relay helix bend/kink angle,\u00b0""")


# SH1 angle
ax = axes[5] 
ax.grid()
ax.plot(tt,sh1_angle,alpha=a)
ax.plot(tt,rmf(sh1_angle,N=N),linewidth=lw)
ax.plot(tt,sh1_angle_center,color='black',linestyle='--',linewidth=lw)


ax.set_ylabel(u"""SH1 tilt angle,\u00b0""")

# SH1 - Relay distance 
ax = axes[6]
ax.grid()
ax.plot(tt,rh_sh1_d,alpha=a)
ax.plot(tt,rmf(rh_sh1_d,N),linewidth=lw)
ax.plot(tt,rh_sh1_d_center,color='black',linestyle='--',linewidth=lw)

ax.set_ylabel(u"""Relay/SH1 inter-helix distance, \u00c5""")


# X' 
ax = axes[7]
ax.plot(tt, xp,alpha=a)
ax.plot(tt, rmf(xp,N),linewidth=lw)
ax.plot(tt,xp_center,color='black',linestyle='--',linewidth=lw)
ax.grid()
ax.set_ylabel(u"""$X'$""")

# Y' 
ax = axes[8]
ax.plot(tt, yp,alpha=a)
ax.plot(tt, rmf(yp,N),linewidth=lw)
ax.plot(tt,yp_center,color='black',linestyle='--',linewidth=lw)
ax.grid()
ax.set_ylabel(u"""$Y'$""")

# Z' 
ax = axes[9]
ax.plot(tt, zp,alpha=a)
ax.plot(tt, rmf(zp,N),linewidth=lw)
ax.plot(tt,zp_center,color='black',linestyle='--',linewidth=lw)
ax.grid()
ax.set_ylabel(u"""$Z'$""")

ax = axes[ncv]

ax.plot(tt,W,linewidth=2.0*lw,color='green')
ax.set_xlabel("Time, ns")
ax.set_xlim(0.0,100.0)
ax.set_ylabel("Non-equilibrium work, kcal/mol")
ax.grid()





fig.savefig("smd-traj.svg")




# Write the path file 

nreplicas = 60 

step = int(np.ceil(len(tt)/(nreplicas-1)))
indexes = np.arange(0,len(tt),step,dtype='int')

path = np.zeros((nreplicas,ncv+1))

path[:,0] = np.arange(nreplicas).T

path[:,1] = rmf(d1,N)[::step]
path[:,2] = rmf(d2,N)[::step]
path[:,3] = rmf(d3,N)[::step]
path[:,4] = rmf(d4,N)[::step]
path[:,5] = rmf(rh_angle,N)[::step]
path[:,6] = rmf(sh1_angle,N)[::step]
path[:,7] = rmf(rh_sh1_d,N)[::step]
path[:,8] = rmf(xp,N)[::step]
path[:,9] = rmf(yp,N)[::step]
path[:,10] = rmf(zp,N)[::step]

np.savetxt(open("%s" %("string.smd-rm.dat"),'w'), path, fmt=' '.join(['%04i'] + ['%08.4f']*ncv))

