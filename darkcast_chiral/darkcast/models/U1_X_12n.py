#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 23:05:46 2025

@author: souvik
"""

import sys, os, inspect, itertools
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "../../"))


xP=1
xH=-1.2




xfs = {
    "e":       (-xP-1/2*xH, -xP-xH),
    "mu":      (-xP-1/2*xH, -xP-xH),
    "tau":     (-xP-1/2*xH, -xP-xH),
    "nue":     (-xP-1/2*xH, 0),
    "numu":    (-xP-1/2*xH, 0),
    "nutau":   (-xP-1/2*xH, 0),
    "d":       (1/3*xP+1/6*xH, 1/3*xP-1/3*xH),
    "u":       (1/3*xP+1/6*xH, 1/3*xP+2/3*xH),
    "s":       (1/3*xP+1/6*xH, 1/3*xP-1/3*xH),
    "c":       (1/3*xP+1/6*xH, 1/3*xP+2/3*xH),
    "b":       (1/3*xP+1/6*xH, 1/3*xP-1/3*xH),
    "t":       (1/3*xP+1/6*xH, 1/3*xP+2/3*xH),
    "Ne":      (0, -xP),
    "Nmu":     (0, -xP),
    "Ntau":    (0, -xP),
    }