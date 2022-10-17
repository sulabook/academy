nums = [12, 24, 35, 70, 88, 120, 155]
result = [nums[i] for i in range(len(nums)) if (i + 1) % 2 == 0]
print(result)
