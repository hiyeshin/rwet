import sys
import random

monologue = {"BOB":[], "CHARLOTTE":[]} #this is a dictionary the dialogues are sorted by speakers

while True:
	line = sys.stdin.readline()
	
	if line == "":
		break

	line = line.strip("\n")
	line = line.strip(" ")

	if "BOB" in line:
		next_line = sys.stdin.readline()
		next_line = next_line.strip()
		monologue["BOB"].append(next_line)

	elif "CHARLOTTE" in line:
		next_line = sys.stdin.readline()
		next_line = next_line.strip()
		monologue["CHARLOTTE"].append(next_line)

#below is the value lists based on key name
bob = monologue["BOB"]
charlotte = monologue["CHARLOTTE"]

#Let's make the order of list element random
random.shuffle(bob)
random.shuffle(charlotte)

#recreate the random conversation. result varies every time when the code running
print bob[1] 
print charlotte[0]
print bob[2] 
print charlotte[1]
print bob[3] 
print charlotte[2]
print bob[4] 
print charlotte[3]