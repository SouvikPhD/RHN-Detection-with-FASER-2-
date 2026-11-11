#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 12:06:10 2024

@author: souvik
"""

import sys
src_path = "/home/souvik/codes/foresee-main"
sys.path.append(src_path)

import numpy as np
# from src.foresee import Foresee, Utility, Model

from matplotlib import pyplot as plt

import os
from matplotlib import pyplot as plt
import math
import random
from skhep.math.vectors import LorentzVector, Vector3D
from scipy import interpolate
from matplotlib import gridspec
import os, inspect

from matplotlib import cm, ticker
import matplotlib
from mpl_toolkits.axes_grid1.inset_locator import inset_axes




sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "/home/souvik/codes/darkcast_chiral/"))
import RHN_decay as ndec
import darkcast_scalar as darkcast

#%%

ths = np.logspace(-8, 1, 100)
g = 0.01
mzp = 100
xH = 0
mN = 1000
name = "U1_X"
modname="U(1)_X"
masses = np.logspace(-3,0,1000)
colors = ["red", "blue", "green"]
for (i,th) in enumerate([1e-2, 1e-3, 1e-4]):
    mN1, mN2, mN3 = mN, 1000, 1000
    modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp) 
    ctaus = []
    for m in masses:
        ctaus.append(modelD.ctau(m, 0, th=th, g=g)) 
    plt.plot(masses, ctaus, color = colors[i])
plt.xscale("log")
plt.yscale("log")
plt.xlim([1e-3, 1])
plt.ylim([1e-4, 1e12])

plt.plot([1e-20], [1e-20], label=r"$\sin\theta=10^{-2}$", linestyle="solid", color = "red")
plt.plot([1e-20], [1e-20], label=r"$\sin\theta=10^{-3}$", linestyle="solid", color = "blue")
plt.plot([1e-20], [1e-20], label=r"$\sin\theta=10^{-4}$", linestyle="solid", color = "green")

plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
plt.xlabel(r"$m_{h_2} \text{[GeV]}$", fontsize=25)
plt.ylabel(r"$c\tau \text{[m]}$", fontsize=25)
plt.legend(fontsize=20)

#%%

ths = np.logspace(-8, 1, 100)
g = 0.01
mzp = 100
xH = 0
name = "U1_X"
modname="U(1)_X"
masses = np.logspace(-3,0,1000)
colors = ["red", "blue", "green"]
style = ["solid", "dashed"]
for (s,mN) in enumerate([0.25, 0.49]):
    for (i,th) in enumerate([1e-2, 1e-3, 1e-4]):
        mN1, mN2, mN3 = mN, 1000, 1000
        modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp) 
        ctaus = []
        for m in masses:
            ctaus.append(modelD.ctau(m, 0, th=th, g=g)) 
        plt.plot(masses, ctaus, color = colors[i], linestyle=style[s])
plt.xscale("log")
plt.yscale("log")
plt.xlim([1e-3, 1])
plt.ylim([1e-6, 1e4])

plt.plot([1e-20], [1e-20], label=r"$\sin\theta=10^{-2}$", linestyle="solid", color = "red")
plt.plot([1e-20], [1e-20], label=r"$\sin\theta=10^{-3}$", linestyle="solid", color = "blue")
plt.plot([1e-20], [1e-20], label=r"$\sin\theta=10^{-4}$", linestyle="solid", color = "green")

plt.plot([1e-20], [1e-20], label=r"$m_N/m_{h_2} = 0.25$", linestyle="solid", color = "black")
plt.plot([1e-20], [1e-20], label=r"$m_N/m_{h_2} = 0.49$", linestyle="dashed", color = "black")

plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
plt.xlabel(r"$m_{h_2} \text{[GeV]}$", fontsize=25)
plt.ylabel(r"$c\tau \text{[m]}$", fontsize=25)
plt.legend(fontsize=18)

#%%
ths = np.logspace(-8, 1, 100)
g = 0.01
mzp = 100
xH = 0
mN1, mN2, mN3 = 0.49, 1000, 1000
name = "U1_X"
modname="U(1)_X"
masses = np.logspace(-3,1,1000)

ctaus = []
modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp)
for th in ths:
    ct = []
    for m in masses:
        ct.append(modelD.ctau(m, 0, th=th, g=g))
    ctaus.append(ct)
    

ctau = np.array(ctaus)

    
hmv, hgv = np.meshgrid(masses, ths)
plt.rcParams["figure.figsize"] = (8, 6)
plt.rcParams.update({
    "text.usetex": False,          # Disable external LaTeX binary call
    "mathtext.fontset": "cm",      # Use Computer Modern fonts for math/text
    "font.family": "serif"})
plt.xscale("log")
plt.yscale("log")
plt.xlim([1e-3, 1])
plt.ylim([1e-6,1])
plt.xlabel(r"$m_{h_2} \text{[GeV]}$", fontsize=25)
plt.ylabel(r"$\sin$$\theta$", fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{Z^\prime}=$" + str(mzp) + "GeV,  $g_{BL}$=" + str(g) , y=0.2, x=0.72, fontsize=20)
plt.tight_layout()


# plt.text(5e-2,5e-8, "FASER2", fontsize=20)

ts = plt.pcolormesh(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm(vmin=1e-6, vmax=1e4))

my_levels = [100, 1500]
my_colors = ['white', "red"]

cs = plt.contour(hmv, hgv, ctau, 
                  levels=my_levels, 
                  colors=my_colors, 
                  linewidths=2)

tax = plt.axes([1.002, 0.14, 0.03, 0.84])
tbar = plt.colorbar(ts, location = "right", cax=tax, extend='both')
tbar.set_label(r'c$\tau \text{ [m]}$', labelpad=2, rotation=90, fontsize=25)
tbar.ax.tick_params(labelsize=20)

tbar.ax.yaxis.set_ticks_position('right')
tbar.ax.yaxis.set_label_position('left')

# levels=[1e-1, 1, 1e2, 1e3]
# cs = plt.contourf(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm())
# cax = plt.axes([1.08, 0.14, 0.03, 0.84])

# cbar = plt.colorbar(cs, location = "right", cax=cax)
# cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
# cbar.ax.tick_params(labelsize=16)


plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/hzpln_ct.pdf",bbox_inches='tight')
plt.show()

       
    
    
#%%

ths = np.logspace(-8, 1, 100)
g = 0.01
mzp = 100
xH = 0
mN1, mN2, mN3 = 1000, 1000, 1000
name = "U1_X"
modname="U(1)_X"
masses = np.logspace(-3,1,1000)

ths = [1e-3, 1e-4, 1e-5]

plt.rcParams["figure.figsize"] = (8, 6)

for th in ths:
    ctaus = []
    modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp)
    for m in masses:
        ctaus.append(modelD.ctau(m, 0, th=th, g=g))
        

    
    plt.plot(masses, ctaus, label=r"$\sin\theta = 10^{"+str(int(np.log10(th)))+"}$")
    
plt.xscale("log")
plt.yscale("log")
plt.xlim([1e-3, 1])
plt.ylim([1e-4, 1e12])
plt.xlabel(r"$m_{h_2}$[GeV]", fontsize=25)
plt.ylabel(r"c$\tau$[m]", fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.title(r"$M_N/M_{Z'} = $"+str(mN1))
plt.legend(fontsize = 20)
# plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{Z^\prime}=$" + str(mzp) + "GeV,  $g_{BL}$=" + str(g) , y=0.2, x=0.72, fontsize=20)
plt.tight_layout()
plt.savefig(f"/home/souvik/codes/FORESEE_fig/scalar_fig/h2length.png",bbox_inches='tight')
plt.show()

ths = np.logspace(-8, 1, 100)
g = 0.01
mzp = 100
xH = 0
mN1, mN2, mN3 = 1/4, 1000, 1000
name = "U1_X"
modname="U(1)_X"
masses = np.logspace(-3,1,1000)

ths = [1e-3, 1e-4, 1e-5]

plt.rcParams["figure.figsize"] = (8, 6)

for th in ths:
    ctaus = []
    modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp)
    for m in masses:
        ctaus.append(modelD.ctau(m, 0, th=th, g=g))
        

    
    plt.plot(masses, ctaus, label=r"$\sin\theta = 10^{"+str(int(np.log10(th)))+"}$")
    
plt.xscale("log")
plt.yscale("log")
plt.xlim([1e-3, 1])
plt.ylim([1e-6, 1e4])
plt.xlabel(r"$m_{h_2}$[GeV]", fontsize=25)
plt.ylabel(r"c$\tau$[m]", fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.title(r"$M_N/M_{Z'} = $"+str(mN1))
plt.legend(fontsize = 20)
# plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{Z^\prime}=$" + str(mzp) + "GeV,  $g_{BL}$=" + str(g) , y=0.2, x=0.72, fontsize=20)
plt.tight_layout()
plt.savefig(f"/home/souvik/codes/FORESEE_fig/scalar_fig/h2length_N.png",bbox_inches='tight')
plt.show()


#%%
ths = np.logspace(-8, 1, 100)
g = 1e-9

mzp = 1/4

xH = 0
mN1, mN2, mN3 = 1000, 1000, 1000
name = "U1_X"
modname="U(1)_X"
masses = np.logspace(-3,1,1000)

ctaus = []
modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=True, cZ=False, mZ=mzp)
for th in ths:
    ct = []
    for m in masses:
        ct.append(modelD.ctau(m, 0, th=th, g=g))
    ctaus.append(ct)
    

ctau = np.array(ctaus)

    
hmv, hgv = np.meshgrid(masses, ths)
plt.rcParams["figure.figsize"] = (8, 6)
plt.xscale("log")
plt.yscale("log")
plt.xlim([1e-3, 1])
plt.ylim([1e-6,1])
plt.xlabel(r"$m_{h_2}$[GeV]", fontsize=25)
plt.ylabel(r"$sin$$\theta$", fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{N}=$" + str(mN1/1000) + "TeV,  $g_{BL}$=" + str(g) , y=0.2, x=0.32, fontsize=20)
plt.tight_layout()


# plt.text(5e-2,5e-8, "FASER2", fontsize=20)

ts = plt.pcolormesh(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm(vmin=1e-6, vmax=1e4))

my_levels = [500]
my_colors = ['white'] 

cs = plt.contour(hmv, hgv, ctau, 
                  levels=my_levels, 
                  colors=my_colors, 
                  linewidths=5)

tax = plt.axes([1.002, 0.14, 0.03, 0.84])
tbar = plt.colorbar(ts, location = "right", cax=tax)
tbar.set_label(r'c$\tau$ [m]', labelpad=2, rotation=90, fontsize=25)
tbar.ax.tick_params(labelsize=20)

tbar.ax.yaxis.set_ticks_position('right')
tbar.ax.yaxis.set_label_position('left')

# levels=[1e-1, 1, 1e2, 1e3]
# cs = plt.contourf(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm())
# cax = plt.axes([1.08, 0.14, 0.03, 0.84])

# cbar = plt.colorbar(cs, location = "right", cax=cax)
# cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
# cbar.ax.tick_params(labelsize=16)

plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/lzphn_ct.pdf",bbox_inches='tight')
plt.show()
    
    
    
#%%

ths = np.logspace(-8, 1, 100)
g = 5e-9

mzp = 0.15

xH = 0
mN1, mN2, mN3 = 1/4, 1000, 1000
name = "U1_X"
modname="U(1)_X"
masses = np.logspace(-3,1,1000)

ctaus = []
modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp)
for th in ths:
    ct = []
    for m in masses:
        ct.append(modelD.ctau(m, 0, th=th, g=g))
    ctaus.append(ct)
    

ctau = np.array(ctaus)

    
hmv, hgv = np.meshgrid(masses, ths)
plt.rcParams["figure.figsize"] = (8, 6)
plt.xscale("log")
plt.yscale("log")
plt.xlim([1e-3, 1])
plt.ylim([1e-6,1])
plt.xlabel(r"$m_{h_2}$[GeV]", fontsize=25)
plt.ylabel(r"$sin$$\theta$", fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{Z^\prime}=$" + str(mzp*1000) + "MeV,  $g_{BL}$=" + str(g) , y=0.2, x=0.32, fontsize=20)
plt.tight_layout()


# plt.text(5e-2,5e-8, "FASER2", fontsize=20)

ts = plt.pcolormesh(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm(vmin=1e-6, vmax=1e4))

my_levels = [500]
my_colors = ['white'] 

cs = plt.contour(hmv, hgv, ctau, 
                  levels=my_levels, 
                  colors=my_colors,
                  linewidths=5)

tax = plt.axes([1.002, 0.14, 0.03, 0.84])
tbar = plt.colorbar(ts, location = "right", cax=tax)
tbar.set_label(r'c$\tau$ [m]', labelpad=2, rotation=90, fontsize=25)
tbar.ax.tick_params(labelsize=20)

tbar.ax.yaxis.set_ticks_position('right')
tbar.ax.yaxis.set_label_position('left')

# levels=[1e-1, 1, 1e2, 1e3]
# cs = plt.contourf(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm())
# cax = plt.axes([1.08, 0.14, 0.03, 0.84])

# cbar = plt.colorbar(cs, location = "right", cax=cax)
# cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
# cbar.ax.tick_params(labelsize=16)


plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/lzpln_ct.pdf", bbox_inches='tight')
plt.show()
    
#%%

# gs = np.logspace(-8, 1, 100)
# th = 1e-6
# mzp = 100
# xH = 0
# mN1, mN2, mN3 = 1/4, 1000, 1000
# name = "U1_X"
# modname="U(1)_X"
# masses = np.logspace(-3,1,1000)

# ctaus = []
# modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp)
# for g in gs:
#     ct = []
#     for m in masses:
#         ct.append(modelD.ctau(m, 0, th=th, g=g))
#     ctaus.append(ct)
    

# ctau = np.array(ctaus)

    
# hmv, hgv = np.meshgrid(masses, gs)
# plt.rcParams["figure.figsize"] = (8, 6)
# plt.xscale("log")
# plt.yscale("log")
# plt.xlim([1e-3, 1])
# plt.ylim([1e-6,1])
# plt.xlabel(r"$m_{h_2}$[GeV]", fontsize=18)
# plt.ylabel(r"$g_{BL}$", fontsize=18)
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# # plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{Z^\prime}=$" + str(mzp) + "GeV,  $\sin\eta$=" + str(th) , y=0.2, x=0.72, fontsize=20)
# plt.tight_layout()


# # plt.text(5e-2,5e-8, "FASER2", fontsize=20)

# ts = plt.pcolormesh(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm(vmin=1e-6, vmax=1e4))

# my_levels = [480, 620, 1500, 1900]
# my_colors = ['red', 'blue', 'brown', 'purple']

# cs = plt.contour(hmv, hgv, ctau, 
#                   levels=my_levels, 
#                   colors=my_colors, 
#                   linewidths=2)

# tax = plt.axes([1, 0.14, 0.03, 0.84])
# tbar = plt.colorbar(ts, location = "right", cax=tax)
# tbar.set_label(r'c$\tau$ [m]', labelpad=2, rotation=90, fontsize=18)
# tbar.ax.tick_params(labelsize=16)

# tbar.ax.yaxis.set_ticks_position('right')
# tbar.ax.yaxis.set_label_position('left')

# # levels=[1e-1, 1, 1e2, 1e3]
# # cs = plt.contourf(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm())
# # cax = plt.axes([1.08, 0.14, 0.03, 0.84])

# # cbar = plt.colorbar(cs, location = "right", cax=cax)
# # cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
# # cbar.ax.tick_params(labelsize=16)


# # plt.savefig("/home/souvik/Downloads/U1X_"+str(xH)+".jpeg", bbox_inches='tight', dpi=300)
# plt.show()

       
    
    
# #%%
# gs = np.logspace(-10, 1, 100)
# th = 1e-9

# mzp = 1/4

# xH = 0
# mN1, mN2, mN3 = 1000, 1000, 1000
# name = "U1_X"
# modname="U(1)_X"
# masses = np.logspace(-3,1,1000)

# ctaus = []
# modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=True, cZ=False, mZ=mzp)
# for g in gs:
#     ct = []
#     for m in masses:
#         ct.append(modelD.ctau(m, 0, th=th, g=g))
#     ctaus.append(ct)
    
# ctau = np.array(ctaus)

    
# hmv, hgv = np.meshgrid(masses, gs)
# plt.rcParams["figure.figsize"] = (8, 6)
# plt.xscale("log")
# plt.yscale("log")
# plt.xlim([1e-3, 1])
# plt.ylim([1e-10,1])
# plt.xlabel(r"$m_{h_2}$[GeV]", fontsize=18)
# plt.ylabel(r"$g_{BL}$", fontsize=18)
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# # plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{N}=$" + str(mN1/1000) + "TeV,  $\sin\eta$=" + str(th) , y=0.2, x=0.32, fontsize=20)
# plt.tight_layout()


# # plt.text(5e-2,5e-8, "FASER2", fontsize=20)

# ts = plt.pcolormesh(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm(vmin=1e-6, vmax=1e4))

# my_levels = [480, 620, 1500, 1900]
# my_colors = ['red', 'blue', 'brown', 'purple'] 

# cs = plt.contour(hmv, hgv, ctau, 
#                   levels=my_levels, 
#                   colors=my_colors, 
#                   linewidths=2)

# tax = plt.axes([1, 0.14, 0.03, 0.84])
# tbar = plt.colorbar(ts, location = "right", cax=tax)
# tbar.set_label(r'c$\tau$ [m]', labelpad=2, rotation=90, fontsize=18)
# tbar.ax.tick_params(labelsize=16)

# tbar.ax.yaxis.set_ticks_position('right')
# tbar.ax.yaxis.set_label_position('left')

# # levels=[1e-1, 1, 1e2, 1e3]
# # cs = plt.contourf(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm())
# # cax = plt.axes([1.08, 0.14, 0.03, 0.84])

# # cbar = plt.colorbar(cs, location = "right", cax=cax)
# # cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
# # cbar.ax.tick_params(labelsize=16)


# # plt.savefig("/home/souvik/Downloads/U1X_"+str(xH)+".jpeg", bbox_inches='tight', dpi=300)
# plt.show()
    
    
    
# #%%

# gs = np.logspace(-10, 1, 100)
# th = 1e-9

# mzp = 0.15

# xH = 0
# mN1, mN2, mN3 = 1/4, 1000, 1000
# name = "U1_X"
# modname="U(1)_X"
# masses = np.logspace(-3,1,1000)

# ctaus = []
# modelD = darkcast.Model("U1_X", Y1 = mN1, Y2 = mN2, Y3 = mN3, cN=False, cZ=True, mZ=mzp)
# for g in gs:
#     ct = []
#     for m in masses:
#         ct.append(modelD.ctau(m, 0, th=th, g=g))
#     ctaus.append(ct)
    

# ctau = np.array(ctaus)

    
# hmv, hgv = np.meshgrid(masses, gs)
# plt.rcParams["figure.figsize"] = (8, 6)
# plt.xscale("log")
# plt.yscale("log")
# plt.xlim([1e-3, 1])
# plt.ylim([1e-10,1])
# plt.xlabel(r"$m_{h_2}$[GeV]", fontsize=18)
# plt.ylabel(r"$g_{BL}$", fontsize=18)
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# # plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
# plt.title(r"$m_{Z^\prime}=$" + str(mzp*1000) + "MeV,  $\sin\eta$=" + str(th) , y=0.3, x=0.7, fontsize=20)
# plt.tight_layout()


# # plt.text(5e-2,5e-8, "FASER2", fontsize=20)

# ts = plt.pcolormesh(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm(vmin=1e-6, vmax=1e4))

# my_levels = [480, 620, 1500, 1900]
# my_colors = ['red', 'blue', 'brown', 'purple'] 

# cs = plt.contour(hmv, hgv, ctau, 
#                   levels=my_levels, 
#                   colors=my_colors)

# tax = plt.axes([1, 0.14, 0.03, 0.84])
# tbar = plt.colorbar(ts, location = "right", cax=tax)
# tbar.set_label(r'c$\tau$ [m]', labelpad=2, rotation=90, fontsize=18)
# tbar.ax.tick_params(labelsize=16)

# tbar.ax.yaxis.set_ticks_position('right')
# tbar.ax.yaxis.set_label_position('left')

# # levels=[1e-1, 1, 1e2, 1e3]
# # cs = plt.contourf(hmv, hgv, ctau, cmap="viridis", norm=matplotlib.colors.LogNorm())
# # cax = plt.axes([1.08, 0.14, 0.03, 0.84])

# # cbar = plt.colorbar(cs, location = "right", cax=cax)
# # cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
# # cbar.ax.tick_params(labelsize=16)


# # plt.savefig("/home/souvik/Downloads/U1X_"+str(xH)+".jpeg", bbox_inches='tight', dpi=300)
# plt.show()
    
        