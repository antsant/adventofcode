import sys

presents = open('input/day2-input.txt', 'r')
length = 0
for present in presents:
  dimensions = present.split('x')
  volume = 1
  min1 = sys.maxint
  min2 = sys.maxint
  for dimension_str in dimensions:
    dimension = int(dimension_str)
    volume *= dimension
    if dimension < min1:
      min2 = min1
      min1 = dimension
    elif dimension < min2:
      min2 = dimension
  length += volume
  length += 2*min1 + 2*min2
  
print(length)
