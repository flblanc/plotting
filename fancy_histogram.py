#!/usr/bin/env python
#-*-encoding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--path_file","-p",type=str)
parser.add_argument("--simulation",type=str)
args = parser.parse_args()

# simulation="run1"


nskip=100

# This scripts should draw a big figure with as many lines as CVs
# and for each CV, the centers and distributions per window



# Read reference path: 

reference_path = np.genfromtxt(args.path_file)
nreplicas = np.shape(reference_path)[0]
ncv = np.shape(reference_path)[1] - 1


cv_index = 1

# Draw the canvas

fig, axes = plt.subplots(nrows=nreplicas,ncols=1,sharex=True)
bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
#fig.set_size_inches(8*width, nreplicas*height)
fig.set_size_inches(2*width, 4*height)


xx = np.linspace(-10.0,+10.0,1000)
density_max = 0

for i in xrange(nreplicas):
    print "Window %i" %i
    
    data_i = np.genfromtxt("%03i/%s.colvars.traj" %(i,args.simulation))
    

    ax = axes[i]
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.spines['bottom'].set_edgecolor('#444444')
    ax.spines['bottom'].set_linewidth(2.0)
    ax.spines['bottom'].set_zorder(3)
    
    ax.get_yaxis().set_ticks([])
    ax.get_yaxis().set_ticklabels([])
    
    
    
    cv = data_i[::nskip,cv_index]
    cv_pdf = kde(cv)
    

    yy = cv_pdf(xx)
    density_max = np.max([density_max,np.max(yy)])
    if i==0:
        ax.plot(xx,yy,color='orangered',linewidth=2.0,label=u"""$P_1$""")
    else:
        ax.plot(xx,yy,color='orangered',linewidth=2.0)
    
    ax.fill_between(xx,yy,facecolor='orange',alpha=0.7)
    
    
    
    cv = data_i[::nskip,cv_index+1]
    cv_pdf = kde(cv)
    yy = cv_pdf(xx)
    density_max = np.max([density_max,np.max(yy)])
    if i==0:
        ax.plot(xx,yy,color='deepskyblue',linewidth=2.0,label=u"""$P_2$""")
        ax.legend()
    else:
        ax.plot(xx,yy,color='deepskyblue',linewidth=2.0)
    
    ax.fill_between(xx,yy,facecolor='cyan',alpha=0.7)

ax.set_xlim(-8.0,+8.0)
ax.set_ylim(ymax=density_max)

fig.subplots_adjust(top=0.95,hspace=0.05)



fig.savefig("fancy_histogram_{0}.png".format(args.simulation))
