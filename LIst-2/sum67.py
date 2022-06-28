def sum67(nums):
  cnt = 0
  t = 0
  if 6 not in nums:
    return sum(nums)
  else:
    for i in range(0, len(nums)):
      if nums[i] == 6:
        while nums[i] != 7:
          nums[i] = 0
          t += nums[i]
          i += 1
        cnt += 1
      else:
        t += nums[i]
  return t - cnt * 7
