# 1st solution
def big_diff(nums):
  mn = nums[0]
  mx = nums[0]
  return max(nums) - min(nums)
  

# 2nd solution
def big_diff(nums):
  mn = nums[0]
  mx = nums[0]
  
  # find minimum
  for i in nums:
    if mn >= i:
      mn = i
  
  # find maximum
  for i in nums:
    if mx <= i:
      mx = i
  
  return mx - mn
