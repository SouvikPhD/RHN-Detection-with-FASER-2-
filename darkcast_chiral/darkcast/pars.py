# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
"""
This module contains all the relevant parameters used by
DarkCast. They can be simply redefined by importing the module and
changing the relevant parameter, e.g. 'import darkcast' and
'darkcast.pars.ge = 1'. The following float value parameters are
defined.

c:    speed of light (m/s).
hbar: reduced Planck's constant (s/GeV).
ge:   electromagnetic coupling (unitless).
bw:   flag for which Breit-Wigner type to use, either 'fix' or 'run'.
cphi: unknown phase factor for hadronic axial currents (unitless).

The remaining parameters are dictionaries.

mfs:  fermion masses (GeV).
cfs:  fermion color factors (unitless).

tms:  on-diagonal U(3) meson generators from equation A.1 (unitless). For
      convenience the photon U(3) quark charge matrix, equation 2.8, is
      also included.
rvs:  pre-factors for each vector contribution R_X^V from equation 2.18
      (unitless).

mms:  needed meson masses (GeV). 
wms:  meson widths (GeV).
dms:  meson branching fractions and final state masses (GeV), 
      e.g. [BR, m1, m2]. These are used for the running Breit-Wigners.

rfs:  interpolation grids for each final state R_mu^f from equation 2.15
      split by individual meson contributions, including interference 
      (unitless). These grids are stored in the 'data' directory.
sfs:  interpolation grids for the light and strange spectral functions
      of the axial hadronic tau decay (unitless). These grids are
      stored in the 'data' directory.
pff:  proton form factor coefficient (unitless).
pms:  proton form factor masses (axial, vector) (GeV).
piff: pion form factor coefficient (unitless).
"""
import math
from . import utils

###############################################################################
# Constants.
c    = 2.99792458e8     # Speed of light (m/s).
hbar = 6.58211951e-25   # Reduced Planck's constant (GeV s).
ge   = 3.02822e-1       # Electromagnetic coupling (unitless).
mw   = 8.0379e1         # Mass of the W (GeV).
mz   = 9.11876e1        # Mass of the Z (GeV).
bw   = "run"            # Flag for Breit-Wigner type, 'fix' or 'run'.
cphi = -0.66            # Interference phase factor for axial couplings.

###############################################################################
# Fermion masses (GeV).
# mfs = {
#     "e":      5.110e-04,
#     "mu":     0.10566,
#     "tau":    1.77682,
#     "nue":    0,
#     "numu":   0,
#     "nutau":  0,
#     "d":      0.33,
#     "u":      0.33,
#     "s":      0.5,
#     "c":      1.5,
#     "b":      4.8,
#     "t":      171.0
#     }

mfs = {
    "e":      0.51099895e-3, 
    "mu":     0.1056583755,
    "tau":    1.77693, 
    "nue":    0,
    "numu":   0,
    "nutau":  0,
    "d":      4.7e-3, 
    "u":      2.16e-3, 
    "s":      93.5e-3, 
    "c":      1.273, 
    "b":      4.183,
    "t":      172.56
    }

# mfs = {
#     "e":      0.510998955e-3,
#     "mu":     0.1056583745,
#     "tau":    1.77686, 
#     "nue":    0,
#     "numu":   0,
#     "nutau":  0,
#     "d":      4.67e-3, 
#     "u":      2.16e-3, 
#     "s":      1.27, #93e-3, 
#     "c":      1.27, 
#     "b":      4.18,
#     "t":      173.1
#     }

###############################################################################
# Fermion color factors (unitless).
cfs = {
    "e":      1.,
    "mu":     1.,
    "tau":    1.,
    "nue":    1.,
    "numu":   1.,
    "nutau":  1.,
    "d":      3.,
    "u":      3.,
    "s":      3.,
    "c":      3.,
    "b":      3.,
    "t":      3.
    }

###############################################################################
# On-diagonal U(3) meson generators from equation A.1 (unitless). For
# convenience the photon U(3) quark charge matrix, equation 2.8, is
# also included.
tms = {
    "gamma": [t/3.0              for t in [2, -1, -1]],
    "rho0":  [t/2.0              for t in [1, -1,  0]],
    "pi0":   [t/2.0              for t in [1, -1,  0]],
    "omega": [t/2.0              for t in [1,  1,  0]],
    "phi":   [t/math.sqrt(2)     for t in [0,  0,  1]],
    "eta":   [t/math.sqrt(6)     for t in [1,  1, -1]],
    "eta'":  [t/(2*math.sqrt(3)) for t in [1,  1,  2]],
    "D0":    [t                  for t in [1,  0,  0]],
    "D*0":   [t                  for t in [1,  0,  0]]
    }

###############################################################################
# Pre-factors for each vector contribution R_X^V from equation 2.18
# (unitless).
rvs = {
    "rho0":  2.0,
    "omega": 6.0,
    "phi":   3.0*math.sqrt(2)
    }

###############################################################################
# Meson masses (GeV).
mms = {
    "rho0":  0.77526,
    "pi0":   0.13498,
    "omega": 0.78266,
    "phi":   1.01946,
    "eta":   0.54786,
    "K":     0.49761,
    "a1":    1.23000
    }

###############################################################################
# Resonance widths (GeV).
wms = {
    "rho0":  0.14910,
    "omega": 0.00849,
    "phi":   0.00426,
    "a1":    0.42000
}

###############################################################################
# Resonance branching fractions and final state masses (GeV), e.g. [BR, m1, m2].
dms = {
    "rho0":  [[0.9988447, 0.13957, 0.13957]],  # pi+ pi-
    "omega": [[0.8994773, 2*0.13957, 0.13498], # pi+ pi- pi0
              [0.0834941, 0.13498, 0],         # pi0 gamma
              [0.0154283, 0.13957, 0.13957]],  # pi+ pi-
    "phi":   [[0.4893042, 0.49368, 0.49368],   # K K
              [0.3422127, 0.49761, 0.49761],   # KS KL
              [0.0130981, 0.54785, 0]],        # eta gamma
    "a1":    [[2*0.3500000, 0.13957, 0.77549], # pi+ rho-
              [2*0.0725000, 0.89166, 0.49368], # K*+ K-
              [2*0.0725000, 0.89594, 0.49761], # K*bar0 K0
              [0.0100000, 0.13498, 0]]         # pi0 gamma
}

###############################################################################
# Interpolation grids for each final state R_mu^f from equation 2.15
# split by individual meson contributions, including interference (unitless).
rfs = {
    "pi+_pi-": [("rho0",)],
    "pi+_pi-_pi+_pi-": [("rho0",)],
    "pi+_pi-_pi0_pi0": [("rho0",)],
    "pi+_pi-_pi0": [("omega",), ("phi",), ("omega", "phi")],
    "pi0_gamma": [("omega",)],
    "K_K": [("phi",)],
    "K_K_pi": [("phi",)],
    "other": [("rho0",), ("omega",), ("phi",)]
    }
for rf, mesons in rfs.items():
    rfs[rf] = {meson: utils.Dataset("data/rf.%s.%s.dat" % (rf, "_".join(meson)))
               for meson in mesons}

###############################################################################
# Interpolation grids for the spectral functions of the axial hadronic tau
# decay, both light (u_d) and strange (s).
sfs = {
    "u_d": utils.Dataset("data/sf.u_d.a.dat"),
    "s":   utils.Dataset("data/sf.s.a.dat"),
    }

###############################################################################
# Proton form factor coefficient (unitless).
pff = 1.6

# Proton form factor masses (axial, vector) (GeV).
pms = [0.84, 1.01]

# Pion form factor coefficient (unitless). Ratio of axial to vector
# form factor for the pion (gamma), taken from Bay:1986kf.
piff = 0.52

# Clean up.
try: del t, rf, mesons
except: pass
