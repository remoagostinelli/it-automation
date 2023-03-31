#!/usr/bin/env python3

import os
from PIL import Image

home = os.path.expanduser("~")

images_path = f"{home}/supplier-data/images"

images = os.listdir(images_path)

for image in images:
  file, extension = os.path.splitext(image)
  try:
    with Image.open(f"{images_path}/{image}") as im:
      im.resize((600, 400), resample=Image.Resampling.NEAREST).convert("RGB").save(f"{images_path}/{file}.jpeg", "jpeg")
      print(f"Converted {image}.")
  except:
    print(f"Could not convert {image}.")
