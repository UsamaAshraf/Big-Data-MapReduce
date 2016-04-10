#!/usr/bin/python

import sys
import collections


currAuthor = None
hourDict = collections.defaultdict(lambda:0)

for line in sys.stdin:
    
	record = line.split("\t")
	if currAuthor and currAuthor != record[0]:
		print currAuthor, "\t", max(hourDict, key=lambda i: hourDict[i])
		currAuthor = record[0]
		hourDict.clear()

	hourDict[record[1]] += 1
	currAuthor = record[0]
