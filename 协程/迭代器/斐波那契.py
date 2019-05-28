nums = list()
# nums列表占用的空间会越来越大
a = 0
b = 1
i = 0
while i < 10:
    nums.append(a)
    a, b = b, a+b
    i += 1

print(nums)