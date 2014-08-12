# -*- coding: utf-8 -*-
__author__ = 'TaurenDruid'
from numpy import *
import numpy as np

#a = array([arange(2)],[arange[2]])
a = arange(5)
print a
print a.dtype
print a.shape
import urllib
query = "abc"
print(urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))