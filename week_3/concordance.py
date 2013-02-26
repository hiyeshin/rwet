import sys
 
concordance = dict()
 
for line in sys.stdin:
  line = line.strip()
  line_words = line.split(" ") #this will make a list of words
  
  for word in line_words:
    if word in concordance:
      concordance[word].append(line)
    else:
      concordance[word] = [line] # add new key and value
 
print concordance
 
search_word = sys.argv[1]
 
if search_word in concordance:
  print "\n".join(concordance[search_word])
