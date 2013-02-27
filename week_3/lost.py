import sys
import random

monologue = {"BOB":[], "CHARLOTTE":[]} #this is a dictionary the dialogues are sorted by speakers

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

bob = monologue["BOB"]
charlotte = monologue["CHARLOTTE"]

random.shuffle(bob)
random.shuffle(charlotte)

print bob[1] 
print charlotte[0]
print bob[2] 
print charlotte[1]
print bob[3] 
print charlotte[2]
print bob[4] 
print charlotte[3]