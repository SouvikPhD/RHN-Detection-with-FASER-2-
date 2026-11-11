#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 01:12:06 2025

@author: souvik
"""
import numpy as np
import matplotlib
import os
from matplotlib import pyplot as plt
import math
import random
from skhep.math.vectors import LorentzVector, Vector3D
from scipy import interpolate
from matplotlib import gridspec
import sys
import os, inspect
from scipy.integrate import quad

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "/home/souvik/codes/darkcast_chiral/"))

# filename1 = "/home/souvik/codes/foresee-main/DUNE/files/hadrons/120GeV/EPOSLHC/EPOSLHC_120GeV_111.dat"

# array1 = []
# with open(filename1) as f:
#     for line in f:
#         if line[0]=="#":continue
#         words = [float(elt.strip()) for elt in line.split( )]
#         array1.append(words)

# dat1 = np.array(array1)

# print(sum(dat1.T[-1]))

# filename2 = "/home/souvik/codes/foresee-main/DUNE/files/hadrons/120GeV/EPOSLHC/EPOSLHC_120GeV_221.dat"

# array2 = []
# with open(filename2) as f:
#     for line in f:
#         if line[0]=="#":continue
#         words = [float(elt.strip()) for elt in line.split( )]
#         array2.append(words)

# dat2 = np.array(array2)

# print(sum(dat2.T[-1]))


# filename1 = "/home/souvik/codes/foresee-main/ILCBD/files/hadrons/125GeV/EPOSLHC/EPOSLHC_125GeV_111.dat"

# array1 = []
# with open(filename1) as f:
#     for line in f:
#         if line[0]=="#":continue
#         words = [float(elt.strip()) for elt in line.split( )]
#         array1.append(words)

# dat1 = np.array(array1)

# print(sum(dat1.T[-1]))

# filename2 = "/home/souvik/codes/foresee-main/ILCBD/files/hadrons/125GeV/EPOSLHC/EPOSLHC_125GeV_221.dat"

# array2 = []
# with open(filename2) as f:
#     for line in f:
#         if line[0]=="#":continue
#         words = [float(elt.strip()) for elt in line.split( )]
#         array2.append(words)

# dat2 = np.array(array2)

# print(sum(dat2.T[-1]))

# files = os.listdir("/home/souvik/codes/foresee-main/DUNE/files/120GeV/") 


# brt = []

# for filename in files:
#     array = []
#     name = "/home/souvik/codes/foresee-main/DUNE/files/120GeV/"+filename
#     with open(name) as f:
#         for line in f:
#             if line[0]=="#":continue
#             words = [float(elt.strip()) for elt in line.split( )]
#             array.append(words)

#     dat = np.array(array)

#     brt.append(sum(dat.T[-1]))
    
# print(brt)

# files = os.listdir("/home/souvik/codes/foresee-main/ILCBD/files/125GeV/") 


# brt = []

# for filename in files:
#     array = []
#     name = "/home/souvik/codes/foresee-main/ILCBD/files/125GeV/"+filename
#     with open(name) as f:
#         for line in f:
#             if line[0]=="#":continue
#             words = [float(elt.strip()) for elt in line.split( )]
#             array.append(words)

#     dat = np.array(array)

#     brt.append(sum(dat.T[-1]))
    
# print(brt)


files = os.listdir("/home/souvik/codes/foresee-main/Models/U1_slzplln_faser/model/LLP_spectra/") 

ws = []
ms = []

for filename in files:
    mass = filename.split("_")[-1].split(".npy")[0]
    ms.append(float(mass))
    th, p, w = np.load("/home/souvik/codes/foresee-main/Models/U1_slzplln_faser/model/LLP_spectra/"+filename)
    ws.append(sum(w)*1000*3000)
    
dic = {}



print(ws)