presents = open('input/day2-input.txt', 'r')
area = 0
for present in presents:
  dimensions = present.split('x')
  l = int(dimensions[0])
  w = int(dimensions[1])
  h = int(dimensions[2])
  area += 2*l*w + 2*l*h + 2*w*h
  max_dim = max(l, w, h)
  volume = l*w*h
  area += volume / max_dim
  
print(area)
