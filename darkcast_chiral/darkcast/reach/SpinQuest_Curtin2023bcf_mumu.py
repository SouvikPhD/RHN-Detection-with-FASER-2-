# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import darkcast
notes = """
This projection was taken from figure 6 (left plot, solid red line) of
Curtin:2023bcf.

Production is from charged-pion bremsstrahlung and the decay is to a
dimuon final state.

In Curtin:2023bcf this is considered a displaced search with a decay
volume of 7 meters and shielding length of 5 meters.
"""
bibtex = """
@article{Curtin:2023bcf,
 author = "Curtin, David and Kahn, Yonatan and Nguyen, Rachel",
 title = "{Dark Photons from Charged Pion Bremsstrahlung at Proton Beam 
           Experiments}",
 eprint = "2305.19309",
 archivePrefix = "arXiv",
 primaryClass = "hep-ph",
 month = "5",
 year = "2023"
}
"""
model = darkcast.Model("dark_photon")
production = darkcast.Production("pi_brem")
decay = ["mu_mu"]
bounds = darkcast.Datasets("reach/SpinQuest_Curtin2023bcf_mumu.lmt")
efficiency = darkcast.Efficiency(lratio = 7.0/5.0)
