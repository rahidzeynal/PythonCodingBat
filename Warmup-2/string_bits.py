def string_bits(str):
  s = ''
  for i in range(0, int(len(str))):
    if i%2 == 0:
      s = s + str[i]
  return s
