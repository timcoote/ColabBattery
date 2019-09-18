The program devs.py includes a list of hubs and associated devices as spat out by a version of Simple_Battery_Analysis.ipynb

It checks this list against what pumphouse tells it and identifies common, historical only (ie there's battery reports from some time
but pumphouse doesn't report the device slot), and current only (battery never reported by this device).

the device slot used by anthropos to identify a device is actually a container that can have 1 or more physical devices in it
this is not captured in devs.py and is of some concern: some devices either move nodes or are replaced, and we cannot tell which.
For instance, there are on Simple_Battery_Analysis.ipynb, three devices identified on the top hub with the same slot, but different
nodes (the structure of the name of a devices is <device slot uuid>_<ZWave node>)

devs.py ignores devices that are power sockets (and so have no battery level to support). 

There's still some tidying up to get to data that's of a reasonable quality to make any assertions about, I think.

