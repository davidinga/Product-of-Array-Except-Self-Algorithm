# O(n) time | O(1) space if result not counted
def productExceptSelf(nums):
  result = [1] * len(nums)

  prefix = 1
  # calculate product of all values from [:i]
  for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]

  postfix = 1
  # calculate product of all values from [:i:]
  for i in range(len(nums) - 1, -1, -1):
    result[i] *= postfix
    postfix *= nums[i]

  return result

print(productExceptSelf([1,2,3,4]))