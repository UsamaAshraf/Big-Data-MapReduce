#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) == 5:      # Users
        writer.writerow([line[0], "A", line[1], line[2], line[3], line[4]])
        
    if len(line) >= 10:     # Posts
        writer.writerow([line[3], "B", line[0], line[1], line[2], line[5], line[6], line[7], line[8], line[9]])

