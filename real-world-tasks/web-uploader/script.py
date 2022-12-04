#!/usr/bin/env python3

import os
import requests

dir = "/data/feedback/"
for file in os.listdir("/data/feedback/"): 
    format = ["title","name","date","feedback"]
    
    # You need to have a dictionary with keys and their respective values (content from feedback files). 
    # This will be uploaded through the Django REST API.
    content = {}
    
    with open('{}{}'.format(dir,file), 'r') as txtfile:
        counter = 0
        for line in txtfile:
            line = line.replace("\n", "")
            content[format[counter]] = line.strip('\n')
            counter += 1
    
    # Post the dictionary to the company's website. 
    # Make a POST request to http://<corpweb-external-IP>/feedback. 
    # Replace <corpweb-external-IP> with corpweb's external IP address.
    response = requests.post("http://104.198.31.42/feedback/",json = content)

    # You can print the status_code and text of the response objects to check out what's going on. 
    # You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(response.status_code, file))
    print("Feedback added!")