def xyz_there(str):
  total = 0
  for i in range(0, len(str) - 2):
    if len(str)>=3:
      if str[i:i+3] == 'xyz' and str[i-1] != '.':
        total += 1
      else:
        continue
  return total > 0
