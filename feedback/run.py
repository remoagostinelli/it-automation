#! /usr/bin/env python3

import os
import requests

# List all the feedback files
files = os.listdir("/data/feedback")

# Create a dictionary with feedback for every file
feedback = {}
for file in files:
    with open(f"/data/feedback/{file}") as f:
        lines = f.read().splitlines()
        feedback["title"] = lines[0]
        feedback["name"] = lines[1]
        feedback["date"] = lines[2]
        feedback["feedback"] = lines[3]

    # Post to the company's website
    response = requests.post("http://localhost/feedback/", json=feedback)

    # Return HTTP request status code
    if not response.ok:
        raise Exception(f"GET failed with status code {response.status_code}.")
