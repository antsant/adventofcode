f = open('input/day5-input.txt')

num_nice_strings = 0
for line in f:
  three_vowels = False
  repeat_letters= False
  bad_substr = False
  num_vowels = 0
  buff = []
  for char in line:
    if len(buff) < 2:
      buff.append(char)
    else:
      buff[0] = buff[1]
      buff[1] = char
    if len(buff) == 2 and buff[0] == buff[1]:
      repeat_letters = True
    if char in ('a', 'e', 'i', 'o', 'u'):
      num_vowels += 1
    if num_vowels >= 3:
      three_vowels = True
    buff_str = ''.join(buff)
    if buff_str in ('ab', 'cd', 'pq', 'xy'):
      bad_substr = True
  if three_vowels and repeat_letters and not bad_substr:
    num_nice_strings += 1
  else:
    print(line, three_vowels, repeat_letters, bad_substr)
print(num_nice_strings)
