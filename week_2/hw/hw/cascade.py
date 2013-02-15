import sys

period = "."

for line in sys.stdin:
	# line = line.strip()

	for period in line:
		line = line.strip(period)
		print line

		# else:
		# 	print "Hey, every line here is so short."




