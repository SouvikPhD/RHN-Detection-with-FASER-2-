#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:33:00 2023

@author: daslinux
"""
# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2021 Philip Ilten, Yotam Soreq, Mike Williams, and Wei Xue.

# This example calculates the branching fractions for every model
# available in darkcast/models. If matplotlib is available these
# branching fractions are then plotted. The produced figures
# correspond to figure 3 of Ilten:2018crw.

# Update the system path to find the Darkcast module.
# This assumes that 'examples' is in 'darkcast/examples.'
import sys, os, inspect, itertools, numpy
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "../../"))
import matplotlib.pyplot as plt
import matplotlib

# Import the Darkcast module.
import darkcast

# names = ["U1_X"]
# M_Zs = numpy.logspace(-2, 1, 1000) #3
# xH = 0

# # Load all the available models in darkcast/models and DARKCAST_MODEL_PATH.
# # model = darkcast.Model("U1_X")
# # name="U1_X"


# # names = ["axial", "2hdm", "dark_photon", "chiral"]



# # Alternatively, all the models from a folder, '/foo/bar', could be
# # loaded as:
# #
# # models = darkcast.Models("/foo/bar")
# #
# # Note that any models in the directory that are not valid will not be
# # loaded. A single model with name 'foo_bar' can be loaded as:
# #
# # model = darkcast.Model("foo_bar")

# # Create the dictionary of channels for which to calculate the
# # branching fractions. A channel can be either a single state,
# # e.g. 'mu_mu' or a list of final states, e.g. ['mu_mu', 'e_e']. The
# # following can be commented in or out depending on the channels
# # needed. Note this is an 'OrderedDict' to ensure that the keys remain
# # in the order specified. Keys which require mathmode in LaTeX are
# # enclosed in '$'.
# import collections
# channels = collections.OrderedDict([
#         # Entries take the form (key, value).
        
#         # All available fundamental fermion pairs.
#         #("$e_e$",                 "e_e"),
#         #("$mu_mu$",               "mu_mu"),
#         #("$tau_tau$",             "tau_tau"),
#         # ("$nue_nue$",             "nue_nue"),
#         # ("$numu_numu$",           "numu_numu"),
#         # ("$nutau_nutau$",         "nutau_nutau"),
#         #("$d_d$",                 "d_d"), # Included in exclusive hadrons.
#         #("$u_u$",                 "u_u"), # Included in exclusive hadrons.
#         #("$s_s$",                 "s_s"), # Included in exclusive hadrons.
#         #("$c_c$",                 "c_c"),
#         #("$b_b$",                 "b_b"),
#         #("$t_t$",                 "t_t"),

#         # Combine Neutrinos into a single channel.
#         #("$nu_nu$",               ["nue_nue", "numu_numu", "nutau_nutau"]),

#         # All available exclusive hadronic states.
#         #("$pi+_pi-$",             "pi+_pi-"),
#         #("$pi+_pi-_pi+_pi-$",     "pi+_pi-_pi+_pi-"),
#         #("$pi+_pi-_pi0_pi0$",     "pi+_pi-_pi0_pi0"),
#         #("$pi+_pi-_pi0$",         "pi+_pi-_pi0"),
#         #("$pi0_gamma$",           "pi0_gamma"),
#         #("$K_K$",                 "K_K"),
#         #("$K_K_pi$",              "K_K_pi"),
#         #("other hadrons",         "other"),
        
#         # Combine Right Handed Neutrinos into a single channel.
#         # ("$N_N$",               ["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"]),
#         # ("$Ne_Ne$",             "Ne_Ne"),
#         # ("$Nmu_Nmu$",           "Nmu_Nmu"),
#         # ("$Ntau_Ntau$",         "Ntau_Ntau"),

#         # Alias for all exclusive hadronic final states above.
#         # ("hadrons",                "hadrons"),

#         # Alias for all visible final states, e.g. everything above
#         # except 'd_d', 'u_u', and 's_s'.
#         #("visible",                "visible"),

#         # All invisible final states.
#         #("invisible",              "invisible"),
        
#         # All possible final states to consider when calculating the
#         # total width. Typically 'visible' and 'invisible' but this
#         # can be specified by the user when creating the model with
#         # the 'states' variable, e.g. darkcast.Model('dark_photon',
#         # states = ['e_e', 'mu_mu']).
#         #("total",                  "total"),
#         ])

# # Create the list of masses for which to calculate the branching fractions.
# # masses1 = [mass for mass in numpy.logspace(-3, -1, 1000)]
# # masses2 = [mass for mass in numpy.logspace(-1, 0, 1000)]
# # masses3 = [mass for mass in numpy.logspace(0, 1, 3000)]
# # masses = numpy.concatenate((masses1, masses2, masses3))

# # xHs = numpy.linspace(-3,2, 5000)


# # Try to load matplotlib.
# try: import matplotlib.pyplot as pyplot
# except: pyplot = None
# colors = ["red", "orange", "green", "blue", "indigo"]

# # types = ["solid", "solid", "solid", "solid"]

# # colors = ["skyblue", "darkcyan", "red", "brown", "green", "limegreen"]

# # colors = ["black"]
# types = ["solid"]

# # Loop over all the models.
# #for name, model in models.items():

#     # If possible, initialize the plot.
# if pyplot:
#     pyplot.rcParams["figure.figsize"] = (8,4)
#     # pyplot.subplots_adjust(left=0, bottom=0)
#     fig, ax = pyplot.subplots()
#     icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

#     # Loop over the channels.
# for name in names:
    
#     # model = darkcast.Model(name)
#         # Calculate the branching fraction for the model and channel
#         # as a function of mass.
#     # bfracs = [model.bfrac("hadrons", mass, 0) for mass in masses]
    
#     # bfracs = [model.bfrac("hadrons", 1, xH) for xH in xHs]
    
#     for mass in [[0.25, 0.5, 0.75], [0.5, 0.5, 0.75], [0.75, 0.75, 0.75], [0.75, 0.75, 2], [0.75, 2, 2]]:
#         bfracs = []
#         for M_Z in M_Zs:
#             m1, m2, m3 = mass[0]*M_Z/2, mass[1]*M_Z/2, mass[2]*M_Z/2
#             model = darkcast.Model(name, m1, m2, m3)
#             bfracs.append(model.bfrac("rhns", M_Z, xH)/model.bfrac("visible", M_Z, xH))

#         # Additionally, the width can be calculated using the 'width'
#         # method and the same channels as for 'bfrac'.
#         #
#         # widths = [model.width(channel, mass, g = 1) for mass in masses]

#         # Save the branching fraction to a text file.
#     # txt = open("bfrac_%s_%s.txt" % (name, label.replace("$", "")), "w")
#     # for mass, bfrac in zip(masses, bfracs):
#     #     txt.write("%11.4e %11.4e\n" % (mass, bfrac))
#     # txt.close()
            
#         # Plot. The 'latex' utility converts commonly used symbols to
#         # LaTeX, e.g. 'pi0' -> '\pi^{0}'.
#         if pyplot:
#             color, linestyle = next(icolor), next(itype)
#         # else: color, linestyle = labels[label], labels[label]; label = None
#         # ax.plot(masses, bfracs, label = darkcast.utils.latex(name),
#         #         color = color, linestyle = linestyle)
#             label = r"$m_1$ = " + str(mass[0]) + "$M_{Z\prime}$, $m_2$ = " + str(mass[1]) + "$M_{Z\prime}$, $m_3$ = " + str(mass[2])+ "$M_{Z\prime}$"
#             ax.plot(M_Zs, bfracs, label = label,
#                     color = color, linestyle = linestyle)
#         # ax.plot(xHs, bfracs, label = darkcast.utils.latex(name),
#         #         color = color, linestyle = linestyle)
        
#         # label_x = masses[-50]  # Adjust the x-position of the label
#         # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
#         # pyplot.text(label_x, label_y, name)
#     # Save the plot.
    
# if pyplot:
#     title = r"$x_H$ = " + str(xH) + r", $x_\Phi=1$"
#     legend = ax.legend(loc = "lower left", fontsize = 8)
#     ax.set_xlim([1e-2, 10])
#     ax.set_ylim([1e-3, 1])
#     ax.semilogx()
#     ax.semilogy()
#     ax.set_xlabel("mass [GeV]")
#     # ax.set_ylabel("branching ratio")
#     # ax.set_ylabel("decay width")
#     ax.set_ylabel(r"$BR (Z'\rightarrow NN)/ BR (Z'\rightarrow visible)$")
#     # ax.semilogy()
#     # ax.set_title(darkcast.utils.latex(model.name))
#     # ax.set_title(r"$M_{Z'} = 3$ $GeV$")
#     ax.set_title(title)
#     #darkcast.utils.logo()
#     fig.savefig("bfrac_%s.pdf" % name)

xHs = numpy.linspace(-20, 20, 100)
MZs = numpy.logspace(-2, 1, 100)


# for MZ in MZs:
#     M1, M2, M3 = MZ/4, MZ/4, MZ/4
#     model = darkcast.Model("U1_X", m1=M1, m2=M2, m3=M3)
#     bfracs.append([model.bfrac("visible", MZ, xH) for xH in xHs])
    
# for iM,MZ in enumerate(MZs):
#     for ix,xH in enumerate(xHs):
#         xs.append(xH)
#         Ms.append(MZs[iM])
#         brs.append(numpy.exp(bfracs[iM][ix]))
    

# fig = plt.figure(figsize=(8,8))
# ax = plt.subplot(1,1,1)
# ax.semilogx()
# # h=ax.hist2d(x=Ms,y=xs,weights=brs,
# #             bins=[100,100],#range=[[tmin,tmax],[pmin,pmax]],
# #             norm=matplotlib.colors.LogNorm(vmin=1e-10, vmax=1), 
# #             cmap= "rainbow",
# # )
# Ms, xs = numpy.meshgrid(MZs, xHs)
# brs = numpy.log10(numpy.array(bfracs).T+1e-20)
# ax.contour (Ms,xs,brs, levels=[numpy.log10(0.6)]) 

for mass in [[0.25, 0.5, 0.75], [0.5, 0.5, 0.75], [0.75, 0.75, 0.75], [0.75, 0.75, 2], [0.75, 2, 2]]:
    bfracs = []
    xs = []
    Ms = []
    brs = []
    for MZ in MZs:
        M1, M2, M3 = MZ*mass[0]/2, MZ*mass[1]/2, MZ*mass[2]/2
        model = darkcast.Model("U1_X", m1=M1, m2=M2, m3=M3)
        bfracs.append([model.bfrac("rhns", MZ, xH)/model.bfrac("visible", MZ, xH) for xH in xHs])
        
    for iM,MZ in enumerate(MZs):
        for ix,xH in enumerate(xHs):
            xs.append(xH)
            Ms.append(MZs[iM])
            brs.append(numpy.exp(bfracs[iM][ix]))
    # print(bfracs)    
    title = r"$2m_1 = $"+str(mass[0])+"$M_{Z'}$, $2m_2 = $"+str(mass[1])+"$M_{Z'}$, $2m_3 = $"+str(mass[2])+"$M_{Z'}$"
    fig = plt.figure()
    ax = plt.subplot(1,1,1)
    ax.set_xlabel("mass of Z' (GeV)")
    ax.set_ylabel(r"$x_H$")
    ax.semilogx()
    # h=ax.hist2d(x=Ms,y=xs,weights=brs,
    #             bins=[100,100],#range=[[tmin,tmax],[pmin,pmax]],
    #             norm=matplotlib.colors.LogNorm(vmin=1e-10, vmax=1), 
    #             cmap= "rainbow",
    # )
    Ms, xs = numpy.meshgrid(MZs, xHs)
    brs = numpy.log10(numpy.array(bfracs).T+1e-20)
    ax.contour (Ms,xs,brs, cmap="Reds")#, levels=[numpy.log10(0.1)]) 
    ax.set_title(title)#(darkcast.utils.latex(title))