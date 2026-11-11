#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:20:04 2023

@author: daslinux
"""

# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2021 Philip Ilten, Yotam Soreq, Mike Williams, and Wei Xue.

# Define the fermion couplings.
import sys, os, inspect, itertools
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "../../"))

import darkcast

from darkcast.models import U1_X as x
xP=x.xP
xH=x.xH



xfs = {
    "e":      (0,sum([-xP-1/2*xH,-xP-xH])/2),
    "mu":     (0,sum([-xP-1/2*xH,-xP-xH])/2),
    "tau":    (0,sum([-xP-1/2*xH,-xP-xH])/2),
    "nue":    (0,sum([-xP-1/2*xH,0])/2),
    "numu":   (0,sum([-xP-1/2*xH,0])/2),
    "nutau":  (0,sum([-xP-1/2*xH,0])/2),
    "d":       (0,sum([1/3*xP+1/6*xH,1/3*xP-1/3*xH])/2),
    "u":       (0,sum([1/3*xP+1/6*xH,1/3*xP+2/3*xH])/2),
    "s":       (0,sum([1/3*xP+1/6*xH,1/3*xP-1/3*xH])/2),
    "c":       (0,sum([1/3*xP+1/6*xH,1/3*xP+2/3*xH])/2),
    "b":       (0,sum([1/3*xP+1/6*xH,1/3*xP-1/3*xH])/2),
    "t":       (0,sum([1/3*xP+1/6*xH,1/3*xP+2/3*xH])/2),
    }
