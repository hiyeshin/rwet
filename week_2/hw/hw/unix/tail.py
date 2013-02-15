import sys

all_lines = list()

for line in sys.stdin:
	line = line.strip()
	all_lines.append(line)

i = len(all_lines) - 10

# for line in all_lines:
	
	#if i < len(all_lines):
	#	print all_lines[i]
		# i = i + 1
		# usually in for loop in Python, 
		# counting / incrementing is not much used like other programs.
		
	# so rather than above, I can try something like this:
	
for line in all_lines[-10:]:
	print line
	
# because basically list and word has same tendency of being countable like [0:-1] or such such

# next assignment is being more creative than just making UNIX command.
# making something weirder and have fun!
	

