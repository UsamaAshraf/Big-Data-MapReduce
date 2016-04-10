#!/usr/bin/python

import sys


currNode = None
currUsers = []

for line in sys.stdin:
    
	k, v = line.strip().split("\t", 2)
	
	if currNode and currNode != k:
		print currNode, "\t", currUsers	
		del currUsers[0:len(currUsers)]
				
	currUsers.append(v)
	currNode = k

print currNode, "\t", currUsers
