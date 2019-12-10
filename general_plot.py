#!/usr/bin/env python
#-*-:encoding:utf-8-*-

import numpy as np
from scipy.stats import gaussian_kde as kde



import matplotlib.pyplot as plt 
import matplotlib as mpl
import matplotlib.ticker as plticker 
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from matplotlib.lines import Line2D

ref_repertory = "/home/tb/flblanc/DATA/Polytomella_ATP_synthase/analysis_of_cryoEM/simplified_models_for_colvars_analysis"


mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 18.0

mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['legend.frameon'] = False


#######################
# AUXILIARY FUNCTIONS # 
#######################

N=20

def runningMeanFast(x, N=N):
    """Updated version with modification by Prof. Hugues Talbot."""
    x1 = np.pad(x,N,mode='reflect')
    output =np.convolve(x1, np.ones((N,))/N)[(N-1):]
    return output[N:-N]

rrr=runningMeanFast

def shift_angle(x):
    if x<0:
        return x+360.0
    else:
        return x

vec_shift_angle = np.vectorize(shift_angle)

################
# CRYO-EM DATA #
################



data = np.genfromtxt("{0}/rotary_substates.traj".format(ref_repertory))

hinge1 = vec_shift_angle(data[:,1])
hinge2 = vec_shift_angle(data[:,2])
c_rota = vec_shift_angle(data[:,3])
c_tilt = data[:,4]
f_rota = vec_shift_angle(data[:,5])
f_tilt = data[:,6]
g_rota = vec_shift_angle(data[:,7])
g_tilt = data[:,8]
#g_rota = data[:,5]
g_rota[0] = 0.0 # it is 360 - epsilon

###################
# SIMULATION DATA #
###################

class Simulation:
    
    def __init__(self,name,structural_state,label,color):
        
        self.name = name 
        self.structural_state = structural_state
        self.label = label
        self.color = color
        
    def load_MD_data(self,repertory,last_traj_index):
        
        for k in range(1,last_traj_index+1):
    
            if k==1:
                md_data = np.genfromtxt("{0}/umd1.traj".format(repertory))
            else:
                tmp_ = np.genfromtxt("{0}/umd{1}.traj".format(repertory,k))[1:,:]
                md_data = np.r_[md_data,tmp_]
            
        self.md_data = md_data
        
    def extract_MD_observables(self):
        
        self.oscp1_md = self.md_data[:,1]
        self.oscp2_md = self.md_data[:,2]
        
        self.c_md = self.md_data[:,3]       
        self.c_md_tilt = self.md_data[:,4]
        self.f_md = self.md_data[:,5]
        self.f_md_tilt = self.md_data[:,6]
        self.g_md = self.md_data[:,7]
        self.g_md_tilt = self.md_data[:,8]
        
        self.t_md = np.arange(0,np.shape(self.md_data)[0])
        
        
                
        
        
        



color_all_1="deepskyblue"
color_all_2="darkblue"

color_0_1 = "forestgreen"
color_0_2 = "lime"

color_3_1 = "yellow"
color_3_2 = "orange"

last_traj_index_all_1 = 40
last_traj_index_all_2 = 30

last_traj_index_0_1 = 30
last_traj_index_0_2 = 26

last_traj_index_3_1 = 21
last_traj_index_3_2 = 23


all_free_1 = Simulation(name="all_free_1",structural_state="All Free",label="All free (1)",color="deepskyblue")
all_free_1.load_MD_data(repertory="ALL_FREE_21.6nm_21.6nm_28nm/Unbiased-MD-1",last_traj_index = last_traj_index_all_1)
all_free_1.extract_MD_observables()

all_free_2 = Simulation(name="all_free_2",structural_state="All Free",label="All free (2)",color="dodgerblue")
all_free_2.load_MD_data(repertory="ALL_FREE_21.6nm_21.6nm_28nm/Unbiased-MD-2",last_traj_index = last_traj_index_all_2)
all_free_2.extract_MD_observables()

state0_1 = Simulation(name="state0_1",structural_state="State 0",label="State 0 (1)",color="forestgreen")
state0_1.load_MD_data(repertory="state0_21.6nm_21.6nm_28nm/Unbiased-MD-1",last_traj_index = last_traj_index_0_1)
state0_1.extract_MD_observables()

state0_2 = Simulation(name="state0_2",structural_state="State 0",label="State 0 (2)",color="lime")
state0_2.load_MD_data(repertory="state0_21.6nm_21.6nm_28nm/Unbiased-MD-2",last_traj_index = last_traj_index_0_2)
state0_2.extract_MD_observables()

state3_1 = Simulation(name="state3_1",structural_state="State 3",label="State 3 (1)",color="orangered")
state3_1.load_MD_data(repertory="state3_21.6nm_21.6nm_28nm/Unbiased-MD-1",last_traj_index = last_traj_index_3_1)
state3_1.extract_MD_observables()

state3_2 = Simulation(name="state3_2",structural_state="State 3",label="State 3 (2)",color="sienna")
state3_2.load_MD_data(repertory="state3_21.6nm_21.6nm_28nm/Unbiased-MD-2",last_traj_index = last_traj_index_3_2 )
state3_2.extract_MD_observables()

simulation_list = [all_free_1,all_free_2,state0_1,state0_2,state3_1,state3_2]

def PlotTimeSeries(simulation,observable,ax,lw1,lw2,alpha):
    
    ax.plot(simulation.t_md, rrr(observable), color=simulation.color,linewidth=lw1,zorder=2,label=simulation.label)
    ax.plot(simulation.t_md, observable, color=simulation.color,linewidth=lw2,alpha=alpha,zorder=1,label=simulation.label)
    
def PlotDensity(simulation,observable,ax,lwd,padding=5.0):
    
    xx = np.linspace(observable.min()-padding,observable.max()+padding,1000)
    pdf = kde(observable)
    
    ax.plot(pdf(xx),xx,color=simulation.color,linewidth=lwd)
    ax.set_xlim(xmin=0.0)
    
    density_max = np.max(pdf(xx))
    return density_max


def DrawPlot1(simulation_list,lw1=1.5,lw2=5.0,alpha=0.2,lwd=2.5):

    # Prepare canvas

    #fig, axes = plt.subplots(nrows=3, ncols=3,sharey='row',dpi=600)
    fig = plt.figure(dpi=600)
    
    ww = [2,1]
    hh = [1,1,1,0.7]
    
    gs = fig.add_gridspec(nrows=4,ncols=2,width_ratios=ww,height_ratios=hh)
    
    axes = [[fig.add_subplot(gs[0,0]),fig.add_subplot(gs[0,1])],
    [fig.add_subplot(gs[1,0]),fig.add_subplot(gs[1,1])],
    [fig.add_subplot(gs[2,0]),fig.add_subplot(gs[2,1])]]
    
    
    
    
    bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    fig.set_size_inches(3*width, 4*height)
    
    
    # Adjust relative size of subplots using gridspec

    # Plot time series and densities for each simulation

    maxd1 = 0.0
    maxd2 = 0.0
    maxd3 = 0.0

    for i in simulation_list:
        
        PlotTimeSeries(simulation=i, observable=i.c_md,ax=axes[0][0],lw1=lw1,lw2=lw2,alpha=alpha)
        PlotTimeSeries(simulation=i, observable=i.g_md,ax=axes[1][0],lw1=lw1,lw2=lw2,alpha=alpha)
        PlotTimeSeries(simulation=i, observable=i.f_md,ax=axes[2][0],lw1=lw1,lw2=lw2,alpha=alpha)
        
        maxd1 = np.max([maxd1,PlotDensity(simulation=i,observable=i.c_md,ax = axes[0][1],lwd=lwd)])
        maxd2 = np.max([maxd2,PlotDensity(simulation=i,observable=i.g_md,ax = axes[1][1],lwd=lwd)])
        maxd3 = np.max([maxd3,PlotDensity(simulation=i,observable=i.f_md,ax = axes[2][1],lwd=lwd)])
        
            
    axes[0][1].set_xlim(xmax=maxd1+0.05)
    axes[1][1].set_xlim(xmax=maxd2+0.05)
    axes[2][1].set_xlim(xmax=maxd3+0.05)
    
    for j in range(3):
        #axes[j][1].set_xticks([])
        axes[j][1].set_xticklabels(['    '])
        
        # Adjust axes (emulates sharey='row')
        axes[j][1].set_ylim(axes[j][0].get_ylim())
        
        # 
        axes[j][0].set_xlim(xmin=0.0)
        
    axes[2][0].set_xlabel("Time, ns")
    axes[2][1].set_xlabel("Probability density (arbitrary units)")
    
    zoom_schema = 0.03
    
    F_schema = mpimg.imread("atp_synthase_schema_F.png")
    imagebox = OffsetImage(F_schema,zoom=zoom_schema)
    ab = AnnotationBbox(imagebox, (1500,10),frameon=False)
    axes[2][0].add_artist(ab)
    
    g_schema = mpimg.imread("atp_synthase_schema_g.png")
    imagebox = OffsetImage(g_schema,zoom=zoom_schema)
    ab = AnnotationBbox(imagebox, (1500.,10),frameon=False)
    axes[1][0].add_artist(ab)

    c_schema = mpimg.imread("atp_synthase_schema_c.png")
    imagebox = OffsetImage(c_schema,zoom=zoom_schema)
    ab = AnnotationBbox(imagebox, (1500.,-2.5),frameon=False)
    axes[0][0].add_artist(ab)    
    
    
    fig.suptitle("Global conformational dynamics of ATP synthase",fontsize=30,weight='bold')
    
    axes[0][0].set_ylabel("c-ring rotation angle, deg")
    axes[1][0].set_ylabel("Central stalk rotation angle, deg")
    axes[2][0].set_ylabel("$F_1$ head rotation angle, deg")
    
    # Draw custom legend
    legend_ax = fig.add_subplot(gs[3,:])
    
    
    custom_lines = []
    
    for t in simulation_list:
        
        custom_lines.append(Line2D([0], [0], color=t.color, lw=2*lw1,label=t.label))
        
    legend_ax.legend(handles=custom_lines,loc='lower center',ncol=3,fontsize=25,frameon=False,markerscale=10.0)
    legend_ax.spines['bottom'].set_visible(False)
    legend_ax.spines['left'].set_visible(False)
    legend_ax.set_xticks([])
    legend_ax.set_xticklabels([])
    legend_ax.set_yticks([])
    legend_ax.set_yticklabels([])
    
    
    fig.canvas.draw_idle()
    fig.savefig("general_time_series_conformational_state.png")
    plt.close('all')
    return 0.0        
    
    
def DrawPlot2(simulation_list,lw1=1.5,lw2=5.0,alpha=0.2,lwd=2.5):

    # Prepare canvas

    #fig, axes = plt.subplots(nrows=3, ncols=3,sharey='row',dpi=600)
    fig = plt.figure(dpi=600)
    
    ww = [2,1]
    hh = [1,1,0.7]
    
    gs = fig.add_gridspec(nrows=3,ncols=2,width_ratios=ww,height_ratios=hh)
    
    axes = [[fig.add_subplot(gs[0,0]),fig.add_subplot(gs[0,1])],
    [fig.add_subplot(gs[1,0]),fig.add_subplot(gs[1,1])]]
    
    
    
    
    bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    fig.set_size_inches(3*width, 4*height)
    
    
    # Adjust relative size of subplots using gridspec

    # Plot time series and densities for each simulation

    maxd1 = 0.0
    maxd2 = 0.0

    for i in simulation_list:
        
        PlotTimeSeries(simulation=i, observable=i.oscp1_md,ax=axes[0][0],lw1=lw1,lw2=lw2,alpha=alpha)
        PlotTimeSeries(simulation=i, observable=i.oscp2_md,ax=axes[1][0],lw1=lw1,lw2=lw2,alpha=alpha)
        
        maxd1 = np.max([maxd1,PlotDensity(simulation=i,observable=i.oscp1_md,ax = axes[0][1],lwd=lwd)])
        maxd2 = np.max([maxd2,PlotDensity(simulation=i,observable=i.oscp2_md,ax = axes[1][1],lwd=lwd)])
        
            
    axes[0][1].set_xlim(xmax=maxd1+0.05)
    axes[1][1].set_xlim(xmax=maxd2+0.05)
    
    for j in range(2):
        #axes[j][1].set_xticks([])
        axes[j][1].set_xticklabels(['    '])
        
        # Adjust axes (emulates sharey='row')
        axes[j][1].set_ylim(axes[j][0].get_ylim())
        
        # 
        axes[j][0].set_xlim(xmin=0.0)
        
    axes[1][0].set_xlabel("Time, ns")
    axes[1][1].set_xlabel("Probability density (arbitrary units)")
 
    
    
    fig.suptitle("Conformational Dynamics of the OSCP peptide",fontsize=30,weight='bold')
    
    axes[0][0].set_ylabel("OSCP bending angle, deg")
    axes[1][0].set_ylabel("OSCP bending dihedral angle, deg")
    
    # Draw custom legend
    legend_ax = fig.add_subplot(gs[2,:])
    
    
    custom_lines = []
    
    for t in simulation_list:
        
        custom_lines.append(Line2D([0], [0], color=t.color, lw=2*lw1,label=t.label))
        
    legend_ax.legend(handles=custom_lines,loc='lower center',ncol=3,fontsize=25,frameon=False,markerscale=10.0)
    legend_ax.spines['bottom'].set_visible(False)
    legend_ax.spines['left'].set_visible(False)
    legend_ax.set_xticks([])
    legend_ax.set_xticklabels([])
    legend_ax.set_yticks([])
    legend_ax.set_yticklabels([])
    
    
    fig.canvas.draw_idle()
    fig.savefig("general_time_series_oscp.png")
    plt.close('all')
    return 0.0        

            
DrawPlot1(simulation_list)
DrawPlot2(simulation_list)



