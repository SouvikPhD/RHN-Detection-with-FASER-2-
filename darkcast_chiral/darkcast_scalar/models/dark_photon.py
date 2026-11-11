# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).

# Define the fermion couplings (axial, vector).
from darkcast.pars import ge
xfs = {
    "e":     (0, -1*ge), 
    "mu":    (0, -1*ge),
    "tau":   (0, -1*ge),
    "nue":   (0,  0*ge),
    "numu":  (0,  0*ge),
    "nutau": (0,  0*ge),
    "d":     (0, -1*ge/3),
    "u":     (0,  2*ge/3),
    "s":     (0, -1*ge/3),
    "c":     (0,  2*ge/3),
    "b":     (0, -1*ge/3),
    "t":     (0,  2*ge/3)
    }
