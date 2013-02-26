import sys
#import random

monologue = {"BOB":[], "CHARLOTTE":[]}

for line in sys.stdin:
	line = line.strip(" ")
	line = line.strip("\n") # strip the each line by line
	line_words = line.split(" ") #create the list of word by splitting anything btwn space
	#new_line = line_words.join()

	for word in line_words:
		if "BOB" == word:			
			monologue["BOB"].append(line)

		elif "CHARLOTTE" == word:
			monologue["CHARLOTTE"].append(line)

		else:
			monologue["BOB"] = [line]

# print line
	print line

