def end_other(a, b):
  la = len(a)
  lb = len(b)
  if la >= lb:
    x = a.lower()
    return x[-lb:] == b.lower()
  else:
    x = b.lower()
    return x[-la:] == a.lower()
