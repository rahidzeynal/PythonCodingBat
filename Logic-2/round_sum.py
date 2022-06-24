def round_sum(a, b, c):
  l = [a, b, c]
  nl = []
  for i in l:
    if i % 10 >= 5:
      nl.append(i + 10 - i % 10)
    elif i % 10 < 5:
      nl.append(i - i % 10)
  return sum(nl)
