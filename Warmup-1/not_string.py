def not_string(str):
  s = str[0:3]
  if s.lower() == 'not':
    return str
  else:
    return 'not ' + str
