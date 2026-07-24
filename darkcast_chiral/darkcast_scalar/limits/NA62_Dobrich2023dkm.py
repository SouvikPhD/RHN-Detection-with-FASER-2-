# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import darkcast
notes = """
This limit was extracted from figure 14 (black line) of the
associated paper, Dobrich:2023dkm.

The production fraction is assumed to be entirely from eta
decays. Production from proton bremsstrahlung is neglected.

NA62 has 82 meters of shielding followed by a decay volume of 135
meters. However, the first spectrometer chamber is 180 meters from the
interaction point, reducing the effective decay volume. Following the
convention of Tsai:2019mtm, a decay volume of 75 meters is used with a
shielding length of 142 meters.
"""
bibtex = """
@article{Dobrich:2023dkm,
 author = {D\"obrich, B. and Minucci, E. and Spadaro, T.},
 collaboration = "NA62",
 title = "{Search for dark photon decays to $\mu^+\mu^-$ at NA62}",
 eprint = "2303.08666",
 archivePrefix = "arXiv",
 primaryClass = "hep-ex",
 reportNumber = "CERN-EP-2023-032",
 month = "3",
 year = "2023"
}
"""
model = darkcast.Model("dark_photon")
production = darkcast.Production("eta_gamma")
decay = ["mu_mu"]
bounds = darkcast.Datasets("limits/NA62_Dobrich2023dkm.lmt")
efficiency = darkcast.Efficiency(lratio = 75.0/142.0)
