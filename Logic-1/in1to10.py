def in1to10(n, outside_mode):
  return (n in range(1, 11) and not outside_mode) or ((n <= 1 or n >= 10) and outside_mode)
