# 1st 
def no_teen_sum(a, b, c):
  l = [a, b, c]
    
  nl = []
  for i in l:
    if i in range(13, 20) and i not in (15, 16):
      nl.append(0)
    else:
      nl.append(i)
  
  return sum(nl)


# 2nd
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
    
def fix_teen(n):
  if n in range(13, 20) and n not in (15, 16):
    return 0
  else:
    return n
