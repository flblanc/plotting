
# coding: utf-8

# In[21]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']="Arial"
mpl.rcParams['font.size'] = 20
get_ipython().magic(u'matplotlib inline')


# # Determination of a suitable toy potential

# In[10]:


def ExpQuadratic(x,y,xc,yc,xs,ys):
    
    a = ((x-xc)/xs)**2 + ((y-yc)/ys)**2 + (((x-xc)*(y-yc))/(xs*ys))
    return np.exp(-a)


# In[11]:


xx = np.linspace(-20.,40.0,1000)
yy = np.linspace(-20.,40.0,1000)

XX, YY = np.meshgrid(xx,yy)


# In[83]:


xc1 = -3.0
yc1 = -1.0
xs1 = -1.8
ys1 = 4.0

w1 = ExpQuadratic(XX,YY,xc1,yc1,xs1,ys1)

xc2 = 10
yc2 = 12
xs2 = 4.5
ys2 = 3.5

w2 = ExpQuadratic(XX,YY,xc2,yc2,xs2,ys2)

xc3 = xc1
yc3 = yc2
xs3 = +3.0
ys3 = -3.5

w3 = ExpQuadratic(XX,YY,xc3,yc3,xs3,ys3)


# In[222]:


A = 5.0
B = 5.0
C = 3.0


F = - (A*w1+B*w2+C*w3)
F -= F.min()




# In[220]:


fig, ax = plt.subplots()

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(1*width, 1*height)


cax = ax.contour(XX,YY,F,cmap='coolwarm')
# ax.contour(XX,YY,F,levels=[0.5,1.5,2.5],colors='black')
# fig.colorbar(cax)



ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_linewidth(2.0)
ax.spines['bottom'].set_linewidth(2.0)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')




ax.xaxis.set_ticklabels('')
ax.yaxis.set_ticklabels('')

ax.set_xlim(-10.0,+20)
ax.set_ylim(-10.0,+20)

ax.set_xlabel(u"""$\\xi$""", fontsize=25)
ax.set_ylabel(u"""$\eta$   """,rotation='horizontal', fontsize=25)


eps = 1.0
ax.annotate(s="R",color="grey",xy=(xc1,yc1),xytext=(xc1+5*eps,yc1-5.*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='bottom')


ax.annotate(s="P",color="grey",xy=(xc2,yc2),xytext=(xc2,yc2-10*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='center')

ax.annotate(s="I",color="grey",xy=(xc3,yc3),xytext=(xc3-5*eps,yc3+5*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='center')


# Pathway 

ax.annotate(s="", xy=(xc3,yc3), xytext=(xc1,yc1),
           arrowprops=dict(facecolor='black',width=2.0,linewidth=0.5,shrink=0.05))

circle_box = dict(boxstyle="circle",fc="lightgrey",lw=0.0,alpha=0.8)
ax.text(x = xc1-2*eps, y=0.5*(yc1+yc3),s="1",ha="center",va="center",size=20,bbox=circle_box)




ax.annotate(s="", xy=(xc2,yc2), xytext=(xc3,yc3),
           arrowprops=dict(facecolor='black',width=2.0,linewidth=0.5,shrink=0.05))
ax.text(x =0.5*(xc2+xc3),y = yc2+3*eps, s="2",ha="center",va="center",size=20,bbox=circle_box)
fig.show();


# In[221]:


fig.savefig("statistical_coupling.pdf")


# # Mechanical coupling situation

# In[234]:


xcv1 = -3.0
ycv1 = -1.0
xsv1 = +4.0
ysv1 = 4.0

v1 = ExpQuadratic(XX,YY,xcv1,ycv1,xsv1,ysv1)

xcv2 = 10
ycv2 = 12
xsv2 = 5.5
ysv2 = -5.5

v2 = ExpQuadratic(XX,YY,xcv2,ycv2,xsv2,ysv2)


A2 = 6.0
B2 = 6.0

G = - (A2*v1+B2*v2)
G -= G.min()


# In[248]:


fig, axes = plt.subplots(ncols=2,sharey=True)

bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
fig.set_size_inches(2*width, 1*height)


# Statistical coupling

ax = axes[1]


cax = ax.contour(XX,YY,F,cmap='coolwarm')
# ax.contour(XX,YY,F,levels=[0.5,1.5,2.5],colors='black')
# fig.colorbar(cax)



ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_linewidth(2.0)
ax.spines['bottom'].set_linewidth(2.0)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')




ax.xaxis.set_ticklabels('')
ax.yaxis.set_ticklabels('')

ax.set_xlim(-10.0,+20)
ax.set_ylim(-10.0,+20)

ax.set_xlabel(u"""$\\xi$""", fontsize=25)
ax.set_ylabel(u"""$\eta$   """,rotation='horizontal', fontsize=25)


eps = 1.0
ax.annotate(s="R",color="grey",xy=(xc1,yc1),xytext=(xc1+5*eps,yc1-5.*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='bottom')


ax.annotate(s="P",color="grey",xy=(xc2,yc2),xytext=(xc2,yc2-10*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='center')

ax.annotate(s="I",color="grey",xy=(xc3,yc3),xytext=(xc3-5*eps,yc3+5*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='center')


# Pathway 

ax.annotate(s="", xy=(xc3,yc3), xytext=(xc1,yc1),
           arrowprops=dict(facecolor='black',width=2.0,linewidth=0.5,shrink=0.05))

circle_box = dict(boxstyle="circle",fc="lightgrey",lw=0.0,alpha=0.8)
ax.text(x = xc1-2*eps, y=0.5*(yc1+yc3),s="1",ha="center",va="center",size=20,bbox=circle_box)




ax.annotate(s="", xy=(xc2,yc2), xytext=(xc3,yc3),
           arrowprops=dict(facecolor='black',width=2.0,linewidth=0.5,shrink=0.05))
ax.text(x =0.5*(xc2+xc3),y = yc2+3*eps, s="2",ha="center",va="center",size=20,bbox=circle_box)

ax.set_title("Statistical coupling",fontsize=22)

# Mechanical coupling

ax = axes[0]


cax = ax.contour(XX,YY,G,cmap='coolwarm')
# ax.contour(XX,YY,F,levels=[0.5,1.5,2.5],colors='black')
# fig.colorbar(cax)



ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_linewidth(2.0)
ax.spines['bottom'].set_linewidth(2.0)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')




ax.xaxis.set_ticklabels('')
ax.yaxis.set_ticklabels('')

ax.set_xlim(-10.0,+23)
ax.set_ylim(-10.0,+23)

ax.set_xlabel(u"""$\\xi$""", fontsize=25)
ax.set_ylabel(u"""$\eta$   """,rotation='horizontal', fontsize=25)


eps = 1.0
ax.annotate(s="R",color="grey",xy=(xc1,yc1),xytext=(xc1,yc1+12*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='center')


ax.annotate(s="P",color="grey",xy=(xc2,yc2),xytext=(xc2+10*eps,yc2-10*eps), 
            fontsize=25, 
            arrowprops=dict(facecolor='grey',arrowstyle='->'),
            verticalalignment='center',
            horizontalalignment='center')

# ax.annotate(s="I",color="grey",xy=(xc3,yc3),xytext=(xc3-5*eps,yc3+5*eps), 
#             fontsize=25, 
#             arrowprops=dict(facecolor='grey',arrowstyle='->'),
#             verticalalignment='center',
#             horizontalalignment='center')


# Pathway 

ax.annotate(s="", xy=(xc2,yc2), xytext=(xc1,yc1),
           arrowprops=dict(facecolor='black',width=2.0,linewidth=0.5,shrink=0.05))

# circle_box = dict(boxstyle="circle",fc="lightgrey",lw=0.0,alpha=0.8)
# ax.text(x = xc1-2*eps, y=0.5*(yc1+yc3),s="1",ha="center",va="center",size=20,bbox=circle_box)




# ax.annotate(s="", xy=(xc2,yc2), xytext=(xc3,yc3),
#            arrowprops=dict(facecolor='black',width=2.0,linewidth=0.5,shrink=0.05))
# ax.text(x =0.5*(xc2+xc3),y = yc2+3*eps, s="2",ha="center",va="center",size=20,bbox=circle_box)

ax.set_title("Mechanical coupling",fontsize=22)

plt.tight_layout()

fig.show();

fig.savefig("mechanical_vs_statistical.pdf")


# In[260]:


# Reaction coordinate for mechanical coupling

# RCx = xcv1 + ((xx-xcv2)/(xcv2-xcv1))
# RCy = ycv1 + ((yy-ycv2)/(ycv2-ycv1))

RCx = np.linspace(xcv1-1.0,xcv2+3.0,100)
RCy = np.linspace(ycv1-1.0,ycv2+3.0,100)

fig, axes = plt.subplots(ncols=2)

vg1 = ExpQuadratic(RCx,RCy,xcv1,ycv1,xsv1,ysv1)
vg2 = ExpQuadratic(RCx,RCy,xcv2,ycv2,xsv2,ysv2)

g = - (A2*vg1+B2*vg2)
g -= g.min()
ax = axes[0]
ax.plot(RCx,g)

ax = axes[1]
ax.plot(RCy,g)
fig.show();


# Now I need to implement Langevin dynamics on both potentials and show trajectories; also, string method; 
# 
# The interesting case for our study is when one dof is much faster than the other, so that it locally equilibrates in each basin. In this case it is justified to talk about population shift even though no-ligand binding, or other external perturbation to the potential energy surface, is involved.
