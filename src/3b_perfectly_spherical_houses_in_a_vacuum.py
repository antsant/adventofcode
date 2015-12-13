moves = open('input/day3-input.txt', 'r').read()

visited = set()
santa_location = (0,0)
robo_location = (0,0)
num_moves = 0
visited.add(santa_location)

for move in moves:
  x_movement = 0
  y_movement = 0
  if move == '^':
    y_movement = 1
  elif move == 'v':
    y_movement = -1
  elif move == '>':
    x_movement = 1
  elif move == '<':
    x_movement = -1

  if num_moves % 2 == 0: # Santa's turn
    santa_location = (santa_location[0] + x_movement, santa_location[1] + y_movement)
    visited.add(santa_location)
  else: # Robo-Santa's turn
    robo_location = (robo_location[0] + x_movement, robo_location[1] + y_movement)
    visited.add(robo_location)
  num_moves += 1

print(len(visited))
