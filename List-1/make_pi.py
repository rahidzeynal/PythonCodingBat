def make_pi():
  pi = 3.14
  ar = []
  p = round(math.pi,2)
  l = str(p).replace('.','')
  ll = list(l)
  for i in ll:
    ar.append(int(i))
  return ar
