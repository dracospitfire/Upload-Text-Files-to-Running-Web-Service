#! /usr/bin/env python3

import os
import requests

reviews = {}
for file in os.listdir("."):
    if file.endswith(".txt"):
        review = open(file, "r")
        text = review.readlines()
        review = {}
        review.update({"title":text[0].strip("\n")})
        review.update({"name":text[1].strip("\n")})
        review.update({"date":text[2].strip("\n")})
        review.update({"feedback":text[3].strip("\n")})
        reviews.update({file:review})

url = http://http://34.123.148.210//feedback
requests.post(url, data = reviews)
