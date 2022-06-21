def reverse3(nums):
  nums[0], nums[len(nums)-1] = nums[len(nums)-1], nums[0]
  return nums
