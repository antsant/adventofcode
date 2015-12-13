moves = open('input/day3-input.txt', 'r').read()

visited = set()
location = (0,0)
visited.add(location)

for move in moves:
  if move == '^':
    location = (location[0], location[1] + 1)
  elif move == 'v':
    location = (location[0], location[1] - 1)
  elif move == '>':
    location = (location[0] + 1, location[1])
  elif move == '<':
    location = (location[0] - 1, location[1])
  visited.add(location)

print(len(visited))
