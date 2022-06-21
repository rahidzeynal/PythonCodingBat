def string_splosion(str):
  s = ''
  if len(str) > 1:
    for i in range(len(str)+1):
      s = s + str[0:i]
    return s
  else:
    return str
