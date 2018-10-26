#!/bin/python

import time
import datetime
# https://docs.python.org/2/library/time.html
TIMESTAMP1 = time.strftime('%Y%m%d-%H%M%S')
TIMESTAMP2 = time.strftime('%Y%b%d-%H%M%S')
TIMESTAMP3 = time.strftime('%Y%B%d-%H%M%S')
TIMESTAMP4 = time.strftime('%Z-%Y%B%d-%H%M%S')

print TIMESTAMP1

print TIMESTAMP2
print TIMESTAMP3
print TIMESTAMP4
