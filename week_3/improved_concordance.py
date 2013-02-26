import sys
 
concordance = dict()
 
for line in sys.stdin:
  line = line.strip()
  line_words = line.split(" ")
  for word in line_words:
    if word in concordance:
      concordance[word].append(line)
    else:
      concordance[word] = [line]
 
print concordance
 
search_word = sys.argv[1]
 
if search_word in concordance:
  print "\n".join(concordance[search_word])