#!/usr/bin/env python
#-*-encoding:utf-8-*-




import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import gaussian_kde as kde
import copy
import sys


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

#~ ppaw_color="mediumslateblue"# pps atp
#~ ppawr_color= "#3943B7"
#~ ppawr2_color= "#5F758E"

#~ ppiw_color="aquamarine"      # pih pps
#~ ppiwr_color="darkturquoise"  







#~ name = "myo6"
#~ suffix = "eABF"

#~ data_rep="/data/flblanc/Unbiased-replica-simulations-analysis"



#~ def Build2dDensity(data_file1,data_file2,xmin=150,xmax=350,ymin=150,ymax=350,index1=0,index2=1):
    
    
    #~ xx = np.genfromtxt(data_file1)[:,index1]
    #~ yy = np.genfromtxt(data_file2)[:,index2]
    

        
    #~ ii = np.where(xx < 0.0)
    #~ xx[ii] += 360.0
        

    #~ ii = np.where(yy < 0.0)
    #~ yy[ii] += 360.0
    
    #~ XX, YY = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    #~ positions = np.vstack([XX.ravel(), YY.ravel()])



    #~ pdf_xy = np.reshape(kde(np.vstack([xx, yy]))(positions).T, XX.shape)
    #~ return XX, YY, pdf_xy


#~ XX, YY, pdf_pr1 = Build2dDensity(data_file1="./other_data/dihedrals_PR-with-waters.dat",data_file2="./other_data/dihedrals_PR-with-waters.dat",index1=1,index2=2)
#~ XX, YY, pdf_pr2 = Build2dDensity(data_file1="./other_data/dihedrals_PR-with-waters-replica.dat",data_file2="./other_data/dihedrals_PR-with-waters-replica.dat",index1=1,index2=2)
#~ XX, YY, pdf_pr3 = Build2dDensity(data_file1="./other_data/dihedrals_PR-with-waters-replica2.dat",data_file2="./other_data/dihedrals_PR-with-waters-replica2.dat",index1=1,index2=2)

#~ XX, YY, pdf_pts1 = Build2dDensity(data_file1="./other_data/dihedrals_PTS-with-waters.dat",data_file2="./other_data/dihedrals_PTS-with-waters.dat",index1=1,index2=2)
#~ XX, YY, pdf_pts2 = Build2dDensity(data_file1="./other_data/dihedrals_PTS-with-waters-replica.dat",data_file2="./other_data/dihedrals_PTS-with-waters-replica.dat",index1=1,index2=2)
#~ XX, YY, pdf_pts3 = Build2dDensity(data_file1="./other_data/dihedrals_PTS-with-waters-replica2.dat",data_file2="./other_data/dihedrals_PTS-with-waters-replica2.dat",index1=1,index2=2)




fig, axes = plt.subplots(ncols=1,nrows=8)

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 8*height)


aa = 0.7
lw = 1.5







# Load strings

simu1="normalized-fixed-500fs"
simu2="normalized-fixed-500fs-from-straight"
simu3="normalized-free-extend-fixed"
simu4="normalized-free-extend-straight"


last_iteration = ["run9.iter019-rst", "run6.iter019-rst" , "run10.iter019-rst", "run6.iter019-rst","run7.iter009-rst", "run7.iter019-rst","run3.iter013-rst"]
string_names = ["Mixed 1", "Mixed 2","Straight 1","Straight 2", "Straight 3","Free mixed","Free straight"]
string_colors= ["#F422D4","#9F138A","#0b557c","cyan","#267ead","#ad264d","#798ba8"]

for kk,run in enumerate([simu1, simu1+"-replica",simu2,simu2+"-replica",simu2+"-replica2",simu3,simu4]):
    
    

    data = np.genfromtxt("./%s/%s.relay_dist.traj" %(run,last_iteration[kk]))

    
    k1 = data[:,1]
    k2 = data[:,2]
    k3 = data[:,3]
    k4 = data[:,4]
    k5 = data[:,5]
    k6 = data[:,6]
    k7 = data[:,7]
    
    i1 = data[:,8]
    i2 = data[:,9]
    i3 = data[:,10]
    i4 = data[:,11]
    i5 = data[:,12]

    
    
    for jj in xrange(8):
        axes[jj].plot(data[:,jj+5],marker='o',label="%s" %string_names[kk],color=string_colors[kk])


cv_list = ["490O--494N","491O--495N","492O--496N","65O--707OG","66CE--763 phenyl ring","702NE2--65O","702NE2--66O","64O--761N"]
for jj in xrange(8):
    axes[jj].set_ylabel(cv_list[jj])


axes[7].legend(loc='lower center', ncol = 4, bbox_to_anchor=(0.5,-0.5))

fig.savefig("auxiliary_cv.pdf")



plt.close('all')







