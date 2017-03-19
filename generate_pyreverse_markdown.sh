#!/bin/bash
DATE=`date +%Y-%m-%d`

echo """
# Pyreverse automatically made by Travis builder at $DATE

# Classes:

![Pyreverse Classes](classes_Biking-Endorphines-Web.png)

# Packages:

![Pyreverse Packages](packages_Biking-Endorphines-Web.png)
""" > generated_pyreverse/pyreverse.md
