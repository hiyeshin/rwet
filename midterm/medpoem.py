import sys
import re
import random


def shuffle_shuffle(filename):
	all_words = list()
	for line in open(filename):
		word = line.strip()
		#for w in word:
		all_words.append(word)
	return all_words


prefix = shuffle_shuffle("prefix.txt")
suffix = shuffle_shuffle("suffix.txt")

print random.choice(prefix)
print random.choice(suffix)


# for line in sys.stdin:
# 	line = line.strip()
# 	# words = line.split(" ")

# 	for p in re.findall(r'[Oo+(?:a-zA-Z)+]', line):
# 		p.sub()