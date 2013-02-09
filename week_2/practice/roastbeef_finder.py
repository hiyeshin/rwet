import sys

for line in sys.stdin:
	line = line.strip()
	offset = line.find("ROASTBEEF")
	if offset != -1:
		print line[offset:]
