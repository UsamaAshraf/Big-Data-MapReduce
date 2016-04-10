#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    
	if len(line) >= 9:
		
		if line[5] == "question":
			print line[0], "\t", "A", "\t", len(line[4])
		
		if line[5] == "answer":
			print line[6], "\t", "B", "\t", len(line[4])
		

