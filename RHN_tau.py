#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 12:06:10 2024

@author: souvik
"""

import sys
src_path = "/home/souvik/codes/FORESEE-main"
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

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "/home/souvik/codes/darkcast_chiral/"))
import RHN_decay as ndec
import darkcast




#%%

mass = np.logspace(np.log10(0.1), np.log10(10), 10000)
name = "U1_X"
states = ndec.states_all("e")
taus_e = []
for m in mass:
    tau = 0
    for state in ndec.states_all("e"):
        tau += ndec.Nwidth(m, 0, state, 1, 1)*ndec.factor(state)
    tau = 1/tau
    tau *= 1.97e-13
    taus_e.append(tau)
taus_e = np.array(taus_e)

mass = np.logspace(np.log10(0.1), np.log10(10), 10000)
name = "U1_X"
states = ndec.states_all("e")
taus_mu = []
for m in mass:
    tau = 0
    for state in ndec.states_all("mu"):
        tau += ndec.Nwidth(m, 0, state, 1, 1)*ndec.factor(state)
    tau = 1/tau
    tau *= 1.97e-13
    taus_mu.append(tau)
taus_mu = np.array(taus_mu)

#%%
def exp(x, a):
    return [a for i in x]


plt.rcParams["figure.figsize"] = (8,6)
fig, ax = plt.subplots()
ax.loglog()
plt.xlim(0.1, 10)
plt.ylim(0.1, 1e5)
ax.set_xticks([0.1, 0.5, 1, 5, 10], labels=["0.1", "0.5", "1", "5", "10"])
ax.set_yticks([0.1, 1, 10, 100, 1000, 10000, 100000], labels=["0.1", "1", "10", r"$10^2$", r"$10^3$", r"$10^4$", r"$10^5$"])
plt.xlabel(r"$M_{N_1}$[GeV]", fontsize=15)
plt.ylabel(r"$c\tau[m]$", fontsize=15)
plt.plot(mass, taus_e/1e-6/1000, color="violet", label=r"$|V_{e N}|^2 = 10^{-6}$")
plt.plot(mass, taus_e/1e-7/1000, color="maroon", label=r"$|V_{e N}|^2 = 10^{-7}$")
plt.plot(mass, exp(mass, 625), "--y", label="FASER(2) cavern: L = 625 m")
plt.plot(mass, exp(mass, 131), "--r", label="ILC-BD: L = 131 m")
plt.plot(mass, exp(mass, 480), "--b", label="FASER(2): L = 480 m")
plt.plot(mass, exp(mass, 579), "--g", label="DUNE: L = 579 m")
plt.legend(loc = "lower left", fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig("/home/souvik/codes/FORESEE_fig/decay length/DL_e.pdf")

plt.show()

plt.rcParams["figure.figsize"] = (8,6)
fig, ax = plt.subplots()
ax.loglog()
plt.xlim(0.1, 10)
plt.ylim(0.1, 1e5)
ax.set_xticks([0.1, 0.5, 1, 5, 10], labels=["0.1", "0.5", "1", "5", "10"])
ax.set_yticks([0.1, 1, 10, 100, 1000, 10000, 100000], labels=["0.1", "1", "10", r"$10^2$", r"$10^3$", r"$10^4$", r"$10^5$"])
plt.xlabel(r"$M_{N_2}$[GeV]", fontsize=20)
plt.ylabel(r"$c\tau[m]$", fontsize=20)
plt.plot(mass, taus_mu/1e-6/1000, color="violet", label=r"$|V_{\mu N}|^2 = 10^{-6}$")
plt.plot(mass, taus_mu/1e-7/1000, color="maroon",  label=r"$|V_{\mu N}|^2 = 10^{-7}$")
plt.plot(mass, exp(mass, 625), "--y", label="FASER(2) cavern: L = 625 m")
plt.plot(mass, exp(mass, 131), "--r", label="ILC-BD: L = 131 m")
plt.plot(mass, exp(mass, 480), "--b", label="FASER(2): L = 480 m")
plt.plot(mass, exp(mass, 579), "--g", label="DUNE: L = 579 m")
plt.legend(loc = "lower left", fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig("/home/souvik/codes/FORESEE_fig/decay length/DL_mu.pdf")

plt.show()

#%%

plt
plt.loglog()
plt.xlim(0.1, 10)
plt.ylim(1e-12, 1)
plt.xlabel(r"$M_{N_1}$[GeV]", fontsize=15)
plt.ylabel(r"$|U_{e N}|^2$", fontsize=15)
plt.plot(mass, (taus_e/1000)/125, color="violet", label="L = 125 m")
plt.plot(mass, (taus_e/1000)/477, color="maroon",  label="L = 477 m")
plt.plot(mass, (taus_e/1000)/577, color="cyan",  label="L = 577 m")
plt.plot(mass, (taus_e/1000)/620, color="purple",  label="L = 620 m")
# plt.plot(mass, exp(mass, 131), "--r", label=r"$ILC Beam Dump: L=131 m$")
# plt.plot(mass, exp(mass, 480), "--b", label=r"$FASER(2): L=480 m$")
# plt.plot(mass, exp(mass, 579), "--g", label=r"$DUNE: L=579 m$")
plt.legend(loc = "lower left", fontsize=12)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()

plt.loglog()
plt.xlim(0.1, 10)
plt.ylim(1e-12, 1)
plt.xlabel(r"$M_{N_2}$[GeV]", fontsize=15)
plt.ylabel(r"$|U_{\mu N}|^2$", fontsize=15)
plt.plot(mass, (taus_mu/1000)/125, color="violet", label="L = 125 m")
plt.plot(mass, (taus_mu/1000)/477, color="maroon",  label="L = 477 m")
plt.plot(mass, (taus_mu/1000)/577, color="cyan",  label="L = 577 m")
plt.plot(mass, (taus_mu/1000)/620, color="purple",  label="L = 620 m")
# plt.plot(mass, exp(mass, 131), "--r", label=r"$ILC Beam Dump: L=131 m$")
# plt.plot(mass, exp(mass, 480), "--b", label=r"$FASER(2): L=480 m$")
# plt.plot(mass, exp(mass, 579), "--g", label=r"$DUNE: L=579 m$")
plt.legend(loc = "lower left", fontsize=12)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()

#%%

f = open("/home/souvik/codes/FORESEE_fig/decay length/DL_e.txt", "w")
for i in range(len(mass)):
        f.write(str(mass[i])+"   "+str(taus_e[i]/1000)+"\n")
f.close()

f = open("/home/souvik/codes/FORESEE_fig/decay length/DL_mu.txt", "w")
for i in range(len(mass)):
        f.write(str(mass[i])+"   "+str(taus_mu[i]/1000)+"\n")
f.close()

#%%

model = darkcast.Model("U1_X", m1 = 1/3, m2= 1/3, m3= 1/3)

def exp(x, a):
    return [a for i in x]

xHs=[-2, -1, -0.5, 0, 0.5, 1, 2]
names = ["2n", "1n", "05n", "0", "05p", "1p", "2p"]
ctaus = []

mass = np.logspace(np.log10(0.001), np.log10(10), 10000)

for i, xH in enumerate(xHs):
    ctaux=[]
    for m in mass:
        ctaux.append(model.tau(m, xH, g = 1.0)*2.99e8)
    ctaux=np.array(ctaux)
    plt.rcParams["figure.figsize"] = (12,6)
    fig, ax = plt.subplots()
    plt.loglog()
    plt.xlim(0.001, 10)
    plt.ylim(1e-14, 1e6)
    plt.xlabel(r"$M_{Z^\prime}$[GeV]", fontsize=20)
    plt.ylabel(r"$c\tau[m]$", fontsize=20)
    # plt.plot(mass, ctaux/1e-8, color="violet", label=r"$|U_{e N}|^2 = 10^{-4}$")
    plt.plot(mass, ctaux/1e-10, color="purple", label=r"$g_X = 10^{-5}$")
    plt.plot(mass, ctaux/1e-14, color="cyan", label=r"$g_X = 10^{-7}$")
    plt.plot(mass, ctaux/1e-16, color="maroon", label=r"$g_X = 10^{-8}$")
    plt.plot(mass, exp(mass, 131), "--r", label="ILC-BD: L = 131 m")
    plt.plot(mass, exp(mass, 480), "--b", label="FASER(2): L = 480 m")
    plt.plot(mass, exp(mass, 579), "--g", label="DUNE: L = 579 m")
    plt.plot(mass, exp(mass, 625), "--y", label="FASER(2) cavern: L = 625 m")
    title=r"$x_\Phi=1$, $x_H=$"+str(xH)
    plt.legend(loc = "best", fontsize=14, ncol=3)
    ax.set_xticks([0.001, 0.01, 0.1, 1, 10], labels=["0.001", "0.01", "0.1", "1", "10"], fontsize=21)
    ax.set_yticks([1e-12, 1e-8, 1e-4, 1, 1e4, 1e6], labels=[r"$10^{-12}$", r"$10^{-8}$", r"$10^{-4}$", r"$1$", r"$10^4$", r"$10^6$"], fontsize=21)
    plt.text(0.3,1e4, title, fontsize=20)
    plt.savefig("/home/souvik/codes/FORESEE_fig/decay length/DL_"+names[i]+".pdf")
    plt.show()
    
#%%


xHs = [-2, -1.2, 0, 2]
mN1, mN2, mN3 = 1/3, 1/3, 1000
name = "U1_X"
modname="U(1)_X"
modelD = darkcast.Model(name, mN1, mN2, mN3)
masses = np.logspace(-3,1,1000)
gXs = np.logspace(-10, -3, 1000)

ctaus = {}
for xH in xHs:
    ctau = []
    for m in masses:
        ct = []
        for gX in gXs:
            ct.append(modelD.ctau(m, xH, g=gX))
        ctau.append(ct)
    ctaus[xH] = ctau
    
#%%

print(modelD.ctau(10, -2, g=5e-10))

#%%
from matplotlib import cm, ticker
import matplotlib
from mpl_toolkits.axes_grid1.inset_locator import inset_axes



cts = []

for xH in xHs:
       
    ctau = ctaus[xH]
    ctau = np.array(ctau).T
    
    mvs = []
    gvs = []
    ctvs = []
    
    hmv, hgv = np.meshgrid(masses, gXs)
    plt.rcParams["figure.figsize"] = (8, 6)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$M_{Z'}$[GeV]", fontsize=18)
    plt.ylabel(r"$g_X$", fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
    plt.title(r"$"+modname+": x_H=$"+str(xH), y=0.01, x=0.22, fontsize=20)
    plt.tight_layout()
    
    plt.contour(hmv, hgv, ctau, levels=[np.log(620)])
    
    plt.text(5e-2,5e-8, "FASER2", fontsize=20)
        
    levels=[1e-9, 1e-8, 1e-7, 1e-6]
    ts = plt.pcolormesh(hmv, hgv, ctau/3e8, cmap="cool", norm=matplotlib.colors.LogNorm(vmin=1e-9, vmax=1e-6))
    tax = plt.axes([1.08, 0.14, 0.03, 0.84])
    
    tbar = plt.colorbar(ts, location = "right", cax=tax)
    tbar.set_label(r'$\tau$ [s]', labelpad=-18, rotation=90, fontsize=18)
    tbar.ax.tick_params(labelsize=16)
    
    tbar.ax.yaxis.set_ticks_position('left')
    tbar.ax.yaxis.set_label_position('left')
    
    levels=[1e-1, 1, 1e2, 1e3]
    cs = plt.pcolormesh(hmv, hgv, ctau, cmap="cool", norm=matplotlib.colors.LogNorm(vmin=1e-1, vmax=1e3))
    cax = plt.axes([1.08, 0.14, 0.03, 0.84])
    
    cbar = plt.colorbar(cs, location = "right", cax=cax)
    cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
    cbar.ax.tick_params(labelsize=16)
    
    
    # plt.savefig("/home/souvik/Downloads/U1X_"+str(xH)+".jpeg", bbox_inches='tight', dpi=300)
    plt.show()
    
#%%

path = "/home/souvik/codes/foresee-main/Models/U1_llzplln_faser/model/"

xHs = [-2, -1.2, 0, 2]
mN1, mN2, mN3 = 1/3, 1/3, 1000
name = "U1_X_phi4"
modname = "alternative"
modelD = darkcast.Model(name, mN1, mN2, mN3)
masses = np.logspace(-3,1,1000)
gXs = np.logspace(-10, -3, 1000)

ctaus = {}
for xH in xHs:
    ctau = []
    for m in masses:
        ct = []
        for gX in gXs:
            ct.append(modelD.ctau(m, xH, g=gX))
        ctau.append(ct)
    ctaus[xH] = ctau
    
#%%

print(modelD.ctau(10, -2, g=5e-10))

#%%
from matplotlib import cm, ticker
import matplotlib
from mpl_toolkits.axes_grid1.inset_locator import inset_axes



cts = []

for xH in xHs:
       
    ctau = ctaus[xH]
    ctau = np.array(ctau).T
    
    mvs = []
    gvs = []
    ctvs = []
    
    hmv, hgv = np.meshgrid(masses, gXs)
    plt.rcParams["figure.figsize"] = (8, 6)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$M_{Z'}$[GeV]", fontsize=18)
    plt.ylabel(r"$g_X$", fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
    plt.title(r"$"+modname+": x_H=$"+str(xH), y=0.01, x=0.22, fontsize=20)
    plt.tight_layout()
    
    plt.contour(hmv, hgv, ctau, levels=[np.log(620)])
    
    plt.text(5e-2,5e-8, "FASER2", fontsize=20)
        
    levels=[1e-9, 1e-8, 1e-7, 1e-6]
    ts = plt.pcolormesh(hmv, hgv, ctau/3e8, cmap="cool", norm=matplotlib.colors.LogNorm(vmin=1e-9, vmax=1e-6))
    tax = plt.axes([1.08, 0.14, 0.03, 0.84])
    
    tbar = plt.colorbar(ts, location = "right", cax=tax)
    tbar.set_label(r'$\tau$ [s]', labelpad=-18, rotation=90, fontsize=18)
    tbar.ax.tick_params(labelsize=16)
    
    tbar.ax.yaxis.set_ticks_position('left')
    tbar.ax.yaxis.set_label_position('left')
    
    levels=[1e-1, 1, 1e2, 1e3]
    cs = plt.pcolormesh(hmv, hgv, ctau, cmap="cool", norm=matplotlib.colors.LogNorm(vmin=1e-1, vmax=1e3))
    cax = plt.axes([1.08, 0.14, 0.03, 0.84])
    
    cbar = plt.colorbar(cs, location = "right", cax=cax)
    cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
    cbar.ax.tick_params(labelsize=16)
    
    
    # plt.savefig("/home/souvik/Downloads/454_"+str(xH)+".jpeg", bbox_inches='tight', dpi=300)
    plt.show()

#%%   

ns = [1,2,3]

masses = np.logspace(-2,1,1000)
Us = np.logspace(-10, -2, 1000)

ctaus = {}
for n in ns:
    modelN = ndec.Calculate(n)
    ctau = []
    for m in masses:
        ct = []
        for U in Us:
            ct.append(modelN.Nctau(m, U=np.sqrt(U)))
        ctau.append(ct)
    ctaus[n] = ctau
    
#%%

modelN = ndec.Calculate(3)
print(modelN.Nctau(m=10, U=np.sqrt(np.logspace(-10, -2, 100))))  

#%%

from matplotlib import cm, ticker
import matplotlib
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

xlabel = { 1: r"m_{N_1}",
          2: r"m_{N_2}",
          3: r"m_{N_3}"}

ylabel = { 1: r"|V_{eN_1}|^2",
          2: r"|V_{\mu N_1}|^2",
          3: r"|V_{\tau N_1}|^2"}


for n in ns:
       
    ctau = ctaus[n]
    ctau = np.array(ctau)
    
    mvs = []
    Uvs = []
    ctvs = []
    
    hmv, hUv = np.meshgrid(masses, Us)
    plt.rcParams["figure.figsize"] = (8, 6)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(ylabel[n], fontsize=18)
    plt.ylabel(r"$|V_{N\ell_"+str(n)+"}|^2$", fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.text(2e-3, 2e-10, r"$x_H=$"+str(xH), fontsize=20)
    # plt.title(r"$N_"+str(n)+"\to X$", y=0.01, x=0.22, fontsize=20)
    plt.tight_layout()
    
    plt.contour(hmv, hUv, ctau, levels=[np.log(620)])
    
    plt.text(1.4,1e-4, "FASER2", fontsize=20)
        
    levels=[1e-9, 1e-8, 1e-7, 1e-6]
    ts = plt.pcolormesh(hmv, hUv, ctau/3e8, cmap="cool", norm=matplotlib.colors.LogNorm(vmin=1e-9, vmax=1e-5))
    tax = plt.axes([1.12, 0.14, 0.03, 0.84])
    
    tbar = plt.colorbar(ts, location = "right", cax=tax)
    tbar.set_label(r'$\tau$ [s]', labelpad=2, rotation=90, fontsize=18)
    tbar.ax.tick_params(labelsize=16)
    
    tbar.ax.yaxis.set_ticks_position('left')
    tbar.ax.yaxis.set_label_position('left')
    
    levels=[1e-1, 1, 1e2, 1e3]
    cs = plt.pcolormesh(hmv, hUv, ctau, cmap="cool", norm=matplotlib.colors.LogNorm(vmin=1e-1, vmax=1e3))
    cax = plt.axes([1.12, 0.14, 0.03, 0.84])
    
    cbar = plt.colorbar(cs, location = "right", cax=cax)
    cbar.set_label(r'$c\tau$ [m]', labelpad=1, rotation=90, fontsize=18)
    cbar.ax.tick_params(labelsize=16)
    
    
    plt.savefig("/home/souvik/Downloads/N_"+str(n)+".jpeg", bbox_inches='tight', dpi=300)
    plt.show()
#%%

distance, length = 620, 10

xHs = [-2, -1.2, 0, 2]

gX = 1e-7

probs = {}
for xH in xHs:
    probs[xH] = []
masses = np.logspace(-3,1,1000)
gXs = np.logspace(-10, -3, 1000)

name = "U1_X"
mN1, mN2, mN3 = 1000, 1000, 1000
modelD = darkcast.Model(name, mN1, mN2, mN3)
for xH in xHs:
    prob = []
    for m in masses:
        dbar = modelD.ctau(m, xH, g=gX)*500/m
        prob_decay = np.exp(-(distance)/dbar)-np.exp(-(distance+length)/dbar)
        prob.append(prob_decay)
    probs[xH].append(prob)

name = "U1_X"
mN1, mN2, mN3 = 1/3, 1/3, 1000
modelD = darkcast.Model(name, mN1, mN2, mN3)
for xH in xHs:
    prob = []
    for m in masses:
        dbar = modelD.ctau(m, xH, g=gX)*500/m
        prob_decay = np.exp(-(distance)/dbar)-np.exp(-(distance+length)/dbar)
        prob.append(prob_decay)
    probs[xH].append(prob)
    
name = "U1_X_phi4"
mN1, mN2, mN3 = 1/3, 1/3, 1000
modelD = darkcast.Model(name, mN1, mN2, mN3)
for xH in xHs:
    prob = []
    for m in masses:
        dbar = modelD.ctau(m, xH, g=gX)*500/m
        prob_decay = np.exp(-(distance)/dbar)-np.exp(-(distance+length)/dbar)
        prob.append(prob_decay)
    probs[xH].append(prob)
    
#%%

for xH in xHs:
    plt.plot(masses, probs[xH][0], label ="Heavy RHN", linestyle="dashed")
    plt.plot(masses, probs[xH][1], label = r"$U(1)_X$")
    plt.plot(masses, probs[xH][2], label = "alternative")
    plt.title(r"$g_X = $"+str(float(gX))+", $x_H = $"+str(xH))
    plt.xscale("log")
    plt.yscale("log")
    plt.ylim(1e-9, 1)
    plt.xlim(1e-3, 10)
    plt.legend()
    plt.savefig("/home/souvik/codes/FORESEE_fig/gX="+str(gX)+"_xH="+str(xH)+".png", bbox_inches='tight', dpi=300)
    plt.show()
    
#%%

ts, ps, ws = np.load("/home/souvik/codes/foresee-main/Models/U1_llzplln_faser/model/LLP_spectra/14TeV_221_m_0.11497569953977368.npy")
moms = [ps[i] for i in range(len(ps)) if ws[i]!=0]
print(max(moms))

#%%

distance, length = 620, 10

xHs = [-2, -1.2, 0, 2]


probs = {}
for xH in xHs:
    probs[xH] = []
masses = np.logspace(-3,1,1000)
gXs = np.logspace(-10, -3, 1000)

m = 0.02


name = "U1_X"
mN1, mN2, mN3 = 1000, 1000, 1000
modelD = darkcast.Model(name, mN1, mN2, mN3)
for xH in xHs:
    prob = []
    for g in gXs:
        dbar = modelD.ctau(m, xH, g=g)*500/m
        prob_decay = np.exp(-(distance)/dbar)-np.exp(-(distance+length)/dbar)
        prob.append(prob_decay*modelD.bfrac("visible", m, xH))
    probs[xH].append(prob)

name = "U1_X"
mN1, mN2, mN3 = 1/3, 1/3, 1000
modelD = darkcast.Model(name, mN1, mN2, mN3)
for xH in xHs:
    prob = []
    for g in gXs:
        dbar = modelD.ctau(m, xH, g=g)*500/m
        prob_decay = np.exp(-(distance)/dbar)-np.exp(-(distance+length)/dbar)
        prob.append(prob_decay*modelD.bfrac("visible", m, xH))
    probs[xH].append(prob)
    
name = "U1_X_phi4"
mN1, mN2, mN3 = 1/3, 1/3, 1000
modelD = darkcast.Model(name, mN1, mN2, mN3)
for xH in xHs:
    prob = []
    for g in gXs:
        dbar = modelD.ctau(m, xH, g=g)*500/m
        prob_decay = np.exp(-(distance)/dbar)-np.exp(-(distance+length)/dbar)
        prob.append(prob_decay*modelD.bfrac("visible", m, xH))
    probs[xH].append(prob)
    
#%%

for xH in xHs:
    plt.plot(gXs, probs[xH][0], label ="Heavy RHN", linestyle="dashed")
    plt.plot(gXs, probs[xH][1], label = r"$U(1)_X$")
    plt.plot(gXs, probs[xH][2], label = "alternative")
    plt.title(r"$x_H = $"+str(xH)+", mass = "+str(m)+" GeV")
    plt.xscale("log")
    plt.yscale("log")
    plt.ylim(1e-9, 1)
    plt.xlim(1e-10, 1e-3)
    plt.legend()
    plt.savefig("/home/souvik/codes/FORESEE_fig/mass="+str(m)+"GeV_xH="+str(xH)+".png", bbox_inches='tight', dpi=300)
    plt.show()