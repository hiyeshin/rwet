import sys
#import random

monologue = {"BOB":[], "CHARLOTTE":[]}

# for line in sys.stdin:
# 	line = line.strip("\n")/
# 	line = line.strip(" ")
	
# 	line_words = line.split(" ")

	

# 	for word in line_words:
# 		if "BOB" == word:			
# 			monologue["BOB"].append(line)
# 			# how can I print next line?
# 			# range()?


# 		elif "CHARLOTTE" == word:
# 			monologue["CHARLOTTE"].append(line)

# 		else:
# 			monologue["BOB"] = [line]


# #print monologue["BOB"]
# #print monologue["CHARLOTTE"]
# 	print line

while True:
	line = sys.stdin.readline()
	

	if line == "":
		break

	line = line.strip("\n")
	line = line.strip(" ")

	print line

	if "BOB" in line:
		next_line = sys.stdin.readline()
		next_line = next_line.strip()
		monologue["BOB"].append(next_line)

	elif "CHARLOTTE" in line:
		next_line = sys.stdin.readline()
		next_line = next_line.strip()
		monologue["CHARLOTTE"].append(next_line)

charlotte = monologue["CHARLOTTE"]
print charlotte[3:9]
