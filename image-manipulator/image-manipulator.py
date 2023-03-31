#!/usr/bin/env python3

import os, sys
from PIL import Image

# Get user's home directory
home = os.path.expanduser("~")

# Ensure a command line argument is given
if len(sys.argv) < 2:
    print("Usage: ./image-manipulator.py [DIRECTORY]")
    sys.exit(1)

# Get images folder
indir = sys.argv[1]

# Ensure images folder has a full path
if home not in indir:
    indir = f"{home}/{indir}"

# Determine output folder
os.mkdir("converted_images")
outdir = "converted_images"

""" For each file,
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image to a new folder in .jpeg format """

exceptions = 0

files = os.listdir(indir)
files.remove(".DS_Store")

for infile in files:
    try:
        with Image.open(f"{indir}/{infile}") as im:
            im.rotate(-90).resize((128, 128), resample=Image.Resampling.NEAREST).convert("RGB").save(f"{outdir}/{infile}", "jpeg") 
            print(f"Converted {infile}.")
    except OSError:
        print(f"Could not convert {infile}.")
        exceptions += 1

if exceptions == 0:
    print("Success!")