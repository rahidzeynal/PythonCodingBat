def close_far(a, b, c):
  l = [a, b, c]
  l.sort()
  if abs(l[0]-l[1]) <= 1 and abs(l[1]-l[2]) <= 1:
    return False
  else:
    return True
