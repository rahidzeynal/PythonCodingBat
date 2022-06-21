def make_ends(nums):
  l = []
  if len(nums) >= 1:
    l.append(nums[0])
    l.append(nums[len(nums)-1])
    return l
  else:
    return nums
