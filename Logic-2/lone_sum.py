def lone_sum(a, b, c):
  l = [a, b, c]
  if a == b == c:
    return 0
  else:
    ls = sum(l)
    result = []
    for i in l:
      if i not in result: 
        result.append(i)
    dls = sum(result)
    return dls - (ls - dls)
