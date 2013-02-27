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

#Let's make the order of list element random
random.shuffle(monologue["BOB"])
random.shuffle(monologue["CHARLOTTE"])

#recreate the random conversation. result varies every time when the code running
print monologue["BOB"][1] 
print monologue["CHARLOTTE"][0]
print monologue["BOB"][2] 
print monologue["CHARLOTTE"][1]
print monologue["BOB"][3] 
print monologue["CHARLOTTE"][2]
print monologue["BOB"][4] 
print monologue["CHARLOTTE"][3]

