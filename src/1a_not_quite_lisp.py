f = open('input/day1-input.txt', 'r')
parens = f.read()
floor = 0
for paren in parens:
  if paren == '(':
    floor += 1
  elif paren == ')':
    floor -= 1
print(floor)
