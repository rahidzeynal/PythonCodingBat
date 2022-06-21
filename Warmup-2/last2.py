def last2(str):
  # get last 2 characters in str
  l2 = str[-2:]
  
  cnt = 0
  if len(str) <= 2:
    return 0
  else:
    for i in range(len(str)-2):
      if str[i] + str[i+1] == l2:
        cnt = cnt + 1
    return cnt
