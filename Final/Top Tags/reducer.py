#!/usr/bin/python

import sys
import collections


counter = collections.defaultdict(lambda:0)

for line in sys.stdin:
    
	k, v = line.strip().split("\t", 2)
	counter[k] += int(v)

print sorted(counter, key=lambda i:counter[i], reverse=True)[:10]
