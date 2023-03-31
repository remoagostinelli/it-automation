#!/usr/bin/env python3

import os
import requests
import json

# URL
url = "http://localhost/fruits/"

# Home
home = os.path.expanduser("~")

# Path
files_path = f"{home}/supplier-data/descriptions"

# List of files
files = os.listdir(files_path)

# Headers
headers = ["name", "weight", "description", "image_name"]

# Traverse over files and create a dictionary
payload = {}
for file in files:
  # Read over file
  with open(f"{files_path}/{file}", "r") as text:

    lines = text.read().splitlines()

    # Fill payload
    for count, header in enumerate(headers):

      # Convert weight to integer
      if count == 1:
        payload[header] = int(lines[count].rstrip(" lbs"))

      # Store image file name
      elif count == 3:
        payload[header] = file.replace(".txt", ".jpeg")

      else:
        payload[header] = lines[count]

    # Submit file data
    r = requests.post(url, json=payload)

    print(r.status_code)

    if r.ok:
      print(f"Submitted {file}.")
