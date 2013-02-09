import sys

adj_set = set()
for line in open('adjectives'):
  line = line.strip()
  adj_set.add(line)

for line in sys.stdin:
  line = line.strip()
  adjs = [s for s in line.split(" ") if s.lower() in adj_set]
  if len(adjs) > 0:
    print ', '.join(adjs)

