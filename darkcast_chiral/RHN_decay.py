#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:30:46 2024

@author: daslinux
"""

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import sys, os, inspect, itertools, numpy



all_states_e = [
        "e_pi", "nue_pi0", "nue_eta", "e_rho", "nue_rho0", "nue_omega",
        "nue_K0", "nue_Ks0", "e_K", "e_Ks",
        "nu_nu_nu", 
        "nue_e_e", "nue_mu_mu", "nue_tau_tau", 
        "numu_e_mu", "nutau_e_tau", 
        "nue_u_u", "nue_d_d", "nue_c_c", "nue_s_s",
        "e_u_d", "e_u_s", "e_c_d", "e_c_s"
        ]

vis_e = ["e_pi", "nue_pi0", "nue_eta", "e_rho", "nue_rho0", "nue_omega",
                      "nue_K0", "nue_Ks0", "e_K", "e_Ks", 
                      "nue_u_u", "nue_d_d", "nue_c_c", "nue_s_s",
                      "e_u_d", "e_u_s", "e_c_d", "e_c_s", 
                      "nue_e_e", "nue_mu_mu", "nue_tau_tau", "numu_e_mu", "nutau_e_tau"]

statesN_e = {
                  "Semileptons":          ["e_pi", "nue_pi0", "nue_eta", "e_rho", "nue_rho0", "nue_omega",
                                        "nue_K0", "nue_Ks0", "e_K", "e_Ks", 
                                        "nue_u_u", "nue_d_d", "nue_c_c", "nue_s_s",
                                        "e_u_d", "e_u_s", "e_c_d", "e_c_s"
                                        ],
                        r"$\nu_e\sum\nu_i\nu_i$":          ["nu_nu_nu"],
                        "Leptons":      ["nue_e_e", "nue_mu_mu", "nue_tau_tau", "numu_e_mu", "nutau_e_tau"],
                        
                        "Visible": ["e_pi", "nue_pi0", "nue_eta", "e_rho", "nue_rho0", "nue_omega",
                                              "nue_K0", "nue_Ks0", "e_K", "e_Ks", 
                                              "nue_u_u", "nue_d_d", "nue_c_c", "nue_s_s",
                                              "e_u_d", "e_u_s", "e_c_d", "e_c_s", 
                                              "nue_e_e", "nue_mu_mu", "nue_tau_tau", "numu_e_mu", "nutau_e_tau"]
            }



all_states_mu = [ 
        "mu_pi", "numu_pi0", "numu_eta", "mu_rho", "numu_rho0", "numu_omega",
        "numu_K0", "numu_Ks0", "mu_K", "mu_Ks",
        "nu_nu_nu", 
        "numu_e_e", "numu_mu_mu", "numu_tau_tau",
        "nutau_mu_tau", "nue_mu_e",
        "numu_u_u", "numu_d_d", "numu_c_c", "numu_s_s",
        "mu_u_d", "mu_u_s", "mu_c_d", "mu_c_s"
        ]

vis_mu = [ 
        "mu_pi", "numu_pi0", "numu_eta", "mu_rho", "numu_rho0", "numu_omega",
        "numu_K0", "numu_Ks0", "mu_K", "mu_Ks",
        # "nu_nu_nu", 
        "numu_e_e", "numu_mu_mu", "numu_tau_tau",
        "nutau_mu_tau", "nue_mu_e",
        "numu_u_u", "numu_d_d", "numu_c_c", "numu_s_s",
        "mu_u_d", "mu_u_s", "mu_c_d", "mu_c_s"
        ]

statesN_mu = {
                  "Semileptons":          ["mu_pi", "numu_pi0", "numu_eta", "mu_rho", "numu_rho0", "numu_omega",
                                        "numu_K0", "numu_Ks0", "mu_K", "mu_Ks",
                                        "numu_u_u", "numu_d_d", "numu_c_c", "numu_s_s",
                                        "mu_u_d", "mu_u_s", "mu_c_d", "mu_c_s"
                                          ],
           r"$\nu_\mu\sum\nu_i\nu_i$":          ["nu_nu_nu"],
           
           "Leptons":   ["numu_mu_mu", "numu_tau_tau", "numu_e_e", "nue_mu_e", "nutau_mu_tau"],
           "Visible":   ["mu_pi", "numu_pi0", "numu_eta", "mu_rho", "numu_rho0", "numu_omega",
                                 "numu_K0", "numu_Ks0", "mu_K", "mu_Ks",
                                 "numu_u_u", "numu_d_d", "numu_c_c", "numu_s_s",
                                 "mu_u_d", "mu_u_s", "mu_c_d", "mu_c_s", 
                                 "numu_mu_mu", "numu_tau_tau", "numu_e_e", "nue_mu_e", "nutau_mu_tau"]
          
         #            r"$\nu_\mu\mu\mu$":          ["numu_mu_mu"],
         # r"$\nu_\mu\tau\tau$ + $\nu_\mu ee$":          ["numu_tau_tau", "numu_e_e"],
         #                r"$\mu e\nu_e$ + $\mu\tau\nu_\tau$":          ["nue_mu_e", "nutau_mu_tau"]
            }



all_states_tau = [
        "tau_pi", "nutau_pi0", "nutau_eta", "tau_rho", "nutau_rho0", "nutau_omega",
        "nutau_K0", "nutau_Ks0", "tau_K", "tau_Ks", 
        "nu_nu_nu", 
        "nutau_e_e", "nutau_mu_mu", "nutau_tau_tau",
        "nue_tau_e", "numu_tau_mu", 
        "nutau_u_u", "nutau_d_d", "nutau_c_c", "nutau_s_s",
        "tau_u_d", "tau_u_s", "tau_c_d", "tau_c_s"
        ]

vis_tau = [
        "tau_pi", "nutau_pi0", "nutau_eta", "tau_rho", "nutau_rho0", "nutau_omega",
        "nutau_K0", "nutau_Ks0", "tau_K", "tau_Ks", 
        # "nu_nu_nu", 
        "nutau_e_e", "nutau_mu_mu", "nutau_tau_tau",
        "nue_tau_e", "numu_tau_mu", 
        "nutau_u_u", "nutau_d_d", "nutau_c_c", "nutau_s_s",
        "tau_u_d", "tau_u_s", "tau_c_d", "tau_c_s"
        ]

statesN_tau = {
                  "Semileptons":          ["tau_pi", "nutau_pi0", "nutau_eta", "tau_rho", "nutau_rho0", "nutau_omega", 
                                        "nutau_K0", "nutau_Ks0", "tau_K", "tau_Ks", 
                                        "nutau_u_u", "nutau_d_d", "nutau_c_c", "nutau_s_s",
                                        "tau_u_d", "tau_u_s", "tau_c_d", "tau_c_s"],
                r"$\nu_\tau\sum\nu_i\nu_i$":          ["nu_nu_nu"],
                
                "Leptons":   ["nutau_tau_tau", "nutau_e_e", "nutau_mu_mu", "numu_tau_mu", "nue_tau_e"],
                "Visible":   ["tau_pi", "nutau_pi0", "nutau_eta", "tau_rho", "nutau_rho0", "nutau_omega", 
                                      "nutau_K0", "nutau_Ks0", "tau_K", "tau_Ks", 
                                      "nutau_u_u", "nutau_d_d", "nutau_c_c", "nutau_s_s",
                                      "tau_u_d", "tau_u_s", "tau_c_d", "tau_c_s", "nutau_tau_tau", "nutau_e_e", "nutau_mu_mu", "numu_tau_mu", "nue_tau_e"]
                
              # r"$\nu_\tau\tau\tau$":          ["nutau_tau_tau"],
              #         r"$\nu_\tau$ee + $\nu_\tau\mu\mu$":          ["nutau_e_e", "nutau_mu_mu"],
              #       r"$\tau\mu\nu_\mu$ + $\tau e \nu_e$":         ["numu_tau_mu", "nue_tau_e"],
                    
          }



GF = 1.166e-5
hbar = 6.58211951e-25
mu0 = 0.9578
thetaw = 0.22305

def theta(x,y):
    if x>=y: return 1
    else: return 0

def states_decay(flavor):
    if flavor=="e": return statesN_e
    elif flavor=="mu": return statesN_mu
    elif flavor=="tau": return statesN_tau

def states_all(flavor):
    if flavor=="e": return all_states_e
    elif flavor=="mu": return all_states_mu
    elif flavor=="tau": return all_states_tau
    else: print("error")

# Fermion masses (GeV)
mfs = {
    "e":      0.51099895e-3, 
    "mu":     0.1056583755,
    "tau":    1.77693, 
    "d":      4.7e-3, 
    "u":      2.16e-3, 
    "s":      93.5e-3, 
    "c":      1.273, 
    "b":      4.183,
    "t":      172.56
    }

nus = {
       "nue":    0,
       "numu":   0,
       "nutau":  0,
       "nu":     0
       }


# Meson masses (GeV).
mps = {
    "pi":    0.1396,
    "pi0":   0.13498,
    "eta":   0.5478,
    "K":     0.4937,
    "K0":    0.4976,
    }

mvs = {
       "rho0":  0.776,
       "rho":   0.7758,
       "omega": 0.78259,
       "Ks":    0.89166,
       "Ks0":   0.8961,
       }

fps = {
    "pi":    0.1307,
    "pi0":   0.130,
    "eta":   0.1647,
    "K":     0.1598,
    "K0":    0.159,
    }

fvs = {
       "rho0":  0.22,
       "rho":   0.22,
       "omega": 0.195,
       "Ks":    0.217,
       "Ks0":   0.217,
       }

kps = {
       "pi0": -1/(2*np.sqrt(2)),
       "eta": -1/(2*np.sqrt(6)),
       "K0":   1/4
       }

kvs = {
       "rho0":  np.sqrt(1/2)*(1/2 - thetaw),
       "omega": -np.sqrt(1/2)*(thetaw/3),
       "Ks0":   1/2*(thetaw*(2/3) - 1/2)
       }

quarks = ["u", "d", "c", "s", "t", "b"]

def Vqq(x, y):
    if x=="u" and y=="d": return 0.974
    elif x=="u" and y=="s": return 0.217
    elif x=="u" and y=="b": return 0.004
    
    elif x=="c" and y=="d": return 0.221
    elif x=="c" and y=="s": return 0.975
    elif x=="c" and y=="b": return 0.041
    
    elif x=="t" and y=="d": return 0.009
    elif x=="t" and y=="s": return 0.042
    elif x=="t" and y=="b": return 1.041
    
Vs = {
      "pi": Vqq("u", "d"),
      "K":  Vqq("u", "s"),
      "rho": Vqq("u", "d"),
      "Ks":  Vqq("u", "s"),
      }

    
modes = []



def lN(f):
    if f in ["e", "nue"]: return 1
    if f in ["mu", "numu"]: return 2
    if f in ["tau", "nutau"]: return 3
    else: return 0

def mfi(particle):
    if particle in mfs.keys():
        return mfs[particle]
    elif particle in mps.keys():
        return mps[particle]
    elif particle in mvs.keys():
        return mvs[particle]
    elif particle in nus.keys():
        return nus[particle]
    elif particle == "nu":
        return 0

def delta(nu, l):
    if nu == "nue" and l == "e":
        return 1
    elif nu == "numu" and l == "mu":
        return 1
    elif nu == "nutau" and l == "tau":
        return 1
    else:
        return 0
    
  
    
def lamda(a, b, c):
    return np.sqrt(a**2 + b**2 + c**2 - 2*a*b - 2*b*c - 2*c*a)    

def FP(x, y):
    return lamda(1, x**2, y**2) * ((1 + x**2) * (1 + x**2 - y**2) - 4*(x**2))

def FV(x, y):
    return lamda(1, x**2, y**2) * ((1 - x**2)**2 + (1 + x**2) * (y**2) - 2*(y**4))

def I1(x, y, z):
    def IF1(s, x, y, z):
        i1 = (s - x**2 - y**2) * (1 + z**2 - s) 
        i2 = lamda(s, x**2, y**2) * lamda(1, s, z**2)
        return i1*i2/s
    return quad(IF1, (x + y)**2, (1 - z)**2, args = (x, y, z))[0]

def I2(x, y, z):
    def IF2(s, x, y, z):
        i1 = y * z * (1 + x**2 - s) 
        i2 = lamda(s, y**2, z**2) * lamda(1, s, x**2)
        return i1*i2/s
    return quad(IF2, (y + z)**2, (1 - x)**2, args = (x, y, z))[0]


class Calculate:

    def __init__(self, flavor):
        
        self.flavor = flavor
        
        self.all_states = [all_states_e, all_states_mu, all_states_tau][flavor-1] if flavor in [1,2,3] else None
        
        self.visible_states = [statesN_e, statesN_mu, statesN_tau][flavor-1]["Visible"] if flavor in [1,2,3] else None
        self.__cache = {}

    def Nwidth(self, mass, states, U=1, weight=True): 
        total = 0
        
        for state in states:
            
            cache = self.__cache.get(state)
            if cache and cache[0] == mass: total += cache[-1]; continue
         
            mode = state.split("_")
            nm = len(mode)
            
            thetaw = 0.2229
            gL, gR = -0.5 + thetaw, thetaw
            guL, guR = 0.5 - (2/3)*thetaw, -(2/3)*thetaw
            gdL, gdR = -0.5 + (1/3)*thetaw, (1/3)*thetaw
            cA = 3
            
            if nm == 3 and  (mass>= (mfi(mode[0]) + mfi(mode[1]) + mfi(mode[2]))):
                
                if lN(mode[1]) == lN(mode[2]) and lN(mode[0]) != lN(mode[1]) and lN(mode[-1])!=0:
                    xvl1, xl2 = mfi(mode[0])/mass, mfi(mode[1])/mass
                    dtr = mode[-1]
                    
                    w = ((GF**2)*(mass**5))/(8*(np.pi**3))*((gL**2+gR**2)*I1(xvl1,xl2,xl2)+2*gL*gR*I2(xvl1,xl2,xl2))
                    
                elif lN(mode[1]) != lN(mode[2]) and (lN(mode[0]) == lN(mode[1]) or lN(mode[0]) == lN(mode[2])) and lN(mode[-1])!=0:
                   if lN(mode[1]) == lN(mode[0]):  xvl1, xl1, xl2 = mfi(mode[0])/mass, mfi(mode[1])/mass, mfi(mode[2])/mass
                   else: xvl1, xl2, xl1 = mfi(mode[0])/mass, mfi(mode[1])/mass, mfi(mode[2])/mass
                    
                   w = ((GF**2)*(mass**5)/(16*(np.pi**3)))*I1(xvl1, xl1, xl2)
                   if weight: w = 2*w
                    
                elif lN(mode[0]) == lN(mode[1]) == lN(mode[2]) and mode[0] != mode[1] and lN(mode[-1])!=0:
                    xvl2, xl2 = mfi(mode[0])/mass, mfi(mode[1])/mass
                    w = ((GF**2)*(mass**5)/(8*(np.pi**3)))*(((gL+1)**2+gR**2)*I1(xvl2, xl2, xl2)+2*gR*(gL+1)*I2(xvl2, xl2, xl2))
                    
                elif mode[0] == mode[1] == mode[2] and mode[0]=="nu":
                    
                    w = ((GF**2)*(mass**5)/(96*(np.pi**3)))
                    
                elif lN(mode[1]) == lN(mode[2]) == 0 and mode[1] != mode[2] and mass>=mu0: 
                    xl, xq1, xq2 =  mfi(mode[0])/mass, mfi(mode[1])/mass, mfi(mode[2])/mass
                    
                    w = (Vqq(mode[1], mode[2])**2)*cA*((GF**2)*(mass**5)/(16*(np.pi**3)))*I1(xl,xq1,xq2)
                    if weight: w = 2*w
                    
                elif lN(mode[-1]) == lN(mode[-2]) == 0 and mode[1] == mode[2] and mass>=mu0:
                    xvl, xq =  mfi(mode[0])/mass, mfi(mode[1])/mass
                    if mode[-1] in ["u", "c", "t"]: gqL, gqR = guL, guR
                    elif mode[-1] in ["d", "s", "b"]: gqL, gqR = gdL, gdR
                    w = cA*((GF**2)*(mass**5)/(8*(np.pi**3)))*((gqL**2+gqR**2)*I1(xvl,xq,xq)+(2*gqL*gqR)*I2(xvl,xq,xq))
                
                # else: w=0
                    
            elif nm == 2 and  (mass >= (mfi(mode[0]) + mfi(mode[1]))) and mu0>mass:    
                
                if mode[0] in nus.keys() and mode[1] in mps:
                    xvl, xP = mfi(mode[0])/mass, mfi(mode[1])/mass
                    kp = kps[mode[1]]
                    
                    w = ((GF**2)*(mass**3)/(2*np.pi))*(fps[mode[1]]**2)*(kp**2)*FP(xvl,xP)
                                   
                elif mode[0] in mfs.keys() and mode[1] in mps:
                    VP = Vs[mode[1]]                        
                    xl1, xP = mfi(mode[0])/mass, mfi(mode[1])/mass
                    
                    w = ((GF**2)*(mass**3)/(16*np.pi))*(VP**2)*(fps[mode[1]]**2)*FP(xl1, xP)
                    if weight: w = 2*w
                    
                elif mode[0] in nus.keys() and mode[1] in mvs:
                    xvl, xV = mfi(mode[0])/mass, mfi(mode[1])/mass
                    kv = kvs[mode[1]]
                    
                    w = ((GF**2)*(mass**3)/(2*np.pi))*(fvs[mode[1]]**2)*(kv**2)*FV(xvl,xV)
                    
                elif mode[0] in mfs.keys() and mode[1] in mvs:
                    xl, xV = mfi(mode[0])/mass, mfi(mode[1])/mass
                    Vv = Vs[mode[1]]
                    
                    w = ((GF**2)*(mass**3)/(16*np.pi))*(Vv**2)*(fvs[mode[-1]]**2)*FV(xl, xV)
                    if weight: w = 2*w
                    
                # else: w=0
            else: 
                w = 0
                
            total += w
            self.__cache[state]=(mass, w)
                    
        return total*(U**2) 
    
    def Ntau(self, m, U = 1.0):
        return hbar/self.Nwidth(m, self.all_states, U=U)
    
    def Nctau(self, m,  U = 1.0):
        return 1.97e-16/self.Nwidth(m, self.all_states, U)
    
    def NBR(self, mass, states, weight=True): 
        
        den = self.Nwidth(mass, self.all_states, U=1)
        if den == 0: return 0.0
        
        num = self.Nwidth(mass, states, U=1, weight=weight)
        if num == 0: return 0.0
        elif num == None: return 1.0
             
        return num/den
    

#%%    
# mN = np.logspace(-3,1,10000)

# colors = ["red", "blue", "green", "purple", "orange"]
    
    
# calc1 = Calculate(1)

# plt.rcParams["figure.figsize"] = (8, 4)
# for key, color in zip(statesN_e.keys(), colors):
#     brs = []
#     for mass in mN:
#         brs.append(calc1.NBR(mass, statesN_e[key]) + 1e-200)
#     plt.plot(mN, brs, label = key, color = color)
#     plt.xlim(1e-3, 10)
#     plt.ylim(1e-3, 1.5)
#     plt.xlabel(r"$m_{N_3}$ (GeV)", fontsize=12)
#     plt.xticks(fontsize=10)
#     plt.yticks(fontsize=10)
#     plt.xticks([0.1, 0.2], ["0.1", "0.2"])
#     plt.ylabel(r"BR($N_1 \to X$)", fontsize=12)
#     plt.xscale("log")
#     plt.yscale("log")
# plt.legend(loc="lower left", fontsize = 14)
# plt.title(r"Mixing with $\nu_e$")
# plt.show()

# calc2 = Calculate(2)
    
# plt.rcParams["figure.figsize"] = (8, 4)
# for key, color in zip(statesN_mu.keys(), colors):
#     brs = []
#     for mass in mN:
#         brs.append(calc2.NBR(mass, statesN_mu[key]) + 1e-200)
#     plt.plot(mN, brs, label = key, color=color)
#     plt.xlim(1e-3, 10)
#     plt.ylim(1e-3, 1.5)
#     plt.xlabel(r"$m_{N_2}$ (GeV)", fontsize=12)
#     plt.xticks(fontsize=10)
#     plt.yticks(fontsize=10)
#     plt.xticks([0.1, 0.2], ["0.1", "0.2"])
#     plt.ylabel(r"BR($N_2 \to X$)", fontsize=12)
#     plt.xscale("log")
#     plt.yscale("log")
# plt.legend(loc="lower left", fontsize = 14)
# plt.title(r"Mixing with $\nu_\mu$")
# plt.show()

# calc3 = Calculate(3)

# plt.rcParams["figure.figsize"] = (8, 4)
# for key, color in zip(statesN_tau.keys(), colors):
#     brs = []
#     for mass in mN:
#         brs.append(calc3.NBR(mass, statesN_tau[key]) + 1e-200)
#     plt.plot(mN, brs, label = key, color=color)
#     plt.xlim(1e-3, 10)
#     plt.ylim(1e-3, 1.5)
#     plt.xlabel(r"$m_{N_3}$ (GeV)", fontsize=12)
#     plt.xticks(fontsize=10)
#     plt.yticks(fontsize=10)
#     plt.xticks([0.1, 0.2], ["0.1", "0.2"])
#     plt.ylabel(r"BR($N_3 \to X$)", fontsize=12)
#     plt.xscale("log")
#     plt.yscale("log")
# plt.legend(loc="lower left", fontsize = 14)
# plt.title(r"Mixing with $\nu_\tau$")
# plt.show()

#%%    

# calc1 = Calculate(1)

# plt.rcParams["figure.figsize"] = (8, 4)
# wids = []
# for mass in mN:
#     wids.append(calc1.Nctau(mass) + 1e-200)
# plt.plot(mN, wids)
# plt.xlim(1e-4, 14)
# # plt.ylim(1e-3, 1.5)
# plt.xlabel(r"$m_{N_3}$ (GeV)", fontsize=12)
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.xticks([0.1, 0.2], ["0.1", "0.2"])
# plt.ylabel(r"$N_1 \to X$", fontsize=12)
# plt.xscale("log")
# plt.yscale("log")
# plt.legend(loc="lower left", fontsize = 14)
# plt.title(r"Mixing with $\nu_e$")
# plt.show()

# calc2 = Calculate(2)
    
# plt.rcParams["figure.figsize"] = (8, 4)
# wids = []
# for mass in mN:
#     wids.append(calc2.Nctau(mass) + 1e-200)
# plt.plot(mN, wids)
# plt.xlim(1e-4, 14)
# # plt.ylim(1e-3, 1.5)
# plt.xlabel(r"$m_{N_2}$ (GeV)", fontsize=12)
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.xticks([0.1, 0.2], ["0.1", "0.2"])
# plt.ylabel(r"$N_2 \to X$", fontsize=12)
# plt.xscale("log")
# plt.yscale("log")
# plt.legend(loc="lower left", fontsize = 14)
# plt.title(r"Mixing with $\nu_\mu$")
# plt.show()

# calc3 = Calculate(3)

# plt.rcParams["figure.figsize"] = (8, 4)
# wids = []
# for mass in mN:
#     wids.append(calc3.Nctau(mass) + 1e-200)
# plt.plot(mN, wids)
# plt.xlim(1e-4, 14)
# # plt.ylim(1e-3, 1.5)
# plt.xlabel(r"$m_{N_3}$ (GeV)", fontsize=12)
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.xticks([0.1, 0.2], ["0.1", "0.2"])
# plt.ylabel(r"$N_3 \to X$", fontsize=12)
# plt.xscale("log")
# plt.yscale("log")
# plt.legend(loc="lower left", fontsize = 14)
# plt.title(r"Mixing with $\nu_\tau$")
# plt.show()
