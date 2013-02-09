import sys

searchstr = "salmon"

for line in sys.stdin:
	line = line.strip()
	if searchstr in line:
		print line

	searchstr = searchstr.upper()
	if searchstr in line:
		print line

	searchstr = searchstr.title()
	if searchstr in line:
		print line 