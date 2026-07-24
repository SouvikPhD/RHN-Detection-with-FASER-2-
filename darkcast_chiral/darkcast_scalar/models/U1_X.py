#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:56:58 2023

@author: daslinux
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:51:02 2023

@author: daslinux
"""

# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2021 Philip Ilten, Yotam Soreq, Mike Williams, and Wei Xue.

# Define the fermion couplings.
import sys, os, inspect, itertools
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "../../"))


xP=1




xfs = {
    "e":       (lambda m, xH: -xP-1/2*xH, lambda m, xH: -xP-xH),
    "mu":      (lambda m, xH: -xP-1/2*xH, lambda m, xH: -xP-xH),
    "tau":     (lambda m, xH: -xP-1/2*xH, lambda m, xH: -xP-xH),
    "nue":     (lambda m, xH: -xP-1/2*xH, lambda m, xH: 0),
    "numu":    (lambda m, xH: -xP-1/2*xH, lambda m, xH: 0),
    "nutau":   (lambda m, xH: -xP-1/2*xH, lambda m, xH: 0),
    "d":       (lambda m, xH: 1/3*xP+1/6*xH, lambda m, xH: 1/3*xP-1/3*xH),
    "u":       (lambda m, xH: 1/3*xP+1/6*xH, lambda m, xH: 1/3*xP+2/3*xH),
    "s":       (lambda m, xH: 1/3*xP+1/6*xH, lambda m, xH: 1/3*xP-1/3*xH),
    "c":       (lambda m, xH: 1/3*xP+1/6*xH, lambda m, xH: 1/3*xP+2/3*xH),
    "b":       (lambda m, xH: 1/3*xP+1/6*xH, lambda m, xH: 1/3*xP-1/3*xH),
    "t":       (lambda m, xH: 1/3*xP+1/6*xH, lambda m, xH: 1/3*xP+2/3*xH),
    "Ne":      (lambda m, xH: 0, lambda m, xH: -xP),
    "Nmu":     (lambda m, xH: 0, lambda m, xH: -xP),
    "Ntau":    (lambda m, xH: 0, lambda m, xH: -xP),
    }




