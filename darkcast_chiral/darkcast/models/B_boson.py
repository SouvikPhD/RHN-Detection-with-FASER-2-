# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).

# Define the fermion couplings (axial, vector).
from darkcast.pars import ge
from math import pi
xfs = {
    "e":     (0, -ge**2/(4*pi)**2),
    "mu":    (0, -ge**2/(4*pi)**2),
    "tau":   (0, -ge**2/(4*pi)**2),
    "nue":   (0,  0),
    "numu":  (0,  0),
    "nutau": (0,  0),
    "d":     (0,  1./3),
    "u":     (0,  1./3),
    "s":     (0,  1./3),
    "c":     (0,  1./3),
    "b":     (0,  1./3),
    "t":     (0,  1./3)
    }
