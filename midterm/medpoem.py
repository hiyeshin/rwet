import sys
import re
import random

#create the function that spits random one word in pre/suffix text files
def shuffle_shuffle(filename):
	all_words = list()
	for line in open(filename):
		word = line.strip()
		all_words.append(word)
	return random.choice(all_words)

#this will spit out one random prefix
prefix = shuffle_shuffle("prefix.txt")
#this will spit out one random suffix
suffix = shuffle_shuffle("suffix.txt")

#print prefix
#print suffix

#breaker = ". "

#let's make a random poem by printing 3 * 3 lines.

#below is a container for containing random lines


#function for creating the random lines
sources = []

def liner():
	

	for line in sys.stdin:
		line = line.strip()
		sentences = line.split(". ")

		for s in sentences:
			if len(s) == 0:
				continue
			else:
				sources.append(s)

	random.shuffle(sources)
	return sources
	#print sources[0:10]


def medpoem():
	for e in sources[0:3]:
		print e


	# print sources[0]
	# print sources[1]
	# print sources[2]
	# print "\n"
	# print sources[3]
	# print sources[4]
	# print sources[5]
	# print "\n"
	# print sources[6]
	# print sources[7]
	# print sources[8]

liner()
print "\n"
medpoem()
liner()
print "\n"
medpoem()
liner()
print "\n"
medpoem()
print "\n"



	# words = line.split(" ")

	# for p in re.findall(r'[Oo+(?:a-zA-Z)+]', line):
	# 	p.sub()