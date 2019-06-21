import math
import sys
from os import rename

import requests
import tweepy

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://google.com")
print(r.status_code)
print(sys.version)

