def count_hi(str):
  total = 0
  
  for i in range(0, len(str) - 1):
    if str[i:i+2] == 'hi':
      total = total + 1
    else:
      continue
  return total
