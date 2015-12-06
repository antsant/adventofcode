f = open('input/day1-input.txt', 'r')
parens = f.read()
floor = 0
position = 0
for paren in parens:
  position += 1
  if paren == '(':
    floor += 1
  elif paren == ')':
    floor -= 1
  if floor <= -1:
    break
print(position)
