# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
#
# This model is based on the results of "Light Weakly Coupled Axial Forces:
# Models, Constraints, and Projections" by Kahn, Krnjaic, Mishram-Sharma, and
# Tait.
#
# @article{Kahn:2016vjr,
#  author        = "Kahn, Yonatan and Krnjaic, Gordan and Mishra-Sharma, 
#                   Siddharth and Tait, Tim M. P.",
#  title         = "{Light Weakly Coupled Axial Forces: Models, Constraints,
#                   and Projections}",
#  eprint        = "1609.09072",
#  archivePrefix = "arXiv",
#  primaryClass  = "hep-ph",
#  reportNumber  = "FERMILAB-PUB-16-385-PPD, UCI-HEP-TR-2016-15, MITP-16-098, 
#                   PUPT-2507",
#  doi           = "10.1007/JHEP05(2017)002",
#  journal       = "JHEP",
#  volume        = "05",
#  pages         = "002",
#  year          = "2017"
# }

# Parameters defining the model.
the = 0.1  # Mixing parameter.
qhd = 0.1  # Up-type Higgs charge.
qhu = 2.   # Down-type Higgs charge.
sw2 = 0.22 # sin^2(Weinberg angle).
kap = 0.   # Muon vector coupling with respect to the electron.

# Define the fermion couplings (axial, vector). Taken from tables 2 - 4.
xfs = {
    "e":     (-0.5*qhd - 0.5*the, 0.5*qhd + the*(-0.5 + 2*sw2)),
    "mu":    (-0.5*qhd - 0.5*the, 0.5*qhd + the*(-0.5 + 2*sw2) + kap),
    "tau":   (-0.5*qhd - 0.5*the, 0.5*qhd + the*(-0.5 + 2*sw2) - kap),
    "nue":   (0.5*the,            0.5*the),
    "numu":  (0.5*(the + kap),    0.5*(the + kap)),
    "nutau": (0.5*(the - kap),    0.5*(the - kap)),
    "d":     (-0.5*qhd - 0.5*the, 0.5*qhd + the*(-0.5 + 2./3.*sw2)), 
    "u":     (-0.5*qhu + 0.5*the, 0.5*qhu + the*( 0.5 - 4./3.*sw2)), 
    "s":     (-0.5*qhd - 0.5*the, 0.5*qhd + the*(-0.5 + 2./3.*sw2)), 
    "c":     (-0.5*qhu + 0.5*the, 0.5*qhu + the*( 0.5 - 4./3.*sw2)),
    "b":     (-0.5*qhd - 0.5*the, 0.5*qhd + the*(-0.5 + 2./3.*sw2)), 
    "t":     (-0.5*qhu + 0.5*the, 0.5*qhu + the*( 0.5 - 4./3.*sw2))
    }
