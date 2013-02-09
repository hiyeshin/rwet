import sys

# below means standard input. is used for all interpreter input except for scrips 
for line in sys.stdin:
	line = line.strip()
	# as a default, 'strip' strips off the white space including white spaces. 
	# if there're arguments such as characters, then it omits that specific characters.
	# it's because usually there're line breakers which automatically added after when a line is completed
	# so it makes this function more look like cat, without interpreting line breaker
	print line
