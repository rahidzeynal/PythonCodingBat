def centered_average(nums):
  l = []
  cmn = 0
  cmx = 0
  mn = min(nums)
  mx = max(nums)
  
  # remove dublicates
  for i in nums:
    # remove one of the minimums
    if i == mn:
      cmn += 1
      if cmn > 1:
        l.append(i)
    # remove one of the maximums
    elif i == mx:
      cmx += 1
      if cmx > 1:
        l.append(i)
    else:
      l.append(i)
      
  return sum(l)/len(l)
