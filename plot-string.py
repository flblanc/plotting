#!/usr/bin/env python
#-*-encoding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

st = np.genfromtxt("string2000.dat")

energy = st[1:,1]
alpha = np.linspace(0,1,len(energy))


st_tmd = np.genfromtxt("../relay-helix-zts-tmd-30/data/string2000.dat")


# there are only 30 replicas in the TMD string, so I rescale alpha



energy_tmd = st_tmd[1:,1]
alpha_tmd = np.linspace(0,1,len(energy_tmd))

fig, ax  = plt.subplots() 

ax.plot(alpha, energy, color='red',marker='o', label="Interpolated guess")
ax.plot(alpha_tmd, energy_tmd, color='green',marker='x', label="TMD guess")

ax.set_xlabel(u"""String parameter $\\alpha$""")
ax.set_ylabel(u"""Potential energy, kcal/mol""")

ax.grid()
ax.legend(loc='best')

ax.set_xlim(xmin=0.0, xmax=1.0)

fig.savefig("string-rh.svg")


