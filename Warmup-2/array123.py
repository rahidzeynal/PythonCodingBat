def array123(nums):
  cnt = 0
  if len(nums) >= 3:
    for i in range(len(nums)-2):
      if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
        cnt += 1
  else:
    cnt = 0
    
    
  return cnt > 0
