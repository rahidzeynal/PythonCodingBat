def sum13(nums):
  t = 0
  if len(nums) == 0:
    return 0
  elif len(nums) == 1 and nums[0] == 13:
    return 0
  else:
    for i in range(0, len(nums)-1):
      if nums[i] == 13:
        nums[i] = 0
        nums[i+1] = 0
      elif 13 not in nums:
        return sum(nums)
      t += nums[i]
      
    return t
