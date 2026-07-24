# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import math
from . import utils, pars, pmodel
model = pmodel
###############################################################################
class BreitWignerError(Exception):
    """
    Simple exception for the 'BreitWigner' class.
    """
    pass

###############################################################################
class BreitWigner:
    """
    Provide a running width Breit-Wigner for a given resonance.
    
    mr:  mass of the resonance (GeV).
    sr:  mass squared of the resonance (GeV^2).
    wr:  width of the resonance (1/GeV).
    lr:  orbital angular momentum for the resonance.
    drs: decay channels for the resonance of the form 
         [branching, mass 0, mass 1].
    """
    ###########################################################################
    def __init__(self, resonance, lr = 1):
        """
        Initialize the needed data for a given resonance and orbital
        angular momentum.

        resonance: resonance string, e.g. 'rho0'.
        lr:        orbital angular momentum for the resonance, e.g. 0 for 
                   s-wave, 1 for p-wave, etc. If 'None', a fixed width is used.
        """
        self.lr = None if pars.bw == "fix" else lr
        try:
            self.mr, self.wr = pars.mms[resonance], pars.wms[resonance]
            self.sr, self.drs = self.mr**2, pars.dms[resonance]
        except:
            raise BreitWignerError(
                "No data is available for the %s resonance." % resonance)

    ###########################################################################
    def __call__(self, m, square = False):
        """
        Return the Breit-Wigner for a given mass.
        
        m:      mass (GeV).
        square: if True, return the normalized BW squared, rather than complex.
        """
        from math import pi
        k, sm = 0, m**2
        # Running width, equation A.3.
        if self.lr != None:
            for br, m0, m1 in self.drs:
                if m > m0 + m1: k += br*math.sqrt(
                    ((sm - (m0 + m1)**2)*(sm - (m0 - m1)**2)/(4*sm))/
                    ((self.sr - (m0 + m1)**2)*(self.sr - (m0 - m1)**2)/
                     (4*self.sr)))**(2*self.lr + 1)
            if square:
                g = (self.sr*(self.sr + (self.wr*k/m)**2))**0.5
                n = 8**0.5*self.mr*self.wr*k/m*g/(pi*(self.sr + g)**0.5)
                return n/((self.sr - sm)**2 + (self.sr*self.wr*k/m)**2)
            else:
                return self.sr/(self.sr - sm - complex(0, self.sr*self.wr*k/m))
       
       # Fixed width, equation A.2.
        else:
            if square:
                g = (self.sr*(self.sr + self.wr**2))**0.5
                n = 8**0.5*self.mr*self.wr*g/(pi*(self.sr + g)**0.5)
                return n/((self.sr - sm)**2 + (self.mr*self.wr)**2)
            else:
                return self.sr/(self.sr - sm - complex(0, self.mr*self.wr))

###############################################################################
class ProductionError(Exception):
    """
    Simple exception for the 'Production' class.
    """
    pass

###############################################################################
class Production:
    """
    Represents the possible production mechanisms for an X-boson,
    given an experiment.

    name:     name of the production.
    channels: list of production channels taking the form 
              [production of type 'Production', production fraction function]
    """
    ###########################################################################
    def __init__(self, channels, frac = 1.0):
        """
        Load a production, given its channel or channels. When
        specifying a single channel, 'channels' can be a mechanism
        name, e.g. 'p_brem' for proton-beam bremsstrahlung. The
        built-in mechanisms are:

        p_brem:  proton-beam bremsstrahlung.
        pi_brem: charged-pion beam bremsstrahlung.
        A_brem:  A-beam bremsstrahlung, where A can be any fundamental
                 fermion.
        A_A:     Drell-Yan, where A can be any fundamental fermion.
        A:       vector meson mixing, where A is the vector meson.
        A_B:     meson decays of the form A -> B + X, where A is the 
                 decaying meson, B is the SM daughter and X is the NP
                 daughter.

        Alternatively, a user defined function that is mass and model
        dependent can be provided, taking the form 'mechanism(mass
        (GeV), model)'. The mechanism is assumed to be dependent upon
        the square of the global coupling. However, if the form
        'mechanism(mass (GeV), global couploing, model)', is provided
        then this assumption is not made and the fast-caching used in
        the limit finding is no longer performed.

        If multiple channels are specified, these are provided in a
        dictionary via 'channels' where the keys are the mechanisms
        and their associated values are the fractions. The mechanism
        is given as above. The fraction can be given either as a
        number, or a mass dependent function, e.g. 'fraction(mass
        (GeV))'.

        The 'Datasets' class provides a dictionary of datasets, and
        consequently can be passed as the 'channels' argument. The
        first column of the dataset is the mass interpolation points
        and all remaining columns are the mass dependent ratios for
        each mechanism. The first row specifies the built-in mechanism
        for each column. User defined mechanisms cannot be used here.

        channels: the production channel, see above.
        frac:     the production fraction for this channel.
        """
        # Initialize the cached results.
        self.name = "undefined"
        self.fast = True
        self.__cache = (None, None)

        # Multiple mechanisms from a dictionary.
        try:
            self.channels = []
            for prd, frc in channels.items():
                self.channels.append(Production(prd, frc))
            return
        except: pass

        # Pre-defined mechanism.
        if isinstance(channels, str):
            self.name = channels
            moms = channels.split("_")

            # Decoupled production mechanism.
            if channels == "none": self.__sigma = lambda m, model: 1.0
            
            # Proton-beam bremsstrahlung, equation 2.4.
            if channels == "p_brem":
                self.__sigma = lambda m, model: (
                    (2*model.xfs["u"][1](m) + model.xfs["d"][1](m))**2 +
                    pars.pff*(2*model.xfs["u"][0](m) + model.xfs["d"][0](m))**2 
                    *((1 + (m/pars.pms[1])**2)/(1 + (m/pars.pms[0])**2))**4)

            # Charged-pion beam bremsstrahlung, based on equation 2.4.
            # Calculate F_A(m)/F_V(m) as:
            # (gamma*m_a1/m_rho0) * (BW_a1(m)/BW_rho0(m))
            # where gamma is F_A(0)/F_V(0). Both the rho0 and a1 BWs
            # are treated as fixed width and mass dependence is loosely
            # based on Stetz:1977ge.
            elif channels == "pi_brem":
                bwr, bwa = BreitWigner("rho0", None), BreitWigner("a1", None)
                pre = pars.piff*(bwr(0, True)/bwa(0, True))
                self.__sigma = lambda m, model: (
                    (model.xfs["u"][1](m) - model.xfs["d"][1](m))**2 +
                    (model.xfs["u"][0](m) - model.xfs["d"][0](m))**2 
                    *(pre*bwa(m, True)/bwr(m, True))**2)
                
            # Drell-Yan or lepton-beam bremsstrahlung, equation 2.3 and 2.6.
            elif (len(moms) == 2 and (moms[1] == 'brem' or moms[0] == moms[1]) 
                  and moms[0] in pars.mfs):
                self.__sigma = lambda m, model: (
                    model.xfs[moms[0]][1](m)**2 + model.xfs[moms[0]][0](m)**2)
    
            # Vector meson decay, equation 2.11.
            elif channels in pars.rvs:
                self.__sigma = lambda m, model: (
                    model.trq(m, 1, pars.tms[channels]))**2
    
            # Meson decay of the form A -> B + X, equation 2.7 - 2.10.
            elif len(moms) == 2 and moms[0] in pars.tms and moms[1] in pars.tms:
                ta, tb, vs = pars.tms[moms[0]], pars.tms[moms[1]], []
                for v in pars.rvs:
                    tv = pars.tms[v]
                    pf = utils.trace(ta, tb, tv)
                    if pf: vs.append((tv, pf, BreitWigner(v, 1)))
                self.__sigma = lambda m, model: (
                    abs(sum([pf*model.trq(m, 1, tv)*
                             bw(m) for tv, pf, bw in vs])))**2

            # Unknown mechanism.
            else: raise ProductionError(
                "Unknown production mechanism '%s'." % self.name)

        # User supplied mechanism.
        else:
            self.__sigma = channels
            try:
                self.__sigma(0, model.Model("dark_photon"))
            except:
                self.__sigma(0, 1, model.Model("dark_photon"))
                self.__cache = False
            
        # Set the channels.
        try: float(frac); self.__frac = lambda m, frac = frac: float(frac)
        except: self.__frac = frac
        self.channels = [self]

    ###########################################################################
    def ratio(self, m, g0, g1, model0, model1):
        """
        Return the cross-section ratio between two models, for a given
        mass and global couplings.
        
        m:      mass (GeV).
        g0:     global coupling for the first model.
        g1:     global coupling for the second model.
        model0: first model, numerator.
        model1: second model, denominator.
        """
        # Assume the global coupling is squared and use the cache.
        if self.__cache != False:
            # Return the cached result if valid.
            if self.__cache[0] == m: return (g0/g1)**2*self.__cache[-1]

            # Calculate the result, equation 2.12.
            ratio = 0
            for channel in self.channels:
                den = channel.__sigma(m, model1)
                if den: ratio += channel.__frac(m)*channel.__sigma(
                        m, model0)/den
            self.__cache = (m, ratio)
            return (g0/g1)**2*ratio
        # Calculate the full coupling dependent ratio with no cache.
        else:
            # Calculate the result, equation 2.12.
            ratio = 0
            for channel in self.channels:
                den = channel.__sigma(m, g1, model1)
                if den: ratio += channel.__frac(m)*channel.__sigma(
                        m, g0, model0)/den
            return ratio

###############################################################################
def dxsNuL2NuL(m, g, model, n, l, en):
    """
    Absolute difference between model and SM scattering cross-section for 
    (the initial lepton is assumed to be at rest):

        nu + l -> nu + l (different flavor)

    m:     mass (GeV).
    g:     global coupling (unitless).
    model: model, if not provided, calculate SM cross-section.
    n:     name of the neutrino.
    l:     name of the lepton.
    en:    energy of the neutrino beam (GeV).
    """
    from math import pi, log
    if m == 0: m = 1e-5
    sm, an, vn, al, vl = 0, 0, 0, 0, 0
    if model:
        an, vn = model.xfs[n]
        al, vl = model.xfs[l]
        an, vn, al, vl = an(m), vn(m), al(m), vl(m)
        sm = dxsNuL2NuL(m, g, False, n, l, en)    
    ml, mw, mz = pars.mfs[l], pars.mw, pars.mz
    cw = mw/mz                                           # Cosine theta_W.
    sw = (1 - cw**2)**0.5                                # Sine theta_W.
    gf = 4*pi**2*pars.ge**2/(2**0.5*mz**2*cw**2*sw**2)   # Fermi constant.
    return abs(-sm + 
        (1/(12*ml**2*pi))*((16*en**2*gf**2*ml**3*(3*(2*en + ml)**2 - 6*(2*en +
        ml)*(4*en + ml)*sw**2 + 4*(16*en**2 + 12*en*ml + 3*ml**2)*sw**4))/(2*en
        + ml)**3 + (1/(en**2))*3*gf*g**2*(an - vn)*(-((4*en**2*ml*(-2*(2*en +
        ml)*(2*ml*(2*en + ml) + m**2)*sw**2*(al + vl) + ml*(4*en**2*sw**2*(al +
        vl) + ml*(2*en + ml)*(al + 4*sw**2*al + vl))))/(2*en + ml)**2) +
        (8*en*ml*m**2*sw**2*(al + vl) + 2*m**4*sw**2*(al + vl) - ml**2*m**2*(al
        + vl - 4*sw**2*vl) + 4*en**2*ml**2*(al + (-1 + 4*sw**2)*vl))*log(((2*en
        + ml)*m**2)/(4*en**2*ml + (2*en + ml)*m**2))) + 3*g**4*((1/((2*en +
        ml)*m**2*(4*en**2*ml + (2*en + ml)*m**2)))*4*ml*(-ml**3*m**2*(al -
        vl)*(al + vl)*(an**2 + vn**2) + 8*en**3*ml**2*(al**2 + vl**2)*(an**2 +
        vn**2) + ml*m**4*(an**2*(al**2 + vl**2) - 4*al*an*vl*vn + (al**2 +
        vl**2)*vn**2) + 2*en*m**2*(2*ml**2*vl*(an**2*vl - 2*al*an*vn +
        vl*vn**2) + m**2*(an**2*(al**2 + vl**2) - 4*al*an*vl*vn + (al**2 +
        vl**2)*vn**2)) + 2*en**2*ml*(2*ml**2*(al**2 + vl**2)*(an**2 + vn**2) +
        3*m**2*(an**2*(al**2 + vl**2) - 4*al*an*vl*vn + (al**2 +
        vl**2)*vn**2))) + ((-2*ml**2*al*(-2*an*vl*vn + al*(an**2 + vn**2)) +
        (2*en*ml + ml**2 + m**2)*(-4*al*an*vl*vn + al**2*(an**2 + vn**2) +
        vl**2*(an**2 + vn**2)))*log(((2*en + ml)*m**2)/(4*en**2*ml + (2*en +
        ml)*m**2)))/en**2)))

##############################################################################
def dxsNulL2NulL(m, g, model, n, l, en):
    """
    Absolute difference between model and SM scattering cross-section for 
    (the initial lepton is assumed to be at rest):

        nul + l -> nul + l (same flavor)

    m:     mass (GeV).
    g:     global coupling (unitless).
    model: model, if not provided, calculate SM cross-section.
    n:     name of the neutrino.
    l:     name of the lepton.
    en:    energy of the neutrino beam (GeV).
    """
    from math import pi, log
    if m == 0: m = 1e-5
    sm, an, vn, al, vl = 0, 0, 0, 0, 0
    if model:
        an, vn = model.xfs[n]
        al, vl = model.xfs[l]
        an, vn, al, vl = an(m), vn(m), al(m), vl(m)
        sm = dxsNulL2NulL(m, g, False, n, l, en)    
    ml, mw, mz = pars.mfs[l], pars.mw, pars.mz
    cw = mw/mz                                           # Cosine theta_W.
    sw = (1 - cw**2)**0.5                                # Sine theta_W.
    gf = 4*pi**2*pars.ge**2/(2**0.5*mz**2*cw**2*sw**2)   # Fermi constant.
    return abs(-sm + 
        1/(4*ml**2*pi)*((4*ml*(ml*((al**2 + vl**2)*an**2 - 4*al*vl*vn*an +
        (al**2 + vl**2)*vn**2)*m**4 - ml**3*(al - vl)*(al + vl)*(an**2 +
        vn**2)*m**2 + 2*en*(2*vl*(vl*an**2 - 2*al*vn*an + vl*vn**2)*ml**2 +
        m**2*((al**2 + vl**2)*an**2 - 4*al*vl*vn*an + (al**2 +
        vl**2)*vn**2))*m**2 + 8*en**3*ml**2*(al**2 + vl**2)*(an**2 + vn**2) +
        2*en**2*ml*(2*(al**2 + vl**2)*(an**2 + vn**2)*ml**2 + 3*m**2*((al**2 +
        vl**2)*an**2 - 4*al*vl*vn*an + (al**2 + vl**2)*vn**2))))/((2*en +
        ml)*m**2*(4*ml*en**2 + (2*en + ml)*m**2)) + 1/en**2*(-(al - vl)*(al +
        vl)*(an**2 + vn**2)*ml**2 + 2*en*((an**2 + vn**2)*al**2 - 4*an*vl*vn*al
        + vl**2*(an**2 + vn**2))*ml + m**2*((al**2 + vl**2)*an**2 -
        4*al*vl*vn*an + (al**2 + vl**2)*vn**2))*(2*log(m) -
        log((4*ml*en**2)/(2*en + ml) + m**2)))*g**4 +
        1/(4*ml**2*mw**2*pi)*gf*(an - vn)*(-4*((al + (4*sw**2 - 1)*vl)*mw**2 +
        2*cw**2*mz**2*(vl - al))*log((4*ml*en**2)/(2*en + ml) + m**2)*ml**2 +
        1/(2*en + ml)**2*(-4*(2*en + ml)*(mw**2 - 2*cw**2*mz**2)*al*ml**3 -
        4*(2*en + ml)*(mw**2 - 2*cw**2*mz**2)*vl*ml**3 + 8*mw**2*((2*en +
        ml)*m**2 + 2*en*ml*(3*en + 2*ml))*sw**2*al*ml + 8*mw**2*((2*en +
        ml)*m**2 + 2*ml*(en + ml)*(3*en + ml))*sw**2*vl*ml) +
        1/en**2*2*(2*mw**2*sw**2*(al + vl)*m**4 + 8*en*ml*mw**2*sw**2*(al +
        vl)*m**2 + ml**2*(2*cw**2*mz**2*(al + vl) - mw**2*(-4*vl*sw**2 + al +
        vl))*m**2 + 4*en**2*ml**2*((4*vl*sw**2 + al - vl)*mw**2 +
        2*cw**2*mz**2*(vl - al)))*log(m) + (m**2*((2*cw**2*mz**2*(al + vl) -
        mw**2*(-4*vl*sw**2 + al + vl))*ml**2 + 8*en*mw**2*sw**2*(al + vl)*ml +
        2*mw**2*m**2*sw**2*(al + vl))*log((2*en + ml)/(4*ml*en**2 + (2*en +
        ml)*m**2)))/en**2)*g**2 + (4*en**2*gf**2*ml*(4*(16*en**2 + 12*ml*en +
        3*ml**2)*mw**4*sw**4 - 6*(2*en + ml)*(4*en + ml)*mw**2*(mw**2 -
        2*cw**2*mz**2)*sw**2 + 3*(2*en + ml)**2*(mw**2 -
        2*cw**2*mz**2)**2))/(3*(2*en + ml)**3*mw**4*pi))

###############################################################################
def dxsNulbarL2NulbarL(m, g, model, n, l, en):
    """
    Absolute difference between model and SM scattering cross-section for 
    (the initial lepton is assumed to be at rest):

        nulbar + l -> nulbar + l (same flavor)

    m:     mass (GeV).
    g:     global coupling (unitless).
    model: model, if not provided, calculate SM cross-section.
    n:     name of the neutrino.
    l:     name of the lepton.
    en:    energy of the neutrino beam (GeV).
    """
    from math import pi, log
    if m == 0: m = 1e-5
    sm, an, vn, al, vl = 0, 0, 0, 0, 0
    if model:
        an, vn = model.xfs[n]
        al, vl = model.xfs[l]
        an, vn, al, vl = an(m), vn(m), al(m), vl(m)
        sm = dxsNulbarL2NulbarL(m, g, False, n, l, en)    
    ml, mw, mz = pars.mfs[l], pars.mw, pars.mz
    cw = mw/mz                                           # Cosine theta_W.
    sw = (1 - cw**2)**0.5                                # Sine theta_W.
    gf = 4*pi**2*pars.ge**2/(2**0.5*mz**2*cw**2*sw**2)   # Fermi constant.
    return abs(-sm + 
        1/(4*ml**2*pi)*(1/((2*en + ml)*m**2*(4*ml*en**2 + (2*en +
        ml)*m**2))*4*ml*(ml*((al**2 + vl**2)*an**2 + 4*al*vl*vn*an + (al**2 +
        vl**2)*vn**2)*m**4 - ml**3*(al - vl)*(al + vl)*(an**2 + vn**2)*m**2 +
        2*en*(2*vl*(vl*an**2 + 2*al*vn*an + vl*vn**2)*ml**2 + m**2*((al**2 +
        vl**2)*an**2 + 4*al*vl*vn*an + (al**2 + vl**2)*vn**2))*m**2 +
        8*en**3*ml**2*(al**2 + vl**2)*(an**2 + vn**2) + 2*en**2*ml*(2*(al**2 +
        vl**2)*(an**2 + vn**2)*ml**2 + 3*m**2*((al**2 + vl**2)*an**2 +
        4*al*vl*vn*an + (al**2 + vl**2)*vn**2))) + 1/en**2*(-(al - vl)*(al +
        vl)*(an**2 + vn**2)*ml**2 + 2*en*((an**2 + vn**2)*al**2 + 4*an*vl*vn*al
        + vl**2*(an**2 + vn**2))*ml + m**2*((al**2 + vl**2)*an**2 +
        4*al*vl*vn*an + (al**2 + vl**2)*vn**2))*(2*log(m) -
        log((4*ml*en**2)/(2*en + ml) + m**2)))*g**4 +
        1/(4*ml**2*mw**2*pi)*gf*(an - vn)*(1/en**2*(-2*mw**2*m**2*(m**2 +
        4*en*ml)*al*sw**2 + 2*mw**2*(m**4 + 2*ml*(2*en + ml)*m**2 +
        8*en**2*ml**2)*vl*sw**2 + (2*en*ml + m*(m - ml))*(2*en*ml + m*(ml +
        m))*(mw**2 - 2*cw**2*mz**2)*al - (m**4 + ml*(4*en + ml)*m**2 +
        4*en**2*ml**2)*(mw**2 - 2*cw**2*mz**2)*vl)*(2*log(m) -
        log((4*ml*en**2)/(2*en + ml) + m**2)) - 1/(2*en +
        ml)**2*4*ml*(-2*mw**2*((2*en + ml)*m**2 + 2*ml*(en + ml)*(3*en +
        ml))*vl*sw**2 + (2*mw**2*((2*en + ml)*m**2 + 2*en*ml*(3*en +
        2*ml))*sw**2 - (-ml**3 + 6*en**2*ml + m**2*ml + 2*en*(ml**2 +
        m**2))*(mw**2 - 2*cw**2*mz**2))*al + ((2*en + ml)*m**2 + ml*(6*en**2 +
        6*ml*en + ml**2))*(mw**2 - 2*cw**2*mz**2)*vl))*g**2 +
        (4*en**2*gf**2*ml*(4*(16*en**2 + 12*ml*en + 3*ml**2)*mw**4*sw**4 -
        2*(8*en**2 + 6*ml*en + 3*ml**2)*mw**2*(mw**2 - 2*cw**2*mz**2)*sw**2 +
        (4*en**2 + 6*ml*en + 3*ml**2)*(mw**2 - 2*cw**2*mz**2)**2))/(3*(2*en +
        ml)**3*mw**4*pi))
