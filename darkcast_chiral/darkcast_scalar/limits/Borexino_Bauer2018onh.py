# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import darkcast
notes = """
This limit corresponds to the figure 13 top (filled brown curve
labeled Borexino), which is based on the Borexino result of
Bellini:2011rx. The neutrino energy is taken as 862 keV, and equal parts
of all three neutrino flavors are assumed to be produced from the sun.

Given the nature of the limit, the efficiency ratio is unity, e.g. t0
= 0 and t1 = infinity.
"""
bibtex = """
@article{Bauer:2018onh,
 author        = "Bauer, Martin and Foldenauer, Patrick and Jaeckel, Joerg",
 title         = "{Hunting All the Hidden Photons}",
 eprint        = "1803.05466",
 archivePrefix = "arXiv",
 primaryClass  = "hep-ph",
 doi           = "10.1007/JHEP07(2018)094",
 journal       = "JHEP",
 volume        = "07",
 pages         = "094",
 year          = "2018"
}"""
model = darkcast.Model("B-L_boson")
dxs0 = darkcast.production.dxsNulL2NulL
dxs1 = darkcast.production.dxsNuL2NuL
production = darkcast.Production(
    lambda m, g, model, dxs0 = dxs0, dxs1 = dxs1:
    dxs0(m, g, model, "nue", "e", 8.62e-4) +
    dxs1(m, g, model, "numu", "e", 8.62e-4) +
    dxs1(m, g, model, "nutau", "e", 8.62e-4))
production.name = "nu_scat"
decay = "none"
bounds = darkcast.Dataset("limits/Borexino_Bauer2018onh.lmt")
efficiency = darkcast.Efficiency(t0 = 0, t1 = float("inf"))
