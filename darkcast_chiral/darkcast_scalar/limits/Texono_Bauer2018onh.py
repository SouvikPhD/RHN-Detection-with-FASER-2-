# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).
import darkcast
notes = """
This limit corresponds to the figure 13 top (filled salmon curve
labeled Texono), which is based on the Texono result of
TEXONO:2009knm. The neutrino energy is taken as 2 MeV.

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
dxs = darkcast.production.dxsNulbarL2NulbarL
production = darkcast.Production(lambda m, g, model, dxs = dxs:
                                 dxs(m, g, model, "nue", "e", 2.0e-3))
production.name = "nu_scat"
decay = "none"
bounds = darkcast.Dataset("limits/Texono_Bauer2018onh.lmt")
efficiency = darkcast.Efficiency(t0 = 0, t1 = float("inf"))
