def count_evens(nums):
    return sum([not i % 2 for i in nums])

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)

def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total


def sum67(nums):
  sum = 0 
  in67 = False
  for i in nums:
    if i ==6:
      in67 = True
    elif not in67:
      sum += i
    elif i == 7 and in67:
      in67 = False
  return sum

def has22(nums):
  has = False
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      has = True
  return has

