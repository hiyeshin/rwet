import sys 

for line in sys.stdin: # for each line in standard input
	line = line.strip() # delete the white space and line breaker
	line = line.replace("the", "motherfucking")
	line = line.replace("and", "and that thingy")
	line = line.replace("a", "um um um err a")
	print line