#!/usr/bin/env python3

import requests
import os

# Home
home = os.path.expanduser("~")

# URL
url = "http://localhost/upload/"

# Path
images_path = f"{home}/supplier-data/images"

# List of images
images = os.listdir(images_path)

# Take jpeg images only
images = [image for image in images if ".jpeg" in image]

# Upload every image
for image in images:
  try:
    with open(f"{images_path}/{image}", "rb") as im:
      r = requests.post(url, files={"file": im})
      print(r.status_code)
        #print(f"Submitted {image}.")
  except:
    print(f"Could not submit {image}.")
