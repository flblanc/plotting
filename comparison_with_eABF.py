#!/usr/bin/env python
#-*-encoding:utf-8-*-




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





name = "thesis"
suffix = "thesis"

data_rep1="/media/florian/FBLANC_PRO/Data_for_thesis/Unbiased-replica-simulations-analysis"
data_rep2="/media/florian/FBLANC_PRO/Data_for_thesis/Unbiased-replica-simulations-analysis/Seesaw-dRMSD-470-480-vs-kink-ref-transducer"

pmf_rep="/media/florian/FBLANC_PRO/Data_for_thesis/eABF-kink-PR2PTS/2D-kink-converter/Occigen/Stratification"

smd_rep="SMD-RSH1-PR2PTS-100ns_2"


obs_prw  = np.genfromtxt("%s/PR-with-waters.colvars.traj" %data_rep1)
obs_prwr = np.genfromtxt("%s/PR-with-waters-replica.colvars.traj" %data_rep1)
obs_prwr2 = np.genfromtxt("%s/PR-with-waters-replica2.colvars.traj" %data_rep1)

obs_ptsw = np.genfromtxt("%s/PTS-with-waters.colvars.traj" %data_rep1)
obs_ptswr = np.genfromtxt("%s/PTS-with-waters-replica.colvars.traj" %data_rep1)
obs_ptswr2 = np.genfromtxt("%s/PTS-with-waters-replica2.colvars.traj" %data_rep1)

obs_ppaw = np.genfromtxt("%s/PPA-with-waters.colvars.traj" %data_rep1)
#~ obs_ppawr = np.genfromtxt("%s/PPA-with-waters-replica.colvars.traj" %data_rep1)
#~ obs_ppawr2 = np.genfromtxt("%s/PPA-with-waters-replica2.colvars.traj" %data_rep1)
#~ 
#~ obs_ppiw = np.genfromtxt("%s/PPI-with-waters.colvars.traj" %data_rep1)
#~ obs_ppiwr = np.genfromtxt("%s/PPI-with-waters-replica.colvars.traj" %data_rep1)


#~ obs_xray = np.genfromtxt("%s/XRAY.colvars.traj" %data_rep1)

# Time

tt_prw = obs_prw[:,0]/100.0
tt_prwr = obs_prwr[:,0]/100.0
tt_prwr2 = obs_prwr2[:,0]/100.0


tt_ptsw = obs_ptsw[:,0]/100.0
tt_ptswr = obs_ptswr[:,0]/100.0
tt_ptswr2 = obs_ptswr2[:,0]/100.0



# X'
x_prw = obs_prw[:,1]
x_prwr = obs_prwr[:,1]
x_prwr2 = obs_prwr2[:,1]


x_ptsw = obs_ptsw[:,1]
x_ptswr = obs_ptswr[:,1]
x_ptswr2 = obs_ptswr2[:,1]


# Y'
y_prw = obs_prw[:,2]
y_prwr = obs_prwr[:,2]
y_prwr2 = obs_prwr2[:,2]





y_ptsw = obs_ptsw[:,2]
y_ptswr = obs_ptswr[:,2]
y_ptswr2 = obs_ptswr2[:,2]


x_ppaw = obs_ppaw[:,1]
y_ppaw = obs_ppaw[:,2]


obs_prw  = np.genfromtxt("%s/PRw1.colvars.traj" %data_rep2)
obs_prwr = np.genfromtxt("%s/PRw2.colvars.traj" %data_rep2)
#~ obs_prwr2 = np.genfromtxt("%s/PRw3.colvars.traj" %data_rep2)

obs_ptsw = np.genfromtxt("%s/PTSw1.colvars.traj" %data_rep2)
obs_ptswr = np.genfromtxt("%s/PTSw2.colvars.traj" %data_rep2)
obs_ptswr2 = np.genfromtxt("%s/PTSw3.colvars.traj" %data_rep2)


obs_ppaw = np.genfromtxt("%s/PPAw1.colvars.traj" %data_rep2)

dr_kink_prw = obs_prw[:,5]
dr_kink_prwr = obs_prwr[:,5]
#~ dr_kink_prwr2 = obs_prwr2[:,5]
dr_kink_prwr2 = np.genfromtxt("%s/PR-with-waters-replica2/kink-rmsd_pts.dat" %data_rep1)[:,1] - np.genfromtxt("%s/PR-with-waters-replica2/kink-rmsd_pr.dat" %data_rep1)[:,1]


dr_kink_ptsw = obs_ptsw[:,5]
dr_kink_ptswr = obs_ptswr[:,5]
dr_kink_ptswr2 = obs_ptswr2[:,5]

dr_kink_ppaw = obs_ppaw[:,5]


obs_smd = np.genfromtxt("%s/run_full-subsampled.colvars.traj" %smd_rep)
smd_xp = obs_smd[:,24]
smd_dr = np.genfromtxt("%s/kink-rmsd_pts.dat" %smd_rep)[:,1] - np.genfromtxt("%s/kink-rmsd_pr.dat" %smd_rep)[:,1]


### PANEL ####

Ncont=8
lw=3.0

fig, ax = plt.subplots(ncols=1,nrows=1)

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 2*height)



xmin=-20.0
xmax=+10.0

ymin=-1.5
ymax=+1.5

Emax =20.0


prefix="%s/abf_prod22.czar" %pmf_rep
pmf = np.genfromtxt("%s.grad.pmf" %prefix)

npoints = []


# parse gradient file for number of grid points
with open("%s.grad" %prefix,'r') as gr:
    first_line = True
    for li in gr:
        if li.startswith("#"):
            if first_line ==True:
                number_of_colvars = int(li.split()[-1])
                assert number_of_colvars == 2
                first_line =False
            else:
                npoints.append(int(li.split()[-2]))
                print int(li.split()[-2])
        else:
            break
            

                
                    
            
            

npoints_x = npoints[0]
npoints_y = npoints[1]

X = pmf[:,0].reshape(npoints_x, npoints_y)
Y = pmf[:,1].reshape(npoints_x, npoints_y)
F = pmf[:,2].reshape(npoints_x, npoints_y)

#Emax = 25
if Emax >1.:
    levels = np.linspace(0.,Emax,30)

else:
    levels = np.linspace(0, Emax, 5)

#~ CMAP = "cool"
CMAP = "RdBu"
#~ CMAP = "RdBu"


cax = ax.contourf(X,Y,F, levels=levels, cmap=CMAP)

ax.set_ylabel(u""" Kink \u0394RMSD, \u00c5""")
ax.set_xlabel(u"""X' component, \u00c5""")



levels2 = [1.,3,5.,7,10.,13,15.,17, 20.]
#~ 
#~ levels2 = levels[::2]


cax2 = ax.contour(X,Y,F, colors="black", levels=levels2, linewidths=1.0)

ax.clabel(cax2, fontsize=12,inline=1,fmt="%i")

fig.colorbar(cax)

ax.scatter(smd_xp, smd_dr, s=7.0,color='black')

ax.grid(linewidth=0.5, color='black',linestyle='--')

plt.tight_layout()
#~ fig.savefig("SMD_converter_vs_kink_%s_%s.svg" %(name,suffix))
fig.savefig("SMD_converter_vs_kink_%s_%s.pdf" %(name,suffix))
#~ fig.savefig("SMD_converter_vs_kink-%s-%s.png" %(name,suffix),dpi=600)


#####################################################################
###################################################################
###

#####################################################################
###################################################################
###

#####################################################################
###################################################################
###
#####################################################################
###################################################################
###

fig, ax = plt.subplots(ncols=1,nrows=1)

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 2*height)



xmin=-20.0
xmax=+10.0

ymin=-1.5
ymax=+1.5

Emax =20.0


prefix="%s/abf_prod22.czar" %pmf_rep
pmf = np.genfromtxt("%s.grad.pmf" %prefix)

npoints = []


# parse gradient file for number of grid points
with open("%s.grad" %prefix,'r') as gr:
    first_line = True
    for li in gr:
        if li.startswith("#"):
            if first_line ==True:
                number_of_colvars = int(li.split()[-1])
                assert number_of_colvars == 2
                first_line =False
            else:
                npoints.append(int(li.split()[-2]))
                print int(li.split()[-2])
        else:
            break
            

                
                    
            
            

npoints_x = npoints[0]
npoints_y = npoints[1]

X = pmf[:,0].reshape(npoints_x, npoints_y)
Y = pmf[:,1].reshape(npoints_x, npoints_y)
F = pmf[:,2].reshape(npoints_x, npoints_y)

#Emax = 25
if Emax >1.:
    levels = np.linspace(0.,Emax,30)

else:
    levels = np.linspace(0, Emax, 5)

#~ CMAP = "cool"
CMAP = "RdBu"
#~ CMAP = "RdBu"


#~ cax = ax.contourf(X,Y,F, levels=levels, cmap=CMAP)

ax.set_ylabel(u""" Kink \u0394RMSD, \u00c5""")
ax.set_xlabel(u"""X' component, \u00c5""")



levels2 = [1.,3,5.,7,10.,15.]
#~ 
#~ levels2 = levels[::2]


cax2 = ax.contour(X,Y,F, colors="black", levels=levels2, linewidths=1.0)

ax.clabel(cax2, fontsize=12,inline=1,fmt="%i")

#~ fig.colorbar(cax)


X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])



pdf_pr1 = np.reshape(kde(np.vstack([x_prw, dr_kink_prw]))(positions).T, X.shape)
pdf_pr2 = np.reshape(kde(np.vstack([x_prwr, dr_kink_prwr]))(positions).T, X.shape)
pdf_pr3 = np.reshape(kde(np.vstack([x_prwr2, dr_kink_prwr2]))(positions).T, X.shape)


pdf_pts1 = np.reshape(kde(np.vstack([x_ptsw, dr_kink_ptsw]))(positions).T, X.shape)
pdf_pts2 = np.reshape(kde(np.vstack([x_ptswr, dr_kink_ptswr]))(positions).T, X.shape)
pdf_pts3 = np.reshape(kde(np.vstack([x_ptswr2, dr_kink_ptswr2]))(positions).T, X.shape)

pdf_ppa1 = np.reshape(kde(np.vstack([x_ppaw, dr_kink_ppaw]))(positions).T, X.shape)


ax.contour(X,Y,pdf_pr1,Ncont, colors=prw_color,linewidths=lw,label="PR+ATP (1)")
ax.contour(X,Y,pdf_pr2,Ncont, colors=prwr_color,linewidths=lw,label="PR+ATP (2)")
ax.contour(X,Y,pdf_pr3,Ncont, colors=prwr2_color,linewidths=lw,label="PR+ATP (3)")


ax.contour(X,Y,pdf_pts1,Ncont, colors=ptsw_color,linewidths=lw,label="PTS+ATP (1)")
ax.contour(X,Y,pdf_pts2,Ncont, colors=ptswr_color,linewidths=lw,label="PTS+ATP (2)")
ax.contour(X,Y,pdf_pts3,Ncont, colors=ptswr2_color,linewidths=lw,label="PTS+ATP (3)")

ax.contour(X,Y,pdf_ppa1,Ncont, colors=ppaw_color,linewidths=lw)

#~ ax.legend(loc="upper left")





ax.grid(linewidth=0.5, color='black',linestyle='--')
#~ ax.legend(loc='lower center',ncol=3,fontsize=16,frameon=False,markerscale=10.0)



plt.tight_layout()
fig.savefig("converter_vs_kink_%s_%s.pdf" %(name,suffix))
#~ fig.savefig("converter_vs_kink_%s_%s.svg" %(name,suffix))
#~ fig.savefig("converter_vs_kink-%s-%s.png" %(name,suffix),dpi=600)









