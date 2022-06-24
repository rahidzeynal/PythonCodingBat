def lucky_sum(a, b, c):
  l = [a, b, c]
  result = []
  for i in l:
    if i != 13:
      result.append(i)
    else:
      break
  return sum(result)
