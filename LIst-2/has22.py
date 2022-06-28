def has22(nums):
  cnt = 0
  for i in range(0, len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      cnt += 1
  return cnt > 0
