#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    
	if len(line) >= 9 and line[5] == "question":
		_tags = line[2].strip().split()
		for _tag in _tags:
			print _tag, "\t", 1
		

