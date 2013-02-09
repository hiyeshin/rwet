# our very first program
import sys
for line in sys.stdin:
	line = line.strip() # this strips off the line breaker which automatically adds after one line.
						# therefore, it resembles more like cat function
	print line
