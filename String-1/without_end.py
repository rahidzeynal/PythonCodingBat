def without_end(str):
  l = len(str)
  if l > 2:
    return str[1:l-1]
  else:
    return ''
