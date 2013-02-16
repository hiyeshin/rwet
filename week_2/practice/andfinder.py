import sys

for line in sys.stdin:
	line = line.strip()
	startpoint = line.find("It")
	if startpoint != -1:
		print line[startpoint:startpoint+15]