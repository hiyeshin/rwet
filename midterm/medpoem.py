import sys
import re
import random


#create the function that spits random one word in pre/suffix text files
def shuffle_shuffle(filename):
	all_words = []
	#chosen_three = []

	for line in open(filename):
		word = line.strip()
		all_words.append(word)

	random.shuffle(all_words)
	return all_words[:3]


#this will spit out one random prefix
prefix = shuffle_shuffle("prefix.txt")

#this will spit out one random suffix
suffix = shuffle_shuffle("suffix.txt")


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
	# for e in sources[0:3]:
	# 	print e


	#Let's have fun with suffix!
	if re.findall(r'(?:[a-zA-Z])+o+', sources[2]) == True:
		sources[2] = sources[2] + random.choice(suffix)
	else:
		sources[2] = sources[2] + 'o' + random.choice(suffix)


	#Now it's for prefix!
	if re.findall(r'Oo(?:[a-zA-Z])+]', sources[2]) == True:
		sources[2] = random.choice(prefix) + sources[2]
	else:
		sources[2] = random.choice(prefix) + 'o' + sources[2]


	print sources[0]
	print sources[1]
	print sources[2]



	# words = line.split(" ")

	# for p in re.findall(r'[Oo+(?:a-zA-Z)+]', line):
	# 	p.sub()






# AND HERE COMES THE RESULT
print "\n"
liner() #strip line and shuffle!
medpoem() # make a structure of 3*3
print "\n" # so I can rest a while
liner()
medpoem()
print "\n"
liner()
medpoem()
print "\n"
