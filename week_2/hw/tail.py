import sys

all_lines = list()

for line in sys.stdin:
	line = line.strip()
	all_lines.append(line)

i = len(all_lines) - 10

for line in all_lines:
	
	if i < len(all_lines):
		print all_lines[i]
		i = i + 1

