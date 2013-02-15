import sys

all_lines = list()

for line in sys.stdin:
	line = line.strip()
	all_lines.append(line)

for line in all_lines[-10:]:
	print line

