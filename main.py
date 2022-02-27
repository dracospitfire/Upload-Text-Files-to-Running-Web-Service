#!/usr/bin/env python3

import os
import requests

url = 'http://###.###.###.###/feedback/'
path = "." #/data/feedback

for file in os.listdir(path):
  if file.endswith(".txt"):
    file = open(file, "r") #os.path.join(path
    text = file.readlines()
    review = {}
    review.update({"title":text[0].strip("\n")})
    review.update({"name":text[1].strip("\n")})
    review.update({"date":text[2].strip("\n")})
    review.update({"feedback":text[3].strip("\n")})
    status = requests.post(url, data = review)
    print(status.status_code)
