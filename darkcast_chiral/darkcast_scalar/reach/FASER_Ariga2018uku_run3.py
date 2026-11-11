# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import darkcast
notes = """ 
This limit is a projection for FASER searches using meson decay
production. This limit was extracted from the right plot of figure 6
(black line labeled FASER) of Ariga:2018uku. Here the decay of the pi0
is taken as the predominant production mechanism below the pi0 mass,
and the decay of the eta above. Production from proton bremsstrahlung
is neglected.

This is a displaced search where the decay volume length over the
shielding length is 5/480.
"""
bibtex = """
@article{Ariga:2018uku,
 author         = "Ariga, Akitaka and others",
 title          = "{FASER's Physics Reach for Long-Lived Particles}",
 collaboration  = "FASER",
 year           = "2018",
 eprint         = "1811.12522",
 archivePrefix  = "arXiv",
 primaryClass   = "hep-ph",
 reportNumber   = "UCI-TR-2018-19, KYUSHU-RCAPP-2018-06",
 SLACcitation   = "%%CITATION = ARXIV:1811.12522;%%"
}
"""
model = darkcast.Model("dark_photon")
from darkcast.pars import mms, mfs
production = darkcast.Production({
    "pi0_gamma": lambda m: 1.0*(m <  mms["pi0"] - 2*mfs["e"]),
    "eta_gamma": lambda m: 1.0*(m >= mms["pi0"] - 2*mfs["e"])})
production.name = "$pp$"
decay = "e_e"
bounds = darkcast.Datasets("reach/FASER_Ariga2018uku_run3.lmt")
efficiency = darkcast.Efficiency(lratio = 5.0/480.0)
