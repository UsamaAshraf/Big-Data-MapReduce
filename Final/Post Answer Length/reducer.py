#!/usr/bin/python

import sys


currThread = None
currPostLength = None
currTotalAnswersLength = 0.0
currTotalAnswers = 0

for line in sys.stdin:
    
	record = line.strip().split("\t")
	if currThread and currThread != record[0] and currPostLength:
		
		if currTotalAnswers != 0: 
			print currThread, "\t", currPostLength, "\t", currTotalAnswersLength/float(currTotalAnswers)
		else:
			print currThread, "\t", currPostLength, "\t", 0.0	
		
		currTotalAnswersLength = 0.0
		currTotalAnswers = 0
	
	if record[1] == "A ":
		currPostLength = record[2]
		
	if record[1] == "B ":
		currTotalAnswers += 1
		currTotalAnswersLength += float(record[2])

	currThread = record[0]


if currTotalAnswers != 0: 
	print currThread, "\t", currPostLength, "\t", currTotalAnswersLength/float(currTotalAnswers)
else:
	print currThread, "\t", currPostLength, "\t", 0.0


