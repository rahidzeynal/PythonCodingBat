def left2(str):
  l = len(str)
  
  if l > 2:
    return str[2:] + str[0:2]
  else:
    return str
