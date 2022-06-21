def max_end3(nums):
  n = max(nums[0], nums[2])
  l = []
  
  for i in range(len(nums)):
    l.append(n)
  return l
  
