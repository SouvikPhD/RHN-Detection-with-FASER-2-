#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:57:26 2023

@author: daslinux
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:33:00 2023

@author: daslinux
"""
# # DARKCAST is licensed under the GNU GPL version 2 or later.
# # Copyright (C) 2021 Philip Ilten, Yotam Soreq, Mike Williams, and Wei Xue.

# # This example calculates the branching fractions for every model
# # available in darkcast/models. If matplotlib is available these
# # branching fractions are then plotted. The produced figures
# # correspond to figure 3 of Ilten:2018crw.

# # Update the system path to find the Darkcast module.
# # This assumes that 'examples' is in 'darkcast/examples.'
import sys, os, inspect, itertools, numpy
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "../../"))

# Import the Darkcast module.
import darkcast_scalar as darkcast
import matplotlib.pyplot as plt



import collections
channels = collections.OrderedDict([
        # Entries take the form (key, value).
        
        # All available fundamental fermion pairs.
        (r"$e$ $e$",                 "e_e"),
        (r"$\mu$ $\mu$",               "mu_mu"),
        # (r"$\tau$_$\tau$",             "tau_tau"),
        # ("$nue_nue$",             "nue_nue"),
        # ("$numu_numu$",           "numu_numu"),
        # ("$nutau_nutau$",         "nutau_nutau"),
        # ("$d_d$",                 "d_d"), # Included in exclusive hadrons.
        # ("$u_u$",                 "u_u"), # Included in exclusive hadrons.
        # ("s_s",                 "s_s"), # Included in exclusive hadrons.
        # ("c_c",                 "c_c"),
        # ("$b_b$",                 "b_b"),
        # ("$t_t$",                 "t_t"),
        
        # Combine charged leptons into a single channel.
        # ("l_l",                  ["e_e", "mu_mu", "tau_tau"]),
        # (r"$\sum Leptons$",                  ["e_e", "mu_mu", "tau_tau"]),
        
        # ("vis",                  ["e_e", "mu_mu", "tau_tau", "hadrons"])

        # Combine quarks into a single channel.
        # ("q_q",                   ["u_u", "d_d", "s_s", "t_t", "c_c", "b_b"]),



        # Combine Neutrinos into a single channel.
        # ("$nu_nu$",               ["nue_nue", "numu_numu", "nutau_nutau"]),
                
        # All available exclusive hadronic states.
        #("$pi+_pi-$",             "pi+_pi-"),
        #("$pi+_pi-_pi+_pi-$",     "pi+_pi-_pi+_pi-"),
        #("$pi+_pi-_pi0_pi0$",     "pi+_pi-_pi0_pi0"),
        #("$pi+_pi-_pi0$",         "pi+_pi-_pi0"),
        #("$pi0_gamma$",           "pi0_gamma"),
        #("$K_K$",                 "K_K"),
        #("$K_K_pi$",              "K_K_pi"),
        #("other hadrons",         "other"),
        
        # Alias for all exclusive hadronic final states above.
        (r"$\pi$ $\pi$",                ["pi0_pi0", "pi_pi"]),

        # Alias for all visible final states, e.g. everything above
        # except 'd_d', 'u_u', and 's_s'.
        # ("Visible",                "visible"),


        # Combine Right Handed Neutrinos into a single channel.
           
        # (r"$\sum N_i N_i$",               ["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"]), 
        
        # (r"$\sum\nu_i\nu_i$",               ["nue_nue", "numu_numu", "nutau_nutau"]),
        
        (r"$\gamma$ $\gamma$",               "gamma_gamma"),
        # (r"$Z^\prime$ $Z^\prime$",               "Zp_Zp"),
        # (r"g_g",               ["g_g"]),
        # ("$Ne_Ne$",             "Ne_Ne"),
        # ("$Nmu_Nmu$",           "Nmu_Nmu"),
        # ("$Ntau_Ntau$",         "Ntau_Ntau"),
        # All invisible final states.
        #("invisible",              "invisible"),
        
        ("N N",               ["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"]),
        
        # All possible final states to consider when calculating the
        # total width. Typically 'visible' and 'invisible' but this
        # can be specified by the user when creating the model with
        # the 'states' variable, e.g. darkcast.Model('dark_photon',
        # states = ['e_e', 'mu_mu']).
        # ("total",                  "total"),
        ])

xH = 0
# mass = 1
def pos(x, name):
    if name=="U1_X" and (x==0): return "center left"
    elif (x==2 or x== -1.2 or  x==-2) and name=="U1_X_phi4": return "center left"
    else: return "lower left" 

masses = numpy.logspace(-3, 0, 1500)
# masses = numpy.linspace(0, 2, 1000)
# xHs = numpy.linspace(-2, 2, 1000)



# Try to load matplotlib.
try: import matplotlib.pyplot as pyplot
except: pyplot = None
colors = ["red", "blue", "orange", "green", "purple", "black", "cyan"]#["red", "green", "brown", "blue", "black", "red", "blue", "purple", 
          # "magenta", "orange"]
# colors = ["red", "blue", "green"#"u_u", "d_d", "t_t",]
types = ["solid", "solid", "solid", "solid", "solid"]#, "solid", "dotted", "solid",  "dotted", "solid", "dotted", "dotted",
          # "dotted", "dotted"]
          
#%%    
# model = darkcast.Model("U1_X", Y1 = 1000, Y2=1000, Y3=1000)
name = "U1_X"
mZ = 100
g = 0.01
ths = [1e-5, 1e-4]
linestyles = ["solid", "dashed"]
mN = 1/4
model = darkcast.Model("U1_X", Y1 = mN, cN=False, cZ=True, Y2 = 1000, Y3 = 1000, mZ=mZ)

for style, th in zip(linestyles, ths):
    if pyplot:
        pyplot.rcParams["figure.figsize"] = (10,6)
        # pyplot.subplots_adjust(left=0, bottom=0)
        # fig, ax = pyplot.subplots()
        icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

        # Loop over the channels.
    for label, channel in channels.items():
            # Calculate the branching fraction for the model and channel
            # as a function of mass.
        bfracs = []
        for mass in masses:
            bfrac = model.bfrac(channel, mass, xH, th=th, g=g)
            bfracs.append(bfrac)
        if pyplot:
            if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
            else: color, linestyle = labels[label], labels[label]; label = None
            if sum(bfracs)==0:
                plt.plot(masses, bfracs,
                        color = color, linestyle = style)
            else:
                plt.plot(masses, bfracs, #label = label,
                        color = color, linestyle = style)
            # plt.plot(xHs, bfracs, label = label,
                    # color = color, linestyle = linestyle)
            # label_x = masses[-50]  # Adjust the x-position of the label
            # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
            # pyplot.text(label_x, label_y, label)
        # Save the plot.


    if pyplot:
        title = r"$m_{Z^\prime}=$" + str(mZ) + "GeV, $g_{BL}$=" + str(g) + ", $sin^2 \zeta = $" + str(th**2) #+ "MeV, $m_N =$"+ str(mN/1000) + "TeV"
        # title = r"$U_1(X):$ $M_{Zp}$ = " + str(mass) + " GeV"
        # legend = plt.legend(loc = (0.1,0.7), fontsize = 20, ncol=3)

    plt.xlim([1e-2, 1])
    plt.ylim([1e-15,10])
    # plt.xlim([-2, 2])
    # plt.ylim([0, 1])
    # plt.axvline(x=2, color="k")
    plt.semilogx()
    plt.semilogy()


    plt.xticks(fontsize=21)
    plt.yticks(fontsize=21)
    
icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}
for label, channel in channels.items():
    if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
    else: color, linestyle = labels[label], labels[label]; label = None
    plt.plot([1e-20], [1e-20], label=label, color = color)
plt.legend(loc = (0.1,0.7), fontsize = 20, ncol=3)

# plt.text(0.015, 8e-4, title, fontsize=20)
plt.xlabel(r"$m_{h_2}$ [GeV]", fontsize=25)
# plt.xlabel(r"$x_H$", fontsize=25)
plt.ylabel(r"BR$(h_2 \to XX $)", fontsize=25)
# plt.title(title, fontsize=18, loc="center")
#darkcast.utils.logo()
# plt.savefig("bfrac_%s.pdf" % name) 
plt.tight_layout()
plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/hzpln.pdf",bbox_inches='tight')
plt.show()


#%%

name = "U1_X"
mZ = 1/4
g = 1e-9
th = numpy.sqrt(1e-9)
mN = 1000
model = darkcast.Model("U1_X", Y1 = mN, Y2 = 1000, Y3 = 1000, cN=True, cZ=False, mZ=mZ)



if pyplot:
    pyplot.rcParams["figure.figsize"] = (10,6)
    # pyplot.subplots_adjust(left=0, bottom=0)
    # fig, ax = pyplot.subplots()
    icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

    # Loop over the channels.
for label, channel in channels.items():
        # Calculate the branching fraction for the model and channel
        # as a function of mass.
    bfracs = []
    for mass in masses:
        bfrac = model.bfrac(channel, mass, xH, th=th, g=g)
        bfracs.append(bfrac)
    if pyplot:
        if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
        else: color, linestyle = labels[label], labels[label]; label = None
        if sum(bfracs)==0:
            plt.plot(masses, bfracs,
                    color = color, linestyle = linestyle)
        else:
            plt.plot(masses, bfracs, label = label,
                    color = color, linestyle = linestyle)
        # plt.plot(xHs, bfracs, label = label,
        #         color = color, linestyle = linestyle)
        # label_x = masses[-50]  # Adjust the x-position of the label
        # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
        # pyplot.text(label_x, label_y, label)
    # Save the plot.


if pyplot:
    title = r"$m_{N}=$" + str(mN/1000) + "TeV,  $g_{BL}$=" + str(g) + ", $sin^2 \zeta = $" + str(th**2) #+ ", $m_N = $"+ str(mN*1e3)+ "TeV"
    # title = r"Alternative: $M_{Zp}$ = " + str(mass) + " GeV"
    legend = plt.legend(loc = (1e-3, 0.5), fontsize = 20, ncol=2)
    

plt.xlim([1e-3, 1])
plt.ylim([1e-4, 1.5])
# plt.xlim([-2, 2])
# plt.ylim([0, 1])
plt.semilogx()
plt.semilogy()
plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
# plt.text(0.015, 8e-4, title, fontsize=20)
plt.xlabel(r"$m_{h_2}$ [GeV]", fontsize=25)
# plt.xlabel(r"$x_H$", fontsize=25)
plt.ylabel(r"BR($h_2\to  XX$)", fontsize=25)
# plt.title(title, fontsize=18, loc="center")
#darkcast.utils.logo()
# fig.savefig("bfrac_%s.pdf" % name)
plt.tight_layout()
# plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/lzphn.pdf",bbox_inches='tight')


#%%

name = "U1_X"
mZ = 1/4
g = 1e-5
th = numpy.sqrt(1e-9)
mN = 1000
model = darkcast.Model("U1_X", Y1 = mN, Y2 = 1000, Y3 = 1000, cN=True, cZ=False, mZ=mZ)



if pyplot:
    pyplot.rcParams["figure.figsize"] = (10,6)
    # pyplot.subplots_adjust(left=0, bottom=0)
    # fig, ax = pyplot.subplots()
    icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

    # Loop over the channels.
for label, channel in channels.items():
        # Calculate the branching fraction for the model and channel
        # as a function of mass.
    bfracs = []
    for mass in masses:
        bfrac = model.bfrac(channel, mass, xH, th=th, g=g)
        bfracs.append(bfrac)
    if pyplot:
        if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
        else: color, linestyle = labels[label], labels[label]; label = None
        if sum(bfracs)==0:
            plt.plot(masses, bfracs,
                    color = color, linestyle = "dashed")
        else:
            plt.plot(masses, bfracs, label = label,
                    color = color, linestyle = "dashed")
        # plt.plot(xHs, bfracs, label = label,
        #         color = color, linestyle = linestyle)
        # label_x = masses[-50]  # Adjust the x-position of the label
        # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
        # pyplot.text(label_x, label_y, label)
    # Save the plot.


if pyplot:
    title = r"$m_{N}=$" + str(mN/1000) + "TeV,  $g_{BL}$=" + str(g) + ", $sin^2 \zeta = $" + str(th**2) #+ ", $m_N = $"+ str(mN*1e3)+ "TeV"
    # title = r"Alternative: $M_{Zp}$ = " + str(mass) + " GeV"
    legend = plt.legend(loc = "center left", fontsize = 20, ncol=2)
    

plt.xlim([1e-3, 1])
plt.ylim([1e-4, 1.5])
# plt.xlim([-2, 2])
# plt.ylim([0, 1])
plt.semilogx()
plt.semilogy()
plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
# plt.text(0.015, 8e-4, title, fontsize=20)
plt.xlabel(r"$m_{h_2}$ [GeV]", fontsize=25)
# plt.xlabel(r"$x_H$", fontsize=25)
plt.ylabel(r"BR($h_2\to  XX$)", fontsize=25)
# plt.title(title, fontsize=18, loc="center")
#darkcast.utils.logo()
# fig.savefig("bfrac_%s.pdf" % name)
plt.tight_layout()
plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/lzphn_comb.pdf",bbox_inches='tight')
plt.show()

#%%

name = "U1_X"
mZ = 0.15
g = 1e-9
th = numpy.sqrt(1e-9)
mN = 1/4
model = darkcast.Model("U1_X", Y1 = mN, Y2 = 1000, Y3 = 1000, cN=False, cZ=True, mZ=mZ)



if pyplot:
    pyplot.rcParams["figure.figsize"] = (10,6)
    # pyplot.subplots_adjust(left=0, bottom=0)
    # fig, ax = pyplot.subplots()
    icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

    # Loop over the channels.
for label, channel in channels.items():
        # Calculate the branching fraction for the model and channel
        # as a function of mass.
    bfracs = []
    for mass in masses:
        bfrac = model.bfrac(channel, mass, xH, th=th, g=g)
        bfracs.append(bfrac)
    if pyplot:
        if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
        else: color, linestyle = labels[label], labels[label]; label = None
        if sum(bfracs)==0:
            plt.plot(masses, bfracs,
                    color = color, linestyle = linestyle)
        else:
            plt.plot(masses, bfracs, label = label,
                    color = color, linestyle = linestyle)
        # plt.plot(xHs, bfracs, label = label,
        #         color = color, linestyle = linestyle)
        # label_x = masses[-50]  # Adjust the x-position of the label
        # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
        # pyplot.text(label_x, label_y, label)
    # Save the plot.


if pyplot:
    title = r"$m_{Z^\prime}=$" + str(mZ*1000) + "MeV,  $g_{BL}$=" + str(g) + ", $sin^2 \zeta = $" + str(th**2) #+ ", $m_N = $"+ str(mN*1e3)+ "TeV"
    # title = r"Alternative: $M_{Zp}$ = " + str(mass) + " GeV"
    legend = plt.legend(loc = "lower left", fontsize = 20, ncol=3)
    

plt.xlim([1e-3, 1])
plt.ylim([1e-6, 1.5])
# plt.xlim([-2, 2])
# plt.ylim([0, 1])
plt.semilogx()
plt.semilogy()
plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
# plt.text(0.015, 8e-4, title, fontsize=20)
plt.xlabel(r"$m_{h_2}$ [GeV]", fontsize=25)
# plt.xlabel(r"$x_H$", fontsize=25)
plt.ylabel(r"BR($h_2\to  XX$)", fontsize=25)
# plt.title(title, fontsize=18, loc="center")
#darkcast.utils.logo()
# fig.savefig("bfrac_%s.pdf" % name)
plt.tight_layout()
# plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/lzpln.pdf",bbox_inches='tight')

#%%

name = "U1_X"
mZ = 0.15
g = 1e-5
th = numpy.sqrt(1e-9)
mN = 1/4
model = darkcast.Model("U1_X", Y1 = mN, Y2 = 1000, Y3 = 1000, cN=False, cZ=True, mZ=mZ)



if pyplot:
    pyplot.rcParams["figure.figsize"] = (10,6)
    # pyplot.subplots_adjust(left=0, bottom=0)
    # fig, ax = pyplot.subplots()
    icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

    # Loop over the channels.
for label, channel in channels.items():
        # Calculate the branching fraction for the model and channel
        # as a function of mass.
    bfracs = []
    for mass in masses:
        bfrac = model.bfrac(channel, mass, xH, th=th, g=g)
        bfracs.append(bfrac)
    if pyplot:
        if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
        else: color, linestyle = labels[label], labels[label]; label = None
        if sum(bfracs)==0:
            plt.plot(masses, bfracs,
                    color = color, linestyle = "dashed")
        else:
            plt.plot(masses, bfracs, label = label,
                    color = color, linestyle = "dashed")
        # plt.plot(xHs, bfracs, label = label,
        #         color = color, linestyle = linestyle)
        # label_x = masses[-50]  # Adjust the x-position of the label
        # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
        # pyplot.text(label_x, label_y, label)
    # Save the plot.


if pyplot:
    title = r"$m_{Z^\prime}=$" + str(mZ*1000) + "MeV,  $g_{BL}$=" + str(g) + ", $sin^2 \zeta = $" + str(th**2) #+ ", $m_N = $"+ str(mN*1e3)+ "TeV"
    # title = r"Alternative: $M_{Zp}$ = " + str(mass) + " GeV"
    legend = plt.legend(loc = "lower left", fontsize = 20, ncol=3)
    

plt.xlim([1e-3, 1])
plt.ylim([1e-6, 1.5])
# plt.xlim([-2, 2])
# plt.ylim([0, 1])
plt.semilogx()
plt.semilogy()
plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
# plt.text(0.015, 8e-4, title, fontsize=20)
plt.xlabel(r"$m_{h_2}$ [GeV]", fontsize=25)
# plt.xlabel(r"$x_H$", fontsize=25)
plt.ylabel(r"BR($h_2\to  XX$)", fontsize=25)
# plt.title(title, fontsize=18, loc="center")
#darkcast.utils.logo()
# fig.savefig("bfrac_%s.pdf" % name)
plt.tight_layout()
plt.savefig("/home/souvik/codes/FORESEE_fig/scalar_fig/lzpln_comb.pdf",bbox_inches='tight')
plt.show()

#%%


import numpy as np
import matplotlib.pyplot as plt

name = "U1_X"
mZ = 1000
g = 1#e-9
th = 1#numpy.sqrt(1e-9)
mN = 1000
model = darkcast.Model("U1_X", Y1 = mN, Y2 = 1000, Y3 = 1000, cN=True, cZ=True, mZ=mZ)

masses = np.linspace(0.3, 1.4, 1000)
mpi = 0.135
v   = 246 
mz0 = 90 
als = 0.18

mqs = {
    "d":      4.7e-3, 
    "u":      2.16e-3, 
    "s":      93.5e-3, 
    "c":      1.273, 
    "b":      4.183,
    "t":      172.56
    }

def width_mes(m, sth=1):
    if isinstance(m, (int, float)): m = np.array([m])
    C = 5.1e-9
    beta = np.where(m>4*mpi, np.sqrt(1 - (4*mpi/m)**2), 0)
    Gamma = np.where(m<2, sth**2 * m**3 * beta * C, 0)
    return Gamma

def x(mq, m):
    return m**2/(4*mq**2)

# def als(Q):
#     Nf = 5
#     beta = (33 - 2*Nf)/(12 * np.pi)
#     return al0 / (1 + al0 * beta * np.log(Q**2/mz0**2))

def f(x):
    if isinstance(x, (int, float)): x = np.array([x])
    return np.where(x>1, - (1/4)*(np.log( (1 + np.sqrt(1-1/x)) / (1 - np.sqrt(1-1/x)) ) - 1j*np.pi)**2, np.arcsin(np.sqrt(x))**2)

def width_gg(m, sth=1):
    if isinstance(m, (int, float)): m = np.array([m])
    return np.where(m>2, sth**2 * m**3  * als**2/ (32 * np.pi**3 * v**2) * abs(sum([(x(mqs[q], m) + (1 - x(mqs[q], m)) * f(x(mqs[q], m)))/x(mqs[q], m)**2 for q in mqs.keys()]))**2, 0)

# def width_pi(m, sth=1):
#     if isinstance(m, (int, float)): m = np.array([m])
#     fac = (3*sth**2*GF/(16*np.sqrt(2)*np.pi*m)) * np.sqrt(1 - 4*(mpi**2/m**2))
#     fac *= ((7/9)*mpi**2 + (2/9)*(mpi**2 + 2*mpi**2))**2
#     return np.where(m<2, fac, 0)

width_pi = []
for mass in masses:
    if mass< 2:
        w = model.width(["pi_pi", "pi0_pi0"], mass, xH=0, th=th, g=g)/model.width(["mu_mu"], mass, xH=0, th=th, g=g)
    else:
        w = 0
    width_pi.append(w)

plt.plot(masses, width_pi)
# plt.plot(masses, width_mes(masses))
# plt.plot(masses, width_gg(masses))
# plt.ylim([5e-10, 3e-5])
plt.loglog()