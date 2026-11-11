# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
#
# This model is based on the results of "Solar neutrino probes of the
# muon anomalous magnetic moment in the gauged U(1)Lmu-Ltau" by
# Amaral, Cerdeno, Foldenauer, and Reid.
#
# @article{Amaral:2020tga,
#  author        = "Amaral, Dorian Warren Praia, do. and Cerdeno, David G.
#                   and Foldenauer, Patrick and Reid, Elliott",
#  title         = "{Solar neutrino probes of the muon anomalous magnetic
#                   moment in the gauged $U(1)_{L_\mu-L_\tau}$}",
#  eprint        = "2006.11225",
#  archivePrefix = "arXiv",
#  primaryClass  = "hep-ph",
#  reportNumber  = "IPPP/20/24, IFT-UAM/CSIC-20-70",
#  month         = "6",
#  year          = "2020"
# }

# One loop induced kinetic mixing from equation 7 of Amaral:2020tga,
# integrated over x. Note this differs from Bauer:2018onh where the
# quark couplings have an additional factor of 3/2.
from cmath import sqrt as csqrt, atan as catan
from math import sqrt, log, pi
from darkcast.pars import ge, mfs
def epsilon(m, m0 = mfs["mu"], m1 = mfs["tau"]):
    if m <= 0: return 1
    if 4*m0**2 == m**2 or 4*m1**2 == m**2: return 0
    return abs(ge**2/(12*pi**2)*(
        4*m*(m0 - m1)*(m0 + m1) -
        2*(m**2 + 2*m0**2)*csqrt(4*m0**2 - m**2)*
        catan(m/csqrt(4*m0**2 - m**2)) +
        2*(m**2 + 2*m1**2)*csqrt(4*m1**2 - m**2)*
        catan(m/csqrt(4*m1**2 - m**2)) -
        m**3*log(m0**2/m1**2))/m**3)

# Define the fermion couplings (axial, vector).
xfs = {
    "e":     (0,  1),
    "mu":    (0, -1),
    "tau":   (0,  lambda m: -1*epsilon(m)),
    "nue":   (0,  1),
    "numu":  (0, -1),
    "nutau": (0,  0),
    "d":     (0,  lambda m: -1*epsilon(m)/3),
    "u":     (0,  lambda m:  2*epsilon(m)/3),
    "s":     (0,  lambda m: -1*epsilon(m)/3),
    "c":     (0,  lambda m:  2*epsilon(m)/3),
    "b":     (0,  lambda m: -1*epsilon(m)/3),
    "t":     (0,  lambda m:  2*epsilon(m)/3)
    }
