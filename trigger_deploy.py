#!/usr/bin/env python

"""Simple program to forward requests to an autodeploy"""


import os

import requests

print(os.environ)

api = os.environ["API_KEY"]
print("Api key len is", len(api))


