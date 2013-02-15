import sys

searchstr = "more"

for line in sys.stdin:
	line = line.strip()
	fr = line.find(searchstr)
	
	
	if searchstr in line:
			
			print line[fr:]

		# else:
		# 	print "Hey, every line here is so short."




