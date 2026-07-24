#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:56:26 2023

@author: daslinux
"""

# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import os, sys, inspect, math, collections, warnings
from . import utils, pars

###############################################################################
class ModelError(Exception):
    """
    Simple exception for the 'Model' class.
    """
    pass

###############################################################################
class Model:
    """
    Provides the information and methods needed to define a given
    model, e.g. 'dark_photon'.

    name: name of the model.
    xav:  flags if the model contains non-zero [axial, vector] couplings.
    xfs:  dictionary of fermion couplings (axial, vector). Each coupling is 
          a function dependent upon mass (GeV).
    q:    quark U(3) charge matrix.

    The final states for a model can be specified with the following string
    keys.

    All available fundamental fermion pairs.
    * 'e_e'
    * 'mu_mu'
    * 'tau_tau'
    * 'nue_nue'
    * 'numu_numu'
    * 'nutau_nutau'
    * 'd_d' - included in exclusive hadrons.
    * 'u_u' - included in exclusive hadrons.
    * 's_s' - included in exclusive hadrons.
    * 'c_c'
    * 'b_b'
    * 't_t'

    Three photon final state, available for vector-only models.
    * 'gamma_gamma_gamma'

    Alias for all neutrinos, i.e. 'nue_nue', 'numu_numu', 'nutau_nutau'.
    * 'neutrinos'

    Alias for all charged leptons, i.e. 'e_e', 'mu_mu', and 'tau_tau'.
    * 'leptons',

    Alias for all perturbative quark final states, i.e. 'c_c', 
    'b_b', and 't_t'.
    * 'quarks'

    All exclusive hadronic states, available for vector-only models.
    * 'pi+_pi-'
    * 'pi+_pi-_pi+_pi-'
    * 'pi+_pi-_pi0_pi0'
    * 'pi+_pi-_pi0'
    * 'pi0_gamma'
    * 'K_K'
    * 'K_K_pi'
    * 'other'

    Alias for all exclusive hadronic final states above.
    * 'hadrons'

    The dark sector final states.
    * 'dark'
        
    All invisible final states, i.e. 'neutrinos' and 'dark'.
    * 'invisible'

    Alias for all visible final states, e.g. everything above
    except 'invisible', 'd_d', 'u_u', and 's_s'.
    * 'visible'
    
    All possible final states to consider when calculating the
    total width. Typically 'visible' and 'invisible' but this
    can be specified by the user when creating the model with
    the 'states' variable, e.g. Model('dark_photon',
    states = ['e_e', 'mu_mu']).
    * 'total'
    """
    ###########################################################################
    def __init__(self, name, m1 = 0, m2 = 0, m3 = 0, states = None, dwidth = None, path = None):
        """
        Load a model, given its name.

        The model must exist in the form '<name>.py' and is searched
        for along these paths in the following order:
        (0) The current directory within the Python interpreter.
        (1) The paths defined by the environment variable 
            'DARKCAST_MODEL_PATH'.
        (2) The 'models' directory of the DarkCast package.

        Each model must contain a fermion coupling dictionary named
        'xfs', where each coupling can either be a constant, or a mass 
        dependent function.

        The list 'states' may be defined, specifying the allowed final
        states for the model, e.g. ['e_e', 'mu_mu', 'invisible',
        ...]. Only these final states are used when calculating the
        total width. If not defined, all visible and invisible final
        states are used when calculating the total width.

        Optionally, a 'dwidth' function provides the dark sector width
        for the model, given a mass and model and taking the form
        'dwidth(mass (GeV), model)'. Consequently, the dark sector
        width can be defined as a function of another width, e.g. the
        visible width. If no 'dwidth' is defined, the dark sector
        width is taken as zero. The dark sector width is assumed to be
        dependent on the square of the global coupling. See the
        example model for further details.
        
        name:   name of the model.
        states: optionally, specify the allowed final states of the model,
                see the documentation for this class for details.
        dwidth: optionally, specify the dark sector width as a function of 
                a given mass and this model.
        path:   optionally, specify the path to load the module from.
        """
        # Set the name, axial/vector configuration, and cache.
        self.name, self.xav = name, [False, False]
        self.__cache = {}
        
        self.m1, self.m2, self.m3 = m1, m2, m3

        # Import the model.
        model = utils.envimport(name, [path] if path else (
            [""] + utils.envpaths("MODEL", "models")))

        # Load the model's fermion couplings (axial, vector).
        self.xfs = {}
        for f in pars.mfs:
            xf = [0., 0.]
            for i in [0, 1]:
                try:
                    float(model.xfs[f][i])
                    xf[i] = lambda m, f = f, i = i: float(model.xfs[f][i])
                    if float(model.xfs[f][i]) != 0: self.xav[i] = True
                except: 
                    try:
                        xf[i] = model.xfs[f][i]
                        self.xav[i] = True
                    except: raise ModelError(
                        "Error loading '%s' coupling from '%s'." % (f, name))
            self.xfs[f] = tuple(xf)

        # Load the model's dark sector width function.
        try: self.__dwidth = dwidth if dwidth != None else model.dwidth
        except: self.__dwidth = lambda m, model: 0.0
        self.__dwidth(0, self)
        
        # Create the quark U(3) charge matrix.
        self.q = [self.xfs["u"], self.xfs["d"], self.xfs["s"]]

        # Load the model's defined final states.
        try: self.__states = states if states != None else model.states
        except: self.__states = ["visible", "invisible"]
        self.width("total", 0, 0)
        try: self.width("total", 0, 0)
        except: raise ModelError(
            "Invalid definition of allowed final states from '%s'." % name)

    ###########################################################################
    def trq(self, m, s, t):
        """
        Return the trace of the quark U(3)-charge matrix for the model
        with the diagonal of a given matrix, e.g. a meson generator T.
        
        m: mass at which to evaulate the couplings (GeV).
        s: coupling type, either 0 for axial or 1 for vector.
        t: diagonal of the matrix to perform the trace with, must be
           size 3.
        """
        try: return (t[0]*self.xfs["u"][s](m) + t[1]*self.xfs["d"][s](m) +
                     t[2]*self.xfs["s"][s](m))
        except: raise ModelError(
            "Invalid diagonal provided to the trace.")

    ###########################################################################
    def width(self, states, m, g = 1.0):
        """
        Return the width, in GeV, for the specified states, mass,
        and global coupling.

        states: final state or states, see the documentation for this class 
                for details.
        m:      mass (GeV).
        g:      global coupling (unitless).
        """
        # Loop over the states.
        total = 0
        for state in (states,) if isinstance(states, str) else states:

            # Decoupled decay.
            if state == "none": return None

            # Use cached result if valid.
            cache = self.__cache.get(state)
            if cache and cache[0] == m: total += cache[-1]; continue
    
            # Invisible, visible, dark sector, neutrino, lepton,
            # quark, hadron, and total widths.
            dtrs = state.split("_")
            if state == "invisible":
                part = self.width(["dark", "neutrinos", "rhns"], m)
            elif state == "visible":
                part = self.width(
                    ["leptons", "quarks", "hadrons"]
                     +([] if self.xav[0] else ["gamma_gamma_gamma"])
                    , m)
            elif state == "dark":
                part = self.__dwidth(m, self)
            elif state == "neutrinos":
                part = self.width(["nue_nue", "numu_numu", "nutau_nutau"], m)
            elif state == "leptons":
                part = self.width(["e_e", "mu_mu", "tau_tau"], m) 
            elif state == "quarks":
                part = self.width(["c_c", "b_b", "t_t"], m)#"u_u", "d_d", "s_s", 
            elif state == "rhns":
                part = self.width(["Ne_Ne", "Nmu_Nmu", "Ntau_Ntau"], m)
            elif state == "total":
                part = self.width(self.__states, m)

            # Hadronic width.
            elif state == "hadrons":
                # Remove axial check for vector components.
                axial, self.xav[0] = self.xav[0], False
                part = self.width(pars.rfs.keys(), m)
                self.xav[0] = axial
                # Axial component from equation 2.11 of axial paper.
                ps = 1. if m > 2*pars.mms["K"] else 0.
                part += m/(4.*math.pi)*(
                    self.trq(m, 0, [1, -1, 0])**2.*pars.sfs["u_d"](m)
                    + ps*self.xfs["s"][0](m)**2.*(
                        pars.sfs["u_d"](m)/4. + pars.sfs["s"](m)
                        - pars.cphi*(pars.sfs["u_d"](m)*pars.sfs["s"](m))**0.5))
                
                # xe, me = (self.xfs["e"][0](m)+self.xfs["e"][1](m))/2, pars.mfs["e"]
                # if m > 2*me:
                #     eeov = (m*(xe**2)/(12*math.pi))*(1+2*(me/m)**2)*math.sqrt(1-4*(me/m)**2)
                #     part = eeov*part/self.width("e_e", m)
    
            # Perturbative decay into a fermion pair, equation 2.13.
            elif len(dtrs) == 2 and dtrs[0] == dtrs[1] and dtrs[0] in pars.mfs:
                dtr = dtrs[0]
                cf, mf   = pars.cfs[dtr], pars.mfs[dtr]
                axf, vxf = self.xfs[dtr][0](m), self.xfs[dtr][1](m)
                if m > 2.*mf: part = (cf*vxf**2.*m/(12.*math.pi)*(
                        1. + 2.*mf**2./m**2.)*math.sqrt(1. - 4.*mf**2./m**2.) +
                                      cf*axf**2.*m/(12.*math.pi)*(
                        1. + 2.*mf**2./m**2.)*math.sqrt(1. - 4.*mf**2./m**2.))
                else: part = 0
                
            elif len(dtrs) == 2 and dtrs[0] == dtrs[1] and dtrs[0] in ["Ne", "Nmu", "Ntau"]:
                dtr = dtrs[0]
                
                if dtr == "Ne": mN = self.m1*m
                if dtr == "Nmu": mN = self.m2*m
                if dtr == "Ntau": mN = self.m3*m
                
                xP = 1
                
                if m > 2*mN: part = m/(24*math.pi)*(xP**2)*(1 - 4*(mN/m)**2)**(3/2)
                else: part = 0

            # Perturbative decay into three photons via an electron loop,
            # equation 3.5 of Seo:2020dtx.
            elif len(dtrs) == 3 and dtrs[0] == dtrs[1] == dtrs[2] == "gamma":
                part = 0
                if self.xav[0]: warnings.warn(
                        "Cannot calculate width for state '%s' with non-zero "
                        "axial couplings." % state)
                else:
                    mf = pars.mfs["e"]
                    axf, vxf = self.xfs["e"][0](m), self.xfs["e"][1](m)
                    if m < 2.*mf: part = (
                        ((axf**2. + vxf**2)*pars.ge**6.)/(4.*math.pi)**4./(
                        2.**7.*3.**6.*5.**2.*math.pi**3.)*(m**9./mf**8.)*(
                        17./5. + (67.*m**2.)/(42.*mf**2.) +
                        (128941.*m**4.)/(246960.*mf**4.)))

            # Decay into hadrons, equations 2.17 and 2.18.
            elif state in pars.rfs:
                part = 0
                if self.xav[0]: warnings.warn(
                        "Cannot calculate width for state '%s' with non-zero "
                        "axial couplings." % state)
                else:
                    for mesons, rf in pars.rfs[state].items():
                        sub = 1
                        for meson in mesons: sub *= pars.rvs[meson]*self.trq(
                                m, 1, pars.tms[meson])
                        sub *= sub if len(mesons) == 1 else 2
                        sub *= rf(m)
                        part += m/(12*math.pi)*sub

            else: raise ModelError(
                "Unknown state '%s'." % state)

            # Cache the result.
            total += part
            self.__cache[state] = (m, part)
        return g*g*total

    ###########################################################################
    def tau(self, m, g = 1.0):
        """
        Return the lifetime, in seconds, for the specified mass and
        and global coupling.

        m: mass (GeV).
        g: global coupling (unitless).
        """
        return pars.hbar/self.width("total", m, g)

    ###########################################################################
    def g(self, m, tau):
        """
        Return the global coupling, for the specified mass and lifetime.

        m:   mass (GeV).
        tau: lifetime (seconds).
        """
        return math.sqrt(self.tau(m)/tau)

    ###########################################################################
    def bfrac(self, states, m):
        """
        Return the branching fraction for the specified states and mass.

        states: final state or states, see the documentation for this class 
                for details.
        m:      mass (GeV).
        """ 
        num = self.width(states, m)
        if num == 0: return 0.0
        elif num == None: return 1.0
        den = self.width("total", m)
        if den == 0: return 0.0
        return num/den

###############################################################################
class Models(collections.OrderedDict):
    """
    Loads all 'Model's along the provided paths. The 'Models' object
    acts as an ordered dictionary for the individual models.
    """
    ###########################################################################
    def __init__(self, paths = None, states = None, dwidth = None):
        """
        Load all available models along the specified paths.

        paths:  paths to search for models. If no paths are specified,
                search the paths specified by DARKCAST_MODEL_PATH and
                the local DarkCast model directory.
        states: optionally, specify the allowed final states of the models.
        dwidth: optionally, specify the dark sector width as a function of 
                a given mass and model.
        """
        super(Models, self).__init__()
        if paths == None: paths = utils.envpaths("MODEL", "models")
        for path in (paths,) if not hasattr(paths, "__iter__") else paths:
            models = sorted(os.listdir(path))
            for model in models:
                if not model.endswith(".py"): continue
                try: self[model[0:-3]] = Model(
                        model[0:-3], states, dwidth, path)
                except: warnings.warn("Cannot load model '%s'." % model)
