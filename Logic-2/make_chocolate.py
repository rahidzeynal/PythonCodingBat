def make_chocolate(small, big, goal):
  if goal > small + big*5:
    return -1
  elif goal % 5 > small:
    return -1
  else:
    if goal % 5 <= small and goal - big * 5 < 0 :
      return goal % 5
    elif goal - big * 5 >= 0:
      return goal - big * 5
    else:
      return small
