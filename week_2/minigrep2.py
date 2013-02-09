import sys

searchstr = "salmon"

for line in sys.stdin:
	line = line.strip()

	if len(line) > 10:
		if searchstr in line:
			print line

		# else:
		# 	print "Hey, every line here is so short."




