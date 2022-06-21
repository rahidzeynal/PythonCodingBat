def front_back(str):
  n = int(len(str))
  if n > 1:
    l = str[n-1]
    m = str[1:n-1]
    f = str[0]
    return l + m + f
  else:
    return str
