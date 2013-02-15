import sys

breaker = ". "
period = "."


lines = list()

for line in sys.stdin:

	line = line.strip()

	#line = line.split(breaker)
	sentences = line.split(breaker)
	
	#below will be filtering empty string
	for s in sentences:
		if len(s) == 0:
			continue
		if s[-1] == period:
			print s
		else:
			print s + "."
			
		#if period in l or "\n" in l:
		#	print l
		#else:
		#	print l + "."
	
#print lines


