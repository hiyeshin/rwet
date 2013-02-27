import sys

while True:
	line = sys.stdin.readline()
	
	if line == "":
		break

	line = line.strip()

	print line

	if "rose" in line:
		next_line = sys.stdin.readline()
		next_line = next_line.strip()
		print 



