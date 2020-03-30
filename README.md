This repo contains a jupyter notebook that is intended to run either in a local repo on a laptop, or in a colab notebook. The intention
is to use colab to produce easily shareable analysis of data sets such as the exported`batteryDetails.csv.

The colab process, although it's nominally integrated with the GDrive funcitonality, does not seem to be able to get files from there
automatically, and the UI reports versions that are not current. For simplicity in starting, the code grabs the data from github.

It is initially envisaged that the workflow would be:

1/ run colab in a browser `https://colab.research.google.com
2/ select File -> Open notebook
3/ in the dialog box, select Github, and unselect "Include private repos" (this avoids entering credentials for github)
4/ Enter 'https://github.com/timcoote/ColabBattery' into the search line. This will find the notebook: `Simple_Battery_Analysis.ipynb`
5/ Click the upload button to the right of the notebook's name
6/ Select `Runtime` -> `Run all`, and the `Run Anyway` button.
7/ Confirm that the notebook runs
8/ Updating the git repo will require establishing a new repo as a fork of the original, after that learning curve has been climbed.
In the meantime, I'd anticipate downloading and emailing the notebooks.


However,
the proposed way of working with colab after familiarity is establised with the tools is as follows:

1/ checkout the repo into a local directory
2/ run colab in a browser `https://colab.research.google.com`
3/ upload the notebook from the checked out directory
4/ run it, and upload the `battery analysis.xlsx` data set
5/ modify the notebook as appropriate
6/ ensure that the changes are downloaded to the checked out local directory
7/ `git add`, `git commit` `git push` to put the changes back into the shared revision control

It checks this list against what pumphouse tells it and identifies common, historical only (ie there's battery reports from some time
but pumphouse doesn't report the device slot), and current only (battery never reported by this device).

the device slot used by anthropos to identify a device is actually a container that can have 1 or more physical devices in it
this is not captured in devs.py and is of some concern: some devices either move nodes or are replaced, and we cannot tell which.
For instance, there are on Simple_Battery_Analysis.ipynb, three devices identified on the top hub with the same slot, but different
nodes (the structure of the name of a devices is <device slot uuid>_<ZWave node>)


There is a Rakefile to press a `pdf` from the ipynb, but that requires an installation of `jupyter`.

There's still some tidying up to get to data that's of a reasonable quality to make any assertions about, I think.


