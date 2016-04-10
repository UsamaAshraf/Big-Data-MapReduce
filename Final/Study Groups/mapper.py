#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
next(reader, None)

for line in reader:
    
	if len(line) >= 9:
		print line[0], "\t", line[3]
		
		if unicode(line[6]).isnumeric():
			print line[6], "\t", line[3]
		if unicode(line[7]).isnumeric():
			print line[7], "\t", line[3]

