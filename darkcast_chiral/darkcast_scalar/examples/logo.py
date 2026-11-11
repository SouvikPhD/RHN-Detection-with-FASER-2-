# DARKCAST is licensed under the GNU GPL version 2 or later.
# Copyright (C) 2023 DARKCAST authors (see AUTHORS.md).

# This example just draws the DarkCast logo, in case anyone needs it!

# Update the system path to find the DarkCast module.
# This assumes that 'examples' is in 'darkcast/examples.'
import sys, os, inspect, itertools
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(
                inspect.getfile(inspect.currentframe()))), "../../"))

# Load the DarkCast module.
import darkcast

# Draw the logo.
from matplotlib import pyplot
darkcast.utils.logo(0, 0, 1)
pyplot.savefig("logo.pdf", bbox_inches = "tight")
