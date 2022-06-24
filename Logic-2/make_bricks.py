# Actually I cound't do it myself :)
def make_bricks(small, big, goal):
  # fail if not enough
  if goal > small + big * 5:
    return False
  elif goal % 5 > small:
    return False
  else:
    return True
