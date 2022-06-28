def count_code(str):
  t = 0
  
  for i in range(0, len(str) - 3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      t += 1
    else:
      continue
  return t
