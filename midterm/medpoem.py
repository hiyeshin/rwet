# Adam's suggestion
# 1. Use suffixes more often because it set the poem's tone more interestingly
# 2. Exclude some stopwords by filtering the stopword lists
# 3. Attach prefix only to the word that has a minimum length


import sys
import re
import random


#create the function that spits random one word in pre/suffix text files
def shuffle_shuffle(filename):
	all_words = []

	for line in open(filename):
		word = line.strip()
		all_words.append(word)

	random.shuffle(all_words)
	return all_words


#this will spit out one random prefix
prefix = shuffle_shuffle("prefix.txt")

#this will spit out one random suffix
suffix = shuffle_shuffle("suffix.txt")

#this is for rhyme. I am choosing only three suffix to make rhyme in every last line of the paragraph
rhyme = shuffle_shuffle("suffix.txt")[0:3]


#let's make a random poem by printing 3 * 3 lines.
#below is a container for containing random lines
#function for creating the random lines
sources = []

def liner():	
	for line in sys.stdin:
		line = line.strip()
		line = line.lower()
		sentences = line.split(". ")

		for s in sentences:
			if len(s) == 0:
				continue
			else:
				sources.append(s)

	random.shuffle(sources)
	return sources


def last_word(string, list):
	string = string[ :-1]

	if re.findall(r'(?:[a-zA-Z])+o+', string) == True:
		string = string + random.choice(list) + '.'
	else:
		string = string + 'o' + random.choice(list) + '.'

	return string


def first_word(string, list):
	#string = string[ :-1]

	if re.findall(r'Oo(?:[a-zA-Z])+', string) == True:
		string = random.choice(list) + string
	else:
		string = random.choice(list) + 'o'+ string

	return string[0].upper() + string[1: ]


def medpoem():
	
	sources[0] = last_word(sources[0], suffix)
	sources[1] = first_word(sources[1], prefix)
	sources[2] = last_word(sources[2], rhyme)
	sources[2] = first_word(sources[2], prefix)

	print sources[0]
	print sources[1]
	print sources[2]



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
