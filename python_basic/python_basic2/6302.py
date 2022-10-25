nums = [12, 24, 35, 70, 88, 120, 155]
result = [nums[i] for i in range(len(nums)) if i != 0 and i != 4 and i != 5]
print(result)
