import sys

all_lines = list()

for line in sys.stdin:
	line = line.strip()
	all_lines.append(line)

i = 0

for line in all_lines:
	

	if i < 10:
		print all_lines[i]
		i = i + 1

