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
# import sys, os, inspect, itertools, numpy
# sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
#                 inspect.getfile(inspect.currentframe()))), "../../"))

# # Import the Darkcast module.
# import darkcast
# import matplotlib.pyplot as plt



# import collections
# channels = collections.OrderedDict([
#         # Entries take the form (key, value).
        
#         # All available fundamental fermion pairs.
#         # ("$e_e$",                 "e_e"),
#         # ("$mu_mu$",               "mu_mu"),
#         # ("$tau_tau$",             "tau_tau"),
#         # ("$nue_nue$",             "nue_nue"),
#         # ("$numu_numu$",           "numu_numu"),
#         # ("$nutau_nutau$",         "nutau_nutau"),
#         # ("$d_d$",                 "d_d"), # Included in exclusive hadrons.
#         # ("$u_u$",                 "u_u"), # Included in exclusive hadrons.
#         # ("$s_s$",                 "s_s"), # Included in exclusive hadrons.
#         # ("$c_c$",                 "c_c"),
#         # ("$b_b$",                 "b_b"),
#         # ("$t_t$",                 "t_t"),
        
#         # Combine charged leptons into a single channel.
#         # ("l_l",                  ["e_e", "mu_mu", "tau_tau"]),
#         (r"$\sum Leptons$",                  ["e_e", "mu_mu", "tau_tau"]),
        
#         # ("vis",                  ["e_e", "mu_mu", "tau_tau", "hadrons"])

#         # Combine quarks into a single channel.
#         # ("q_q",                   ["u_u", "d_d", "s_s", "t_t", "c_c", "b_b"]),



#         # Combine Neutrinos into a single channel.
#         # ("$nu_nu$",               ["nue_nue", "numu_numu", "nutau_nutau"]),
                
#         # All available exclusive hadronic states.
#         #("$pi+_pi-$",             "pi+_pi-"),
#         #("$pi+_pi-_pi+_pi-$",     "pi+_pi-_pi+_pi-"),
#         #("$pi+_pi-_pi0_pi0$",     "pi+_pi-_pi0_pi0"),
#         #("$pi+_pi-_pi0$",         "pi+_pi-_pi0"),
#         #("$pi0_gamma$",           "pi0_gamma"),
#         #("$K_K$",                 "K_K"),
#         #("$K_K_pi$",              "K_K_pi"),
#         #("other hadrons",         "other"),
        
#         # Alias for all exclusive hadronic final states above.
#         ("Hadrons",                ["hadrons"]),

#         # Alias for all visible final states, e.g. everything above
#         # except 'd_d', 'u_u', and 's_s'.
#         ("Visible",                "visible"),


#         # Combine Right Handed Neutrinos into a single channel.
#         # ("$N_N$",               ["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"]),   
#         (r"$\sum N_i N_i$",               ["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"]), 
        
#         (r"$\sum\nu_i\nu_i$",               ["nue_nue", "numu_numu", "nutau_nutau"]),
#         # ("$Ne_Ne$",             "Ne_Ne"),
#         # ("$Nmu_Nmu$",           "Nmu_Nmu"),
#         # ("$Ntau_Ntau$",         "Ntau_Ntau"),
#         # All invisible final states.
#         #("invisible",              "invisible"),
        
#         # All possible final states to consider when calculating the
#         # total width. Typically 'visible' and 'invisible' but this
#         # can be specified by the user when creating the model with
#         # the 'states' variable, e.g. darkcast.Model('dark_photon',
#         # states = ['e_e', 'mu_mu']).
#         # ("total",                  "total"),
#         ])

# xH = -1.2
# # mass = 1
# def pos(x, name):
#     if name=="U1_X" and (x==2): return "center left"
#     elif (x==2 or x== -1.2 or  x==-2) and name=="U1_X_phi4": return "center left"
#     else: return "lower left" 

# masses = numpy.logspace(-4, 1, 1500)
# # masses = numpy.linspace(0, 2, 1000)
# # xHs = numpy.linspace(-2, 2, 1000)



# # Try to load matplotlib.
# try: import matplotlib.pyplot as pyplot
# except: pyplot = None
# colors = ["blue", "green", "red", "orange", "purple"]#["red", "green", "brown", "blue", "black", "red", "blue", "purple", 
#           # "magenta", "orange"]
# # colors = ["red", "blue", "green"#"u_u", "d_d", "t_t",]
# types = ["solid", "solid", "solid", "solid", "solid"]#, "solid", "dotted", "solid",  "dotted", "solid", "dotted", "dotted",
#          # "dotted", "dotted"]

# #%%    
# # model = darkcast.Model("U1_X", m1 = 1000, m2=1000, m3=1000)
# name = "U1_X"
# model = darkcast.Model("U1_X", m1 = 1/3, m2= 1/3, m3= 1000)


# if pyplot:
#     pyplot.rcParams["figure.figsize"] = (10,6)
#     # pyplot.subplots_adjust(left=0, bottom=0)
#     # fig, ax = pyplot.subplots()
#     icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

#     # Loop over the channels.
# for label, channel in channels.items():
#         # Calculate the branching fraction for the model and channel
#         # as a function of mass.
#     bfracs = []
#     for mass in masses:
#         bfrac = model.bfrac(channel, mass, xH)
#         bfracs.append(bfrac)
#     # bfracs = []
#     # for xH in xHs:
#     #     bfrac = model.bfrac(channel, mass, xH)
#     #     bfracs.append(bfrac)
#     # if channel == "l_l": #in ["e_e", "mu_mu", "tau_tau"]:
#     #     bfracs = [model.bfrac(channel, 1, xH)/3 for xH in xHs]
#     # elif channel == "q_q": #in ["t_t", "u_u", "d_d", "s_s", "c_c", "b_b"]:
#     #     bfracs = [model.bfrac(channel, 1, xH)/6 for xH in xHs]
#     # else:
#         # bfracs = [model.bfrac(channel, 1, xH) for xH in xHs]
    
# ############### xfs are ok, but bfracs is taking value of the first one only


#         # Additionally, the width can be calculated using the 'width'
#         # method and the same channels as for 'bfrac'.
#         #
#         # widths = [model.width(channel, mass, g = 1) for mass in masses]

#         # Save the branching fraction to a text file.
#     txt = open("bfrac_%s_%s.txt" % (name, label.replace("$", "")), "w")
#     for mass, bfrac in zip(masses, bfracs):
#         txt.write("%11.4e %11.4e\n" % (mass, bfrac))
#     # for xH, bfrac in zip(xHs, bfracs):
#     #     txt.write("%11.4e %11.4e\n" % (xH, bfrac))
#     txt.close()            
#         # Plot. The 'latex' utility converts commonly used symbols to
#         # LaTeX, e.g. 'pi0' -> '\pi^{0}'.
#     if pyplot:
#         if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
#         else: color, linestyle = labels[label], labels[label]; label = None
#         if sum(bfracs)==0:
#             plt.plot(masses, bfracs,
#                     color = color, linestyle = linestyle)
#         else:
#             plt.plot(masses, bfracs, label = label,
#                     color = color, linestyle = linestyle)
#         # plt.plot(xHs, bfracs, label = label,
#                 # color = color, linestyle = linestyle)
#         # label_x = masses[-50]  # Adjust the x-position of the label
#         # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
#         # pyplot.text(label_x, label_y, label)
#     # Save the plot.


# if pyplot:
#     title = r"$U_1(X): x_H$ = " + str(xH) 
#     # title = r"$U_1(X):$ $M_{Z'}$ = " + str(mass) + " GeV"
#     legend = plt.legend(loc = pos(xH, name), fontsize = 16, ncol=2)

# plt.xlim([1e-3, 10])
# plt.ylim([1e-2, 1.5])
# # plt.xlim([-2, 2])
# # plt.ylim([0, 1])
# plt.semilogx()
# plt.semilogy()
# plt.xticks(fontsize=21)
# plt.yticks(fontsize=21)
# # plt.text(0.015, 8e-4, title, fontsize=20)
# plt.xlabel(r"$M_{Z^\prime}$ [GeV]", fontsize=20)
# # plt.xlabel(r"$x_H$", fontsize=25)
# plt.ylabel(r"BR($Z' \to X $)", fontsize=20)
# plt.title(title, y=0.9,  fontsize=18, loc="center")
# #darkcast.utils.logo()
# # plt.savefig("bfrac_%s.pdf" % name) 
# plt.savefig("/home/souvik/codes/FORESEE_fig/bfrac/U1X_xH_"+str(xH)+".jpeg", bbox_inches='tight', dpi=300)   

# plt.show()

# #%%

# # model = darkcast.Model("U1_X", m1 = 1000, m2=1000, m3=1000)
# name = "U1_X_phi4"
# model = darkcast.Model("U1_X_phi4", m1 = 1/3, m2= 1/3, m3= 1000)



# if pyplot:
#     pyplot.rcParams["figure.figsize"] = (10,6)
#     # pyplot.subplots_adjust(left=0, bottom=0)
#     # fig, ax = pyplot.subplots()
#     icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

#     # Loop over the channels.
# for label, channel in channels.items():
#         # Calculate the branching fraction for the model and channel
#         # as a function of mass.
#     bfracs = []
#     for mass in masses:
#         bfrac = model.bfrac(channel, mass, xH)
#         bfracs.append(bfrac)
#     # bfracs = []
#     # for xH in xHs:
#     #     bfrac = model.bfrac(channel, mass, xH)
#     #     bfracs.append(bfrac)
#     # if channel == "l_l": #in ["e_e", "mu_mu", "tau_tau"]:
#     #     bfracs = [model.bfrac(channel, 1, xH)/3 for xH in xHs]
#     # elif channel == "q_q": #in ["t_t", "u_u", "d_d", "s_s", "c_c", "b_b"]:
#     #     bfracs = [model.bfrac(channel, 1, xH)/6 for xH in xHs]
#     # else:
#         # bfracs = [model.bfrac(channel, 1, xH) for xH in xHs]
    
# ############### xfs are ok, but bfracs is taking value of the first one only


#         # Additionally, the width can be calculated using the 'width'
#         # method and the same channels as for 'bfrac'.
#         #
#         # widths = [model.width(channel, mass, g = 1) for mass in masses]

#         # Save the branching fraction to a text file.
#     txt = open("bfrac_%s_%s.txt" % (name, label.replace("$", "")), "w")
#     for mass, bfrac in zip(masses, bfracs):
#         txt.write("%11.4e %11.4e\n" % (mass, bfrac))
#     # for xH, bfrac in zip(xHs, bfracs):
#     #     txt.write("%11.4e %11.4e\n" % (xH, bfrac))
#     txt.close()            
#         # Plot. The 'latex' utility converts commonly used symbols to
#         # LaTeX, e.g. 'pi0' -> '\pi^{0}'.
#     if pyplot:
#         if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
#         else: color, linestyle = labels[label], labels[label]; label = None
#         if sum(bfracs)==0:
#             plt.plot(masses, bfracs,
#                     color = color, linestyle = linestyle)
#         else:
#             plt.plot(masses, bfracs, label = label,
#                     color = color, linestyle = linestyle)
#         # plt.plot(xHs, bfracs, label = label,
#         #         color = color, linestyle = linestyle)
#         # label_x = masses[-50]  # Adjust the x-position of the label
#         # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
#         # pyplot.text(label_x, label_y, label)
#     # Save the plot.


# if pyplot:
#     title = r"Alternative: $x_H$ = " + str(xH) 
#     # title = r"Alternative: $M_{Z'}$ = " + str(mass) + " GeV"
#     legend = plt.legend(loc = pos(xH, name), fontsize = 16, ncol=2)
    

# plt.xlim([1e-3, 10])
# plt.ylim([1e-2, 1.5])
# # plt.xlim([-2, 2])
# # plt.ylim([0, 1])
# plt.semilogx()
# plt.semilogy()
# plt.xticks(fontsize=21)
# plt.yticks(fontsize=21)
# # plt.text(0.015, 8e-4, title, fontsize=20)
# plt.xlabel(r"$M_{Z^\prime}$ [GeV]", fontsize=20)
# # plt.xlabel(r"$x_H$", fontsize=25)
# plt.ylabel(r"BR($Z'\to  X$)", fontsize=20)
# plt.title(title, y=0.93, fontsize=18, loc="center")
# #darkcast.utils.logo()
# # fig.savefig("bfrac_%s.pdf" % name)
# plt.savefig("/home/souvik/codes/FORESEE_fig/bfrac/454_xH_"+str(xH)+".jpeg", bbox_inches='tight', dpi=300) 
# plt.show()

#%%


import sys, os, inspect, itertools, numpy
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "../../"))

# Import the Darkcast module.
import darkcast
import matplotlib.pyplot as plt



import collections
channels = collections.OrderedDict([
        # Entries take the form (key, value).
        
        # All available fundamental fermion pairs.
        # ("$e_e$",                 "e_e"),
        # ("$mu_mu$",               "mu_mu"),
        # ("$tau_tau$",             "tau_tau"),
        # ("$nue_nue$",             "nue_nue"),
        # ("$numu_numu$",           "numu_numu"),
        # ("$nutau_nutau$",         "nutau_nutau"),
        # ("$d_d$",                 "d_d"), # Included in exclusive hadrons.
        # ("$u_u$",                 "u_u"), # Included in exclusive hadrons.
        # ("$s_s$",                 "s_s"), # Included in exclusive hadrons.
        # ("$c_c$",                 "c_c"),
        # ("$b_b$",                 "b_b"),
        # ("$t_t$",                 "t_t"),
        
        # Combine charged leptons into a single channel.
        # ("l_l",                  ["e_e", "mu_mu", "tau_tau"]),
        (r"$\sum Leptons$",                  ["e_e", "mu_mu", "tau_tau"]),
        
        # ("vis",                  ["e_e", "mu_mu", "tau_tau", "hadrons"])

        # Combine quarks into a single channel.
        # ("q_q",                   ["u_u", "d_d", "s_s", "t_t", "c_c", "b_b"]),



        # Combine Neutrinos into a single channel.
        # ("$nu_nu$",               ["nue_nue", "numu_numu", "nutau_nutau"]),
        (r"$\sum\nu_i\nu_i$",               ["nue_nue", "numu_numu", "nutau_nutau"]),
        
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
        ("Hadrons",                ["hadrons"]),

        # Alias for all visible final states, e.g. everything above
        # except 'd_d', 'u_u', and 's_s'.
        ("Visible",                "visible"),


        # Combine Right Handed Neutrinos into a single channel.
        # ("$N_N$",               ["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"]),   
        (r"$\sum N_i N_i$",               ["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"]),  
        # ("$Ne_Ne$",             "Ne_Ne"),
        # ("$Nmu_Nmu$",           "Nmu_Nmu"),
        # ("$Ntau_Ntau$",         "Ntau_Ntau"),
        # All invisible final states.
        #("invisible",              "invisible"),
        
        # All possible final states to consider when calculating the
        # total width. Typically 'visible' and 'invisible' but this
        # can be specified by the user when creating the model with
        # the 'states' variable, e.g. darkcast.Model('dark_photon',
        # states = ['e_e', 'mu_mu']).
        # ("total",                  "total"),
        ])

# xH = -2
mass = 1
def pos(x, name):
    if name=="U1_X_phi4"  and mass==0.1: return "center left"
    return "upper right" 

# masses = numpy.logspace(-4, 1, 1500)
# masses = numpy.linspace(0, 2, 1000)
xHs = numpy.linspace(-2, 2, 1000)



# Try to load matplotlib.
try: import matplotlib.pyplot as pyplot
except: pyplot = None
colors = ["blue", "purple", "green", "red", "orange"]#["red", "green", "brown", "blue", "black", "red", "blue", "purple", 
          # "magenta", "orange"]
# colors = ["red", "blue", "green"#"u_u", "d_d", "t_t",]
types = ["solid", "solid", "solid", "solid", "solid"]#, "solid", "dotted", "solid",  "dotted", "solid", "dotted", "dotted",
          # "dotted", "dotted"]

#%%    
# model = darkcast.Model("U1_X", m1 = 1000, m2=1000, m3=1000)
name = "U1_X"
model = darkcast.Model("U1_X", m1 = 1/3, m2= 1/3, m3= 1000)


if pyplot:
    pyplot.rcParams["figure.figsize"] = (10,6)
    # pyplot.subplots_adjust(left=0, bottom=0)
    # fig, ax = pyplot.subplots()
    icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

    # Loop over the channels.
for label, channel in channels.items():
        # Calculate the branching fraction for the model and channel
        # as a function of mass.
    # bfracs = []
    # for mass in masses:
    #     bfrac = model.bfrac(channel, mass, xH)
    #     bfracs.append(bfrac)
    bfracs = []
    for xH in xHs:
        bfrac = model.bfrac(channel, mass, xH)
        bfracs.append(bfrac)
    # if channel == "l_l": #in ["e_e", "mu_mu", "tau_tau"]:
    #     bfracs = [model.bfrac(channel, 1, xH)/3 for xH in xHs]
    # elif channel == "q_q": #in ["t_t", "u_u", "d_d", "s_s", "c_c", "b_b"]:
    #     bfracs = [model.bfrac(channel, 1, xH)/6 for xH in xHs]
    # else:
        # bfracs = [model.bfrac(channel, 1, xH) for xH in xHs]
    
############### xfs are ok, but bfracs is taking value of the first one only


        # Additionally, the width can be calculated using the 'width'
        # method and the same channels as for 'bfrac'.
        #
        # widths = [model.width(channel, mass, g = 1) for mass in masses]

        # Save the branching fraction to a text file.
    txt = open("bfrac_%s_%s.txt" % (name, label.replace("$", "")), "w")
    # for mass, bfrac in zip(masses, bfracs):
    #     txt.write("%11.4e %11.4e\n" % (mass, bfrac))
    for xH, bfrac in zip(xHs, bfracs):
        txt.write("%11.4e %11.4e\n" % (xH, bfrac))
    txt.close()            
        # Plot. The 'latex' utility converts commonly used symbols to
        # LaTeX, e.g. 'pi0' -> '\pi^{0}'.
    if pyplot:
        if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
        else: color, linestyle = labels[label], labels[label]; label = None
        # if sum(bfracs)==0:
        #     plt.plot(masses, bfracs,
        #             color = color, linestyle = linestyle)
        # else:
        #     plt.plot(masses, bfracs, label = label,
        #             color = color, linestyle = linestyle)
        plt.plot(xHs, bfracs, label = label,
                color = color, linestyle = linestyle)
        # label_x = masses[-50]  # Adjust the x-position of the label
        # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
        # pyplot.text(label_x, label_y, label)
    # Save the plot.


if pyplot:
    # title = r"$U(1)_X: x_H$ = " + str(xH) 
    title = r"$U(1)_X:$ $M_{Z'}$ = " + str(mass) + " GeV"
    legend = plt.legend(loc = pos(xH, name), fontsize = 16, ncol=3)

# plt.xlim([1e-3, 10])
# plt.ylim([1e-2, 1.5])
plt.xlim([-2, 2])
plt.ylim([0, 1])
# plt.semilogx()
# plt.semilogy()
plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
# plt.text(0.015, 8e-4, title, fontsize=20)
# plt.xlabel(r"$M_{Z^\prime}$ [GeV]", fontsize=20)
plt.xlabel(r"$x_H$", fontsize=25)
plt.ylabel(r"BR($Z' \to X $)", fontsize=20)
plt.title(title,  y=0.65, x=0.5,  fontsize=18, loc="center")
#darkcast.utils.logo()
# fig.savefig("bfrac_%s.pdf" % name)    
plt.savefig("/home/souvik/codes/FORESEE_fig/bfrac/U1X_mass_"+str(mass)+".jpeg", bbox_inches='tight', dpi=300) 
plt.show()

#%%

# model = darkcast.Model("U1_X", m1 = 1000, m2=1000, m3=1000)
name = "U1_X_phi4"
model = darkcast.Model("U1_X_phi4", m1 = 1/3, m2= 1/3, m3= 1000)



if pyplot:
    pyplot.rcParams["figure.figsize"] = (10,6)
    # pyplot.subplots_adjust(left=0, bottom=0)
    # fig, ax = pyplot.subplots()
    icolor, itype, labels = itertools.cycle(colors), itertools.cycle(types), {}

    # Loop over the channels.
for label, channel in channels.items():
        # Calculate the branching fraction for the model and channel
        # as a function of mass.
    # bfracs = []
    # for mass in masses:
    #     bfrac = model.bfrac(channel, mass, xH)
    #     bfracs.append(bfrac)
    bfracs = []
    for xH in xHs:
        bfrac = model.bfrac(channel, mass, xH)
        bfracs.append(bfrac)
    # if channel == "l_l": #in ["e_e", "mu_mu", "tau_tau"]:
    #     bfracs = [model.bfrac(channel, 1, xH)/3 for xH in xHs]
    # elif channel == "q_q": #in ["t_t", "u_u", "d_d", "s_s", "c_c", "b_b"]:
    #     bfracs = [model.bfrac(channel, 1, xH)/6 for xH in xHs]
    # else:
        # bfracs = [model.bfrac(channel, 1, xH) for xH in xHs]
    
############### xfs are ok, but bfracs is taking value of the first one only


        # Additionally, the width can be calculated using the 'width'
        # method and the same channels as for 'bfrac'.
        #
        # widths = [model.width(channel, mass, g = 1) for mass in masses]

        # Save the branching fraction to a text file.
    txt = open("bfrac_%s_%s.txt" % (name, label.replace("$", "")), "w")
    # for mass, bfrac in zip(masses, bfracs):
    #     txt.write("%11.4e %11.4e\n" % (mass, bfrac))
    for xH, bfrac in zip(xHs, bfracs):
        txt.write("%11.4e %11.4e\n" % (xH, bfrac))
    txt.close()            
        # Plot. The 'latex' utility converts commonly used symbols to
        # LaTeX, e.g. 'pi0' -> '\pi^{0}'.
    if pyplot:
        if not label in labels: color, linestyle = next(icolor), next(itype); labels[label] = color
        else: color, linestyle = labels[label], labels[label]; label = None
        # if sum(bfracs)==0:
        #     plt.plot(masses, bfracs,
        #             color = color, linestyle = linestyle)
        # else:
        #     plt.plot(masses, bfracs, label = label,
        #             color = color, linestyle = linestyle)
        plt.plot(xHs, bfracs, label = label,
                color = color, linestyle = linestyle)
        # label_x = masses[-50]  # Adjust the x-position of the label
        # label_y = bfracs[-50]  # Use the y-coordinate of the last point of the curve
        # pyplot.text(label_x, label_y, label)
    # Save the plot.


if pyplot:
    # title = r"alternative: $x_H$ = " + str(xH) 
    title = r"Alternative: $M_{Z'}$ = " + str(mass) + " GeV"
    legend = plt.legend(loc = pos(xH, name), fontsize = 16, ncol=3)
    

# plt.xlim([1e-3, 10])
# plt.ylim([1e-2, 1.5])
plt.xlim([-2, 2])
plt.ylim([0, 1])
# plt.semilogx()
# plt.semilogy()
plt.xticks(fontsize=21)
plt.yticks(fontsize=21)
# plt.text(0.015, 8e-4, title, fontsize=20)
# plt.xlabel(r"$M_{Z^\prime}$ [GeV]", fontsize=20)
plt.xlabel(r"$x_H$", fontsize=25)
plt.ylabel(r"BR($Z'\to  X$)", fontsize=20)
plt.title(title, y=0.7, x=0.75, fontsize=18, loc="center")
#darkcast.utils.logo()
# fig.savefig("bfrac_%s.pdf" % name)
plt.savefig("/home/souvik/codes/FORESEE_fig/bfrac/454_mass_"+str(mass)+".jpeg", bbox_inches='tight', dpi=300) 
plt.show()