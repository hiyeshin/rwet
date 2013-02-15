import sys

breaker = ". "
period = "."


lines = list()

for line in sys.stdin:
	
	#line = line.strip("\n")

	line = line.split(breaker)
	
	for l in line:
		if period in l or "\n" in l:
			print l
		else:
			print l + "."
	
#print lines


