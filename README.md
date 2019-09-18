This repo contains a jupyter notebook that is intended to run either in a local repo on a laptop, or in a colab notebook. The intention
is to use colab to produce easily shareable analysis of data sets such as `battery analysis.xlsx`, as produced by pumphouse.

The program `devs.py` includes a list of hubs and associated devices as spat out by a version of Simple_Battery_Analysis.ipynb, based
on what that notebook found in `battery analysis.xlsx`. I'm not sure that it makes total sense to put `devs.py` into a separate
program, invoking it as embedded in the notebook.

`devs.py` ignores devices that are power sockets (and so have no battery level to support). 


It checks this list against what pumphouse tells it and identifies common, historical only (ie there's battery reports from some time
but pumphouse doesn't report the device slot), and current only (battery never reported by this device).

the device slot used by anthropos to identify a device is actually a container that can have 1 or more physical devices in it
this is not captured in devs.py and is of some concern: some devices either move nodes or are replaced, and we cannot tell which.
For instance, there are on Simple_Battery_Analysis.ipynb, three devices identified on the top hub with the same slot, but different
nodes (the structure of the name of a devices is <device slot uuid>_<ZWave node>)


There is a Rakefile to press a `pdf` from the ipynb, but that requires an installation of `jupyter`.

There's still some tidying up to get to data that's of a reasonable quality to make any assertions about, I think.


