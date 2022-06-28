def cat_dog(str):
  tc = 0
  td = 0
  
  for i in range(0, len(str) - 2):
    if str[i:i+3] == 'cat':
      tc += 1
    elif str[i:i+3] == 'dog':
      td += 1
    else:
      continue
  return tc == td
