# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import darkcast
notes = """
This limit is a projection for run 3 LHCb searches using a di-electron
final state from inclusive production. This limit was extracted from
figure 1 (blue lines) of Craik:2022riw below the dimuon mass. For inclusive
di-muon decays, see Ilten2016tkc.

Here the decay of the pi0 is taken as the predominant production
mechanism below the pi0 mass, and the decay of the eta above. See
Ilten:2019xey for details on the production mechanisms.

The prompt and displaced limits are separated assuming an LHCb
lifetime resolution of c*tau = 14e-6. The prompt lower limit is set at
5*c*tau, while the displaced upper limit is set at 5*c*tau.

The limit is prompt, so t0 = 0 and the definition of the maximum
proper lifetime from Ilten:2016tck is used, 0.04/(m - 2m_mu) + 0.1 ps.
"""
bibtex = """
@inproceedings{Craik:2022riw,
 author         = "Craik, Daniel and Ilten, Phil and Johnson, Daniel and 
                   Williams, Mike",
 title          = "{LHCb future dark-sector sensitivity projections for 
                   Snowmass 2021}",
 booktitle      = "{2022 Snowmass Summer Study}",
 eprint         = "2203.07048",
 archivePrefix  = "arXiv",
 primaryClass   = "hep-ph",
 month          = "3",
 year           = "2022"
}
"""
model = darkcast.Model("dark_photon")
production = darkcast.Production({
    "pi0_gamma": lambda m: 1.0 if m <= darkcast.pars.mms["pi0"] else 0.0,
    "eta_gamma": lambda m: 1.0 if m > darkcast.pars.mms["pi0"] else 0.0})
production.name = "$pp$"
decay = "e_e"
bounds = darkcast.Datasets("reach/LHCb_Craik2022riw_prompt_run3.lmt")
efficiency = darkcast.Efficiency(
    t0 = 0, t1 = lambda m: (0.004/(m - 2*darkcast.pars.mfs['mu']) + 0.1)*1e-12)
