#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:05:57 2024

@author: souvik
"""

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


xP = 1
mN = np.logspace(np.log10(1e-4),np.log10(10),1000)

# all_states = [
#         "e_pi", "nue_pi0", "nue_eta", "e_rho", "nue_rho0", "nue_omega",
#         "nue_K0", "nue_Ks0", "e_K", "e_Ks", #"nue_etap", #"nue_etac", "nue_Bs0",
#         # "nue_phi", "nue_Ds0", "nue_J/psi",
#         # "nue_K0b", "nue_Ks0b", #"nue_Ds0b",
#         # "e_D", "e_Ds", "e_B", "e_Bc", "e_Ds", "e_Dss",
#         "nu_nu_nu", 
#         "nue_e_e", "nue_mu_mu", "nue_tau_tau", 
#         "numu_e_mu", "nutau_e_tau", 
#         "nue_u_u", "nue_d_d", "nue_c_c", "nue_s_s",
#         "e_u_d", "e_u_s", "e_c_d", "e_c_s"
#         ]

# statesN = {
#                   "hadrons":          ["e_pi", "nue_pi0", "nue_eta", "e_rho", "nue_rho0", "nue_omega",
#                                         "nue_K0", "nue_Ks0", "e_K", "e_Ks", 
#                                         #"nue_etap", #"nue_etac", "nue_Bs0",
#                                         # "nue_phi", "nue_Ds0", "nue_J/psi",
#                                         # "nue_K0b", "nue_Ks0b", #"nue_Ds0b",
#                                         # "e_D", "e_Ds", "e_B", "e_Bc", "e_Ds", "e_Dss",
#                                         "nue_u_u", "nue_d_d", "nue_c_c", "nue_s_s",
#                                         "e_u_d", "e_u_s", "e_c_d", "e_c_s"
#                                         ],
#                         r"3$\nu$":          ["nu_nu_nu"],
#                         r"ee$\nu$":          ["nue_e_e"],
#                     r"$\mu\mu\nu$":          ["nue_mu_mu"],
#                     r"$\tau\tau\nu$":         ["nue_tau_tau"],
#                     r"e$\mu\nu$":          ["numu_e_mu"],
#                     r"e$\tau\nu$":           ["nutau_e_tau"]
#             }


# all_states = [ 
#         "mu_pi", "numu_pi0", "numu_eta", "mu_rho", "numu_rho0", "numu_omega",
#         "numu_K0", "numu_Ks0", "mu_K", "mu_Ks", #"numu_etap", #"numu_etac", "numu_Bs0",
#         # "numu_phi", "numu_Ds0", "numu_J/psi",
#         # "numu_K0b", "numu_Ks0b", #"numu_Ds0b",
#         # "mu_D", "mu_Ds", "mu_B", "mu_Bc", "mu_Ds", "mu_Dss",
#         "nu_nu_nu", 
#         "numu_e_e", "numu_mu_mu", "numu_tau_tau",
#         "nutau_mu_tau", "nue_mu_e",
#         "numu_u_u", "numu_d_d", "numu_c_c", "numu_s_s",
#         "mu_u_d", "mu_u_s", "mu_c_d", "mu_c_s"
#         ]

# statesN = {
#                   "hadrons":          ["mu_pi", "numu_pi0", "numu_eta", "mu_rho", "numu_rho0", "numu_omega",
#                                         "numu_K0", "numu_Ks0", "mu_K", "mu_Ks",
#                                         #"numu_etap", #"numu_etac", "numu_Bs0",
#                                         # "numu_phi", "numu_Ds0", "numu_J/psi",
#                                         # "numu_K0b", "numu_Ks0b", #"numu_Ds0b",
#                                         # "mu_D", "mu_Ds", "mu_B", "mu_Bc", "mu_Ds", "mu_Dss",
#                                         "numu_u_u", "numu_d_d", "numu_c_c", "numu_s_s",
#                                         "mu_u_d", "mu_u_s", "mu_c_d", "mu_c_s"
#                                           ],
#                         r"3$\nu$":          ["nu_nu_nu"],
#                         r"ee$\nu$":          ["numu_e_e"],
#                     r"$\mu\mu\nu$":          ["numu_mu_mu"],
#                     r"$\tau\tau\nu$":          ["numu_tau_tau"],
#                         r"e$\mu\nu$":          ["nue_mu_e"],
#                     r"$\mu\tau\nu$":          ["nutau_mu_tau"]
#             }


all_states = [
        "tau_pi", "nutau_pi0", "nutau_eta", "tau_rho", "nutau_rho0", "nutau_omega",
        "nutau_K0", "nutau_Ks0", "tau_K", "tau_Ks", #"nutau_etap", #"nutau_etac", "nutau_Bs0",
        # "nutau_phi", "nutau_Ds0", "nutau_J/psi",
        # "nutau_K0b", "nutau_Ks0b", #"nutau_Ds0b",
        # "tau_D", "tau_Ds", "tau_B", "tau_Bc", "tau_Ds", "tau_Dss",
        "nu_nu_nu", 
        "nutau_e_e", "nutau_mu_mu", "nutau_tau_tau",
        "nue_tau_e", "numu_tau_mu", 
        "nutau_u_u", "nutau_d_d", "nutau_c_c", "nutau_s_s",
        "tau_u_d", "tau_u_s", "tau_c_d", "tau_c_s"
        ]

statesN = {
                  "hadrons":          ["tau_pi", "nutau_pi0", "nutau_eta", "tau_rho", "nutau_rho0", "nutau_omega", 
                                        "nutau_K0", "nutau_Ks0", "tau_K", "tau_Ks", #"nutau_etap", #"nutau_etac", "nutau_Bs0",
                                        # "nutau_phi", "nutau_Ds0", "nutau_J/psi",
                                        # "nutau_K0b", "nutau_Ks0b", #"nutau_Ds0b",
                                        #"tau_D", "tau_Ds", "tau_B", "tau_Bc", "tau_Ds", "tau_Dss",
                                        "nutau_u_u", "nutau_d_d", "nutau_c_c", "nutau_s_s",
                                        "tau_u_d", "tau_u_s", "tau_c_d", "tau_c_s"],
                        r"3$\nu$":          ["nu_nu_nu"],
                      r"ee$\nu$":          ["nutau_e_e"],
                    r"$\mu\mu\nu$":          ["nutau_mu_mu"],
                    r"$\tau\tau\nu$":          ["nutau_tau_tau"],
                      r"$\mu\tau\nu$":         ["numu_tau_mu"],
                      r"e$\tau\nu$":          ["nue_tau_e"],
                    
          }

GF = 1.166e-5

def states_decay(name = "N"):
    return statesN

def states_all(name = "N"):
    return all_states

# Fermion masses
mfs = {
    "e":      0.51099895e-3, 
    "mu":     0.1056583745,
    "tau":    1.77686, 
    "d":      4.67e-3, 
    "u":      2.16e-3, 
    "s":      93.4e-3, 
    "c":      1.27, 
    "b":      4.18,
    "t":      172.69
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
    "etap":  0.9578,
    "K":     0.4937,
    "K0":    0.4976,
    "K0b":   0.4976,
    "etac":  2.9796,
    "Bs0":   5.3675,
    "D":     1.8694,
    "Ds":    1.9683,
    "B":     5.279,
    "Bc":    6.277
    }

mvs = {
       "rho0":  0.776,
       "rho":   0.7758,
       "omega": 0.78259,
       "Ks":    0.89166,
       "Ks0":   0.8961,
       "Ks0b":  0.8961,
       "phi":   1.019456,
       "Ds0":   2.0067,
       "Ds0b":  2.0067,
       "J/psi": 3.096916,
       "Ds":    2.01,
       "Dss":   2.1121
       }

fps = {
    "pi":    0.1307,
    "pi0":   0.130,
    "eta":   0.16,
    "etap":  0.1529,
    "K":     0.1598,
    "K0":    0.159,
    "K0b":   0.159,
    "etac":  0.335,
    "Bs0":   0.216,
    "D":     0.2226,
    "Ds":    0.266,
    "B":     0.19,
    "Bc":    0.399
    }

fvs = {
       "rho0":  0.22,
       "rho":   0.22,
       "omega": 0.19,
       "Ks":    0.217,
       "Ks0":   0.217,
       "Ks0b":  0.217,
       "phi":   0.229,
       "Ds0":   0.31,
       "Ds0b":  0.31,
       "J/psi": 0.459,
       "Ds":    0.31,
       "Dss":   0.315
       }

quarks = ["u", "d", "c", "s", "t", "b"]

Vud = 0.974
Vus = 0.217
Vub = 0.004
Vcd = 0.221
Vcs = 0.975
Vcb = 0.041
Vtd = 0.009
Vts = 0.042
Vtb = 1.041

def V(x, y):
    V = np.array([[Vud, Vus, Vub], [Vcd, Vcs, Vcb], [Vtd, Vts, Vtb]])
    upt, downt = ["u", "c", "t"], ["d", "s", "b"]
    if x in upt and y in downt:
        return V[upt.index(x)][downt.index(y)]
    elif y in upt and x in downt:
        return V[upt.index(y)][downt.index(x)]
    
modes = []

def mfi(particle):
    if particle in mfs.keys():
        return mfs[particle]
    elif particle in mps.keys():
        return mps[particle]
    elif particle in mvs.keys():
        return mvs[particle]
    elif particle in nus.keys():
        return nus[particle]

def delta(nu, l):
    if nu == "nue" and l == "e":
        return 1
    elif nu == "numu" and l == "mu":
        return 1
    elif nu == "nutau" and l == "tau":
        return 1
    else:
        return 0
def theta(x):
    if x >= 0: 
        return 1
    else: 
        return 0
    
  
    
def lamda(a, b, c):
    return (a + b + c)**2 - 4*(a*b + b*c + c*a)    

def FP(x, y):
    return np.sqrt(lamda(1, x**2, y**2)) * ((1 + x**2) * (1 + x**2 - y**2) - 4*(x**2))

def FV(x, y):
    return np.sqrt(lamda(1, x**2, y**2)) * ((1 - x**2)**2 + (1 + x**2) * (y**2) - 2*(y**4))

def I1(x, y, z):
    def IF1(s, x, y, z):
        i1 = 12 * (s - x**2 - y**2) * (1 + z**2 - s) 
        i2 = np.sqrt(lamda(s, x**2, y**2)) * np.sqrt(lamda(1, s, z**2))
        return i1*i2/s
    return quad(IF1, (x + y)**2, (1 - z)**2, args = (x, y, z))[0]

def I2(x, y, z):
    def IF2(s, x, y, z):
        i1 = 24 * y * z * (1 + x**2 - s) 
        i2 = np.sqrt(lamda(s, y**2, z**2)) * np.sqrt(lamda(1, s, x**2))
        return i1*i2/s
    return quad(IF2, (y + z)**2, (1 - x)**2, args = (x, y, z))[0]


    

def Nwidth(mass, xH, state, U, gX):
        
    mode = state.split("_")
    nm = len(mode)
    
    if nm == 3 and  theta(mass - mfi(mode[0]) - mfi(mode[1]) - mfi(mode[2])) == 1:
        
        if mode[-1] == mode[-2] and mode[-1] in mfs.keys():
            thetaw = 0.2229
            gL, gR = -0.5 + thetaw, thetaw
            qL, qR = -xP-1/2*xH, -xP-xH
            yvl1, yl1, yl2 = mfi(mode[0])/mass, mfi(mode[1])/mass, mfi(mode[2])/mass
            mZp = 4*mass
            dtr = mode[-1]
            
            def Z(xL, xR, yL, yR):
                d = abs(U)**2 * (GF**2/(96*(np.pi**3))) * mass**5  
                d *= (xL*yR + xR*yL) * I2(yvl1, yl2, yl2)/2 + (xL*yL + xR*yR)* I1(yvl1, yl2, yl2)
                return d
            
            def ZW(xL, xR):
                # d = -abs(U)**2 * (GF**2/(192*(np.pi**3))) * mass**5 
                # d *= I1(yl1, yvl1, yl2) * delta(mode[0],mode[-1])*delta(mode[0],mode[-1])
                d = abs(U)**2 * (GF**2/(96*(np.pi**3))) * mass**5  
                d *= xR*delta(mode[0],mode[-1]) * I2(yvl1, yl2, yl2) + (1/2 + 2*xL) * delta(mode[0],mode[-1]) * I1(yvl1, yl2, yl2)
                return d
            w = abs(U)**2 * (GF**2/(192*(np.pi**3))) * mass**5 
            if mode[-1] in quarks: 
                if mass > mps["etap"]:
                    w = w * 3 #* V(mode[-1], mode[-2])**2 
                else: return 0
            w *= I1(yl1, yvl1, yl2) * delta(mode[0],mode[-1])
            w += (Z(gL, gR, gL, gR) + ZW(gL, gR)) #+ (gX**2)*(Z(qL, qR, qL, qR) + ZW(qL, qR))/(32 * GF**2 * mZp**4) 
            # w += gX*(Z(gL, gR, qL, qR) + Z(qL, qR, gL, gR))/np.sqrt(32 * GF**2 * mZp**4)  
            
            
            
        elif mode[-1] != mode[-2] and mode[-1] in mfs.keys() and mode[-2] in mfs.keys():
            yvl2, yl1, yl2 = mfi(mode[0])/mass, mfi(mode[1])/mass, mfi(mode[2])/mass
            
            w = abs(U)**2 * (GF**2/(192*(np.pi**3))) * mass**5 
            if mode[-1] in quarks: 
                if mass > mps["etap"]:
                    w = w * 3 * V(mode[-1], mode[-2])**2 
                else: w = 0 
            w *= I1(yl1, yvl2, yl2)
            
        elif mode[0] == mode[1] == mode[2]:
            gL = 0.5 
            qL = -xP-1/2*xH
            mZp = 4*mass
            w = abs(U)**2 * (GF**2/(96*(np.pi**3))) * mass**5 
            # w = w + (gX**2)*w/(32 * GF**2 * mZp**4) + 2*gX*w/np.sqrt(32 * GF**2 * mZp**4)
            
    elif nm == 2 and  theta(mass - mfi(mode[0]) - mfi(mode[1])) == 1 and mass<=mps["etap"]:    
        
        if mode[0] in nus.keys() and mode[1] in mps:
            yvl1, yP = mfi(mode[0])/mass, mfi(mode[1])/mass
            
            w = abs(U)**2 * (GF**2/(64*np.pi)) * (fps[mode[-1]]**2) * mass**3 
            w *= (1 - yP**2)**2
            
        elif mode[0] in mfs.keys() and mode[1] in mps:
            if mode[1] in ["pi"]:
                Vv = Vud
            elif mode[1] in ["K"]:
                Vv = Vus
            elif mode[1] in ["D"]:
                Vv = Vcd
            elif mode[1] in ["Ds"]:
                Vv = Vcd
            elif mode[1] in ["B"]:
                Vv = Vub
            elif mode[1] in ["Bc"]:
                Vv = Vcb
                
            yl1, yP = mfi(mode[0])/mass, mfi(mode[1])/mass
            
            w = abs(U)**2 * (GF**2/(16*np.pi)) * (Vv**2) * (fps[mode[-1]]**2) * mass**3 
            w *= FP(yl1, yP)
            
        elif mode[0] in nus.keys() and mode[1] in mvs:
            thetaw = 0.2229 #Weinberg angle (sin(theta_w)**2)
            yvl1, yV = mfi(mode[0])/mass, mfi(mode[1])/mass
            if mode[1] in ["rho0", "omega"]:
                kv = thetaw/3
            elif mode[1] in ["Ks0", "Ks0b", "phi"]:
                kv = -1/4 + thetaw/3
            elif mode[1] in ["Ds0", "Ds0b", "J/psi"]:
                kv = 1/4 - 2*thetaw/3
            
            w = abs(U)**2 * (GF**2/(2*np.pi)) * (kv**2) * (fvs[mode[-1]]**2) * mass**3
            w *= ((1 - yV**2)**2) * ((1 + 2*yV**2))
            
        elif mode[0] in mfs.keys() and mode[1] in mvs:
            if mode[1] in ["rho"]:
                Vv = Vud
            elif mode[1] in ["Ks"]:
                Vv = Vus
            elif mode[1] in ["Ds"]:
                Vv = Vcd
            elif mode[1] in ["Dss"]:
                Vv = Vcs
                
            yl1, yV = mfi(mode[0])/mass, mfi(mode[1])/mass
            
            w = abs(U)**2 * (GF**2/(16*np.pi)) * (Vv**2) * (fvs[mode[-1]]**2) * mass**3  
            w *= FV(yl1, yV)
            
    else:#if state in all_states: 
        w=0
        # print("Unknown state '%s'." % state)
            
    return w 
    


def factor(state):
    if len(state.split("_")) == 3 and state.split("_")[-1] != state.split("_")[-2] in mfs.keys():
        return 2
    elif len(state.split("_")) == 2 and state.split("_")[0] in mfs.keys():
        return 2
    else:
        return 1

def NBR(mass, xH, states, U, gX): # array of mass is not accepted
    
    width = {}
    den = 0
    for state in all_states:
        den += Nwidth(mass, xH, state, U, gX)*factor(state)
        width[state] = Nwidth(mass, xH, state, U, gX)*factor(state)
    
    num = 0
    for state in states:
        num += width[state]#Nwidth(mass, xH, state, U, gX)*factor(state)
         
    return num/den


plt.rcParams["figure.figsize"] = (10, 8)
for key in statesN.keys():
    brs = []
    for mass in mN:
        brs.append(NBR(mass, 0, statesN[key], 1e-2, 1e-7) + 1e-200)
    if sum(brs)>1e-200:
        plt.plot(mN, brs, label = key)
    else: plt.plot(mN, brs)

plt.xlim(1e-4, 10)
plt.ylim(1e-3, 1.5)
plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
plt.xticks([0.1, 0.2], ["0.1", "0.2"])
plt.ylabel("Branching fraction", fontsize=25)
plt.xscale("log")
plt.yscale("log")

# plt.xlabel(r"$M_{N_1}$ (GeV)", fontsize=25)
# plt.xlabel(r"$M_{N_2}$ (GeV)", fontsize=25)
plt.xlabel(r"$M_{N_3}$ (GeV)", fontsize=25)
    
# plt.title("Decay of Ne")
# plt.title(r"Decay of N$\mu$")
# plt.title(r"Decay of N$\tau$")
plt.legend(loc="lower center", fontsize = 15)