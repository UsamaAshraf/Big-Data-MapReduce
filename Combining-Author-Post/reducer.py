#!/usr/bin/python

import sys
import csv


currRep = None
currGold = None
currSilver = None
currBronze = None
currAuthor = None

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    
    # User
    if line[1] == "A":
        currRep = line[2]
        currGold = line[3]
        currSilver = line[4]
        currBronze = line[5]
        currAuthor = line[0]
    
	print line[1]
    # Node
    if line[1] == "B" and currRep and currGold and currSilver and currBronze and currAuthor == line[0]:
        print line[2], "\t", line[3], "\t", line[4], "\t", line[5], "\t", line[6], "\t", line[7], "\t", line[8], "\t", line[9], "\t", currRep, "\t", currGold, "\t", currSilver, "\t", currBronze
  
