#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    
	if len(line) >= 9:
		print line[3].split(), "\t", line[8].split(':')[0].split()[-1]

