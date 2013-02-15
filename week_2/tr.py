# tr aeiou ooooo
import sys

for line in sys.stdin:
	line = line.strip()
	line = line.replace("a", "o")
	line = line.replace("e", "o")
	line = line.replace("i", "o")
	line = line.replace("u", "o")

	print line