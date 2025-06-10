numbers = [4, 5, 1, 2, 2, 9, 4]

# Mean
total = sum(numbers)
count = len(numbers)
mean = total / count

# Median
sorted_nums = sorted(numbers)
n = len(sorted_nums)
if n % 2 == 1:
    median = sorted_nums[n // 2]
else:
    median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

replace = {}
for num in numbers:
    if num in replace:
        replace[num] += 1
    else:
        replace[num] = 1
f
max_count = max(replace.values())
mode = [key for key, value in replace.items() if value == max_count]

mode_result = mode[0] if len(mode) == 1 else mode

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode_result)