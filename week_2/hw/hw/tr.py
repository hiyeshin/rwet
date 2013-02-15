import sys

for line in sys.stdin:
	line = line.strip()
	line = line.replace("more", "less")


	print line