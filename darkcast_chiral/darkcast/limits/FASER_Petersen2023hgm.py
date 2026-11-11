# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import darkcast
notes = """ 
This limit is a preliminary result from FASER using meson decay
production. This limit was extracted from figure 2 (blue line labeled
Observed Limit) of Petersen:2023hgm. Here the decay of the pi0 is
taken as the predominant production mechanism below the pi0 mass, and
the decay of the eta above. Production from proton bremsstrahlung is
neglected.

This is a displaced search where the decay volume length over the
shielding length is 5/480.
"""
bibtex = """
@inproceedings{Petersen:2023hgm,
 author = "Petersen, Brian",
 collaboration = "FASER",
 title = "{First Physics Results from the FASER Experiment}",
 booktitle = "{57th Rencontres de Moriond on Electroweak Interactions and 
               Unified Theories}",
 eprint = "2305.08665",
 archivePrefix = "arXiv",
 primaryClass = "hep-ex",
 reportNumber = "CERN-FASER-PROC-2023-004",
 month = "5",
 year = "2023"
}
"""
model = darkcast.Model("dark_photon")
from darkcast.pars import mms, mfs
production = darkcast.Production({
    "pi0_gamma": lambda m: 1.0*(m <  mms["pi0"] - 2*mfs["e"]),
    "eta_gamma": lambda m: 1.0*(m >= mms["pi0"] - 2*mfs["e"])})
production.name = "$pp$"
decay = "e_e"
bounds = darkcast.Datasets("limits/FASER_Petersen2023hgm.lmt")
efficiency = darkcast.Efficiency(lratio = 5.0/480.0)
