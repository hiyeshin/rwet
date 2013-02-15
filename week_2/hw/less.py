# I am assuming others use 80*24 bash as well
import sys

all_lines = list()

for line in sys.stdin:
	line = line.strip()
	all_lines.append(line)

i = 0

for line in all_lines:
	
	if i < 24:
		print all_lines[i]
		i = i + 1

